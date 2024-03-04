from dash import html, dcc
import dash_bootstrap_components as dbc
from src.nav_and_utilities import ids


##############################################
#         COMPONENTS FOR LAYOUT FILE
##############################################

title_box = html.H2("Corporate Services",
                    id=ids.CORP_TITLE_SERVICES,
                    className='text-secondary p-2')

icd_dropdown_box = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H4("Select Category",className='text-secondary text-center mt-3')
            ),
        ),
        dbc.Row(
            dbc.Col(
                dcc.Dropdown(
                    id=ids.CORP_SERVICES_DROPDOWN,
                    options=['Injury_Disease', 'Specialty', 'Facility'],
                    value='Injury_Disease',
                    clearable=False,
                    persistence='session',
                    className='text-secondary fs-4 mt-2',
                    style={'width': 200}
                ),
                className='d-flex justify-content-center mb-3'
            )
        )
    ]
)

corp_services_count_card = dbc.Card(
    [
        dcc.Graph(id=ids.CORP_SERVICES_COUNT)
    ]
)

corp_services_paid_card = dbc.Card(
    [
        dcc.Graph(id=ids.CORP_SERVICES_PAID)
    ]
)

corp_services_racing = dbc.Card(
    [
        dcc.Graph(id=ids.CORP_SERVICES_RACING)
    ]
)