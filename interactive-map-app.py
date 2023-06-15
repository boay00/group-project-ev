import streamlit as st
import matplotlib.pyplot as plt
from functions import plot_heatmap_ev, plot_heatmap_aq

st.set_option('deprecation.showPyplotGlobalUse', False)



st.markdown('''## US States - Air Quality vs EV Charging Stations
''')

st.markdown('''#### Bede Young''')
st.write('')
st.image('smog.png')
st.markdown('_*Source - NBC*_')
st.markdown('''---
This app is a demo of the heatmaps which were used to identify the states with the most pressing need of electric charging station installations.

View the github repo here:
> [EV-Air-Quality-Repo-Bede-Young](https://github.com/boay00/group-project-ev)
- Use the slider to select the desired year.
- :white_check_mark: Green heatmaps are indicating the number of charging stations per 10,000 population
- :large_blue_circle: Blue heatmaps are indicating the percentage of days with air quality classed 'bad' anually (ie. polutant levels did not meet satisfactory levels)

''')

slider_value = st.empty()

year = slider_value.slider("Year", min_value=2008, max_value=2022, value=2008)
button_year = st.button('Submit')

# Check if the "Submit" button is clicked
if button_year:
    
    st.pyplot(plot_heatmap_aq(year))

    st.pyplot(plot_heatmap_ev(year))

    st.markdown('---')
    st.markdown('''
    ## Observations
    ---
    - From these heatmaps, we can observe that the Eastern States have shown a proportional improvment in air quality (days classed 'bad')
    - Whilst California led in number of charging stations by a considerable amount in 2008, the Eastern States have greatly improved the availability of charging for Electric Vehicles in the last 15 years.
    - The states with the worst data for Air Quality are in the South West, including Arizona (AZ), Texas (TX) and New Mexico (NM)
    - AZ and NM have also indicated small improvements in EV charging availability in comparison to the rest of the US.
    ''')

