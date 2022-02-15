from .app import app
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output


# setting up control schema
sidebar = html.Div(
    [
        html.H2('Dash Application Template', className='text-style'),
        html.Hr(),
        dbc.Nav(
            children = [
                dbc.NavLink("Page 1", href="/", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
                dbc.NavLink("Page 3", href="/page-3", active="exact"),
            ],
            pills=True,
        ),
        html.Hr(),
        html.Div([
            html.Div(
                children = [
                    html.H3("An Awesome Full Stack Application")
                ]
            ),
        ]),
    ], 
    className='nav-bar',
)

navigator = html.Div(
    children= [
        dcc.Location(id="url", refresh=False),
        sidebar,
        html.Div(id="page-content", className='content-style'),
    ]
)

# page navigator
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/":
        return html.Div(html.H1("Page 1"))
    elif pathname == "/page-2":
        return html.Div(html.H1("Page 2"))
    elif pathname == "/page-3":
        return html.Div(html.H1("Page 3"))
    else: return '404 Error: Page not Found'

