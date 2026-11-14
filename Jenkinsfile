pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    environment {
        SONAR_HOST = 'http://sonarqube:9000'
        SONAR_TOKEN = credentials('sonar-token')
        IMAGE = 'rohitvardhanbattula/aceest-fitness'
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
                      --volumes-from jenkins -w "$WORKSPACE" \
                      sonarsource/sonar-scanner-cli
                '''
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE:${BUILD_NUMBER} -t $IMAGE:latest .'
            }
        }
        stage('Test Inside Container') {
            steps {
                sh 'docker run --rm $IMAGE:${BUILD_NUMBER} python -m pytest test_app.py -q'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
                    sh 'echo $DH_PASS | docker login -u $DH_USER --password-stdin'
                    sh 'docker push $IMAGE:${BUILD_NUMBER}'
                    sh 'docker push $IMAGE:latest'
                }
            }
        }
    }

    post {
        success { echo 'BUILD SUCCESS' }
        failure { echo 'BUILD FAILED' }
    }
}
