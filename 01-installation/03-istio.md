
# Install Istio using istioctl

## Run installation pre-check 

```istioctl x precheck```

    ➜ istioctl x precheck                                                                                  (minikube/default)
    ✔ No issues found when checking the cluster. Istio is safe to install or upgrade!
      To get started, check out https://istio.io/latest/docs/setup/getting-started/.

## Install Istio using istioctl

    ➜  01-installation git:(master) ✗ istioctl install -y --verify                                                                                 (minikube/default)
            |\          
            | \         
            |  \        
            |   \       
          /||    \      
         / ||     \     
        /  ||      \    
       /   ||       \   
      /    ||        \  
     /     ||         \ 
    /______||__________\
    ____________________
      \__       _____/  
         \_____/        
    
    ✔ Istio core installed ⛵️                                                                                                                                 
    ✔ Istiod installed 🧠                                                                                                                                     
    ✔ Ingress gateways installed 🛬                                                                                                                           
    ✔ Installation complete   

## Customize Istio configuration using IstioOperator
    $ cat <<EOF > ./minikube-istio-op.yaml
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    spec:
      meshConfig:
        accessLogFile: /dev/stdout
    EOF
    $ istioctl install -f minikube-istio-op.yaml

## Install Istio using IstioOperator Overlays
    ➜ istioctl install -f minikube-istio-op-overlay.yaml                                                   (minikube/default)
            |\          
            | \         
            |  \        
            |   \       
          /||    \      
         / ||     \     
        /  ||      \    
       /   ||       \   
      /    ||        \  
     /     ||         \ 
    /______||__________\
    ____________________
      \__       _____/  
         \_____/        
    
    This will install the Istio 1.24.2 profile "default" into the cluster. Proceed? (y/N) y
    ✔ Istio core installed ⛵️                                                                                                                                 
    ✔ Istiod installed 🧠                                                                                                                                     
    ✔ Ingress gateways installed 🛬                                                                                                                           
    ✔ Installation complete

