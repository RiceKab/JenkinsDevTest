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
        stage('Testing') {
            environment {
                PYTHON_EGG_CACHE = "$HOME/.py-egg-cache/"
            }
            steps {
                sh 'pip install .'
                sh 'python setup.py pytest'
            }
        }
        //stage('Manual Approval') {
        //    when {
        //        branch 'master'
        //    }
        //    steps{
        //        script {
        //            env.DEPLOY_APPROVED = input message: "Approve deployment?", ok: 'Approve', parameters: [booleanParam(defaultValue: true, name: 'Approve')]
        //        }
        //        sh 'echo "Value is $DEPLOY_APPROVED"'
        //    }
        //}
        stage('Build') {
        //    when {
        //        environment name: 'DEPLOY_APPROVED', value: 'true'
        //    }
            steps {
                sh 'python setup.py sdist'
                sh 'pip install sphinx'
                sh 'sphinx-build docs docs/_build'
                sh 'ls -la docs/_build'
            }
        }
        stage('Deploy') {
        //    when {
        //        environment name: 'DEPLOY_APPROVED', value: 'true'
        //    }
            steps {
                sh 'mkdir -p /export/docs'
                sh 'mkdir -p /export/dist'
                sh 'cp -r docs/_build/* /export/docs'
                sh 'cp -r dist/* /export/dist'
            }
        }
    }
}