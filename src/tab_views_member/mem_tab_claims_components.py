from dash import html
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
from src.tab_views_member import mem_grids
from src.nav_and_utilities import ids


##############################################
#         COMPONENTS FOR LAYOUT FILE
##############################################


title_box = html.H2(id=ids.MEM_TITLE_CLAIMS, className='text-center text-secondary')


claims_grid_title = html.H4("Member Claims Details",
                            className='',
                            style={'color': '#32FBE2'}
                            )


member_claims_grid = dag.AgGrid(
    id=ids.MEM_CLAIMS_GRID,
    defaultColDef=mem_grids.member_claims_defaultColDef,
    columnDefs=mem_grids.member_claims_columnDefs,
    columnSize='sizeToFit',
    style={'height': 1000, 'overflow': 'auto'},
    dashGridOptions={
        'pagination': True,
        'paginationAutoPageSize': True,
        # 'page_action':'none'
    },
)


file_name_input = dbc.Input(id=ids.MEM_CLAIMS_INPUT,
                            placeholder='Save table as abc.csv ... Disabled',
                            type='text',
                            value=None,
                            disabled='',
                            )


file_save_button = dbc.Button(id=ids.MEM_CLAIMS_SAVE,
                              children='Save Table',
                              className='btn-secondary',
                              disabled='',
                              )
