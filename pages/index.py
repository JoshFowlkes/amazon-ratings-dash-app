import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Value Proposition

           

            This is an app that uses Machine Learning to predict the rating of an Amazon Product Listing based on a variety of factors including: price, inventory, categories & sub categories, seller questions & answers, product information, product description etc. All the various factors that are easily viewable to any customer regardless if they are a prime member or not. 
            
            The purpose of this app is twofold:
            
            For Sellers: If your goal is to get a high product rating as well as to rank highly in seach results, this app will model what you should try to implement on your product to maximize its potential to rank high in an Amazon Search.
            
            For Customers: As you shop for any particular item, there might be multiple sellers of the exact same product. This predictive model will help you to compare and contract what an ideal seller's listing might look like, and help you sift through any potentially sketchy sellers.   

            

            """
        ),
        dcc.Link(dbc.Button('Predict', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        html.Img(src='assets/homepagechart.png', className='img-fluid'),
    ]
)

layout = dbc.Row([column1, column2])