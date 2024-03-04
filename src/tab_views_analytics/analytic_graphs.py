import plotly.express as px
import plotly.graph_objects as go

period_range = [0.1, 12]
title_font = dict(size=30)

font = {'size': 16}

yaxis_currency = dict(tickprefix='$')
yaxis_comma = dict(separatethousands=True)
yaxis_thousands = '~s'


def make_quarter_charges_chart(table):
    fig = px.bar(
        table,
        x=table['quarter'],
        y=table['charge_allowed'],
    )

    fig.update_layout(
        title='Total Charges by Quarter',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title=None,
        yaxis_tickprefix='$ ',
        yaxis_tickformat='~s',
        font=font,
    )

    return fig


def make_period_charges_chart(table):
    fig = px.bar(
        table,
        x=table['period'],
        y=table['charge_allowed'],
    )

    fig.update_layout(
        title='Total Charges by Period',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title=None,
        yaxis_tickprefix='$ ',
        yaxis_tickformat='~s',
        font=font,
    )
    fig.update_xaxes(dtick=2)

    return fig


def make_quarter_claims_chart(table):
    fig = px.bar(
        table,
        x=table['quarter'],
        y=table['charge_allowed'],
    )

    fig.update_layout(
        title='Total Claims by Quarter',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title=None,
        yaxis_tickformat='~s',
        font=font,
    )
    fig.update_yaxes(dtick=10000)

    return fig


def make_period_claims_chart(table):
    fig = px.bar(
        table,
        x=table['period'],
        y=table['charge_allowed'],
    )

    fig.update_layout(
        title='Total Claims by Period',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title=None,
        yaxis_tickformat='~s',
        font=font,
    )
    fig.update_xaxes(dtick=2)

    return fig


def make_quarter_average_chart(table):
    fig = px.bar(
        table,
        x=table['quarter'],
        y=table['charge_allowed'],
    )

    fig.update_layout(
        title='Average Charge by Quarter',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title=None,
        yaxis_tickprefix='$ ',
        yaxis_tickformat='~s',
        font=font,
    )

    fig.update_yaxes(
        range=(100, 800),
        dtick=200
    )

    return fig


def make_period_average_chart(table):
    fig = px.bar(
        table,
        x=table['period'],
        y=table['charge_allowed'],
    )

    fig.update_layout(
        title='Average Charge by Period',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title=None,
        yaxis_tickprefix='$ ',
        yaxis_tickformat='~s',
        font=font,
    )
    fig.update_xaxes(dtick=2)
    fig.update_yaxes(
        range=(0, 800),
        dtick=200
    )

    return fig


def make_quarter_members_chart(table):
    fig = px.bar(
        table,
        x=table['quarter'],
        y=table['mem_acct_id'],
    )

    fig.update_layout(
        title='Members by Quarter',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title=None,
        yaxis_tickformat='~s',
        font=font,
    )
    fig.update_yaxes(
        range=(0, 800),
        dtick=200)

    return fig


def make_period_members_chart(table):
    fig = px.bar(
        table,
        x=table['period'],
        y=table['mem_acct_id'],
    )

    fig.update_layout(
        title='Members by Period',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title=None,
        yaxis_tickformat='~s',
        font=font,
    )
    fig.update_xaxes(dtick=2)
    fig.update_yaxes(dtick=200)

    return fig


def make_dist_member_claims_scatbox(table):
    fig = go.Figure()

    fig.add_trace(go.Box(x=table.Q4, name='Q4'))
    fig.add_trace(go.Box(x=table.Q3, name='Q3'))
    fig.add_trace(go.Box(x=table.Q2, name='Q2'))
    fig.add_trace(go.Box(x=table.Q1, name='Q1'))

    fig.update_layout(
        title=dict(text='Member Claims by Quarter', x=0.5, y=.95),
        title_font=title_font,
        title_pad=dict(b=40),
        font=font,
        showlegend=False,
        margin=dict(t=80, r=0, l=0, b=20),
    )

    fig.update_xaxes(
        range=(0, 400),
        dtick=100,
    )

    fig.update_yaxes(
        ticksuffix="  "
    )

    return fig


def make_heatmap(table):
    fig = px.imshow(
        table,
        title='Density of Claims During the Year',
        aspect='auto'
    )
    fig.update_layout(
        title_x=0.5,
        title_font={'size': 25},
        xaxis_title=None,
        yaxis_title='Period',
        font=font,
    )
    fig.update_traces(
        xgap=1,
        ygap=1,
        hoverongaps=False,
        hovertemplate="Id: %{x}"
                      "<br>Period: %{y}"
                      "<br>Claims : %{z}<extra></extra>"
    )

    return fig


# https://plotly.com/python/builtin-colorscales/
def make_icd_spec_heatmap(table):
    fig = px.imshow(
        table,
        title='Specialty Claims by Injury_Disease',
        aspect='auto',
    )
    fig.update_layout(
        title_x=0.5,
        title_font={'size': 25},
        xaxis_title=None,
        yaxis_title=None,
        font=font,
    )
    fig.update_traces(
        xgap=1,
        ygap=1,
        hoverongaps=False,
        hovertemplate="Id: %{x}"
                      "<br>Period: %{y}"
                      "<br>Claims : %{z}<extra></extra>"
    )

    return fig


def make_chained_callback(table):
    fig = px.scatter(
        table,
        x='name',
        y=table.claim_paid / table.claim_count,
        title='Average Charge per Claim',

    )
    fig.update_layout(
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title=None,
        font=font,
        margin=dict(t=80, r=0, l=0, b=140),
    )
    fig.update_traces(
        marker=dict(size=20, color=table.color_code)
    )

    fig.update_yaxes(
        range=[0, 800],
        dtick=200,
        tickprefix='$ ',
        separatethousands=True,
    )

    return fig
