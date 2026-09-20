pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh 'apt-get update && apt-get install -y python3 python3-pip docker.io'
            }
        }
        stage('Build and Lint') {
            steps {
                sh 'pip3 install flake8 --break-system-packages'
                sh 'python3 -m flake8 app.py --max-line-length=100'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t aceest-fitness .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pip3 install pytest --break-system-packages'
                sh 'python3 -m pytest test_app.py'
            }
        }
    }
}