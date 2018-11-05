pipeline {
    agent {
        docker {
            image 'python:2.7.15'
            args '-u root:root'
        }
    }
    environment {
        JENKY_GLOBAL = 'Hello'
        JENKY_STAGE = 'Global'
        JENKY_SECRET = credentials('my-secret-text')
    }
    stages {
        stage('install') {
            environment {
                JENKY_STAGE = 'Build'
            }
            steps {
                sh 'python --version'
                sh 'pip --version'
                sh 'pip install .'
                sh 'pip list'
                sh 'echo $JENKY_SECRET'
            }
        }
        stage('test') {
            environment {
                PYTHON_EGG_CACHE = "$HOME/.py-egg-cache/"
            }
            steps {
                sh 'python setup.py test'
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