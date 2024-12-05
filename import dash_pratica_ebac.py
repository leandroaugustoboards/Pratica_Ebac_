import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

file_name = 'ecommerce_estatistica.csv'
df = pd.read_csv(file_name)
df['Preço'] = pd.to_numeric(df['Preço'], errors='coerce')
df.dropna(subset=['Preço'], inplace=True)
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Dashboard E-commerce", style={'textAlign': 'center'}),
    dcc.Tabs([
        dcc.Tab(label="Distribuição de Preços", children=[
            dcc.Graph(
                id='histogram-precos',
                figure=px.histogram(df, x='Preço', nbins=20, title='Distribuição de Preços',
                                    labels={'Preço': 'Preço'}, color_discrete_sequence=['skyblue'])
            )
        ]),
        dcc.Tab(label="Dispersão: Preço vs Nota", children=[
            dcc.Graph(
                id='scatter-preco-nota',
                figure=px.scatter(df, x='Preço', y='Nota', opacity=0.7,
                                  title='Dispersão: Preço vs Nota',
                                  labels={'Preço': 'Preço', 'Nota': 'Nota'})
            )
        ]),
        dcc.Tab(label="Mapa de Calor de Correlações", children=[
            dcc.Graph(
                id='heatmap-correlation',
                figure=px.imshow(df.corr(), text_auto=True, title='Mapa de Calor: Correlações')
            )
        ]),
        dcc.Tab(label="Top 10 Marcas", children=[
            dcc.Graph(
                id='bar-marcas',
                figure=px.bar(df['Marca'].value_counts().head(10),
                              title='Top 10 Marcas com Mais Produtos',
                              labels={'index': 'Marca', 'value': 'Quantidade de Produtos'})
            )
        ]),
        dcc.Tab(label="Distribuição por Gênero", children=[
            dcc.Graph(
                id='pie-genero',
                figure=px.pie(df, names='Genero', title='Distribuição por Gênero', hole=0.4)
            )
        ]),
        dcc.Tab(label="Regressão: Preço vs Quantidade Vendida", children=[
            dcc.Graph(
                id='regressao-preco-qtd',
                figure=px.scatter(df, x='Preço', y='Quantidade_Vendida', trendline='ols',
                                  title='Regressão: Preço vs Quantidade Vendida',
                                  labels={'Preço': 'Preço', 'Quantidade_Vendida': 'Quantidade Vendida'})
            )
        ]),
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)
