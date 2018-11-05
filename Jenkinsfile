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
        JENKY_OTHER_SECRET = credentials('my-other-secret-text')
    }
    stages {
        stage('Install') {
            environment {
                JENKY_STAGE = 'Build'
            }
            steps {
                sh 'pip install .'
            }
        }
        stage('Testing') {
            environment {
                PYTHON_EGG_CACHE = "$HOME/.py-egg-cache/"
            }
            steps {
                sh 'python setup.py pytest'
            }
        }
        stage('Build') {
            steps {
                sh 'python setup.py sdist'
                sh 'pip install sphinx'
                sh 'sphinx-build docs docs/_build'
                sh 'tree docs/_build'
            }
        }
        stage('Deploy') {
            input {
                message "Good to deploy?"
            }
            steps {
                sh 'mkdir ~/mydocs'
                sh 'mkdir ~/mysources'
                sh 'cp -r docs/_build ~/mydocs'
                sh 'cp dist/* ~/mysources'
                sh 'tree ~'
            }
        }
    }
}