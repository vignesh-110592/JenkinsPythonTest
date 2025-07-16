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
            steps{
                Set-ItemProperty -Path "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\test\\Anschreiben.docx" -Name IsReadOnly -Value $false
            }
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
                        -v "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\test:/app" ^
                        -w /app ^
                        %IMAGE_NAME% ^
                        python test.py "Alten GmbH"
                """
            }
        }
    }
}
