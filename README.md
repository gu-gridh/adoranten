# Adoranten
Repository for Adoranten. Nicer text tbc

## Local Installation

Create a conda environment based on the environment file and activate it.

```bash
$ conda env update --file environment.yml
$ conda activate adoranten
```

Create a .env file with contents similar to this:
```bash
SECRET_KEY="<your-secret-key>"
DB_NAME="adoranten"
DB_USER="<user>"
DB_PASS="<password>"
DB_LOCAL_PASS="<local-password>"
LOCAL_HOST="localhost"
HOST="<gridh07>"
PORT="<postgres-port>"
DJANGO_ALLOWED_HOSTS="<allowed-hosts>"
MEDIA_ROOT="<media-root"
MEDIA_URL="<media-url>"
STATIC_ROOT="<static-root>"
STATIC_URL="<static-url>"
ORIGINS="<trusted-origins>"
```

Set up a local postgres database. Populate it by running migrations and create a superuser for it.
```bash
$ cd adoranten
$ ./manage.py migrate
$ ./manage.py createsuperuser
```

Run the test server and go to localhost:8000
```bash
$ ./manage.py runserver
```
