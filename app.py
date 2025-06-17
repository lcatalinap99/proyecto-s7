import pandas as pd
import plotly.express as px
import streamlit as st


st.header("Cuadro de mandos: Análisis de vehículos en venta")


car_data = pd.read_csv('vehicles_us.csv')


hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer", title="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: precio vs odómetro')
    fig2 = px.scatter(car_data, x="odometer", y="price", title="Precio vs Odómetro")
    st.plotly_chart(fig2, use_container_width=True)