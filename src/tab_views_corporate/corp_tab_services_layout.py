import dash_bootstrap_components as dbc
from src.nav_and_utilities import util_tools
from src.tab_views_corporate import corp_tab_services_components as S

##############################################
#      LAYOUT LINKED TO COMPONENTS FILE
##############################################


def render_corp_tab_services():

    return dbc.Container(
        [
            dbc.Row(
                [
                    S.title_box
                ], className='text-center mb-0'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            S.icd_dropdown_box
                        ],
                        className=''
                    )
                ], className='mb-2'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            S.corp_services_count_card
                        ],
                        className='col-5 border border-primary border-3 p-0'

                    ),
                    dbc.Col(
                        [
                            S.corp_services_paid_card
                        ],
                        className='col-5 border border-primary border-3 p-0'
                    )
                ],
                className='justify-content-evenly mb-4'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            S.corp_services_racing
                        ],
                        className='col-9 border border-primary border-3 p-0'
                    )
                ], className='justify-content-center'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            util_tools.add_footer()
                        ]
                    )
                ], className='my-5'
            ),
        ]
    )
