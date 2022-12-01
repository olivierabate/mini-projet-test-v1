[comment]: <> (Run Postgres database :)
[comment]: <> (`docker compose up -d db`)

# mini-projet-test-v1

Build and launch Python app (first time) : 

`docker compose up --build pythonapp`

Launch Python app (if image already built) : 

`docker compose up`

### Test endpoints with Postman

Download `postman-test-endpoints.json` and import in Postman (File -> Import...)

### Troubleshooting

Building the image more than once with the same tag can generate a "context" error (a <none> image may appear when running `docker images`).
  In this case, just run `docker system prune` and build the image again with `docker compose up --build pythonapp`
