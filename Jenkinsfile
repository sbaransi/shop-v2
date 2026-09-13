pipeline {
    agent any

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
}