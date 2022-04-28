# MLFlow Mini-project

## Aim: Host a MLFlow model registry inside a Docker container on EC2, and log experiments and models to it remotely

## Project Requirements
- MLFlow Model registry running inside a Docker container
- Docker container published to Docker Hub
- Dockerised model registry running on an EC2 instance
- Model registry reachable from any IP address
- Evaluated and tuned decision tree model on the boston housing dataset and registered them to the model registry
- Deployed the best model publicly through FastAPI or Flask