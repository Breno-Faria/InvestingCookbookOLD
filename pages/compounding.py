import dash
from dash import html, dcc

dash.register_page(__name__, path='/compounding')



layout = html.Div(children=[
    html.H1(children='Compounding :What is an interest rate?'),
    html.Div(children=[
        html.H3(children='Initial Investment'),
        dcc.Slider(0.0, 0.2, 0.05,
                value=0.1,
                id='my-slider'
        ),
        html.H3(children='Annual Interest Rate'),
        dcc.Input(
        placeholder='Enter an initial amount ...',
        type='number',
        value=1000
    ),
        html.Div(id='slider-output-container'),
        
    
    ], style ={'height': 350, 'width': 200,}),
    

    html.Div(children='''
        This is our Home page content.
    '''),

])