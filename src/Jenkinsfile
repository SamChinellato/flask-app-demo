pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r ./src/requirements.txt'
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
  }
}