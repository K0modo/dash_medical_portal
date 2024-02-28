import dash
import pandas as pd
from dash import html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import src.nav_and_utilities.ids as ids

from src.tab_views_member import (
    mem_tabs_menu as menu,
    mem_tab_services_layout,
    mem_tab_dashboard_layout,
    mem_tab_claims_layout,
    mem_graphs
)


dash.register_page(__name__,
                   path='/member',
                   name='Member',
                   title='Member Claims',
                   description='Member claims dashboard and claim details')

layout = dbc.Container(
    [
        html.Div(
            id='mem-app-container',
            children=[
                menu.render_member_tab_menu(),
                html.Div(id=ids.MEM_APP_CONTENT)
            ]
        )
    ]
)


"""  RENDER TABS  """

@callback(
    Output(ids.MEM_APP_CONTENT, 'children'),
    Input(ids.MEM_APP_TABS, 'active_tab'))
def render_tab_content(tab_selected):
    if tab_selected == ids.MEM_TAB_DASHBOARD:
        return mem_tab_dashboard_layout.render_member_tab_dashboard()
    elif tab_selected == ids.MEM_TAB_SERVICES:
        return mem_tab_services_layout.render_tab_services_view()
    else:
        return mem_tab_claims_layout.render_tab_claims_view()


@callback(
    Output(ids.MEM_TITLE_DASHBOARD, 'children'),
    Output(ids.STORE_MEM_ACCT, 'data'),
    Output(ids.STORE_DATA_FILTER, 'data'),
    Input(ids.MEM_ACCT_DROPDOWN, 'value'),
    State(ids.STORE_DATA, 'data')
)
def filter_store_data(member, store_data):
    title = f"Dashboard for Member ID 000{member}"

    df = pd.DataFrame(store_data)
    df_filtered = df[df['mem_acct'] == member]
    df_filtered = df_filtered.to_dict('records')

    return title, member, df_filtered



