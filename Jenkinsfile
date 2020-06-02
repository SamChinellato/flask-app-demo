pipeline {
  agent { dockerfile true }
  stages {
    stage('build') {
      steps {
        sh 'python --version'
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