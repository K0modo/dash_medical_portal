import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path='/analytics',
                   name='Analytics',
                   title='Analytics',
                   description='Analytical Data Analysis'
                   )

layout = dbc.Container(
    [
        html.H1("ANALYTICS PAGE - UNDER CONSTRUCTION", className='mt-5 text-primary text-center')
    ]
)