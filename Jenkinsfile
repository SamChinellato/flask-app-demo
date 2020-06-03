pipeline {
  agent { docker { image 'python:3.7.2' } }
  environment {
    FLASK_APP = '/src/app.py'
  }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python -m src.tests.test_basic '
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }       
    }
    stage('run') {
      steps{
          echo "Flask App is ${FLASK_APP}"
          dir("src") {
            sh 'pwd'
            sh 'python -m flask run'
          }
      }
    }
  }
}