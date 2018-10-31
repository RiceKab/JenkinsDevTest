pipeline {
    agent { docker { image 'python:2.7.15' } }
    stages {
        environment {
            JENKY_GLOBAL = 'Hello'
            JENKY_STAGE = 'Global'
        }
        stage('build') {
            environment {
                JENKY_STAGE = 'Build'
            }
            steps {
                sh 'python --version'
                sh 'pip --version'
                sh 'pip list'
                sh 'printenv'
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