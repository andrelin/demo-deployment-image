import os
import sys
import toml

print("Input args: " + str(sys.argv))

application = sys.argv[1]
version = sys.argv[2]
env_repo = sys.argv[3]
dsf_file = sys.argv[4] if sys.argv[4] else "dsf.toml"

filename = env_repo + "/" + dsf_file

print("Loading file: " + filename)
data = toml.load(filename)

if (application in data["apps"]):
    data["apps"][application]["version"] = version

else:
    key = next(iter(data["apps"]))
    values_file = env_repo + "/values/" + application + ".yaml"

    copy = data["apps"][key].copy()
    copy["name"] = application
    copy["description"] = application
    copy["version"] = version
    copy["enabled"] = True
    copy["chart"] = "chartmuseum/" + application
    copy["valuesFiles"] = [ values_file ]

    data["apps"][application] = copy

    f = open(env_repo + "/" + values_file, "w")
    f.write("---\ndummy: value")

print("Updated dsf info")
print(toml.dumps(data))

os.remove(filename)
f = open(filename, "w")
toml.dump(data, f)
f.close()
