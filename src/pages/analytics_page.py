import dash
from dash import html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import pandas as pd

from src.tab_views_analytics import (
    analytic_tabs_menu as tma,
    analytic_tab_dashboard_layout as atd,
    analytic_tab_services_layout as ats, analytic_graphs)
from src.nav_and_utilities import ids
from src.tab_views_corporate.corp_data_calculations import (get_icd_dict,
                                                            get_specialty_dict,
                                                            AnalyticTables)

from src.app import db
from src.postgres_sql_data.orm_models import (InjuryDisease, InjuryDiseaseSummary, Specialty, SpecialtySummary,
                                              ConsolidatedCodes)

dash.register_page(__name__,
                   path='/analytics',
                   name='Analytics',
                   title='Analytics',
                   description='Analytical Data Analysis'
                   )

layout = dbc.Container(
    [
        html.Div(
            id='analytic-app-container',
            children=[
                tma.render_analytic_tab_menu(),
                html.Div(id=ids.ANALYTIC_APP_CONTENT)
            ]
        )
    ]
)


# Callback 1 - Call for Tabs

@callback(
    Output(ids.ANALYTIC_APP_CONTENT, 'children'),
    Input(ids.ANALYTIC_APP_TABS, 'active_tab')
)
def render_tab_content(tab_selected):
    if tab_selected == ids.ANALYTIC_TAB_DASHBOARD:
        return atd.render_analytic_tab_dashboard()
    if tab_selected == ids.ANALYTIC_TAB_SERVICES:
        return ats.render_analytic_tab_services()


# Callback 2 - Analytic Dashboard Quarter & Period Charts

@callback(
    Output(ids.ANALYTIC_CHARGES_BAR, 'figure'),
    Output(ids.ANALYTIC_CLAIMS_BAR, 'figure'),
    Output(ids.ANALYTIC_CHARGES_AVE_LINE, 'figure'),
    Output(ids.ANALYTIC_MEMBERS_COUNT_LINE, 'figure'),
    Output(ids.ANALYTIC_SCATBOX_CHART, 'figure'),
    Input(ids.ANALYTIC_CHARGES_RADIO, 'value')
)
def update_dashboard_charts(axis_col):
    dashboard_data = (db.session.execute(db.select(ConsolidatedCodes.claim_id, ConsolidatedCodes.mem_acct_id,
                                                   ConsolidatedCodes.quarter,
                                                   ConsolidatedCodes.period,
                                                   ConsolidatedCodes.charge_allowed)))
    dashboard_data = pd.DataFrame(dashboard_data)
    analytic_class = AnalyticTables(dashboard_data)

    dist_scat = analytic_class.get_dist_member_claims()
    fig = analytic_graphs.make_dist_member_claims_scatbox(dist_scat)

    if axis_col == 'period':
        charges = analytic_class.get_charges(axis_col)
        charges_chart = analytic_graphs.make_period_charges_chart(charges)
        claims = analytic_class.get_claims(axis_col)
        claims_chart = analytic_graphs.make_period_claims_chart(claims)
        charge_ave = analytic_class.get_charge_ave(axis_col)
        charge_ave_chart = analytic_graphs.make_period_average_chart(charge_ave)
        members = analytic_class.get_member_count(axis_col)
        members_chart = analytic_graphs.make_period_members_chart(members)

        return charges_chart, claims_chart, charge_ave_chart, members_chart, fig

    else:
        charges = analytic_class.get_charges(axis_col)
        charges_chart = analytic_graphs.make_quarter_charges_chart(charges)
        claims = analytic_class.get_claims(axis_col)
        claims_chart = analytic_graphs.make_quarter_claims_chart(claims)
        charge_ave = analytic_class.get_charge_ave(axis_col)
        charge_ave_chart = analytic_graphs.make_quarter_average_chart(charge_ave)
        members = analytic_class.get_member_count(axis_col)
        members_chart = analytic_graphs.make_quarter_members_chart(members)

        return charges_chart, claims_chart, charge_ave_chart, members_chart, fig


# Callback 3 - Analytic Services Heatmaps

@callback(
    Output(ids.ANALYTIC_HEAT_CHART, 'figure'),
    Output(ids.ANALYTIC_HEAT_ICD_SPEC_CHART, 'figure'),
    Input(ids.ANALYTIC_HEAT_RADIO, 'value')
)
def update_services_charts(category):
    heat_data = (db.session.execute(db.select(ConsolidatedCodes.injury_disease_id, ConsolidatedCodes.specialty_id,
                                              ConsolidatedCodes.facility_id, ConsolidatedCodes.period,
                                              ConsolidatedCodes.charge_allowed)))
    icd_dict = db.session.execute(db.select(InjuryDisease.id, InjuryDisease.name))
    icd_dict = get_icd_dict(icd_dict)

    spec_dict = db.session.execute(db.select(Specialty.id, Specialty.name))
    spec_dict = get_specialty_dict(spec_dict)

    heat_data = pd.DataFrame(heat_data)
    heat_data = AnalyticTables(heat_data)

    category_table = heat_data.get_heat_category_table(category)
    if category == 'injury_disease_id':
        category_table.rename(columns=icd_dict, inplace=True)
        category_chart = analytic_graphs.make_heatmap(category_table)
    else:
        category_table.rename(columns=spec_dict, inplace=True)
        category_chart = analytic_graphs.make_heatmap(category_table)

    icd_spec_table = heat_data.get_icd_spec_pivot()
    icd_spec_table.rename(index=icd_dict, inplace=True)
    icd_spec_table.rename(columns=spec_dict, inplace=True)
    icd_spec_chart = analytic_graphs.make_icd_spec_heatmap(icd_spec_table)

    return category_chart, icd_spec_chart


# Callback 4.1 Chained Callback for Injury_Disease & Specialty

@callback(
    Output(ids.ANAL_CHAIN_CATEGORY_DROP, 'options'),
    Output(ids.STORE_ANALYTIC_DATA, 'data'),
    Input(ids.ANAL_CHAIN_GROUP_DROP, 'value')
)
def category_dropdown_options(group):
    if group == 'injury_disease_id':
        data = db.session.execute(db.select(InjuryDiseaseSummary.injury_disease_id, InjuryDiseaseSummary.name,
                                            InjuryDiseaseSummary.claim_count, InjuryDiseaseSummary.claim_paid,
                                            InjuryDiseaseSummary.color_code))
        data = pd.DataFrame(data)
        options = [{'label': x, 'value': x} for x in sorted(data.name)]

    else:
        data = db.session.execute(db.select(SpecialtySummary.specialty_id, SpecialtySummary.name,
                                            SpecialtySummary.claim_count, SpecialtySummary.claim_paid,
                                            SpecialtySummary.color_code))
        data = pd.DataFrame(data)
        options = [{'label': x, 'value': x} for x in sorted(data.name)]

    return options, data.to_dict('records')


# Callback 4.2 Chained Callback for Injury_Disease & Specialty

@callback(
    Output(ids.ANAL_CHAIN_CATEGORY_DROP, 'value'),
    Input(ids.ANAL_CHAIN_CATEGORY_DROP, 'options')
)
def category_dropdown_values(options_selected):
    options = [x['value'] for x in options_selected]

    return options


# Callback 4.3 Chained Callback for Injury_Disease & Specialty

@callback(
    Output(ids.ANAL_CHAIN_GRAPH, 'figure'),
    Input(ids.ANAL_CHAIN_CATEGORY_DROP, 'value'),
    Input(ids.ANAL_CHAIN_GROUP_DROP, 'value'),
    State(ids.STORE_ANALYTIC_DATA, 'data')
)
def update_graph(category, group, store_data):
    if len(category) == 0:
        return dash.no_update
    else:
        if group == 'injury_disease_id':
            data_df = pd.DataFrame(store_data)
            data_df = data_df[data_df['name'].isin(category)]
        else:
            data_df = pd.DataFrame(store_data)
            data_df = data_df[data_df['name'].isin(category)]

    fig = analytic_graphs.make_chained_callback(data_df)

    return fig
