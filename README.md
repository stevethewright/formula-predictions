# formula-predictions

Predictions based game for predicting F1 results &amp; events each weekend.

# Roadmap

# Development

For development on formula-predictions, it can be run locally on your machine or via the docker compose.

## Running Live Serve

### Docker Compose

Running in live serve mode via Docker Compose is the ideal way to develop.

The frontend will need to be setup locally as the node image requires this. See [Running Locally - README.md](./frontend/README.md#running-locally) in the frontend directory for how to do this.

Once frontend is setup locally, formula-predictions can be built at the parent dir, in serve mode with:

```sh
docker compose -f docker-compose.serve.yml
```

Once built, run:

```sh
docker compose up
```

Updating files on the frontend or backend will reload each container.

### Local

For local development, see Running Locally in the README files for [frontend](./frontend/README.md#running-locally) and [backend](./backend/README.md#running-locally) .
