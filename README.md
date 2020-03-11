# Useful commands

Build docker container

    docker build -t mksmtn/k8s-hello-world

Push docker container to its repository

    docker push mksmtn/k8s-hello-world

Start local cluster

    minikube start

Authenticate in DO

    doctl auth init

Connect this folder to DO project

    doctl kubernetes cluster kubeconfig save protsci-s1


Make DO serve this project

    kubectl --context do-frai-protsci-s1 apply -f k8s.yaml 

Expose DO serve to the world

    kubectl --context do-fra1-protsci-s1 expose deployment hello-world --type=LoadBalancer --name=hello-world

Update kubernetes docker image

    kubectl patch deployment web -p "{\"spec\":{\"template\":{\"metadata\":{\"labels\":{\"date\":\"`date +'%s'`\"}}}}}"
