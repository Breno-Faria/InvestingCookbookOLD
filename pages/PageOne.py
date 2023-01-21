import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from pages.sidebar import sidebar


dash.register_page(__name__, path="/test", title="Part 1/x tutorial", name="Part one")

layout = html.Div(children=[
    html.H1(children='This is our Analytics page'),
	html.Div([
        "Select a city: ",
        dcc.RadioItems(['New York City', 'Montreal','San Francisco'],
        'Montreal',
        id='analytics-input')
    ]),
	html.Br(),
    html.Div(id='analytics-output'),

    dbc.Row(
        [dbc.Col(sidebar(), width=2), dbc.Col(html.Div("Topics Home Page"), width=10)]
    )
])


@callback(
    Output(component_id='analytics-output', component_property='children'),
    Input(component_id='analytics-input', component_property='value')
)
def update_city_selected(input_value):
    return f'You selected: {input_value}'