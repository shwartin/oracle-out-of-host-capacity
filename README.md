# Oracle-Out-of-host-capacity
Script to solve the problem of "out of host capacity" on Oracle Cloud while creating A1 Instances.

# Installation python and packeges

Install virtualenv:
```
virtualenv env
```

Activate virtualenv:
```
source env/bin/activate
```

Install requirements:
```
pip install --upgrade pip
pip install -r requirements.txt
```

# Generating API key and saving configuration

Full instruction: https://github.com/hitrov/oci-arm-host-capacity#generating-api-key

Save API key. 

Save configuration file to the file `~/.oci/config` and setup `key_file` as path to the API key.

# Setting up instance parameters

Create .env file
```
cp .env.example .env
```

Get all variables for the instance like described here: https://github.com/hitrov/oci-arm-host-capacity#instance-parameters

# Runing

```
python main.py
```

# Waiting
...