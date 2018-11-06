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
            stages {
                stage('Deploy Master') {
                    when { branch 'master' }
                    input {
                        message "Push to production?"
                    }
                    sh 'mkdir -p /export/docs'
                    sh 'mkdir -p /export/dist'
                    sh 'cp -r docs/_build/* /export/docs'
                    sh 'cp -r dist/* /export/dist'
                }
                stage('Deploy Others') {
                    when { not { branch 'master' }}
                    sh 'echo We are in the $BRANCH_NAME branch'
                }
            }
        }
    }
}