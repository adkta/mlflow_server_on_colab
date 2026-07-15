## Steps
### Create a new virtual environment on colab and add pip.  

Create virtual environment.\
```
PROJ_NAME = 'mlflow_test'
mkdir --parents {PROJ_NAME}/env
python3 -m venv {PROJ_NAME}/env
```

Add pip.\
```
wget https://bootstrap.pypa.io/get-pip.py
./{PROJ_NAME}/env/bin/python3 get-pip.py
rm get-pip.py
```

### Install necessary dependencies from requirements.txt within the new virtual environment.  
Clone this repository into your folder and install necessary dependencies from requirements.txt file:\

```
{PROJ_NAME}/env/bin/pip install -r /content/{PROJ_NAME}/mlflow_server_on_colab/requirements.txt
```

### Run mlflow tracking server

Add 'NGROK_AUTH=<your_auth_key>' to the environment variables.\
Run: \
```/path/to/new/env/python3 -m <namespace_package>.mlflow_server```
