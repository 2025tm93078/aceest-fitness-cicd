pipeline {
    agent any

    stages {
        stage('Build and Lint') {
            steps {
                sh 'pip3 install flake8'
                sh 'pip3 install flake8 --break-system-packages || pip3 install flake8'
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
                sh 'pip3 install pytest --break-system-packages || pip3 install pytest'
                sh 'python3 -m pytest test_app.py'
            }
        }
    }
}