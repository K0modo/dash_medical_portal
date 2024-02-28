##########  DEREK BANAS ##########

# https://github.com/derekbanas/plotly-tutorial/blob/master/Plotly%20Tut.ipynb
# https://www.youtube.com/watch?v=GGL6U0k8WYA&t=1690s

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

period_range = [0.1, 12]
title_font = dict(size=24)

font = {'size': 16}

yaxis_currency = dict(tickprefix='$')
yaxis_comma = dict(separatethousands=True)


def make_dash_bar1(table):
    fig = px.bar(
        table,
        x=table['period'],
        y=table['charge_allowed'],
    )

    fig.update_layout(
        title='Provider Charges by Period',
        title_x=0.5,
        title_font=title_font,
        xaxis_title='Period',
        yaxis=yaxis_currency,
        yaxis_title=None,
        font=font
    )

    fig.update_xaxes(
        range=[0.1, 13],
        dtick=2
    )

    fig.update_yaxes(
        dtick=20000
    )

    return fig


def make_dash_bar2(table):
    fig = px.bar(
        table,
        x=table['period'],
        y=table['claim_id']
    )

    fig.update_layout(
        title='Total # of Claims by Period',
        title_x=0.5,
        title_font=title_font,
        xaxis_title='Period',
        yaxis=yaxis_comma,
        yaxis_title='# Claims',
        font=font,
    )

    fig.update_xaxes(
        range=[0.1, 13],
        dtick=2,
    )

    fig.update_yaxes(
        dtick=20
    )

    return fig


def make_dash_bar3(table):
    fig = px.bar(
        table,
        x=table['injury_disease'],
        y=table['charge_allowed']
    )

    fig.update_layout(
        title='Purpose of Medical Services - Count',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title=None,
        font=font,
    )

    fig.update_xaxes(
        tickangle=45
    )

    return fig


def make_dash_pie1(table):
    fig = go.Figure(data=[go.Pie(
        labels=table['facility_class'],
        values=table['charge_allowed'],
        textinfo='label+percent'
    )])

    fig.update_layout(
        title='Provider Facility Category',
        title_x=0.5,
        title_font=title_font,
        showlegend=False,
    )

    return fig


def make_dash_pie2(table):
    fig = go.Figure(
        data=[
            go.Pie(
                labels=table['specialty'],
                values=table['SPECIALTY_COUNT'],
                textinfo='label+percent'
            )
        ]
    )

    fig.update_layout(
        title='Provider Specialty Distribution',
        title_x=0.5,
        title_font=title_font,
        showlegend=False,
    )

    return fig


def make_dash_bar4(table, log_scale):
    scale = 'linear' if log_scale == 'CHARGES' else 'log'

    fig = make_subplots(
        specs=[[{'secondary_y': True}]]
    )

    fig.update_layout(
        title_text=f"Total Charges vs Number Items Billed",
        title_x=0.5,
        title_font={'size': 24},
        font=font,
        legend=dict(
            yanchor='top',
            y=0.99,
            xanchor='right',
            x=0.8
        )
    )

    fig.add_trace(
        go.Bar(
            x=table['specialty'],
            y=table['CHARGES'],
            name='CHARGES'
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=table['specialty'],
            y=table['COUNT'],
            mode='lines',
            name='# Line Items',
            line={'color': 'firebrick', 'width': 3}
        ),
        secondary_y=True
    )

    fig.update_yaxes(
        title_text='Total Charges',
        tickprefix='$',
        type=scale,
        secondary_y=False
    )

    fig.update_yaxes(
        title_text='# Line Items',
        secondary_y=True
    )

    fig.update_xaxes(
        tickangle=45
    )

    return fig


def make_dash_scatter1(table, spec_list, log_scale):
    scale = 'linear' if log_scale == 'CHARGES' else 'log'

    spec_list = spec_list

    fig = px.scatter(table,
                     x=table['specialty'],
                     y=table['charge_allowed'],
                     category_orders={'specialty': spec_list},
                     )

    fig.update_layout(
        title='Line Item Charges by Specialty',
        title_x=0.5,
        title_font=title_font,
        font=font,
    )

    fig.update_traces(
        marker=dict(size=14)
    )

    fig.update_xaxes(
        title=None,
        tickangle=45,
    )

    fig.update_yaxes(
        type=scale,
        title_text='Claim Charge Amount',
        tickprefix='$',
        separatethousands=True,
    )

    return fig


def make_spec_scatter1(table):

    fig = px.scatter(
        table,
        x=table['period'],
        y=table['charge_allowed']
    )

    fig.update_xaxes(range=period_range)

    return fig


# Bar chart on Medical Services Tab
def make_member_specialty_bar(table):
    fig = px.bar(
        table,
        x=table['period'],
        y=table['charge_allowed']
    )

    fig.update_layout(
        title='Charges by Period',
        title_x=0.5,
        title_font=title_font,
        yaxis_title=None,
        xaxis_title=None
    )

    fig.update_xaxes(
        range=[0.1, 13],
        dtick=2
    )
    fig.update_yaxes(
        tickprefix='$',
        separatethousands=True,
    )

    return fig
