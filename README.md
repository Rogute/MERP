# MERP exercise

This was made for DevsData LLC as a recruitment task.

## How to set up the project

From github clone the repository to any folder.

```bash
git clone https://github.com/Rogute/MERP.git
```

Go to this repository and set up a virtual environment.

```bash
python3 -m venv venv
```

Run your enviroment.

```bash
source venv/bin/activate
```

Install requirements.

```bash
pip install -r requirements.txt
```

Before first runing make sure to make migrations, then you can start the server.

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Go to website (in my case it will be http://127.0.0.1:8000/ )