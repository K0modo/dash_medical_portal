from dash import html, dcc
import dash_bootstrap_components as dbc
from src.nav_and_utilities import ids


##############################################
#         COMPONENTS FOR LAYOUT FILE
##############################################

title_box = html.H2("Corporate Dashboard",
                    id=ids.CORP_TITLE_DASHBOARD,
                    className='text-secondary'
                    )

period_dropdown_box = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H4('Select Period',
                        className='text-secondary text-center mt-3'
                        ),
            ),
        ),
        dbc.Row(
            dbc.Col(
                dcc.Dropdown(
                    id=ids.CORP_PERIOD_DROPDOWN,
                    options=[{"label": int(i), 'value': int(i)} for i in range(1, 13)],
                    value=1,
                    clearable=False,
                    persistence='session',
                    className='text-secondary fs-4 mt-2',
                    style={'width': 100}
                ),
                className='d-flex justify-content-center mb-3'
            )
        )
    ],
)


###########################################
#     ROW 1 CARD - MEDICAL CLAIMS PROCESSED
###########################################

corp_daily_claims_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(id=ids.CORP_DAILY_CLAIMS_CHART,
                                          figure={},
                                          config={'displayModeBar': False}
                                          )
                            ],
                            width=12
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P('Daily Claims Average', className='my-0'),
                                html.P(id=ids.CORP_DAILY_CLAIMS_AVERAGE, className='mb-0')
                            ]
                        ),
                        dbc.Col(
                            [
                                html.P('Total Claims', className='my-0', ),
                                html.P(id=ids.CORP_DAILY_CLAIMS_SUM, className='mb-0')
                            ],
                            className='text-end'
                        )
                    ]
                )
            ]
        )
    ]
)

corp_annual_claims_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(id=ids.CORP_ANNUAL_CLAIMS_CHART,
                                          figure={},
                                          config={'displayModeBar': False}
                                          )
                            ],
                            width=12
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P('YTD Period Average', className='my-0'),
                                html.P(id=ids.CORP_ANNUAL_CLAIMS_AVERAGE, className='mb-0')
                            ],
                            className='fs-6'
                        ),
                        dbc.Col(
                            [
                                html.P('Annual Total', className='my-0'),
                                html.P(id=ids.CORP_ANNUAL_CLAIMS_SUM, className='mb-0')
                            ],
                            className='fs-6 text-end'
                        )
                    ]
                )
            ]
        )
    ]
)


##############################
#     ROW 2 CARD - CLAIMS PAID
##############################

corp_daily_paid_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(id=ids.CORP_DAILY_PAID_CHART,
                                          figure={},
                                          config={'displayModeBar': False}
                                          )
                            ],
                            width=12
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P('Daily Paid Average', className='my-0'),
                                html.P(id=ids.CORP_DAILY_PAID_AVERAGE, className='mb-0')
                            ],
                            className='fs-6'
                        ),
                        dbc.Col(
                            [
                                html.P('Total Paid', className='my-0'),
                                html.P(id=ids.CORP_DAILY_PAID_SUM, className='mb-0')
                            ],
                            className='fs-6 text-end'
                        )
                    ]
                )
            ]
        )
    ]
)

corp_annual_paid_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(id=ids.CORP_ANNUAL_PAID_CHART,
                                          figure={},
                                          config={'displayModeBar': False}
                                          )
                            ],
                            width=12
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P('YTD Period Average', className='my-0'),
                                html.P(id=ids.CORP_ANNUAL_PAID_AVERAGE, className='mb-0')
                            ],
                            className='fs-6'
                        ),
                        dbc.Col(
                            [
                                html.P('Annual Total', className='my-0'),
                                html.P(id=ids.CORP_ANNUAL_PAID_SUM, className='mb-0')
                            ],
                            className='fs-6 text-end'
                        )
                    ]
                )
            ]
        )
    ]
)


##################################
#     ROW 3 CARD - MEMBER ACTIVITY
##################################


corp_period_member_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(id=ids.CORP_DAILY_MEMBER_CHART,
                                          figure={},
                                          config={'displayModeBar': False}
                                          )
                            ],
                            width=12
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P('Daily Member Average', className='my-0'),
                                html.P(id=ids.CORP_DAILY_MEMBER_AVERAGE, className='mb-0')
                            ],
                            className='fs-6'
                        ),
                        dbc.Col(
                            [
                                html.P('Total Members', className='my-0'),
                                html.P(id=ids.CORP_DAILY_MEMBER_SUM, className='mb-0')
                            ],
                            className='fs-6 text-end'
                        )
                    ]
                )
            ]
        )
    ]
)

corp_annual_member_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(id=ids.CORP_ANNUAL_MEMBER_CHART,
                                          figure={},
                                          config={'displayModeBar': False}
                                          )
                            ],
                            width=12
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P('YTD Period Average', className='my-0'),
                                html.P(id=ids.CORP_ANNUAL_MEMBER_AVERAGE, className='mb-0')
                            ],
                            className='fs-6'
                        ),
                        dbc.Col(
                            [
                                html.P('Annual Total', className='my-0'),
                                html.P(id=ids.CORP_ANNUAL_MEMBER_SUM, className='mb-0')
                            ],
                            className='fs-6 text-end'
                        )
                    ]
                )
            ]
        )
    ]
)
