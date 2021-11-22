#/bin/bash

kubectl exec -it -n ingress-apisix  apisix-dc9d99d76-crr2c -- curl --path-as-is http://127.0.0.1:9080$1 -H 'Host: app.test'