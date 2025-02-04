# dash_app.py
from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Input, Output

class Dashboard:
    def __init__(self) -> None:
        external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
        self.app = Dash(__name__, external_stylesheets=external_stylesheets, requests_pathname_prefix='/dashboard/')
        self._configure_layout()
        self._configure_callbacks()

    def _configure_layout(self) -> None:
        self.app.layout = html.Div([
            html.H1("Dashboard de Suplementos Alimenticios"),
            dcc.Tabs(id="tabs-example", value='tab-1', children=[
                dcc.Tab(label='Transacciones y Stock', value='tab-1'),
                dcc.Tab(label='Finanzas', value='tab-2'),
                dcc.Tab(label='Indicadores', value='tab-3'),
                dcc.Tab(label='Análisis Avanzado', value='tab-4')
            ]),
            html.Div(id='tabs-content')
        ])

    def _configure_callbacks(self) -> None:
        @self.app.callback(
            Output('tabs-content', 'children'),
            [Input('tabs-example', 'value')]
        )
        def render_content(tab: str) -> any:
            if tab == 'tab-1':
                return html.Div([
                    html.H3('Gestión de Transacciones y Stock'),
                    # Se pueden agregar formularios y tablas CRUD aquí
                ])
            elif tab == 'tab-2':
                return html.Div([
                    html.H3('Gestión de Finanzas'),
                    # Formularios y tablas para registros de gastos
                ])
            elif tab == 'tab-3':
                return html.Div([
                    html.H3('Indicadores de Ventas'),
                    dcc.Graph(
                        id='grafico-ventas',
                        figure=px.bar(
                            x=["Producto A", "Producto B"],
                            y=[100, 150],
                            title="Ventas"
                        )
                    )
                ])
            elif tab == 'tab-4':
                fig = px.line(
                    x=["2022-01-01", "2022-01-02", "2022-01-03"],
                    y=[200, 250, 300],
                    title="Ventas Diarias"
                )
                return html.Div([
                    html.H3('Análisis Avanzado'),
                    dcc.Graph(figure=fig)
                ])

# Instanciamos el dashboard para exportar la app de Dash
dashboard = Dashboard()
dash_app = dashboard.app

