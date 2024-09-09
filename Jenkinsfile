pipeline {
    agent any

    environment {
        PROJECT_NAME = 'product_manager'
        DOCKER_IMAGE = "${PROJECT_NAME}_image"
        CONTAINER_NAME = "${PROJECT_NAME}_container"
        PORT = "8002"
    }

    stages {
        stage('Build') {
            steps {
                // Construir la imagen Docker
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Deploy') {
            steps {
                // Detener y eliminar el contenedor anterior si existe
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'

                // Desplegar la aplicación en un nuevo contenedor
                sh 'docker run -d --name $CONTAINER_NAME -p $PORT:$PORT $DOCKER_IMAGE'
            }
        }
    }
}
