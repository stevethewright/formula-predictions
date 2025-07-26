# formula-predictions - Backend

Backend for the predictions based game for predicting F1 results &amp; events each weekend.

# Running Locally

## Linux

Local running of the backend is requires python (recommended v3.12.3) and pip.

In `/backend/src`, create a python virtual environment:

```sh
python3 -m venv .venv
```

Activate the virtual environment by running:

```sh
source .venv/bin/activate
```

You can verify the python virtual environment has been activated:

```sh
which python
```

This should return a path to python within the new virtual environment just created.

At `/backend/src`, with the virtual environment active, install the python packages with:

```sh
pip install -r requirements.txt
```

Once installation is complete, the backend can be run with:

```sh
uvicorn main:app --reload
```
