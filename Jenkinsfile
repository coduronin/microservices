pipeline {
    agent any

    environment {
        // Set the working directory for payment and user services
        PAYMENT_SERVICE_DIR = 'payment_service'
        USER_SERVICE_DIR = 'user_service'
        KUBECONFIG = "C:/Users/izzat/.kube/config"
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository from GitHub
                git 'https://github.com/coduronin/microservices.git'
            }
        }

        stage('Pull Payment Service Docker Image') {
            steps {
                script {
                    // Pull the latest Docker image for Payment Service
                    bat 'docker pull "aybukecanoz/payment-service:latest"'
                }
            }
        }

        stage('Pull User Service Docker Image') {
            steps {
                script {
                    // Pull the latest Docker image for User Service
                    bat 'docker pull "aybukecanoz/user-service:latest"'
                }
            }
        }

        stage('Install pytest and Run Unit Tests for Payment Service') {
            steps {
                script {
                    // Navigate to the payment_service directory
                    dir(PAYMENT_SERVICE_DIR) {
                        // Create a virtual environment and install pytest
                        bat '''
                            python -m venv venv
                            venv\\Scripts\\activate
                            pip install --upgrade pip
                            pip install pytest
                        '''
                        // Run unit tests for the Payment Service
                        bat '''
                            venv\\Scripts\\activate
                            pytest --maxfail=1 --disable-warnings -q
                        '''
                    }
                }
            }
        }

        stage('Install pytest and Run Unit Tests for User Service') {
            steps {
                script {
                    // Navigate to the user_service directory
                    dir(USER_SERVICE_DIR) {
                        // Create a virtual environment and install pytest
                        bat '''
                            python -m venv venv
                            venv\\Scripts\\activate
                            pip install --upgrade pip
                            pip install pytest
                        '''
                        // Run unit tests for the User Service
                        bat '''
                            venv\\Scripts\\activate
                            pytest --maxfail=1 --disable-warnings -q
                        '''
                    }
                }
            }
        }

stage('Deploy Payment Service to Kubernetes') {
            steps {
                script {
                    // Payment Service için Kubernetes'e deploy işlemi
                    dir('payment_service') {
                        bat 'kubectl apply -f deployment.yml'
                    }
                }
            }
        }

        stage('Deploy User Service to Kubernetes') {
            steps {
                script {
                    // User Service için Kubernetes'e deploy işlemi
                    dir('user_service') {
                        bat 'kubectl apply -f deployment.yml'
                    }
                }
            }
        }
    }


    post {
        always {
            // Clean up the workspace after the pipeline finishes
            cleanWs()
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs for errors.'
        }
    }
}
