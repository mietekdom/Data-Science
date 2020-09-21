import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash(__name__)
app.layout = html.Div(children=[

    html.H2(children='Sprzedarz'),
    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x=['2017', '2018', '2019', '2020'],
                y=[150, 180, 230, 100],
                name='lokalnie'
            ),
            go.Bar(
                x=['2017', '2018', '2019', '2020'],
                y=[40, 120, 130, 600],
                name='online'
            )
        ])
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)