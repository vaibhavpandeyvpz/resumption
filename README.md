# resumption

Dockerized microservice to extract information from PDF resumes of infinite kind and transform it into uniform [JSON](https://www.json.org/json-en.html) structure to be used for further automation.

## Usage

Firstly, download and create a `config.ini` from the published example using below command:

```shell
wget -O config.ini https://raw.githubusercontent.com/vaibhavpandeyvpz/resumption/main/config.dist.ini
```

Then run the [Docker](https://www.docker.com/) container as below:

```shell
docker run -it --rm \
  -p "8000:8000" \
  -v ./config.ini:/app/config.ini \
  ghcr.io/vaibhavpandeyvpz/resumption:latest
```

Server should be up & running on [127.0.0.1:8000](http://127.0.0.1:8000/).
You can test the API by calling `/` endpoint as below:

```shell
curl -X GET \
  -H "accept: application/json" \
  http://127.0.0.1:8000/
```

To test resume processing, refer to the include [Postman](https://www.postman.com/) collection i.e., [Resumption.postman_collection.json](Resumption.postman_collection.json).

## Development

Clone the project and run below commands in project folder:

```shell
# create app config
cp config.dist.ini config.ini

# update values in config.ini e.g., openai.*

# start the services
docker compose up -d
```
