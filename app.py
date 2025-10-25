import plotly.express as px
from dash import Dash, dcc, html

app = Dash() #Incialización de una app tipo Dash

datos = px.data.tips() #Se guardan los datos de plotly express
figura = px.pie(datos, names="day", values="tip") #Guardar el gráfico en una variable

datos2 = px.data.gapminder()
figura2 = px.bar(datos2, x='year', y='gdpPercap')

app.layout=html.Div([
    html.H1("Gráfico de pastel de propinas por día"),
    dcc.Graph(figure=figura),
    html.H1("Gráfico de barras de PIB per cápita"),
    dcc.Graph(figure=figura2)
])

app.run(debug=True, use_reloader=False)

