# Adoranten
Repository for Adoranten. Nicer text tbc

## Local Installation

Create a conda environment based on the environment file and activate it.

```bash
$ conda env update --file environment.yml
$ conda activate adoranten
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
