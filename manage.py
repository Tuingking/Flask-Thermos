#! /usr/bin/env python
"""Manager
Automaticaly create or drop database with single command.
This module depend on flask-script
"""

from thermos import app, db
from thermos.models import User, Bookmark
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def initdb():
    """Initialized the database"""
    db.create_all()
    db.session.add(User(username="aloysius", email="aloysius@example.com", password="test"))
    db.session.add(User(username="yoko", email="yoko@example.com ", password="test"))
    db.session.commit()
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
