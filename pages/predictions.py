import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
from sklearn.impute import SimpleImputer

from app import app

pipeline = load('pages/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions
            
            Below is a number of Sliders that affect the outcomes of our predicitive modeling.
            
            
            
            Price 

            """
        ),
        dcc.Slider(
            id='price', 
            min=0, 
            max=250, 
            step=1, 
            value=20, 
            marks={n: str(n) for n in range(0,250,25)}, 
            className='mb-5',
            updatemode='drag', 
        ),

        dcc.Markdown(
            """
        
            Number of Available Stock 

            """
        ),
        
        dcc.Slider(
            id='number_available_in_stock', 
            min=0, 
            max=95, 
            step=1, 
            value=20, 
            marks={n: str(n) for n in range(0,95,10)}, 
            className='mb-5',
            updatemode='drag', 
        ),

        dcc.Markdown(
            """
        
            Number of Reviews 

            """
        ),
        
        dcc.Slider(
            id='number_of_reviews', 
            min=0, 
            max=1400, 
            step=1, 
            value=20, 
            marks={n: str(n) for n in range(0,1400,100)}, 
            className='mb-5',
            updatemode='drag', 
        ),

         dcc.Markdown(
            """
        
            Number of Answered Questions

            """
        ),
        
        
         dcc.Slider(
            id='number_of_answered_questions', 
            min=0, 
            max=40, 
            step=1, 
            value=20, 
            marks={n: str(n) for n in range(0,40,5)}, 
            className='mb-5',
            updatemode='drag', 
        ),

         dcc.Markdown(
            """
        
            Description?(1 for Yes, 0 for No) 

            """
        ),
        
        dcc.Slider(
            id='new_description', 
            min=0, 
            max=1, 
            step=1, 
            value=0, 
            marks={n: str(n) for n in range(0,1,1)}, 
            className='mb-5', 
            updatemode='drag',
        ),

        dcc.Markdown(
            """
        
            Customer Written Reviews?(1 for Yes, 0 for No) 

            """
        ),
        
          dcc.Slider(
            id='new_customer_reviews', 
            min=0, 
            max=1, 
            step=1, 
            value=0, 
            marks={n: str(n) for n in range(0,1,1)}, 
            className='mb-5',
            updatemode='drag', 
        ),

        dcc.Markdown(
            """
        
            Seller Answers Customer Questions?(1 for Yes, 0 for No) 

            """
        ),
        
        
           dcc.Slider(
            id='new_customer_questions_and_answers', 
            min=0, 
            max=1, 
            step=1, 
            value=0, 
            marks={n: str(n) for n in range(0,1,1)}, 
            className='mb-5',
            updatemode='drag', 
        ),

        dcc.Markdown(
            """
        
            Product Information Section?(1 for Yes, 0 for No) 

            """
        ),
        
           dcc.Slider(
            id='new_product_information', 
            min=0, 
            max=1, 
            step=1, 
            value=0, 
            marks={n: str(n) for n in range(0,1,1)}, 
            className='mb-5',
            updatemode='drag', 
        ),
        
    ],
    md=5,
)





column2 = dbc.Col(
    [
      html.H2('Predicated Rating', className='mb-5'), 
      html.Div(id='prediction-content', className='lead'),
      html.Img(src='assets/pdp3.png', className='img-fluid'),
      dcc.Markdown(
            """
        
            Important note, majority of the adjustable parameters listed on the left generally operate in a range and outside of that range the results tend to get 
            more unreliable. For example, illustrated in the graph above, majority of the items in the dataset used in this predictive model were $50 or less. 
            Thus this predictive model is most accurate for items around that price area. However, within the dataset there were a few items that were priced
            much higher, one for instance had a price over $2400. This applies for all the adjustable inputs to the left. The parameters are already preset to only
            allow parameter values close to the model's optimal range, however there is a enough wiggle room that outliers on either end will affect accuracy in the prediction. 

            """
        )  
    ], 

    


    
)



layout = dbc.Row([column1, column2])

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('price', 'value'), 
     Input('number_available_in_stock', 'value'),
     Input('number_of_reviews', 'value'),
     Input('number_of_answered_questions', 'value'),
     Input('new_description', 'value'), 
     Input('new_customer_reviews', 'value'),
     Input('new_customer_questions_and_answers', 'value'), 
     Input('new_product_information', 'value')],
)
def predict(price, 
            number_available_in_stock, 
            number_of_reviews, 
            number_of_answered_questions,
            new_description, 
            new_customer_reviews, 
            new_customer_questions_and_answers,
            new_product_information):
 
  
    y_pred = pipeline.predict([[price, 
                                number_available_in_stock, 
                                number_of_reviews, 
                                number_of_answered_questions,
                                new_description, 
                                new_customer_reviews, 
                                new_customer_questions_and_answers,
                                new_product_information]])
  
    estimate = y_pred[0]
  
  
    return f'{estimate:.2f}/5 Star Rated Product'



