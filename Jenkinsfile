pipeline {
    agent { docker { image 'python:2.7.15' } }
    environment {
        JENKY_GLOBAL = 'Hello'
        JENKY_STAGE = 'Global'
    }
    stages {
        stage('install') {
            environment {
                JENKY_STAGE = 'Build'
            }
            steps {
                sh 'python --version'
                sh 'pip --version'
                sh 'pip list'
                sh 'pip install . --user'
                sh 'pip list'
            }
        }
        stage('final') {
            environment {
                JENKY_STAGE = 'Final'
            }
            steps {
                sh 'printenv'
                sh 'ls -la'
            }
        }
    }
}