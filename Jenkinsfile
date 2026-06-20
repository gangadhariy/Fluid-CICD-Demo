pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "gangadhariy/fluid-ai-demo"
    }
    stages {
        stage('Build the code with docker') {
            steps {
                sh 'docker build -it ${DOCKER_IMAGE}:${BUILD_ID}'
                echo 'Image builded susccessfully'
            }
        }
        stage('Docker login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Docker-Creds', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USER')]) {
                    sh 'echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USER} --password-stdin'
            }
            }
        }
        stage('Scan the docker image') {
            steps {
                sh 'trivy image --sevirity HIGH, CRITICAL --exit-code 1 ${DOCKER_IMAGE}:${BUILD_ID}'
            }
        }
        stage('Docker push') {
            steps {
                sh 'docker push ${DOCKER_IMAGE}:${BUILD_ID}'
            }
        }
        stage('Edit the image version in argocd manifest repo') {
            steps {
                withCredentials([string(credentialsId: 'Github_token', variable: 'GITHUB_TOKEN')]) {
                    sh '''
                        git clone https://github.com/gangadhariy/Fluid-CD-Argo.git
                        cd Fluid-CD-Argo
                        git config user.name "github-actions"
                        git config user.email "github-actions@github.com"
                        sed -i "s|image: .*|image: ${DOCKER_IMAGE}:${BUILD_ID}|" Deployment.yaml 
                        git add .
                        git commit -m "Updated the image to new version"
                        git push https://${GITHUB_TOKEN}@github.com/gangadhariy/Fluid-CD-Argo.git HEAD:main
                       '''
            }
            }
        }
    }
}