from dash import html, dcc
import dash_bootstrap_components as dbc
from src.nav_and_utilities import ids

# https://www.youtube.com/watch?v=G8r2BB3GFVY&list=PLh3I780jNsiSDHCReNVtgPC1WkqduZA5R&index=2
# https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Dash%20Components/Graph/dash-graph.py

##############################################
#         COMPONENTS FOR LAYOUT FILE
##############################################

title_box = html.H3("Analytic Dashboard",
                    className='text-center text-secondary p-2'
                    )

scatbox_chart = dbc.Container(
    [
        dcc.Graph(ids.ANALYTIC_SCATBOX_CHART,
                  figure={},
                  className='mb-5'
                  )
    ]
)

charge_claim_title = html.H3("Charges & Claims Summary",
                             className='d-flex justify-content-center text-secondary text-decoration-underline mt-5'
                             )

charges_bar_radio = dbc.Container(
    [
        html.H5("Select Period or Quarter",
                className='d-flex justify-content-center text-secondary mt-3'
                ),
        html.Div(
            [
                dcc.RadioItems(
                    id=ids.ANALYTIC_CHARGES_RADIO,
                    options=[{'label': 'Quarter', 'value': 'quarter'},
                             {'label': 'Period', 'value': 'period'}],
                    value='quarter',
                    className='col-2 text-secondary d-flex justify-content-around',
                )
            ],
            className='d-flex justify-content-center'
        )
    ]
)

charges_bar = dbc.Container(
    [
        dcc.Graph(ids.ANALYTIC_CHARGES_BAR,
                  figure={},
                  className='mt-4'
                  ),
    ]
)

claims_bar = dbc.Container(
    [
        dcc.Graph(ids.ANALYTIC_CLAIMS_BAR,
                  figure={},
                  className='mt-4'
                  ),
    ]
)

charges_ave_line = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Spinner(children=[dcc.Graph(ids.ANALYTIC_CHARGES_AVE_LINE, figure={}, className='mt-4')],
                                    # size='lg',
                                    color='info',
                                    type='border',
                                    fullscreen=True,
                                    spinner_style={"width": "8rem", "height": "8rem"}
                                    )
                    ]
                ),
            ]
        )
    ]
)

members_count_line = dbc.Container(
    [
        dcc.Graph(ids.ANALYTIC_MEMBERS_COUNT_LINE,
                  figure={},
                  className='mt-4'
                  ),
    ]
)
