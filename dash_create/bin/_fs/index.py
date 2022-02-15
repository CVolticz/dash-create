# Main Page of the Application
from components.app import app
from dash import html

# import all the front-end connectors
from components.navigator import navigator

# allow for serving the app on a server
server = app.server

# enable layout re-eval on request
def serve_layout():
    return html.Div([navigator])

app.layout = serve_layout


if __name__ == '__main__':
    # apps.run_server(debug=True)
    app.run_server(debug=True, host='localhost', port=3000,
                   dev_tools_ui=True, dev_tools_props_check=True)
