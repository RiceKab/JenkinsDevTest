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
                sh '. jenkinsenv/bin/activate && pip list && pip install . && pip list'
            }
        }
        stage('test') {
            steps {
                sh '. jenkinsenv/bin/activate && python setup.py test'
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