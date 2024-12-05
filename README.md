Este repositório contém um projeto de análise e visualização de dados de um e-commerce. A aplicação utiliza Python com a biblioteca Dash para criar um dashboard interativo.

Estrutura do Repositório
Arquivos
Pratica_Ebac_.py
Este arquivo contém o código original usado para realizar as análises exploratórias no dataset ecommerce_estatistica.csv. Ele utiliza bibliotecas como pandas, matplotlib e seaborn para gerar gráficos estáticos como:

Histograma de preços.
Dispersão de preço vs nota.
Mapa de calor de correlação entre variáveis.
Análise de marcas mais populares.
Análise de distribuição por gênero.
ecommerce_estatistica.csv
Um arquivo de dados em formato CSV contendo informações relacionadas a produtos de um e-commerce. As principais colunas incluem:

Preço: Preço dos produtos.
Nota: Nota dos produtos.
Marca: Marca dos produtos.
Genero: Categoria do produto.
Quantidade_Vendida: Número de unidades vendidas.
app.py (se você salvou o código Dash neste nome)
Um arquivo Python que contém a implementação de um dashboard interativo utilizando Dash. Este aplicativo permite visualizar:

Distribuição de preços.
Gráficos interativos de dispersão (Preço vs Nota).
Mapas de calor das correlações.
Gráficos de barras das principais marcas.
Gráficos de pizza da distribuição por gênero.
Regressões entre preço e quantidade vendida.
Como Executar
Pré-requisitos
Certifique-se de ter instalado:

Python 3.7+
Bibliotecas Python:
dash
plotly
pandas
numpy
Passos
Clone este repositório:
bash
Copiar código
git clone https://github.com/seu-usuario/dashboard-ecommerce.git
Navegue até a pasta do projeto:
bash
Copiar código
cd dashboard-ecommerce
Instale as dependências:
bash
Copiar código
pip install dash plotly pandas
Execute o dashboard:
bash
Copiar código
python app.py
Abra o navegador em http://127.0.0.1:8050/ para visualizar o dashboard.
Resultados Esperados
O dashboard gerado permitirá:

Analisar a distribuição de preços com gráficos interativos.
Estudar correlações entre variáveis como preço, nota e quantidade vendida.
Visualizar os dados das marcas mais populares e a distribuição dos produtos por gênero.
