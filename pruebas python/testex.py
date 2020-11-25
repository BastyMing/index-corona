import streamlit as st
from streamlit_ace import st_ace
import pandas as pd
import numpy as np

REGION = [
    "I - Tarapaca", "II - Antofagasta", "III - Atacama", "IV - Coquimbo",
    "V - Valparaiso", "VI - O'Higgins", "VII - Maule", "VIII - Bio Bio",
    "IX - La Araucania", "X - Los Lagos", "XI - General Carlos Ibañez del Campo",
    "XII - Magallanes y Antartica Chilena", " XIII - Metropolitana", "XIV - Los Rios",
    "XV - Arica y Parinacota", "XVI - Ñuble"
]

COMUNA = [
    "Temuco", "Padre Las Casas", "Villarrica", "Lautaro", "Victoria",
    "Loncoche", "Puerto Saavedra", "Gorbea", "Curacautin", "Lonquimay"
]



def main():
    st.sidebar.title(":memo: COVID 19")

    st.write("Detalle:")
    st.write(pd.DataFrame({
    'Activos': [67],
    'Recuperados':[121],
    'Fallecidos':[10]
    }))

    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [-38.767351, -72.595902],
        columns=['lat', 'lon'])

    st.map(map_data)
    
    content = st_ace(
        language=st.sidebar.selectbox("Regiones", options=REGION, index=15),
        theme=st.sidebar.selectbox("Comunas", options=COMUNA, index=2)
    )

    st.write(content)
    print("listo¡")


if __name__ == "__main__":
    main()
