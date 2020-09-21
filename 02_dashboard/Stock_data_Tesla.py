import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go


def fetch_financial_data(company='TSLA'):
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')


df = fetch_financial_data()
df.reset_index(inplace=True)
df = df[df.Date > '2019-01-01']

external_stylesheets = ['htttps://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H4('Notowania spółki Tesla'),

    dcc.Graph(
        figure=go.Fiure(
            data=[
                go.Scatter(
                    x=df.Date,
                    y=df.Close,
                    mode='lines',
                    full='tozeroy',
                    name='Tesla'
                )
            ],
            layout=go.layout(
                yaxis_type='log',
                heigh=500,
                title_text='Wykres ceny',
                showlegend=True
            )
        )
    ),
])


if __name__ == '__main__':
    app.run_server(debug=True)