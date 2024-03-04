from dash import html, dcc
import dash_bootstrap_components as dbc
from src.nav_and_utilities import ids

##############################################
#         COMPONENTS FOR LAYOUT FILE
##############################################

title_box = html.H2("Analytic Services",
                    className='text-secondary text-center p-2'
                    )

heat_radio = dbc.Container(
    [
        html.H4("Select Category for Heatmap",
                className='d-flex justify-content-center text-secondary mt-3'
                ),

        dbc.Row(
            [
                dbc.Col(
                    dbc.RadioItems(
                        id=ids.ANALYTIC_HEAT_RADIO,
                        options=[{'label': 'Injury_Disease', 'value': 'injury_disease_id'},
                                 {'label': 'Specialty', 'value': 'specialty_id'}],
                        value='injury_disease_id',
                        className='text-secondary d-flex justify-content-center fs-5',
                    ))
            ],
            className='d-flex justify-content-center'
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Spinner(children=[dcc.Graph(ids.ANALYTIC_HEAT_CHART, figure={})],
                                    # size='lg',
                                    color='info',
                                    type='border',
                                    fullscreen=True,
                                    spinner_style={"width": "8rem", "height": "8rem"}
                                    ),
                    ],
                    className='col-12'
                )
            ],
            className='d-flex justify-content-center'
        )
    ],
    className='border border-primary border-3'
)

icd_spec_chart = dbc.Container(
    [
        dcc.Graph(ids.ANALYTIC_HEAT_ICD_SPEC_CHART,
                  figure={},
                  className='col-12'
                  )
    ],
    className='border border-primary border-3 mt-5'
)

chain_section_title = html.H3("Chained Dropdown for Claim Group and Category",
                              className='text-center text-secondary text-decoration-underline  my-5'
                              )

chain_label = dbc.Container(
    [
        html.Label("Claims Group",
                   className='fs-3 text-secondary mt-3'
                   ),

        dcc.Dropdown(id=ids.ANAL_CHAIN_GROUP_DROP,
                     options=[{'label': 'Injury_Disease', 'value': 'injury_disease_id'},
                              {'label': 'Specialty', 'value': 'specialty_id'}],
                     value='injury_disease_id',
                     clearable=False,
                     className='fs-5 d-inline-block col-2 mb-4 text-secondary'
                     ),

        html.Label("Group Category",
                   className='fs-3 text-secondary'
                   ),

        html.Label("Click  x  to remove from chart.",
                   className='d-block col-2 fst-5 mb-3'
                   ),

        dcc.Dropdown(id=ids.ANAL_CHAIN_CATEGORY_DROP,
                     options=[],
                     multi=True,
                     className='fs-5 d-inline-block mb-2 text-secondary mb-4',
                     ),

        dcc.Graph(id=ids.ANAL_CHAIN_GRAPH,
                  figure={},
                  className='col-12 mt-5'
                  )
    ],
    className='border border-primary border-3'
)
