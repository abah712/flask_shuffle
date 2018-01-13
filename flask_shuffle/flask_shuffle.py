# -*- coding: utf-8 -*-
"""
    ### flask_shuffle ###

    A simple application to manage english terms. Inspired to the
    Flask tutorial, with Flask and sqlite3.

    :copyright: (c) 2018 by Luciano De Falco Alfano.
    :license: MIT (https://opensource.org/licenses/MIT),
              see LICENSE for more details.
"""

# import copy
# import pdb
import os
import sqlite3
from random import randint
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

class Term(object):
    
    def __init__( self, id=None,
                        term=None,
                        pronunciation=None,
                        response=None,
                        url=None,
                        showed=None):
        self.id   = id
        self.term = term
        self.pronunciation = pronunciation
        self.response = response
        self.url  = url
        self.showed = showed

app = Flask(__name__)            # create the application instance :)
app.config.from_object(__name__) # load config from this file


# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flask_shuffle.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('SHUFFLE_SETTINGS', silent=True)

with open('/webroot/flask_shuffle/dbname.txt', mode='a', buffering=1 ) as f:
    f.write('root: ' + app.root_path + '\n')
    f.write('db:   ' + app.config['DATABASE'] + '\n')


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    """Execute DB initialization using schema.sql."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initialize the database."""
    init_db()
    print('Initialized the database.')


@app.route('/')
def show_term():
    """Show randomly a single term."""
    db = get_db()
    cur = db.execute('''SELECT id,
                               term,
                               pronunciation,
                               response,
                               url,
                               showed
                        FROM terms
                        ORDER BY id DESC''')
    terms = cur.fetchall()
    ndx = None
    term = None
    if terms:
        ndx = randint(0, len(terms)-1)
        term = Term(terms[ndx]['id'],
                    terms[ndx]['term'],
                    terms[ndx]['pronunciation'],
                    terms[ndx]['response'],
                    terms[ndx]['url'],
                    terms[ndx]['showed'])
        db.execute('UPDATE terms SET showed = ? WHERE id = ?',
                    (term.showed + 1,
                     term.id ))        # showed: +1
        db.commit()
    return render_template('show_term.html', term=term)
    
    
@app.route('/show')
def show_terms():
    """List all terms."""
    db = get_db()
    cur = db.execute('''SELECT id,
                               term, 
                               pronunciation,
                               response,
                               url,
                               showed
                        FROM terms
                        ORDER BY term ASC''')
    terms = cur.fetchall()
    return render_template('show_terms.html', terms=terms)
    
    
@app.route('/add', methods=['GET', 'POST'])
def add_term():
    """Add a term to handle."""
    if not session.get('logged_in'):
        abort(401)
    if request.method == 'POST':
        # check errors, manage update
        db = get_db()
        db.execute( '''INSERT INTO terms
                             (term,
                              pronunciation,
                              response,
                              url,
                              showed)
                       VALUES (?, ?, ?, ?, ?)''',
                    (request.form['term'],
                     request.form['pronunciation'],
                     request.form['response'],
                     request.form['url'],
                     0))
        db.commit()
        flash('New entry ({}) was successfully added'.format(request.form['term']))
    return render_template('add_term.html')
    
    
@app.route('/modify/<int:id>', methods=['GET', 'POST'])
def modify_term(id):
    """Modify a single term."""
    if not session.get('logged_in'):
        abort(401)
    error = None
    # pdb.set_trace()
    db = get_db()
    cur = db.execute( '''SELECT id,
                                term,
                                pronunciation,
                                response,
                                url
                         FROM terms
                         WHERE id=?''',
                      (id,))
    row = cur.fetchone()
    if not row:
        abort(404)
    term = Term(row['id'],
                row['term'],
                row['pronunciation'],
                row['response'],
                row['url'])
    if request.method == 'POST':
        # check errors (?), manage update
        db.execute( '''UPDATE terms
                       SET term = ?,
                           pronunciation = ?,
                           response = ?,
                           url = ?
                       WHERE id = ?''',
                    (request.form['term'],
                     request.form['pronunciation'],
                     request.form['response'],
                     request.form['url'],
                     id ))
        db.commit()
        flash('entry {} ({}) was successfully modified'.format(id, term.term))
        return redirect(url_for('show_terms'))
    return render_template('modify_term.html', term=term, error=error)
    
    
@app.route('/delete/<int:id>', methods=['GET'])
def delete_term(id):
    """Delete a single term."""
    if not session.get('logged_in'):
        abort(401)
    error = None
    # pdb.set_trace()
    db = get_db()
    db.execute('DELETE FROM terms WHERE id = ?', (id, ))
    db.commit()
    flash('entry {} was successfully deleted'.format(id))
    return redirect(url_for('show_terms'))
    
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login user."""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_term'))
    return render_template('login.html', error=error)
    
    
@app.route('/logout')
def logout():
    """Logout user."""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_term'))
    
    
@app.template_filter()
def head_truncate(s, length=255, ellipsis='...', leeway=None):
    """Truncate head of a string.
    
    This is an Jingia2 custom filter. It acts the opposite of the
    canonical truncate filter, eliminating the left characters
    exceeding the request length.
    
    Parameters:
        s        - string to manage;
        length   - the (max) request length
        ellipsis - these substitute the truncated characters
        leeway   - if len(s) < (length-len(ellipsis)-leeway) doesn't truncate
    
    Return: a string
    """
    start = 0
    if not leeway:
        leeway = 5
    if len(s) > (length-len(ellipsis)-leeway):
        start = len(s) - (length-len(ellipsis))
    else:
        ellipsis = ''
    return ''.join((ellipsis, s[start:],))