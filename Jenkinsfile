pipeline {
    agent any

    environment {
        DOCKER_HUB = credentials('dockerhub')
    }

    stages {

        stage('Build Backend') {
            steps {
                dir('backend') {
                    sh 'docker build -t sammybaransi537/shop-v2-backend:latest .'
                }
            }
        }

        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh 'docker build -t sammybaransi537/shop-v2-frontend:latest .'
                }
            }
        }

        stage('Docker Login') {
            steps {
                sh '''
                echo $DOCKER_HUB_PSW | docker login \
                -u $DOCKER_HUB_USR \
                --password-stdin
                '''
            }
        }

        stage('Push Backend') {
            steps {
                sh 'docker push sammybaransi537/shop-v2-backend:latest'
            }
        }

        stage('Push Frontend') {
            steps {
                sh 'docker push sammybaransi537/shop-v2-frontend:latest'
            }
        }
    }

    post {
        always {
            sh 'docker logout || true'
        }
    }
}