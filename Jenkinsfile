pipeline {
    agent any

    stages {
        stage('Build and Lint') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 app.py --max-line-length=100'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t aceest-fitness .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pip install pytest'
                sh 'pytest test_app.py'
            }
        }
    }
}