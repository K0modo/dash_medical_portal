from dash import html
import dash_bootstrap_components as dbc
from src.nav_and_utilities import util_tools
from src.tab_views_corporate import corp_tab_dashboard_components as D


##############################################
#      LAYOUT LINKED TO COMPONENTS FILE
##############################################


def render_corp_tab_dashboard():

    return dbc.Container(
        [
            dbc.Row(
                [
                    D.title_box
                ],
                className='text-center mb-0'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            D.period_dropdown_box
                        ],
                    )
                ],
                className='mb-2'
            ),
            dbc.Row(
                [
                    html.H3("MEDICAL CLAIMS PROCESSED", className='text-secondary text-center p-2')
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            D.corp_daily_claims_card
                        ],
                        className='col-5 border border-primary border-3 p-0',
                    ),
                    dbc.Col(
                        [
                            D.corp_annual_claims_card
                        ],
                        className='col-5 border border-primary border-3 p-0',
                    )
                ],
                className='justify-content-evenly'
            ),
            dbc.Row(
                [
                    html.H3("MEDICAL CLAIMS PAID", className='text-secondary text-center p-2')
                ],
                className='mt-5'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            D.corp_daily_paid_card
                        ],
                        className='col-5 border border-primary border-3 p-0',
                    ),
                    dbc.Col(
                        [
                            D.corp_annual_paid_card
                        ],
                        className='col-5 border border-primary border-3 p-0',
                    )
                ],
                className='justify-content-evenly'
            ),
            dbc.Row(
                [
                    html.H3("MEMBER PARTICIPATION", className='text-secondary text-center p-2')
                ],
                className='mt-5'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            D.corp_period_member_card
                        ],
                        className='col-5 border border-primary border-3 p-0',
                    ),
                    dbc.Col(
                        [
                            D.corp_annual_member_card
                        ],
                        className='col-5 border border-primary border-3 p-0',
                    ),
                ],
                className='justify-content-evenly '
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            util_tools.add_footer()
                        ]
                    )
                ], className='my-5'
            )
        ]
    )
