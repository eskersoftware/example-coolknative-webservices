### Content

Example of python webservices to install with coolknative. To install this example go to:

https://github.com/eskersoftware/coolknative/


To manually deploy:
```
export U=<YOUR DOCKERHUB USERNAME>
skaffold run -d $U -f api/skaffold.yaml -n api-ns
skaffold run -d $U -f namespace1/asyncwebservice/skaffold.yaml
skaffold run -d $U -f namespace1/readwebservice/skaffold.yaml
skaffold run -d $U -f namespace1/webservice/skaffold.yaml
```

### License

MIT
