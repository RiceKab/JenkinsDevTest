pipeline {
    agent { docker { image 'python:2.7.15' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip --version'
                sh 'pip list'
                sh 'printenv'
            }
        }
    }
}