pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/2025tm93078/aceest-fitness-cicd.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Lint') {
            steps {
                sh 'pip install flake8 --break-system-packages'
                sh 'flake8 app.py --max-line-length=127 --exit-zero'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py -v'
            }
        }

        stage('Docker Build') {
            steps {
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