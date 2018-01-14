

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

Then clone the project fom Github:

```
git clone https://github.com/l-dfa/flask_shuffle.git
```

You'll get this base structure:

```
.../flask_shuffle
      |- flask_shuffle
          |- static
          |- templates
          flask_shuffle.py
          <other stuff>
      setup.py
      <other stuff>
```

Now create
the environment, activate it, install *Flask*.

Seems difficult? Not really. Do these:

```
cd flask_shuffle
virtualenv venv         # load Python and core libs in flask_shuffle/venv
. venv/bin/activate     # (in Windows: venv\Scripts\Activate) start isolation
pip install Flask       # install Flask in flask_shuffle/venv
```

### Installing

Using the activated development environment, install the application as
follows.

Install the application (--editable: in case of corrections it isn't necessary
 to reinstall all from start):

```
pip install --editable .           # install flask_shuffle project
```

Set the environment with the application file, and if you wish, with 
the debugging option:

```
export FLASK_DEBUG=true            # (windows? use: SET FLASK_DEBUG=true)
export FLASK_APP=flask_shuffle.py  # (windows? use: SET FLASK_APP=flask_shuffle.py)
```

Go to the application home directory (.../flask_shuffle/flask_shuffle) and 
once, and only once, initialize the database.

```
cd flask_shuffle
flask initdb
```

Run the development web service:

```
flask run
```

And now you can browse to http://127.0.0.1:5000 to see ... an empty
window. Of course: we have an empty database.

To add terms to show, make login using user *admin* with 
password *default*. Then click on *add* to show the word data entry form.
Compile and submit it.

When you have some terms in, you can show randomly one term at time
clicking on *Shuffle*.

## Deployment

You can found general instructions to deploy *Flask* applications in production 
environment at [this address](http://flask.pocoo.org/docs/0.12/deploying/).

However, if you wish to deploy on a server using Apache (httpd service) with
*mod_wsgi*, and 
using virtualenv to isolate your flask_shuffle application from server
environment, you could check and adapt these files:

* *shuffle.domain.org.conf* contains a tipical httpd configuration
  of a virtual host answering at http://shuffle.domain.org address, with
  deployment directory /webroot/flask_shuffle.
  
  Be aware of *WSGIDaemonProcess*. Here you must indicate *python-path*
  with correct *site-packages* location. If you have more than one
  python versions, it's possible you must indicate the correct python version,
  here: *.../python3.5/site-packages*.
  
* *flask_shuffle/flask_shuffle/flask_shuffle.wsgi* implements the 
  wsgi application starting flask_shuffle from /webroot/flask_shuffle.

Of course it's necessary install using *virtualenv*. So assuming your server
has:

* *Centos* v.6.x,
* *Apache* already installed and configured as vhosts,
* *git* installed,
* *Python* version 3.5 as *python3.5*,
* *virtualenv* already installed,
* */webroot* as root for web sites,
* domain *shuffle.domain.org* correctly configured via DNS to your server IP,

you could use the following instructions:

```
cd /webroot
git clone https://github.com/l-dfa/flask_shuffle.git
cd flask_shuffle
virtualenv -p python3.5 venv
. venv/bin/activate
pip install Flask
pip install --editable .
```

Only once, it's necessary initialize the database:

```
cd flask_shuffle
export FLASK_APP=flask_shuffle.py 
flask initdb
```

**Attention**. Change user and password cabled in *flask_shuffle.py*. Search for 
USERNAME and PASSWORD in file using a whatever text editor.


Include the Apache configuration contained in *shuffle.domain.org.conf* file
in */etc/http/conf/httpd.conf* file. Better: maintaining this file 
displaced from httpd.conf, and including its contents using the directive: 

```
Include /etc/httpd/conf/vhosts/shuffle.domain.org.conf
```

Finally, don't forget to restart Apache:

```
service httpd restart
```

## Built With

* [Python](https://www.python.org/downloads/) - developmant language
* [virtualenv](https://pypi.python.org/pypi/virtualenv/15.1.0) - to isolate the
development environment,
* [Flask](http://flask.pocoo.org/) - web development framework.

## Authors

* *Luciano De Falco Alfano* - Initial work

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

Thanks to all developers and contributors of the used language and environments.

And thanks to everyone has spent some time (his/her life!) to read, or test,
this code.
