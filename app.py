import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv("~/repo_cars/vehicles_us.csv")

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)

#Crear botón para construir gráfica de dispersión
disp_button = st.button('Construir gráfica de dispersión')
if disp_button:
    st.write('Creación de una gráfica de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear una gráfica de dispersión utilizando plotly.graph_objects
    fig_disp = go.Figure(data=go.Scatter(
        x=car_data['model_year'],
        y=car_data['price'],
        mode='markers',
        marker=dict(size=5, color='LightSkyBlue', opacity=0.6)
    ))

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig_disp.update_layout(title_text='Gráfica de Dispersión: Año vs Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig_disp, use_container_width=True)
