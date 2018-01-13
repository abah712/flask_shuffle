import os

activate_this = '/webroot/flask_shuffle/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
    
    os.environ["FLASK_APP"] = "flask_shuffle.py"

    from flask_shuffle import app as application
