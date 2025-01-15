pipeline {
    agent any

    environment {
        REGISTRY = "aybukecanoz"  // Docker Registry (Örneğin Docker Hub)
        PAYMENT_SERVICE_IMAGE = "payment-service"
        USER_SERVICE_IMAGE = "user-service"
    }

    stages {
        stage('Checkout') {
            steps {
                // GitHub reposundan kodu çekiyoruz
                git 'https://github.com/aybukecnz/microservices.git'
            }
        }

        stage('Pull Payment Service Docker Image') {
            steps {
                script {
                    // Docker Hub'dan Payment Service imajını çekiyoruz
                    docker.pull("aybukecanoz/payment-service:latest")
                }
            }
        }

        stage('Pull User Service Docker Image') {
            steps {
                script {
                    // Docker Hub'dan User Service imajını çekiyoruz
                    docker.pull("aybukecanoz/user-service:latest")
                }
            }
        }

        stage('Run Unit Tests for Payment Service') {
            steps {
                script {
                    // Payment Service için unit testlerini çalıştırıyoruz
                    dir('payment_service') {
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Run Unit Tests for User Service') {
            steps {
                script {
                    // User Service için unit testlerini çalıştırıyoruz
                    dir('user_service') {
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Deploy Payment Service to Kubernetes') {
            steps {
                script {
                    // Payment Service için Kubernetes'e deploy işlemi
                    dir('payment_service') {
                        sh 'kubectl apply -f deployment.yml'
                    }
                }
            }
        }

        stage('Deploy User Service to Kubernetes') {
            steps {
                script {
                    // User Service için Kubernetes'e deploy işlemi
                    dir('user_service') {
                        sh 'kubectl apply -f deployment.yml'
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Pipeline tamamlandığında workspace temizleniyor
        }
    }
}
