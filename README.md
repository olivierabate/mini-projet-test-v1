[comment]: <> (Run Postgres database :)
[comment]: <> (`docker compose up -d db`)

# mini-projet-test-v1

Simple CRUD API using Docker, Flask and Postgres.

## How to use 

Get the repo locally :

`git clone 

Build and launch Python app (first time) : 

`docker compose up --build pythonapp`

Launch Python app (if image already built) : 

`docker compose up`

### Routes :

* **Create** : `http://localhost:80/documents` (POST) body : `{"title", "text"}`

* **Read** :
  * Get all : `http://localhost:80/documents` (GET)
  * Get one : `http://localhost:80/documents/{{id}}` (GET)

* **Update** : `http://localhost:80/documents/{{id}}` (PUT) body : `{"title", "text"}`

* **Delete** : `http://localhost:80/documents/{{id}}` (DELETE)


## Test endpoints with Postman

Download `postman-test-endpoints.json` and import in Postman (File -> Import...)

## Troubleshooting

### Reinitialize Postgres database :

Enter psql from command line :

`docker exec -it db psql -U postgres`

Then type :

`SELECT * FROM document;`

`DELETE FROM document;`

`ALTER SEQUENCE document_id_seq RESTART WITH 1`

`\q`


### "Context error" :

Building the image more than once with the same tag can generate a "context" error (a `<none>` image may appear when running `docker images`).

In this case, just run `docker system prune` and build the image again with `docker compose up --build pythonapp`
  
## To do
  
* Unit tests
  
* Authentication
  
* Auto-doc OpenAPI (Swagger)
