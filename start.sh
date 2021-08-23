#!/bin/bash
gunicorn --config gunicorn_config.py manage:app
