from dash import html
import dash_bootstrap_components as dbc
from src.nav_and_utilities import util_tools


##############################################
#      LAYOUT LINKED TO COMPONENTS FILE
##############################################
from src.tab_views_member import mem_tab_claims_components as C


def render_tab_claims_view():

    return [
        html.Div(
            [
                dbc.Row(
                    [
                        C.title_box
                    ],
                    className='my-4 text-center'
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                C.claims_grid_title,
                                C.member_claims_grid,
                            ]
                        )
                    ],
                    className='mt-3 text-center'
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                C.file_name_input

                            ], className='col-3'
                        ),
                        dbc.Col(
                            [
                                C.file_save_button
                            ],
                            className='col-2'
                        )

                    ], className='mt-3'
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
        ),
    ]
