import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            ## Individual Observations: 


            """
        ),

         
         html.Img(src='assets/shap1.png', className='img-fluid'),

         dcc.Markdown(
            """
        
            In this individual observation we see that the predictive model utilized the available stock, manufacturer, and sub category as the 
            primary drivers for pushing the rating higher. And the price and small number of reviews contibuted to predicting a lower value.

            """
        ),


         
         html.Img(src='assets/shap3.png', className='img-fluid'),

         dcc.Markdown(
            """
           
           In this individual observation, we see that an item from the same manufacturer as the previous but at a different price point
           also has the low number of reviews negatively impacting the rating, however, in this instance, interestingly the price contibuted to a slighly higher predicted
           rating.

           ## Leakage
           One factor within my data set that I found to lead to incredible leakage was whether or not the observation had a 
           'Customers Who Bought This Also Bought' section. Whilst very high in cardinality, when this information is included in the predictive modeling
           it leads to a stunning increase in accuracy when it comes to predicting the exact rating that a product gets. Thinking about it from a real 
           world perspective, the most highly rated and frequently bought items will have a very accurate and dead on 'Customers Who Bought This Also Bought'
           selections. Whereas a listing that is fairly new, you'll notice often times won't have one of these and rather will only list 'Similar Items.' 

           
           Also notice how the outlier with 1399 reviews, inherently has a lower rating than ones with few reviews.
           This is because over a large enough sample size, a more accurate rating has been given to the listing. 
           In my opinion, this is quite a good listing since it has survived the test of having many many people buy it, and 
           very few report an issue with it. 

           This is all shown in the graph below.

            """
     ), 

    

      html.Img(src='assets/pdp_interact1.png', className='img-fluid'), 

       dcc.Markdown(
            """
        
            Below is a chart that is simliar to the one on the Predictions page. And it simply is conveying the drop off after $50 since
            majority of the observations in the dataset were around this price range. And this makes sense, if you think about stuff you've ordered from Amazon:
            you've order perhaps a few expensive things over the years such as a TV or a Trampoline, but majority of the items are in the lower to mid price range.


            """
        ),



        html.Img(src='assets/pdp3.png', className='img-fluid'), 

       dcc.Markdown(
            """
        
            


            """
        ),

        dcc.Markdown(
            """
        
            ## Potential Flaws in the Dataset and Predictive Modeling 

            One potential flaw that was contained in the dataset used in this predictive modeling that translates to the real world is that:
            if someone makes a brand new listing on Amazon, they can essentially give out free products to their close friends, work circle and people of that sort,
             in exchange for 
            giving their product a five star rating. So you could get a product that has a literal perfect rating, but is based on single digit number of reviews.
            These were definitely in the dataset used on this predictive modeling, and as a result, it skews much of the predicitve modeling towards 5 star
            ratings. 

            Another draw down was, the sample size of this dataset was a mere 10,000. For the sake of doing predictve modeling something as colossal as the 
            leviathon Amazon, this is rather limited in size.


            """
        ),

 
    ], 
    
)


#column2 = dbc.Col(
   # [
 #    html.Img(src='assets/pdp_interact1.png', className='img-fluid'),   

  #   html.Img(src='assets/pdp3.png', className='img-fluid') 
   # ]
#)

layout = dbc.Row([column1])