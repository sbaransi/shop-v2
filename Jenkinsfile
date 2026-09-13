pipeline {
    agent any

    stages {

        stage('Build Backend') {
            steps {
                dir('backend') {
                    sh 'docker build -t shop-v2-backend:v1 .'
                }
            }
        }

        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh 'docker build -t shop-v2-frontend:v1 .'
                }
            }
        }

    }
}