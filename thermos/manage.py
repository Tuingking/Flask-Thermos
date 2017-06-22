#! /usr/bin/env python
"""Manager
Automaticaly create or drop database with single command.
This module depend on flask-script
"""

from thermos import app, db
from flask.ext.script import Manager, prompt_bool

from thermos import db
from models import User

manager = Manager(app)

@manager.command
def initdb():
    """Initialized the database"""
    db.create_all()
    print 'Initialized the database...'

@manager.command
def dropdb():
    """Drop the database"""
    if prompt_bool(
        "Are you sure you want to lose all your data"):
        db.drop_all()
        print 'Dropped the database...'

if __name__ == '__main__':
    manager.run()
