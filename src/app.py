from dash import Dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import warnings

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"


class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


db = SQLAlchemy()

server = Flask(__name__)
server.config.from_object(Config)
db.init_app(server)

with warnings.catch_warnings():
    warnings.simplefilter("ignore", FutureWarning)


app = Dash(__name__,
           use_pages=True,
           server=server,
           external_stylesheets=[dbc.themes.VAPOR, dbc_css, dbc.icons.BOOTSTRAP, dbc.icons.FONT_AWESOME],
           suppress_callback_exceptions=True,
           meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}]
           )

load_figure_template('vapor')

server = app.server
