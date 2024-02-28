from dash import html
import dash_bootstrap_components as dbc


def stat_card(children, stat_id):

    return dbc.Container(
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4(children),
                    html.H3(id=stat_id)
                ], className='text-center text-primary'
            ),
        ),
    )


def test_stat_card(stat_label, stat):

    return dbc.Card(
            dbc.CardBody(
                [
                    html.H4(stat_label),
                    html.H3(stat)
                ], className='text-center text-primary'
            ),
        )


def spec_log_radio(radio_id):

    return dbc.Container(
        dbc.RadioItems(
            id=radio_id,
            options=['CHARGES', 'CHARGES on LOGarithmic Scale'],
            value='CHARGES'
        )
    )


def add_footer():

    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H4("Tynan HealthCare Portal"),
                    html.H6("James Tynan Mattingly Jr.")
                ],
                className='text-center'
            )
        ], className='border-0 mt-4'
    )