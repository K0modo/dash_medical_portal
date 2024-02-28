import dash
from dash import dcc
import dash_bootstrap_components as dbc
from nav_and_utilities import navigation, ids
from member_store.member_data_loader import data_load


from src.app import app

app.layout = dbc.Container(
    [
        dcc.Store(ids.STORE_DATA, data=data_load),
        dcc.Store(ids.STORE_MEM_ACCT, data=None),
        dcc.Store(ids.STORE_DATA_FILTER, data=None),

        navigation.render_navbar(),

        dash.page_container
    ]
)


if __name__ == '__main__':
    app.run(debug=True)