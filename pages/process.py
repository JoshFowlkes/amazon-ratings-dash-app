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
        
            ## Process

            Due to the unique nature of the dataset and the target feature I was trying to predict(Rating) I was able to run this
            as both a regression model as well as a classifcation model. Both of which return their own unqiue insights as to 
            why products get the ratings they get, and perhaps even a deeper look at how Amazon's ranking system sifts through all the 
            numerous listings on the site. 

            ## The Data Cleaning & Wrangling for those that are interested:

            Below is an image of the data cleaning and wrangling I used for this particular model. 
            Although bare in mind, I did alterations here and there and little tweaks to optimize particular models.
            This data cleaning and wrangling here is optimized for a Linear Regression Model.
            
            Although depending on certain columns that I choose to drop or keep, then I am able to run this as a classification 
            problem.(ie classifying the rating/5 stars which is relatively low cardinality so for this model it was practical to do so)


            """
        ),
      html.Img(src='assets/wrangling.png', className='img-fluid'), 

       dcc.Markdown(
            """
        
             
            ## The Models
            Below is an image of the actual code of the Linear Regression model I ran in conjunction with the data cleaning and wrangling I showed above. 
            Also I kept OneHotEncoder in here since I included some categorical variables that I found useful towards the model,
             


            """
        ),



        html.Img(src='assets/LinReg.png', className='img-fluid'), 

       dcc.Markdown(
            """
        
            Below is an image of the classification model I ran. It merely takes a tweak of just adding any categorical features in the 
            Data Cleaning and Wrangling section by adding a '#' to any categorical feature of your choice. As well as adding a '#' to the 
            line of code in the Data Cleaning and Wrangling Section that makes the 'average_review_rating' a numerical value. Also just changing the model
            type to a classification one, in this case I used XGBClassifier. 


            """
        ),

        html.Img(src='assets/classifier.png', className='img-fluid'),


        dcc.Markdown(
            """
        
            To sum up, whilst this model is by no means perfect, it does convey that just because a product has 5 Stars, it may not be all that it seems. 
            If it has a limited number of customer ratings contibuting to that 5 Star rating, you might be better off going for the same product from a different 
            seller who has a lot more proof and customer support behind their product. 

            Likewise, if you're a seller, the keys to ranking high are naturally to sell a lot of items(that will rank you high on the search for keywords for 
            your product) and to ensure that customers are happy and thus leave good ratings thus supporting your endeavor. In addition, it is important to 
            have your item fairly priced. Not cutting yourself short by any means, but abiding by Amazon's philosophy of 'the customer always comes first.' And once
            your product does start to take off, always keep a good supply in stock, and always cater to any customer questions or comments. Ultimately, just be
            the type of seller that you would be happy to buy from. 

            Below is one last pdp graph, showing that, ratings will typically be high when there are not many reviews, but as more reviews come in, it will go lower
            and stabilize at it's true level. 


            """
        ),

        html.Img(src='assets/pdp_interact2.png', className='img-fluid'),


    ],
)

layout = dbc.Row([column1])