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

from src.tab_views_member.mem_data_calculations import MemberCalculations, GridStats

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


##############################
#   RENDER TABS
##############################

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


################################
#   FILTER DATA STORE FOR MEMBER
################################

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


#################################
#   TAB DASHBOARD - CREATE CHARTS
#################################

@callback(
    Output(ids.MEM_ANNUAL_CHARGE, 'children'),
    Output(ids.MEM_ANNUAL_ITEMS, 'children'),
    Output(ids.MEM_ANNUAL_AVERAGE, 'children'),
    Output(ids.MEM_DASH_BAR_CHARGE, 'figure'),
    Output(ids.MEM_DASH_BAR_CLAIMS, 'figure'),
    Output(ids.MEM_DASH_PIE_FACILITY, 'figure'),
    Output(ids.MEM_DASH_PIE_SPECIALTY, 'figure'),
    Output(ids.MEM_DASH_BAR_PURPOSE, 'figure'),

    Input(ids.STORE_DATA_FILTER, 'data')
)
def populate_dashboard(store_data_filter):
    df = pd.DataFrame(store_data_filter)

    member_table = MemberCalculations(df)

    annual_charge = member_table.annual_charge_calc()
    annual_charge = f'${annual_charge:,.0f}'

    annual_line_items = member_table.annual_line_items_calc()
    annual_line_items = f"{annual_line_items}"

    annual_average = member_table.annual_average_charge()
    annual_average = f'${annual_average:,.0f}'

    bar1_table = member_table.charge_by_period()
    bar1 = mem_graphs.make_dash_bar1(bar1_table)

    bar2_table = member_table.claims_by_period()
    bar2 = mem_graphs.make_dash_bar2(bar2_table)

    pie1_table = member_table.charge_by_facility_class()
    pie1 = mem_graphs.make_dash_pie1(pie1_table)

    pie2_table = member_table.count_by_specialty()
    pie2 = mem_graphs.make_dash_pie2(pie2_table)

    bar3_table = member_table.charge_by_injury_disease()
    bar3 = mem_graphs.make_dash_bar3(bar3_table)

    return annual_charge, \
           annual_line_items, \
           annual_average, \
           bar1, \
           bar2, \
           pie1, \
           pie2, \
           bar3


################################################
#   TAB DASHBOARD - CREATE CHARTS WITH LOG SCALE
################################################

@callback(
    Output(ids.MEM_SPEC_BAR_CHARGE, 'figure'),
    Output(ids.MEM_SPEC_SCATTER, 'figure'),
    Input(ids.MEM_SPEC_BAR_RADIO, 'value'),
    Input(ids.MEM_SPEC_SCATTER_RADIO, 'value'),
    Input(ids.STORE_DATA_FILTER, 'data'),
)
def populate_dashboard_specialty(log_scale_bar, log_scale_scatter, store_data_filter):
    df = pd.DataFrame(store_data_filter)

    member_table = MemberCalculations(df)  # send data to Data_Calculations class
    charge_count_bar_table = member_table.charge_count_spec8()  # call func to get DATA from Data_Calculations class
    bar4 = mem_graphs.make_dash_bar4(charge_count_bar_table, log_scale_bar)  # Send data as arg to chart BUILD func

    spec_list = member_table.spec_nlargest_list8()
    scatter_table1 = member_table.spec_filter_to_list8()
    scatter1 = mem_graphs.make_dash_scatter1(scatter_table1, spec_list, log_scale_scatter)

    return bar4, scatter1


#################################
#   TAB SERVICES - GRIDS & CHARTS
#################################

@callback(
    Output(ids.MEM_TITLE_SERVICES, 'children'),
    Output(ids.MEM_SERV_GRID1, 'rowData'),
    Output(ids.MEM_SERV_GRID1_TABLE, 'rowData'),
    Output(ids.MEM_SERV_GRID1_GRAPH, 'figure'),
    Input(ids.STORE_MEM_ACCT, 'data'),
    Input(ids.STORE_DATA_FILTER, 'data'),
    Input(ids.MEM_SERV_GRID1, 'selectedRows')
)
def display_services_stats(member, store_data_filter, selected_row):
    title = f'Medical Services for Member ID 000{member}'

    df = pd.DataFrame(store_data_filter)
    mem_serv_stats = GridStats(df)
    mem_serv_stats = mem_serv_stats.calc_serv_stats()
    mem_serv_stats = mem_serv_stats.to_dict('records')

    if selected_row is None:
        specialty = 'General_Medicine'
    else:
        specialty = selected_row[0]['specialty']

    mem_claim_hist = GridStats(df)

    mem_claim_hist = mem_claim_hist.spec_claim_hist()
    mem_claim_hist = mem_claim_hist[mem_claim_hist['specialty'] == specialty]
    mem_claim_hist_graph = mem_graphs.make_member_specialty_bar(mem_claim_hist)

    mem_claim_hist = mem_claim_hist.to_dict('records')

    return title, mem_serv_stats, mem_claim_hist, mem_claim_hist_graph


#################################
#   TAB CLAIMS - GRID
#################################

@callback(
    Output(ids.MEM_TITLE_CLAIMS, 'children'),
    Output(ids.MEM_CLAIMS_GRID, 'rowData'),
    Input(ids.STORE_MEM_ACCT, 'data'),
    Input(ids.STORE_DATA_FILTER, 'data')
)
def display_claims(member, store_data_filter):
    title = f'Medical Claims for Member ID 000{member}'

    df = pd.DataFrame(store_data_filter)
    mem_claims_detail = GridStats(df)

    mem_claims_detail = mem_claims_detail.get_member_claim_detail()
    mem_claims_detail = mem_claims_detail.to_dict('records')

    return title, mem_claims_detail
