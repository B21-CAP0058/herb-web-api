# Leafwell Description
Leafwell is apps for herbal identification through images, this is the part of the project as web api to deliver data to mobile apps.

# Database schema

![database](https://raw.githubusercontent.com/sahalaww/bangjek-web/main/docs/db-scheme.png?raw=True)


# Dev ENV

- Python 3.6
- SQLite/MySQL
- Ubuntu

## Setting up for local development

### Install virtualenv
```bash
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
```

### Create virtualenv

```bash
python3 -m venv venv
```

### Activate virtualenv

```bash
source venv/bin/activate
```

### Install Dependecies

```bash
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

### Setting DB

- Copy `.env.example` to `.env`
- Fill the right config on `.env`

### Setting FLASK ENV

```bash
export FLASK_APP=main.py
```

### Migrate DB

```bash
flask db init
flask db migrate
flask db upgrade
```

### Seed Data

```bash
flask seed-data
```

### Run on local

```bash
flask run
```

# Deploy on Production

- Configure serverless VPC, [link](https://cloud.google.com/vpc/docs/configure-serverless-vpc-access)
- Create Cloud SQL, and connect them to serverless VPC
- Deploy the image using cloud builds and cloud run

```bash
git clone https://github.com/sahalaww/bangjek-web
cd bangjek-web
cp .env.example .env
gcloud builds submit --tag gcr.io/$PROJECT_ID/$IMAGE_NAME:$version
gcloud run deploy $SERVICE_NAME --image $IMAGE_URL --region $REGION 
```

# Live Web Apps

[https://herb-bangjek-oiabruca3q-et.a.run.app](https://herb-bangjek-oiabruca3q-et.a.run.app)

[https://herb.azzic.xyz](https://herb.azzic.xyz)
# API Documentation

You can visit our wiki : [link](https://github.com/sahalaww/bangjek-web/wiki/API-Documentation)

