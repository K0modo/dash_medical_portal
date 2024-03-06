import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path='/',
                   name='Home',
                   title='Portals',
                   description='Cards to Login'
                   )

member_card = dbc.Card(
    [
        dbc.CardImg(src='assets/images/member1.jfif', alt='healthcare_binder', top=True,
                    style={'width': '100%', 'height': '15vw', 'object-fit': 'cover'}),
        dbc.CardBody(
            [
                html.H4("Membership", className='card-title text-center'),
                dbc.ListGroup(
                    [
                        dbc.ListGroupItem('Member Dashboard'),
                        dbc.ListGroupItem('Specialty Statistics'),
                        dbc.ListGroupItem('Specialty Detail'),
                        dbc.ListGroupItem('Claim Details'),
                    ],
                    flush=True,
                ),
                html.Div(
                    [
                        dbc.Button('LOG IN', href='/member', className='mt-4')
                    ],
                    className='d-flex justify-content-center'
                )
            ]
        )
    ],
    className='h-100'
)

corporate_card = dbc.Card(
    [
        dbc.CardImg(src='assets/images/admin1.jfif', alt='administration', top=True,
                    style={'width': '100%', 'height': '15vw', 'object-fit': 'cover'}),
        dbc.CardBody(
            [
                html.H4("Corporate", className='card-title text-center'),
                dbc.ListGroup(
                    [
                        dbc.ListGroupItem('Claims Processed & Paid'),
                        dbc.ListGroupItem('Member Participation'),
                        dbc.ListGroupItem('Claims by Category'),
                        dbc.ListGroupItem('Category by Period'),
                    ],
                    flush=True,
                ),
                html.Div(
                    [
                        dbc.Button('LOG IN', href='/corporate', className='mt-4')
                    ],
                    className='d-flex justify-content-center'
                )
            ]
        )
    ],
    className='h-100'
)

analytics_card = dbc.Card(
    [
        dbc.CardImg(src='assets/images/data1.jfif', alt='healthcare_binder', top=True,
                    style={'width': '100%', 'height': '15vw', 'object-fit': 'cover'}),
        dbc.CardBody(
            [
                html.H4("Analytics", className='card-title text-center'),
                dbc.ListGroup(
                    [
                        dbc.ListGroupItem('Claims Distribution'),
                        dbc.ListGroupItem('Claims by Quarter/Period'),
                        dbc.ListGroupItem('Heat Map'),
                        dbc.ListGroupItem('Category by Group'),
                    ],
                    flush=True,
                ),
                html.Div(
                    [
                        dbc.Button('LOG IN', href='/analytics', className='mt-4')
                    ],
                    className='d-flex justify-content-center'
                )
            ]
        )
    ],
    className='h-100'
)

layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1('Health Analytic Portals', className='mt-2 text-center'),
                className='my-3'
            )
        ),
        dbc.Row(
            [
                dbc.Col(member_card),
                dbc.Col(corporate_card),
                dbc.Col(analytics_card)
            ]
        )
    ],
    className='mt-1'
)
