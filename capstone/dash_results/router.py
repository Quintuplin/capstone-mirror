from dash.dependencies import Output, Input

from .server import app, server
from . import layouts



pages = (
    ('', layouts.index),
)

routes = {f"{app.url_base_pathname}{path}": layout for path, layout in pages}


@app.callback(Output('content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    ''' '''
    if pathname is None:
        return ''

    page = routes.get(pathname, 'Unknown link')

    if callable(page):
        # can add arguments to layout functions if needed
        layout = page()
    else:
        layout = page

    return layout
