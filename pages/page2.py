import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.H1(children='Portfolio Construction'),

    html.Div(children='''
        This is our Home page content.
    '''),

])