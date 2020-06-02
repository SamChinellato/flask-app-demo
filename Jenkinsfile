pipeline {
  agent { dockerfile true }
  stages {
    stage('test') {
      steps {
        sh 'sh python --version'
        sh 'python -m src.tests.test_basic'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }       
    }
  }
}