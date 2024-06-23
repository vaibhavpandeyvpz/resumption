# starter-python

Starter template for kick-starting [Python](https://www.python.org/) API projects.

## Prepare

Before running the project, go to [ngrok](https://ngrok.com/) and create a free account.
Once logged in, make note of the auth token.

## Usage

Run below commands in project folder:

```shell
# create ngrok config
cp ngrok.dist.yml ngrok.yml

# update values in ngrok.yml file e.g., your_authtoken_here and domain (optional)

# create app config
cp config.dist.ini config.ini

# start the services
docker compose up -d
```

Server should be up & running on [127.0.0.1:8000](http://127.0.0.1:8000/).

If you are using bundle [MySQL](https://www.mysql.com) database (powered by [SQLAlchemy](https://www.sqlalchemy.org)), run migrations using below commands:

```shell
# spawn a shell
docker compose exec cron sh -c "poetry shell"

# run all migrations
alembic upgrade head
```

## Development

This project includes a cron job scheduled to run `poe welcome` command (see `app/cli.py`) every hour.
You can also use below command to run it on demand (or any added command) anytime.

```shell
# spawn a shell
docker compose exec cron sh -c "poetry shell"

# run "welcome" command
poe welcome
```

You can test the API by calling `/` endpoint as below:

```shell
curl -X GET \
  -H "accept: application/json" \
  http://127.0.0.1:8000/
```

To get [ngrok](https://ngrok.com/) public URL from container, use below command (requires [jq](https://jqlang.github.io/jq/)):

```shell
curl --silent -X GET http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url'
```
