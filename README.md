

# Flask-Shuffle

A simple web application to show randomly a word from a pool of
terms.

## Getting Started

These instructions will get you a copy of the project up and running
on your local machine for development and testing purposes. See deployment
for notes on how to deploy the project on a live system.

### Prerequisites

You need [Python](https://www.python.org/downloads/) as developmant language,
[virtualenv](https://pypi.python.org/pypi/virtualenv/15.1.0) to isolate the
development environment, and [Flask](http://flask.pocoo.org/) as
web development framework.

If you have a recent version of *Python*, good. Otherwise download and 
install it from the previous link.

Then, if needed, you can install *virtualenv* using: 

```
pip install virtualenv
```

Create a directory to host the project (*.../flask_shuffle*), create
the environment, activate it, install *Flask*.

Seems difficult? Not really. Do these:

```
mkdir flask_shuffle
cd flask_shuffle
virtualenv venv         # load Python and core libs in flask_shuffle/venv
. venv/bin/activate     # (in Windows: venv\Scripts\Activate) start isolation
pip install Flask       # install Flask in flask_shuffle/venv
git ...
pip install .           # install flask_shuffle project
cd flask_shuffle
export FLASK_APP=flask_shuffle.py
flask initdb
flask run
```

### Installing

Using the activated development environment, install the application as
follows.

Download the application, and install it:

```
git ...
pip install .           # install flask_shuffle project
```

go to the application home directory (.../flask_shuffle/flask_shuffle) and 
set the environment with the application file:

```
cd flask_shuffle
export FLASK_APP=flask_shuffle.py
```

Once, and only once, initialize the database.

```
flask initdb
```

Run the development web service:

```
flask run
```

And now you can browse to http://127.0.0.1:5000 to see ... an empty
window. Of course: we have an empty database.

To add terms to show make login using user *admin* with 
password *default*. Then click on *add* to show the word data entry form.
Compile and submit it.

When you have some terms in, you can show randomly one term at time
clicking on *Shuffle*.

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python](https://www.python.org/downloads/) - developmant language
* [virtualenv](https://pypi.python.org/pypi/virtualenv/15.1.0) - to isolate the
development environment,
* [Flask](http://flask.pocoo.org/) - web development framework.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc





use:

    cd flask_shuffle
    venv\Scripts\activate
    set FLASK_DEBUG=true
    set FLASK_APP=shuffle
    cd shuffle
    flask run

### development

as flask tutorial indicates

base environment:

    cd flask_shuffle
    virtualenv venv
    venv\Scripts\activate
    pip install Flask
    pip install -r requirements.txt

it's a package. to install:

    cd flask_shuffle
    venv\Scripts\activate
    pip install --editable .

### data structure ###

* foreign term,
* url to online dictionay, where we'll found (hopefully):
    * sound,
    * IPA pronunciation,
    * explanation,
* how many times application showed the term

### available functions

* add term,
* change term,
* delete term,
* show a term
    * next term
    * previous term
* show randomly a term 
    * term only
    * all data about last term showed
