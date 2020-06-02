# Deployment Instructions

## SSH onto minikube and see docker images on local machine
minikube ssh
    `minikube ssh` 
    `eval $(minikube docker-env)`

## Build docker image (name it what you want, here it's flask-app-server) from Dockerfile directory
`docker image build -t flask-app-server`

## Create deployment from manifest file
`kubectl run busybox --image=busybox -it --restart=Never -- /bin/sh`

## Get pods. they should be in a running state
`kubectl get pods`

## Get IP address of deployed pods
`kubectl get po -o wide`

## run the kubectl busybox
`kubectl run busybox --image=busybox -it --restart=Never -- /bin/sh`
`wget <pod-ip>:5001`

## Run unit tests form flask-app directory
`python3 -m src.tests.test_basic`