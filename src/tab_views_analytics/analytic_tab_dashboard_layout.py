import dash_bootstrap_components as dbc
from src.nav_and_utilities import util_tools


##############################################
#      LAYOUT LINKED TO COMPONENTS FILE
##############################################
from src.tab_views_analytics import analytic_tab_dashboard_components as A


def render_analytic_tab_dashboard():

    return dbc.Container(
        [
            dbc.Row(
                [
                    A.title_box
                ],
                className='align-items-center text-center mb-5 mt-3'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            A.scatbox_chart
                        ],
                        className='col-10 border border-primary border-3')
                ],
                className='d-flex justify-content-center mb-6'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            A.charge_claim_title
                        ]
                    )
                ],
                className='mt-4'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            A.charges_bar_radio
                        ],
                    )
                ],
                className='mb-5'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            A.charges_bar
                        ],
                        className='col-5 border border-primary border-3 p-0'
                    ),
                    dbc.Col(
                        [
                            A.claims_bar
                        ],
                        className='col-5 border border-primary border-3 p-0'
                    )
                ],
                className='justify-content-evenly mb-5'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            A.charges_ave_line
                        ],
                        className='col-5 border border-primary border-3 p-0'
                    ),
                    dbc.Col(
                        [
                            A.members_count_line
                        ],
                        className='col-5 border border-primary border-3 p-0'
                    )
                ],
                className='justify-content-evenly mb-5'
            ),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            util_tools.add_footer()
                        ]
                    )
                ],
                className='my-5'
            )
        ],
    )
