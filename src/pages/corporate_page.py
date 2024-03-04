import dash
from dash import html, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
from src.tab_views_corporate import (
    corp_tabs_menu as tmc,
    corp_tab_dashboard_layout,
    corp_tab_services_layout, corp_graphs
)
from src.nav_and_utilities import ids

########################################################
# SQLAlchemy Engine Links to PostgresSQL and ORM Imports
########################################################
from src.app import db
import sqlalchemy as sa
from src.postgres_sql_data.orm_models import (
                            DailyClaims, DailyMember,
                            PeriodSummary, PeriodMember, MemberSummary,
                            InjuryDiseaseSummary, InjuryDiseaseRacing,
                            SpecialtySummary, SpecialtyRacing,
                            FacilitySummary, FacilityRacing
)


dash.register_page(__name__,
                   path='/corporate',
                   name='Corporate',
                   title='Corporate',
                   description='Corporate Level Claim Data'
                   )


layout = dbc.Container(
    [
        html.Div(
            id='corp-app-container',
            children=[
                tmc.render_corporate_tab_menu(),
                html.Div(id=ids.CORP_APP_CONTENT)
            ]
        )
    ]
)

# Callback 1 - Call for Tabs (Default is CORP_TAB_DASHBOARD)
# Data is retrieved from PostgresSQL tables using SQLAlchemy ORM Classes (orm_models.py)

@callback(
    Output(ids.CORP_APP_CONTENT, 'children'),
    Input(ids.CORP_APP_TABS, 'active_tab')
)
def render_tab_content(tab_selected):
    if tab_selected == ids.CORP_TAB_DASHBOARD:
        return corp_tab_dashboard_layout.render_corp_tab_dashboard()
    if tab_selected == ids.CORP_TAB_SERVICES:
        return corp_tab_services_layout.render_corp_tab_services()


@callback(
    Output(ids.CORP_DAILY_CLAIMS_CHART, 'figure'),
    Output(ids.CORP_DAILY_CLAIMS_AVERAGE, 'children'),
    Output(ids.CORP_DAILY_CLAIMS_SUM, 'children'),
    Output(ids.CORP_ANNUAL_CLAIMS_CHART, 'figure'),
    Output(ids.CORP_ANNUAL_CLAIMS_AVERAGE, 'children'),
    Output(ids.CORP_ANNUAL_CLAIMS_SUM, 'children'),

    Output(ids.CORP_DAILY_PAID_CHART, 'figure'),
    Output(ids.CORP_DAILY_PAID_AVERAGE, 'children'),
    Output(ids.CORP_DAILY_PAID_SUM, 'children'),
    Output(ids.CORP_ANNUAL_PAID_CHART, 'figure'),
    Output(ids.CORP_ANNUAL_PAID_AVERAGE, 'children'),
    Output(ids.CORP_ANNUAL_PAID_SUM, 'children'),

    Output(ids.CORP_DAILY_MEMBER_CHART, 'figure'),
    Output(ids.CORP_DAILY_MEMBER_AVERAGE, 'children'),
    Output(ids.CORP_DAILY_MEMBER_SUM, 'children'),
    Output(ids.CORP_ANNUAL_MEMBER_CHART, 'figure'),
    Output(ids.CORP_ANNUAL_MEMBER_AVERAGE, 'children'),
    Output(ids.CORP_ANNUAL_MEMBER_SUM, 'children'),

    Input(ids.CORP_PERIOD_DROPDOWN, 'value')
)
def update_graph(period_chosen):
    # ROW 1 - MEDICAL CLAIMS PROCESSED
    # ROW 1 - COLUMN 1

    daily_claims = (db.session.execute(db.select(DailyClaims.charge_trans_date, DailyClaims.claims_count)
                                       .where(DailyClaims.period == period_chosen)))
    daily_claims_chart = pd.DataFrame(daily_claims)
    daily_claims_chart = corp_graphs.make_daily_claims_chart(daily_claims_chart)

    daily_claims_average = (db.session.execute(db.select(PeriodSummary.claims_daily_avg)
                                               .where(PeriodSummary.period == period_chosen)).scalar())
    daily_claims_average = f"{daily_claims_average:,.0f}"

    daily_claims_sum = (db.session.execute(db.select(PeriodSummary.claims_period_count).where(PeriodSummary.period == period_chosen)).scalar())
    daily_claims_sum = f"{daily_claims_sum:,.0f}"

    # ROW 1 - COLUMN 2

    annual_claims = (db.session.execute(db.select(PeriodSummary.period, PeriodSummary.claims_period_count)
                                        .order_by(PeriodSummary.period)))
    annual_claims_chart = pd.DataFrame(annual_claims)
    annual_claims_chart = corp_graphs.make_annual_claims_chart(annual_claims_chart)

    annual_claims_average = (db.session.execute(db.select(PeriodSummary.claims_period_average_cum)
                                                .where(PeriodSummary.period == 12)).scalar())
    annual_claims_average = f"{annual_claims_average:,.0f}"
    annual_claims_sum = (db.session.execute(db.select(PeriodSummary.claims_period_count_cum)
                                            .where(PeriodSummary.period == 12)).scalar())
    annual_claims_sum = f"{annual_claims_sum:,.0f}"


    # ROW 2 - MEDICAL CLAIMS PAID
    #############################

    # ROW 2 - COLUMN 1

    daily_paid = db.session.execute(db.select(DailyClaims.charge_trans_date, DailyClaims.charges_paid)
                                    .where(DailyClaims.period == period_chosen))
    daily_paid_chart = pd.DataFrame(daily_paid)
    daily_paid_chart = corp_graphs.make_daily_paid_chart(daily_paid_chart)

    daily_paid_average = (db.session.execute(db.select(PeriodSummary.claims_paid_daily_avg)
                                             .where(PeriodSummary.period == period_chosen)).scalar())
    daily_paid_average = f"${daily_paid_average:,.0f}"
    daily_paid_sum = (db.session.execute(db.select(PeriodSummary.claims_period_paid)
                                         .where(PeriodSummary.period == period_chosen)).scalar())
    daily_paid_sum = f"${daily_paid_sum:,.0f}"

    # ROW 2 COLUMN 2

    annual_paid = db.session.execute(db.select(PeriodSummary.period, PeriodSummary.claims_period_paid))
    annual_paid_chart = pd.DataFrame(annual_paid)
    annual_paid_chart = corp_graphs.make_annual_paid_chart(annual_paid_chart)

    annual_paid_average = (db.session.execute(db.select(PeriodSummary.claims_period_paid_average_cum)
                                              .where(PeriodSummary.period == 12)).scalar())
    annual_paid_average = f"${annual_paid_average:,.0f}"
    annual_paid_sum = (db.session.execute(db.select(PeriodSummary.claims_period_paid_cum)
                                          .where(PeriodSummary.period == 12)).scalar())
    annual_paid_sum = f"${annual_paid_sum:,.0f}"


    # ROW 3 - MEMBER PARTICIPATION
    ##############################

    # ROW 3 - COLUMN 1

    daily_member = db.session.execute(db.select(DailyMember.charge_trans_date, DailyMember.member_count)
                                      .where(DailyMember.period == period_chosen))
    daily_member_chart = pd.DataFrame(daily_member)
    daily_member_chart = corp_graphs.make_daily_member_chart(daily_member_chart)

    daily_member_average = (db.session.execute(db.select(MemberSummary.daily_member_avg)
                                               .where(MemberSummary.period == period_chosen)).scalar())
    daily_member_average = f"{daily_member_average:,.0f}"

    daily_member_sum = (db.session.execute(db.select(MemberSummary.daily_member_sum)
                                           .where(MemberSummary.period == period_chosen)).scalar())
    daily_member_sum = f"{daily_member_sum:,.0f}"

    # ROW 3 - COLUMN 2

    annual_member = (db.session.execute(db.select(MemberSummary.period, MemberSummary.daily_member_sum)))
    annual_member_chart = pd.DataFrame(annual_member)
    annual_member_chart = corp_graphs.make_annual_member_chart(annual_member_chart)

    annual_member_average = db.session.execute(db.select(MemberSummary.annual_ytd_avg)
                                               .where(MemberSummary.period == 12)).scalar()
    annual_member_average = f"{annual_member_average:,.0f}"
    annual_member_sum = db.session.execute(db.select(sa.func.count(PeriodMember.mem_acct_id.distinct()))).scalar()
    annual_member_sum = f"{annual_member_sum:,.0f}"

    return daily_claims_chart, daily_claims_average, daily_claims_sum, \
           annual_claims_chart, annual_claims_average, annual_claims_sum, \
           daily_paid_chart, daily_paid_average, daily_paid_sum, \
           annual_paid_chart, annual_paid_average, annual_paid_sum, \
           daily_member_chart, daily_member_average, daily_member_sum, \
           annual_member_chart, annual_member_average, annual_member_sum


@callback(
    Output(ids.CORP_SERVICES_COUNT, 'figure'),
    Output(ids.CORP_SERVICES_PAID, 'figure'),
    Output(ids.CORP_SERVICES_RACING, 'figure'),
    Input(ids.CORP_SERVICES_DROPDOWN, 'value')
)
def update_services_icd(val):
    if val == 'Injury_Disease':
        icd_table = db.session.execute(db.select(InjuryDiseaseSummary.name,
                                                 InjuryDiseaseSummary.claim_count,
                                                 InjuryDiseaseSummary.claim_paid,
                                                 InjuryDiseaseSummary.color_code).order_by(
            InjuryDiseaseSummary.claim_count))
        icd_table = pd.DataFrame(icd_table)
        icd_table = icd_table.nlargest(10, 'claim_count').sort_values('claim_count')
        icd_count_chart = corp_graphs.make_services_icd_count_chart(icd_table)

        icd_table = icd_table.sort_values('claim_paid')
        icd_paid_chart = corp_graphs.make_services_icd_paid_chart(icd_table)

        # RACING CHART
        icd_racing_table = db.session.execute(db.select(InjuryDiseaseRacing.name, InjuryDiseaseRacing.period,
                                      InjuryDiseaseRacing.color_code,InjuryDiseaseRacing.claim_count_ytd))
        icd_racing_table = pd.DataFrame(icd_racing_table)
        icd_racing_chart = corp_graphs.make_services_icd_racing_chart(icd_racing_table)

        return icd_count_chart, icd_paid_chart, icd_racing_chart

    elif val == 'Specialty':
        specialty_table = (db.session.execute(db.select(SpecialtySummary.name, SpecialtySummary.claim_count,
                                                        SpecialtySummary.claim_paid,
                                                        SpecialtySummary.color_code)
                                              .order_by(SpecialtySummary.claim_count))
                           )
        specialty_table = pd.DataFrame(specialty_table)
        specialty_table = specialty_table[specialty_table['name'] != 'Hospital_Clinic']
        specialty_table = specialty_table.nlargest(10, 'claim_count').sort_values('claim_count')

        specialty_count_chart = corp_graphs.make_services_specialty_count_chart(specialty_table)

        specialty_table = specialty_table.sort_values('claim_paid')
        specialty_paid_chart = corp_graphs.make_services_specialty_paid_chart(specialty_table)

        # RACING CHART

        specialty_racing_table = db.session.execute(db.select(SpecialtyRacing.name, SpecialtyRacing.period,
                                                              SpecialtyRacing.color_code, SpecialtyRacing.claim_count_ytd))
        specialty_racing_table = pd.DataFrame(specialty_racing_table)
        specialty_racing_table = specialty_racing_table[specialty_racing_table['name'] != 'Hospital_Clinic']
        specialty_racing_chart = corp_graphs.make_services_specialty_racing_chart(specialty_racing_table)

        return specialty_count_chart, specialty_paid_chart, specialty_racing_chart

    else:
        facility_table = (db.session.execute(db.select(FacilitySummary.name, FacilitySummary.claim_count,
                                                        FacilitySummary.claim_paid,
                                                        FacilitySummary.color_code)
                                              .order_by(FacilitySummary.claim_count))
                           )
        facility_table = pd.DataFrame(facility_table)
        facility_table = facility_table[facility_table['name'] != 'Hospital']
        facility_table = facility_table.nlargest(5, 'claim_count').sort_values('claim_count')

        facility_count_chart = corp_graphs.make_services_facility_count_chart(facility_table)

        facility_table = facility_table.sort_values('claim_paid')
        facility_paid_chart = corp_graphs.make_services_facility_paid_chart(facility_table)

        # RACING CHART

        facility_racing_table = db.session.execute(db.select(FacilityRacing.name, FacilityRacing.period,
                                                              FacilityRacing.color_code,
                                                             FacilityRacing.claim_count_ytd))
        facility_racing_table = pd.DataFrame(facility_racing_table)
        facility_racing_table = facility_racing_table[facility_racing_table['name'] != 'Hospital']
        facility_racing_chart = corp_graphs.make_services_facility_racing_chart(facility_racing_table)

        return facility_count_chart, facility_paid_chart, facility_racing_chart
