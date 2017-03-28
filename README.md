Mini market book
====================

Run project
--------------------

1. Create virtualenv.
```sh
$ virtualenv -p /usr/bin/python3.6 evn_py3
$ cd env_py3
$ source bin/activate
```

2. Create folder for project.
```sh
$ mkdir src
$ cd src
$ git clone https://github.com/ivanhrushkatwo/booklibrary.git
```

3. Install dependencies.
```sh
$ cd locallibrary
$ pip install -r requirements.txt
```

4. Last step.
```sh
$ python manage.py runserver
```

open in browser [http://localhost:8000](http://localhost:8000)

