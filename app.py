######### Import your libraries #######
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import pandas as pd
#import plotly.express as px
import plotly as py
import plotly.graph_objs as go


###### Define your variables #####
tabtitle = 'Elections'
color1='#F7CAC9'
color2='#FF6F61'
color3='#34568B'
#colors = [color1,color2]
sourceurl = 'https://www.kaggle.com/c/titanic'
githublink = 'https://github.com/astever31/304-titanic-dropdown'


###### Import a dataframe #######
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/election.csv")
#df['Female']=df['Sex'].map({'male':0, 'female':1})
#df['Cabin Class'] = df['Pclass'].map({1:'first', 2: 'second', 3:'third'})
variables_list=['total', 'Coderre', 'Bergeron', 'Joly']

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

####### Layout of the app ########
app.layout = html.Div([
    html.H3('Choose a continuous variable for summary statistics:'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in variables_list],
        value=variables_list[0]
    ),
    html.Br(),
    dcc.Graph(id='display-value'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
])


######### Interactive callbacks go here #########
@app.callback(Output('display-value', 'figure'),
              [Input('dropdown', 'value')])
def display_value(continuous_var):
    #grouped_mean=df.groupby(['Cabin Class', 'Embarked'])[continuous_var].mean()
    #results=pd.DataFrame(grouped_mean)
    # Create a grouped bar chart
    #fig = px.bar(df, x='district', y=df.loc['first'][continuous_var], color='winner_won', text="winner", # marker_color=colors #orientation='h',
             #hover_data=["tip", "size"],
      #       height=1000,
     #        title='Election')
    mydata1 = go.Bar(
        x=df['district'],
        y=df[continuous_var],
        marker=dict(color=color1)
    #df = px.data.medals_long()
    )
    """
    mydata2 = go.Bar(
        x=results.loc['second'].index,
        y=results.loc['second'][continuous_var],
        name='Second Class',
        marker=dict(color=color2)
    )
    mydata3 = go.Bar(
        x=results.loc['third'].index,
        y=results.loc['third'][continuous_var],
        name='Third Class',
        marker=dict(color=color3)
    )
    """

    mylayout = go.Layout(
        title='Grouped bar chart',
        xaxis = dict(title = 'Election District'), # x-axis label
        yaxis = dict(title = str(continuous_var)), # y-axis label

    )
    
    fig = go.Figure(data=mydata1, layout=mylayout)
    return fig


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
