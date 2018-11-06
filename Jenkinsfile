pipeline {
    agent {
        docker {
            image 'python:2.7.15'
            args '-u root:root -v /var/jenky/output:/export'
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
                sh 'ls -la docs/_build'
            }
        }
        stage('Deploy') {
            switch (env.BRANCH_NAME) {
                case 'master':
                    input {
                        message "Push to production?"
                    }
                    steps {
                        sh 'echo In master branch'
                        sh 'mkdir /export/docs'
                        sh 'mkdir /export/dist'
                        sh 'cp docs/_build/* /export/docs'
                        sh 'cp dist/* /export/dist'
                    }
                    break;
                default:
                    steps {
                        sh 'echo Not in master but in $BRANCH_NAME'
                    }
            }
        }
    }
}