
## Create a istio-demo namespace:

```kubectl create namespace istio-demo```

## There are 2 ways to enable Istio sidecar injection:

### Namespace level

### Enable Istio sidecar injection for the `istio-demo` namespace:

```kubectl label namespace istio-demo istio-injection=enabled```

### Deployment level

### Add `sidecar.istio.io/inject: "true"` label to the deployment pod spec:
    ....
    ....
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: flask-ping-app
      template:
        metadata:
          labels:
            app: flask-ping-app
            sidecar.istio.io/inject: "true"
    ....
    ....
