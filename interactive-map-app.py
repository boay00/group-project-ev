import streamlit as st
import matplotlib.pyplot as plt
from functions import plot_heatmap_ev, plot_heatmap_aq

st.set_option('deprecation.showPyplotGlobalUse', False)



st.markdown('## US States - Air Quality vs EV Charging Stations')

slider_value = st.empty()

year = slider_value.slider("Year", min_value=2008, max_value=2022, value=2008)
button_year = st.button('Submit')

# Check if the "Submit" button is clicked
if button_year:
    
    st.pyplot(plot_heatmap_aq(year))

    st.pyplot(plot_heatmap_ev(year))





