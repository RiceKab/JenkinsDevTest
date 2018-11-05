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
        stage('Install') {
            environment {
                JENKY_STAGE = 'Build'
            }
            steps {
                sh 'pip install .'
                sh 'echo $JENKY_SECRET'
                sh 'python print_secret.py random_parameter $JENKY_SECRET'
            }
        }
        stage('test') {
            environment {
                PYTHON_EGG_CACHE = "$HOME/.py-egg-cache/"
            }
            steps {
                sh 'python setup.py pytest'
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