from dash import html, dcc
import dash_bootstrap_components as dbc
from src.nav_and_utilities import ids


##############################################
#         COMPONENTS FOR LAYOUT FILE
##############################################


# Style for dbc.cards below
card_style = 'text-center text-body-emphasis py-2 bg-primary border rounded-4'


title_box = html.H2(id=ids.MEM_TITLE_DASHBOARD,
                    className='text-secondary mt-3'
                    )


member_dropdown_box = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H4('Select Member',
                        className='text-secondary text-center mt-3'
                        )
            )
        ),
        dbc.Row(
            dbc.Col(
                dcc.Dropdown(
                    id=ids.MEM_ACCT_DROPDOWN,
                    options=[1, 2, 3, 4],
                    value=1,
                    clearable=False,
                    persistence='session',
                    className='text-secondary fs-4 mt-2',
                    style={'width': 100}
                ),
                className='d-flex justify-content-center mb-3'
            )
        ),
    ]
)


mem_ann_charge = dbc.Card(
    [
        html.H4('Charges'),
        html.H4(id=ids.MEM_ANNUAL_CHARGE)
    ],
    className=card_style,
)


mem_ann_average = dbc.Card(
    [
        html.H4('Avg Charge'),
        html.H4(id=ids.MEM_ANNUAL_AVERAGE)
    ],
    className=card_style
)


mem_ann_claims = dbc.Card(
    [
        html.H4('Claims'),
        html.H4(id=ids.MEM_ANNUAL_CLAIMS)
    ],
    className=card_style
)


mem_ann_items = dbc.Card(
    [
        html.H4('Claim Items'),
        html.H4(id=ids.MEM_ANNUAL_ITEMS)
    ],
    className=card_style
)


specialty_section_title = html.H3("Annual Summary of Charges by Specialty",
                                  className='text-center',
                                  style={'color': '#32FBE2'}
                                  )


specialty_bar_log_radio_box = dbc.Container(
    [
        dbc.Col(
            [
                dbc.RadioItems(
                    id=ids.MEM_SPEC_BAR_RADIO,
                    options=['CHARGES', 'CHARGES on LOGalgorithmic Scale'],
                    value='CHARGES',
                    className='d-flex justify-content-evenly text-secondary fs-6',
                )
            ],
        ),
    ]
)


specialty_scatter_log_radio_box = dbc.Container(
    [
        dbc.Col(
            [
                dbc.RadioItems(
                    id=ids.MEM_SPEC_SCATTER_RADIO,
                    options=['CHARGES', 'CHARGES on LOGalgorithmic Scale'],
                    value='CHARGES',
                    className='d-flex justify-content-evenly text-secondary fs-6',
                )
            ]
        )
    ]
)
