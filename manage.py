#!/usr/bin/env python
import os
from flask_script import Manager, Server, Command

from app import create_app

app = create_app(os.getenv('APP_ENV'))
manager = Manager(app)

@manager.command
def worker(name):
    from celery.bin.celery import main as celery_main
    celery_args = ['celery', 'worker', '-C',
                   '--concurrency=10', '--without-gossip',
                   '-n', '{}@%h'.format(name)]
    with app.app_context():
        loglevel = app.config.get('CELERY_LOGLEVEL', 'INFO')
        celery_args.append('--loglevel={}'.format(loglevel))
        return celery_main(celery_args)


@manager.command
def flower():
    from flower.command import FlowerCommand
    # celery_args = ['celery', 'worker', '-C',
    #                '--autoscale=10,1', '--without-gossip',
    #                '-n', 'worker1@%h']
    with app.app_context():
        flower = FlowerCommand()
        return flower.execute_from_commandline()


@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(
            rule.endpoint, methods, rule.rule))
        output.append(line)
    for line in sorted(output):
        print(line)


@manager.shell
def shell_context():
    import pprint
    import flask

    context = dict(pprint=pprint.pprint)
    context.update(vars(flask))
    context.update(vars(app))

    return context


if __name__ == '__main__':
    manager.add_command('runserver', Server('127.0.0.1', port=8003))
    manager.run()
