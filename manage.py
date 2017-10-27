#! /usr/bin/env python
"""Manager
Automaticaly create or drop database with single command.
This module depend on flask-script
"""
import os

from thermos import create_app, db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

"""
set environment by:
$ export THERMOS_ENV=dev
"""
app = create_app(os.getenv('THERMOS_ENV') or 'dev')
manager = Manager(app)


migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
