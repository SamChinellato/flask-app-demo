# flask-app-demo
## A flask app demo to practice some CI/CD testing and deployment to Kubernetes (minikube)

## To clone

    git clone https://github.com/SamChinellato/flask-app-demo.git

# Running the flask app
To run the flask application, make sure python and flask are installed on your machine, then:

    flask run

From the `src` directory. 

---
 # Build and test the app using a dedicated Jenkins server
 
 [**Make sure you have docker installed on your machine**](https://docs.docker.com/get-docker/)<br><br>
 From the `jenkins-server` directory:

    docker compose up
This should spin up a jenkins server on your machine.

## Configure the jenkins job
* The activation password should be printed out in your terminal output. 
* Follow the installation guide until the jenkins server is ready. 
* Select `New Item > Multibranch Pipeline`
* Under `Branch Sources` select `github` and add `https://github.com/SamChinellato/flask-app-demo.git` as the `Repository HTTPS URL`
* Set the `Path to Jenkinsfile` as `Jenkinsfile` and press Apply and Save.

**You should now be able to build the job, which builds the app in a python 3.7.2 docker image container and tests it.** 

Once complete, test results should be displayed under the `Test Result` tab in the build.

---

# Deploying To Minikube
You can deploy the flask app to minikube by running the `minikube-deploy.sh` bash script in the deploy-to-minikube directory. 

[**Make sure you have minikube installed on your machine**](https://kubernetes.io/docs/tasks/tools/install-minikube/)

Make the script executable (from the `deploy-to-minikube` directory):

    chmod +x minikube-deploy.sh
You should then be able to run the script from the same directory with:

    ./minikube-deploy.sh
Once the script runs successfully you can see deployed pods by running:

    kubectl get pods
They should come up as `Running`

To test these are running the flask app successfully, get the IP address of deployed pods:

    kubectl get po -o wide

Run a busybox container:


    kubectl run busybox --image=busybox -it --restart=Never -- /bin/sh

Run a wget on a deployed pod:

    wget <pod-ip>:5000

You should now have 5 healthy pods running the flask app!

---

# Handy commands

## Open Minikube Dashboard
    minikube dashboard

## Expose local docker images to minikube

    eval $(minikube docker-env)

## Build a docker image (name it what you want, here it's flask-app-server) from Dockerfile directory

    docker image build -t flask-app-server

## Create deployment from deployment.yml file
    kubectl apply -f ./deployment.yml

## Run unit tests form flask-app directory
    python -m src.tests.test_basic