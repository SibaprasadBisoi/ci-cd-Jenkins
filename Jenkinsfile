pipline {
    agent any 
    stages {
        stage('Build'){
            // Build docker image and adding the tag
            steps {
                sh 'docker build -t my-flask-app .'
                sh 'docker tag my-flask-app $DOCKER_BFLASK_IMAWE'
            }
        }
        stage('Test'){
            // Run the container and start the test
            steps {
                sh 'docker run my-flask-app python -m pytest app/tests/'
            }
        }
        stage('Deploy'){
            // Login docker and push the image
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