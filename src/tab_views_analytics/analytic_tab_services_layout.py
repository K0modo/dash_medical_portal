from dash import html
import dash_bootstrap_components as dbc

from src.tab_views_analytics import analytic_tab_services_components as A
from src.nav_and_utilities import util_tools


##############################################
#      LAYOUT LINKED TO COMPONENTS FILE
##############################################

def render_analytic_tab_services():

    return html.Div(
        [
            dbc.Row(
                [
                    A.title_box
                ], className='align-items-center mb-4'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            A.heat_radio
                        ]
                    )
                ],
                className='mb-4'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            A.icd_spec_chart
                        ]
                    )
                ],
                className='mb-4'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            A.chain_section_title
                        ]
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            A.chain_label
                        ]
                    )
                ]
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
