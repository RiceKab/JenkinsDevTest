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
                sh 'virtualenv jenkinsenv'
                sh 'ls jenkinsenv'
                sh 'ls jenkinsenv/bin'
                sh '. jenkinsenv/bin/activate'
                sh 'pip list'
                sh 'pip install .'
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