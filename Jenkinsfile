pipeline {
    agent any

    environment {
        IMAGE_NAME = 'my-python-script'
        WORKDIR = "${env.WORKSPACE}"  // Jenkins job workspace
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/vignesh-110592/JenkinsPythonTest.git']])
            }
        }

        stage('Build Docker Image') {
            steps {
                dir("${WORKDIR}") {
                    bat "docker build -t %IMAGE_NAME% ."
                }
            }
        }

        stage('Run Python Script in Container') {
            steps {
                bat """
                    docker run --rm ^
                        -v "%WORKDIR%:/app" ^
                        -w /app ^
                        %IMAGE_NAME% ^
                        python test.py Google
                """
            }
        }
    }
}
