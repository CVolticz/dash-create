"""
Main Application Loader
Use as initial entry point for application
"""
import dash
import dash_bootstrap_components as dbc


# apply bootstrap components
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

