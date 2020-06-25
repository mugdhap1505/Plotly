import pandas_datareader.data as web
from pandas.util.testing import assert_frame_equal
import datetime
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


start = datetime.datetime(2019,1,1)
end = datetime.datetime.now()

stock ='TSLA'
df = web.DataReader(stock ,'yahoo', start , end)


app = dash.Dash()


app.layout = html.Div(children=[


    html.Div(children='''symbol to graph'''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock}
            ],
            'layout': {
                'title': stock

            }
        }
    )

])




if __name__ == '__main__':
    app.run_server(debug=True)