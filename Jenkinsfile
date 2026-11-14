pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    environment {
        SONAR_HOST = 'http://sonarqube:9000'
        SONAR_TOKEN = credentials('sonar-token')
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
        stage('SonarQube Analysis') {
            steps {
                sh '''
                    docker run --rm --network devops-net \
                      -e SONAR_HOST_URL=$SONAR_HOST \
                      -e SONAR_TOKEN=$SONAR_TOKEN \
                      -v "$WORKSPACE":/usr/src \
                      sonarsource/sonar-scanner-cli
                '''
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
