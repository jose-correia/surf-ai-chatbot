#!/usr/bin/env python
import os
from flask_script import Manager, Server

from app import create_app

app = create_app(os.getenv('APP_ENV'))
manager = Manager(app)


@manager.shell
def shell_context():
    import pprint
    import flask

    context = dict(pprint=pprint.pprint)
    context.update(vars(flask))
    context.update(vars(app))

    return context


if __name__ == '__main__':
    manager.add_command('runserver', Server('127.0.0.1', port=8080))
    manager.run()
