# Oracle-Out-of-host-capacity
Script to solve the problem of "out of host capacity" on Oracle Cloud while creating A1 Instances.

# Install

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

# Set up environmets

Create .env file
```
cp .env.example .env
```

Fill out all variables like described here: https://github.com/hitrov/oci-arm-host-capacity

# Run

```
python main.py
```

# Wait