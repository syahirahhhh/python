pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m py_compile add2vals.py calc.py' 
            }
        }
        stage('Test') {
            steps {
                sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
