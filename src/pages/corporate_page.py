import dash
from dash import html
import dash_bootstrap_components as dbc


dash.register_page(__name__,
                   path='/corporate',
                   name='Corporate',
                   title='Corporate',
                   description='Corporate Level Claim Data'
                   )

layout = dbc.Container(
    [
        html.H1("CORPORATE PAGE - UNDER CONSTRUCTION", className='mt-5 text-primary text-center')
    ]
)
