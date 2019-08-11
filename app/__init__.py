import os
import flask as f
from config import config
from app.bot import bp_surf_bot
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

def create_app(config_name):
    env_config = config[config_name]
    current_path = os.path.dirname(os.path.realpath(__file__))

    app = f.Flask(__name__)
    app.config.from_object(env_config)
    app.url_map.strict_slashes = False
        
    csrf.init_app(app)

    app.register_blueprint(bp_surf_bot)
    csrf.exempt(bp_surf_bot)

    return app
