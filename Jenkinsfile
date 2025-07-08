pipline {
    agent any 
    stages {
        stage('Build'){
            // This step build the application
            steps {
                sh 'docker build -t my-flask-app .'
                sh 'docker tag my-flask-app $DOCKER_BFLASK_IMAWE'
            }
        }
        stage('Deploy'){
            // This stage pushes the image to docker hub
            steps {
                withCredentials([usernamePassword(credentialsID: "${DOCKER_REGISTRY_CREDS}",passwordVariable: 'DOCKER_PASSWORD',usernameVariable: 'DOCKER_USERNAME')]) {
                    sh 'echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin docker.io'
                    sh "docker push $DOCKER_BFLASK_IMAGE"
                }
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}
