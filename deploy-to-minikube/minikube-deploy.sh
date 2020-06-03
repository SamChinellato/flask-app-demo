#!/bin/bash
set -e
echo "Deploying to Minikube...."
echo "Make sure you have docker and minikube installed on your local machine"
echo "######################"
echo "#Starting minikube ###"
echo "######################"
minikube start
echo "######################"
echo "#Setting up minikube #"
echo "######################"
echo "Exposing local Docker Images to Minikube"
eval $(minikube docker-env)
echo "##########################"
echo "# Building Docker Image ##"
echo "##########################"
docker image build -t flask-app-server ../
echo "Docker image built successfully!"
echo "#######################"
echo "# Creating deployment #"
echo "#######################"
kubectl apply -f ./deployment.yml
echo "#############################################################################################"
echo "#############################################################################################"
echo "Deployment Successfull! Run 'kubectl get pods' to see deploted pods."
echo "To view deploted pods: 'minikube dashboard'"
echo "Test the deployment by curling a pod from busybox"
echo "#############################################################################################"
echo "To log in to busybox: 'kubectl run busybox --image=busybox -it --restart=Never -- /bin/sh'"
echo "#############################################################################################"
echo "#############################################################################################"