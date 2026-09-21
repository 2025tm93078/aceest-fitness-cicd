pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling latest code from GitHub...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                echo 'Running lint check...'
                sh 'pip install flake8'
                sh 'flake8 app.py --max-line-length=127 --exit-zero'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Pytest...'
                sh 'pytest test_app.py -v'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t aceest-fitness:jenkins .'
            }
        }
    }

    post {
        success {
            echo 'BUILD SUCCESS - All stages passed!'
        }
        failure {
            echo 'BUILD FAILED - Check the logs above.'
        }
    }
}