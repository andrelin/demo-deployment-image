
// TODO: Set Jenkins Display name
String jenkinsLabel = u.get_jenkins_node_label()
String name = 'demo-deployment-image'
String dockerImage = u.get_docker_image_name("core", name)
// TODO: Set Chartmusuem URL

podTemplate(
        label: jenkinsLabel,
        namespace: "core",
        serviceAccount: "jenkins",
        yaml: """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: helm
    image: vfarcic/helm:3.2.1
    command: ["cat"]
    tty: true
"""
) {
    node(jenkinsLabel) {
        String version
        node("docker") {
            stage("Build") {
                checkout scm
                // version = docker_build(dockerImage)
            }
        }
        if (env.BRANCH_NAME == "master") {
            container("helm") {
                stage('Package and release Helm Chart') {
                    checkout scm
                    // helm_release(name, version)
                }
                stage("Create name release") {
                    // git_release_app()
                }
            }
        }
    }
}
