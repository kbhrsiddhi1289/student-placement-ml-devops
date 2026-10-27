pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/siddhikumbhar/student-placement-ml-devops.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-placement-app .'
            }
        }
        stage('Run Container Test') {
            steps {
                bat 'docker run -d -p 5000:5000 --name test-container student-placement-app'
            }
        }
    }
}