
# SETUP

You will need to install

- python 3
- [virtualenv wrapper](http://virtualenvwrapper.readthedocs.io/en/latest/)


1. clone this repo

2. create virtualenv:

    `mkvirtualenv shortlist`

3. Activate virtualenv:

    `workon shortlist`

4. Install requirements:

    `pip install -r requirements.txt`


# How to run the script
open a terminal window

navigate into the shortlist directory and type the following command

```cmd
$ python app.py --file ./sample.txt

```
you may replace


# Running tests

```cmd
$ pytest test.py

```