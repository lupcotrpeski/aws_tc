from flask import Flask
import logging
from lib.getEnvVariable import getEnvVariable
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from aws_xray_sdk.core import patch_all


# Enable debug logging.
logging.basicConfig(level=logging.DEBUG)

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# # Add Amazon x-ray 
domain = getEnvVariable('DOMAIN')
plugins = ('ECSPlugin', 'EC2Plugin')
xray_recorder.configure(service="{}-frontend".format(domain), dynamic_naming="*{}*".format(domain), plugins=plugins)
patch_all()
XRayMiddleware(app, xray_recorder)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')
