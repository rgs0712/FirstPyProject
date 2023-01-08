pipeline{

    agent any

    stages{
        stage('Build'){
            steps {
                echo "build .."
            }
        }
        stage('test'){
            steps{
                deleteDir()
                checkout scm
                sh """
                    behave --junit
                """
                junit 'reports/*.xml'  // (1)
            }
        }
    }
}