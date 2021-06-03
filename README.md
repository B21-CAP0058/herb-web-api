# Web Api Description
comingsoon

# Dev ENV

- Python 3.6
- SQLite/MySQL
- Ubuntu

## Setting up for local development

### Install virtualenv
```
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
```

### Create virtualenv

```
python3 -m venv venv
```

### Activate virtualenv

```
source venv/bin/activate
```

### Install Dependecies

```
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

### Setting DB

- Copy `.env.example` to `.env`
- Fill the right config on `.env`

### Setting FLASK ENV

```
export FLASK_APP=main.py
```

### Migrate DB

```
flask db init
flask db migrate
flask db upgrade
```

### Seed Data

```
flask seed-data
```

### Run on local

```
flask run
```

# API Documentation

comingsoon

