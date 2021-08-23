import flask
from config import config
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS

csrf = CSRFProtect()


def create_app(config_name):
    env_config = config[config_name]

    app = flask.Flask(__name__)
    app.config.from_object(env_config)
    config[config_name].init_app(app)

    CORS(app)

    csrf.init_app(app)

    with app.app_context():
        from app.bot import bp_surf_bot
        app.register_blueprint(bp_surf_bot)

    csrf.exempt(bp_surf_bot)

    return app
