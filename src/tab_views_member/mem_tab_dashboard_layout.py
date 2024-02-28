from dash import html, dcc
import dash_bootstrap_components as dbc
from src.nav_and_utilities import ids, util_tools


##############################################
#      LAYOUT LINKED TO COMPONENTS FILE
##############################################
from src.tab_views_member import mem_tab_dashboard_components as M


def render_member_tab_dashboard():

    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            M.title_box
                        ],
                        className='text-center',
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            M.member_dropdown_box
                        ],
                    ),
                ],
                className='mb-4'
            ),
            dbc.Row(
                [

                    dbc.Col(
                        [
                            M.mem_ann_charge
                        ]
                    ),
                    dbc.Col(
                        [
                            M.mem_ann_average
                        ]
                    ),
                    dbc.Col(
                        [
                            M.mem_ann_items
                        ]
                    )
                ],
                className='mb-5 row-cols-1 row-cols-sm-2 row-cols-lg-4 gy-2 justify-content-around',
            ),
            dbc.Row(
                html.Hr(className='mt-1 mb-5')
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(ids.MEM_DASH_BAR_CHARGE)
                        ],
                        className='col-md-5 border border-primary border-3 p-0'
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(ids.MEM_DASH_BAR_CLAIMS)
                        ],
                        className='col-md-5 border border-primary border-3 p-0'
                    )
                ],
                className='justify-content-evenly mb-5'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(ids.MEM_DASH_PIE_FACILITY)
                        ],
                        className='col-md-5 border border-primary border-3 p-0'
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(ids.MEM_DASH_PIE_SPECIALTY)
                        ],
                        className='col-md-5 border border-primary border-3 p-0'
                    )
                ],
                className='justify-content-evenly mb-5'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(ids.MEM_DASH_BAR_PURPOSE)
                        ],
                        className='col-md-8 border border-primary border-3 p-0'
                    ),
                ],
                className='justify-content-center'
            ),
            dbc.Row(
                html.Hr(className="my-5")
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            M.bar_line_title
                        ],
                    )
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(className='col-3'),

                    dbc.Col(
                        [
                            M.specialty_bar_log_radio_box
                        ],
                        className='col-6'),

                    dbc.Col(className='col-3')
                ],
                className='mt-4'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(id=ids.MEM_SPEC_BAR_CHARGE),
                        ]
                    )
                ],
                className='mb-5'
            ),
            dbc.Row(
                html.Hr(className="my-5")
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            M.specialty_scatter_title
                        ],
                    )
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(className='col-3'),

                    dbc.Col(
                        [
                            M.specialty_scatter_log_radio_box
                        ],
                        className='col-6'
                    ),

                    dbc.Col(className='col-3'),
                ],
                className='mt-4'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(id=ids.MEM_SPEC_SCATTER),
                        ],
                    ),
                ],
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
        ],
    )
