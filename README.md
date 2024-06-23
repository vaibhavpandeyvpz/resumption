# resumption

Dockerized microservice to extract information from PDF resumes of infinite kind and transform it into uniform JSON structure to be used for further automation.

## Usage

Run below commands in project folder:

```shell
# create app config
cp config.dist.ini config.ini

# update values in config.ini

# start the services
docker compose up -d
```

Server should be up & running on [127.0.0.1:8000](http://127.0.0.1:8000/).
You can test the API by calling `/` endpoint as below:

```shell
curl -X GET \
  -H "accept: application/json" \
  http://127.0.0.1:8000/
```
