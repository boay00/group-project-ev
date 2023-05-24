import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


import geopandas

pop_stations = pd.read_csv('data/pop_stations.csv')
aq = pd.read_csv('data/aq.csv')
aq['pct_bad_days'] = aq.pct_bad_days * 100
# imports geopandas shape file, geopandas df then processed and cleaned
states = geopandas.read_file('data/geopandas-data/usa-states-census-2014.shp')
states = states.to_crs("EPSG:3395")
states = states.sort_values('NAME')
states.rename(columns={
    'NAME': 'state'
}, inplace=True)

def plot_heatmap_ev(year):
    
    '''
    This function takes a 'year' parameter, set by the interactive slider seen in the output
    of this cell. This parameter sets the masking condition for two datasets. 
    
    These are then merged into a geopandas dataframe with geometry values 
    for each of the mainland states of the US.
    
    The values for 'pct_bad_days' and 'electric_by_pop' columns are plotted using the geopandas
    plot function, and heatmap scales are created using the ScalarMappable and
    Normalize classes.
    
    State abbreviations are labelled and centered at the geometric center of the states shape.
    '''
    
    # clears previous output
    # output.clear_output(wait=True)
    cmap_e = 'Greens'
    
    # masks station df at year == 'year'
    year_stations = pop_stations[pop_stations.year == year]
    
    # geopandas df and stations df merged, min and max scale set
    year_stations = pd.merge(states, year_stations)
    year_stations.dropna(inplace=True)
    vmin_e = year_stations['electric_by_pop'].min()
    vmax_e = year_stations['electric_by_pop'].max()
    
    # with output:
    fig, ax = plt.subplots(1, figsize=(20, 9))
    ax.axis('off')

    # annotations made using annotate() function at geometric centers of each value
    year_stations.apply(lambda x: ax.annotate(text=x.STUSPS, xy=x.geometry.centroid.coords[0], ha='center', fontsize=12, color='black'), axis=1);

    # state boundaries plotted
    year_stations.boundary.plot(ax=ax, color='Black', linewidth=.4)

    # station counts plotted
    year_stations.plot(column='electric_by_pop', ax=ax, linewidth=1, cmap=cmap_e)

    # values scaled according to previous min and max scales
    sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=vmin_e, vmax=vmax_e), cmap=cmap_e)
    sm._A = []
    ax.set_title(f'Electric Charging Stations per 10,000 population in the US {year}', fontsize=20)

    cbaxes = fig.add_axes([0.15, 0.25, 0.01, 0.4])
    cbar = fig.colorbar(sm, cax=cbaxes)

def plot_heatmap_aq(year):
    #process repeated for aq df
    cmap_aq = 'Blues'
    year_aq = aq[aq.year == year]

    year_aq = pd.merge(states, year_aq)
    year_aq.dropna(inplace=True)

    vmin_aq = year_aq['pct_bad_days'].min()
    vmax_aq = year_aq['pct_bad_days'].max()
    # with output:
    fig, ax = plt.subplots(1, figsize=(20, 9))
    ax.axis('off')
    year_aq.apply(lambda x: ax.annotate(text=x.STUSPS, xy=x.geometry.centroid.coords[0], ha='center', fontsize=12, color='black'), axis=1);
    year_aq.boundary.plot(ax=ax, color='Black', linewidth=.4)
    year_aq.plot(column='pct_bad_days', ax=ax, linewidth=1, cmap=cmap_aq)
    sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=vmin_aq, vmax=vmax_aq), cmap=cmap_aq)
    sm._A = []
    ax.set_title(f'Percentage of Days Air Quality was classed "Bad" {year}', fontsize=20)

    cbaxes = fig.add_axes([0.15, 0.25, 0.01, 0.4])
    cbar = fig.colorbar(sm, cax=cbaxes)
    