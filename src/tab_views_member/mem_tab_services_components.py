from dash import html
import dash_ag_grid as dag

from src.tab_views_member import mem_grids
from src.nav_and_utilities import ids

##############################################
#         COMPONENTS FOR LAYOUT FILE
##############################################


title_box = html.H2(id=ids.MEM_TITLE_SERVICES,
                    className='text-center text-secondary'
                    )

statistics_grid_title = html.H3("Annual Member Statistics by Specialty",
                                className='text-center py-3',
                                style={'color': '#32FBE2'}
                                )

statistics_grid_note = html.H5("**  Click on Row Data >> Details in Grid/Chart Below",
                               className='text-center',
                               style={'color': '#32FBE2'}
                               )

# This is Main Grid on Medical Services Tab
statistics_grid = dag.AgGrid(
    id=ids.MEM_SERV_GRID1,
    defaultColDef=mem_grids.grid1_defaultColDef,
    columnDefs=mem_grids.grid1_columnDefs,
    columnSize='sizeToFit',
    style={'height': 600, 'overflow': 'auto'},
    dashGridOptions={
        'pagination': True,
        'paginationAutoPageSize': True,
        'rowSelection': 'single',
        'rowHeight': 50,
    },
)


specialty_claims_section_title = html.H3("Selected Specialty Information (From Row Clicked Above **)",
                                         className='text-center text-decoration-underline pb-3',
                                         style={'color': '#32FBE2'}
                                         )


specialty_claims_grid_title = html.H4("Claims for Specialty Selected",
                                      className='text-center pb-3',
                                      style={'color': '#32FBE2'}
                                      )


specialty_claims_grid = dag.AgGrid(
    id=ids.MEM_SERV_GRID1_TABLE,
    columnDefs=mem_grids.spec_grid2_columnDefs,
    columnSize='sizeToFit',
    dashGridOptions={
        'pagination': True,
        'paginationAutoPageSize': True,
        'rowHeight': 50,
    },
)
