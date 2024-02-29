from dash import dcc
import dash_bootstrap_components as dbc

from src.nav_and_utilities import ids, util_tools


##############################################
#      LAYOUT LINKED TO COMPONENTS FILE
##############################################
from src.tab_views_member import mem_tab_services_components as S


def render_tab_services_view():

    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            S.title_box
                        ]
                    )
                ],
                className='my-4'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            S.statistics_grid_title,
                            S.statistics_grid_note
                        ]
                    )
                ],
                className='mt-3'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            S.statistics_grid
                        ]
                    )
                ],
                className='mb-2'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            S.specialty_claims_section_title
                        ]
                    )
                ],
                className='mt-5'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            S.specialty_claims_grid_title,
                            S.specialty_claims_grid
                        ],
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id=ids.MEM_SERV_GRID1_GRAPH)
                        ],
                    )
                ],
                className='d-flex align-items-end mt-4'
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
