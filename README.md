Welcome,

This is a Python-Dash based multi-page website that I developed while learning Python and Web Development. The concept for this website emanates from a career of working as a Certified Public Accountant (CPA) in various industries. The website is not intended to be a deep dive into the needs of a company but merely a framework.  With that said, this tool is geared for a healthcare insurance company that offers a portal for it's members, managers and analysts to view common data...of course permissions would limit accessibility for each gateway.

The website is built with Flask for a Dash Plotly application utilizing SQLAlchemy, Dash Plotly, Pandas and AG-Grid.  The Corporate data is stored/extracted from a PostgreSQL/SQLite database. Data for the Members is extracted from csv and stored on the users browser using a Dash Core Component (dcc.Store).

The application uses SQLAlchemy to model and map database tables.  Data objects are created from SQL-like queres and converted to dataframes with Pandas. 
In turn the data is passed on to Plotly Graphs and HTML/CSS for styling and visualization on a web page.

The data visualization blends Dash_Plotly, Python_Pandas, AG Grid using callbacks to interact between filters/dropdowns and charts and tables.

The Flask website layout uses Bootstrap Grid methodology (Row/Columns) and is styled predominantly with Dash_Bootstrap.  Overall, standard HTML elements and CSS classes were used to contain Bootstrap features.


From the website home page you will see 3 entry points:

Members Link:  Designed for an insured Member to view medical claims, charges for services and types of specialtists providing treatment.
Corporate Tab:  Designed for a corporate manager to view consolidated activity by period, specialists, places of treatment.
Analytics Tab:  Designed for an analyst to get high-level activity and distribution of transactions.


Project Code Structure

The project code is found in the src directory.  The application is run from the index.py file but imports the Dash application and Flask server from the app.py file.  The index.py file provides the "container" to receive for each web page.

- The user website entry point is the Home page with links to Members, Corporate and Analytics and are found in the src.Pages directory.
Each page (e.g. member_page.py) has a complimentary "tab_view" directory (e.g. tab_view_member).  The "view" is what the user "views" when a tab/link is clicked.
    - tab_views_member
      -- mem_data_calculations (data classes used to calucalate and manipulate data)
      -- mem_graphs (functions to create graphs)
      -- mem_grids (functions to create AG-Grid tables)
      -- mem_tab_xxx_components (creation of HTML/CSS components)
      -- mem_tab_xxx_layout (HTML layout of components)
      -- mem_tabs_menu (all tabs associated with "member" page)
    - other directories
      -- assets (images and stylesheets)
      -- member_store (csv file and application data loader for members)
      -- nav_and_utilities(page links and component id
      -- postgres_sql_data (SQLAlchemy-ORM Declarative Base Class) 

The data is stored in a SQLite data file (db_tynan).  The application was originally designed to interact with a Postgres SQL database but was reconfigured to use a lighter weight database for website demonstration purposes.  The member id and provider codes are fictitious.



