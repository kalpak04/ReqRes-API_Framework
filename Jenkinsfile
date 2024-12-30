pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git 'https://github.com/kalpak04/ReqRes-API_Framework.git'
            }
        }
        stage('Set Up Python Environment') {
            steps {
                // Set up Python environment
                sh '''
                python -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                // Run the specific test file
                sh '''
                source venv/bin/activate
                pytest src/tests/test_api1.py --html=reports/report.html --self-contained-html
                '''
            }
        }
        stage('Archive Results') {
            steps {
                // Archive the test report
                archiveArtifacts artifacts: 'reports/report.html', fingerprint: true
            }
        }
    }

    post {
        always {
            // Clean up the workspace
            cleanWs()
        }
    }
}