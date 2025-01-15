pipeline {
    agent any

    environment {
        REGISTRY = "your-docker-registry"  // Docker Registry (Örneğin Docker Hub)
        PAYMENT_SERVICE_IMAGE = "payment-service"
        NOTIFICATION_SERVICE_IMAGE = "notification-service"
    }

    stages {
        stage('Checkout') {
            steps {
                // GitHub reposundan kodu çekiyoruz
                git 'https://github.com/aybukecnz/microservices.git'
            }
        }

        stage('Build Payment Service Docker Image') {
            steps {
                script {
                    // Payment Service için Docker imajını build ediyoruz
                    dir('payment_service') {
                        docker.build("${REGISTRY}/${PAYMENT_SERVICE_IMAGE}:latest")
                    }
                }
            }
        }

        stage('Build Notification Service Docker Image') {
            steps {
                script {
                    // Notification Service için Docker imajını build ediyoruz
                    dir('notification_service') {
                        docker.build("${REGISTRY}/${NOTIFICATION_SERVICE_IMAGE}:latest")
                    }
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

        stage('Run Unit Tests for Notification Service') {
            steps {
                script {
                    // Notification Service için unit testlerini çalıştırıyoruz
                    dir('notification_service') {
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Push Payment Service Docker Image') {
            steps {
                script {
                    // Docker Hub'a Payment Service imajını push ediyoruz
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        docker.image("${REGISTRY}/${PAYMENT_SERVICE_IMAGE}:latest").push()
                    }
                }
            }
        }

        stage('Push Notification Service Docker Image') {
            steps {
                script {
                    // Docker Hub'a Notification Service imajını push ediyoruz
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        docker.image("${REGISTRY}/${NOTIFICATION_SERVICE_IMAGE}:latest").push()
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

        stage('Deploy Notification Service to Kubernetes') {
            steps {
                script {
                    // Notification Service için Kubernetes'e deploy işlemi
                    dir('notification_service') {
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
