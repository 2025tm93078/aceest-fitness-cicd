pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt flake8 pytest'
            }
        }
        stage('Lint') {
            steps {
                sh '. venv/bin/activate && flake8 app.py --max-line-length=127 --exit-zero'
            }
        }
        stage('Unit Tests') {
            steps {
                sh '. venv/bin/activate && pytest test_app.py -v'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t aceest-fitness:${BUILD_NUMBER} .'
            }
        }
    }

    post {
        success { echo 'BUILD SUCCESS' }
        failure { echo 'BUILD FAILED' }
    }
}
