from dash import html, Input, Output, State, callback
import dash_bootstrap_components as dbc


navlink_class_menu = 'fs-4 fst-italic'


def render_navbar():
    return dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(src='../assets/images/TynanJpeg.jpg', width='45px', alt='Tynan',
                                         className='img-fluid my-3 rounded')
                            ),
                            dbc.Col(
                                dbc.NavbarBrand("Tynan Health Analytics", className='fs-1 fst-italic ms-2',)
                            )
                        ],
                        align='center',
                        className='ps-3 g-0'
                    ),
                ),

                dbc.NavbarToggler(id='navbar-toggler', n_clicks=0),

                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavItem(dbc.NavLink('Home', href='/', className=navlink_class_menu)),
                            dbc.NavItem(dbc.NavLink('Member', href='/member', className=navlink_class_menu)),
                            dbc.NavItem(dbc.NavLink('Corporate', href='/corporate', className=navlink_class_menu)),
                            dbc.NavItem(dbc.NavLink('Analytics', href='/analytics', className=navlink_class_menu)),
                        ],
                        className='ms-auto pe-3',
                        navbar=True
                    ),
                    id='navbar-collapse',
                    className='navbar-expand-lg',
                    navbar=True
                )
            ],
            className='navbar'
        ),
        color="dark",
        dark=True,
    )

@callback(
    Output('navbar-collapse', 'is_open'),
    Input('navbar-toggler', 'n_clicks'),
    State('navbar-collapse', 'is_open')
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

