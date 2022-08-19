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
                sh 'python3 test_calc.py'
            }
        }
    }
}
