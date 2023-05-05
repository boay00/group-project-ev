# Project 4: EV Cars
#### General Assembly Data Science Immersive Course - Project 4

Authors: Aichieh Lin, Bede Young, and Charles Ramey

---

### Problem Statement

In a bid to improve air quality, vehicle manufacturers and policy makers are working to reduce carbon emissions from road vehicles by increasing availability of electric vehicles (EVs) and EV charging stations. Policy makers are aiming to meet net zero emission targets, and have requested analysis into the progress and effectiveness of building out EV infrastructure and increasing EV registration on air pollution levels. As part of progressing towards net zero emissions, policy makers are seeking to determine how many EV registrations and charging stations will yield a 10% improvement to the air quality index. This project analyzes EV trends and data collected on air quality, and uses a time-series model to forecast air quality levels, and a regression model to predict the number of charging stations that need to be installed to meet air quality reduction targets

---

### Summary

#### Data Collection

Data was collected from a range of sources. 
Air quality data :
- United States Environmental Protection Agency
Population Data :
- Cencus Bureau
Electric Vehicle and Charging Station Data :
- Alternative Fuels Data Center

#### EDA

Datasets were cleaned and analysed for the US, and subsequently for states of interest.
- Number of EV registrations was evaluated against EV charging station counts, to confirm colinear relationship
- Geopandas heatmaps were used to identify target states
- Air quality was analysed over the time period available for these states

#### Modeling

- Time series models were produced to forecast the air quality projections based on historical data
- Regression models were trained and used to predict the number of EV charging stations required to meet set targets of air quality
---

### Conclusion and Recommendations

Through our analysis, we observed a direct relationship between the number of available EV charging stations and the number of EVs owned. This is consistent with consumer surveys that identify lack EV charging stations as a key reason consumers are choosing not to switch to an EV. Our exploration of the data also revealed a correlation between the number of EV charging stations and the AQI for a number of states, though the evidence is not overwhelming.

The models created in this project do not conclusively suggest that an increase in the number of EV charging stations and EVs will yield the desired reduction in poor air quality days. However, the findings of our EDA lead us to believe that it is worth continuing to investigate this relationship as well as other factors that influence EV ownership. 

Theoretical predictions showed that with a stronger model, we were able to generate predicted targets for EV charging station installments in Arizona - based on 10% annual reductions in the number of days classed 'bad' for air quality.

Our recommendations for advancement of this analysis and next steps include:
- Evaluating Alternative Data Sources:
    - This analysis used daily and annual AQI data, however one shortcoming of this data is that its availability by county, state, and year varies. In some cases, AQI data is collected nearly every day of the year and in others it is collected far less. As a result, a lot of detail was lost through the normalization of the data.
    - Using actual concentrations of emissions-specific pollutants would likely yield better results, as AQI is a measurement of overall air quality and can be influenced heavily by unrelated events like wildfires.
- Improving the Models:
    - While model performance is heavily impacted by the data used, time constraints hindered the optimization of modeling efforts. Additional time and care should be taken to refine and improve both time-series and regression models.
- Investigating Other Factors:
    - Many consumers cited insufficient charging station availability as a reason why they would not purchase an EV, though other major factors include: high cost, battery range (miles), time to charge, and a general preference for gasoline vehicles.

---

### Sources

1. [https://aqs.epa.gov/aqsweb/airdata/download_files.html](https://aqs.epa.gov/aqsweb/airdata/download_files.html)
2. [https://afdc.energy.gov/vehicle-registration](https://afdc.energy.gov/vehicle-registration)
3. [https://afdc.energy.gov/stations/states](https://afdc.energy.gov/stations/states)
4. [https://www.transportation.gov/mission/health/cleaner-air](https://www.transportation.gov/mission/health/cleaner-air)
5. [https://www.who.int/health-topics/air-pollution#tab=tab_1](https://www.who.int/health-topics/air-pollution#tab=tab_1)
6. [https://www.whitehouse.gov/briefing-room/statements-releases/2021/08/05/fact-sheet-president-biden-announces-steps-to-drive-american-leadership-forward-on-clean-cars-and-trucks/](https://www.whitehouse.gov/briefing-room/statements-releases/2021/08/05/fact-sheet-president-biden-announces-steps-to-drive-american-leadership-forward-on-clean-cars-and-trucks/)
7. [https://www.caranddriver.com/news/g35562831/ev-plans-automakers-timeline/](https://www.caranddriver.com/news/g35562831/ev-plans-automakers-timeline/)
8. [https://www.irs.gov/credits-deductions/credits-for-new-clean-vehicles-purchased-in-2023-or-after](https://www.irs.gov/credits-deductions/credits-for-new-clean-vehicles-purchased-in-2023-or-after)
9. [https://www.pbs.org/newshour/nation/many-americans-arent-yet-sold-on-going-electric-for-their-next-car-poll-shows](https://www.pbs.org/newshour/nation/many-americans-arent-yet-sold-on-going-electric-for-their-next-car-poll-shows)
10. [https://www.whitehouse.gov/briefing-room/statements-releases/2023/02/15/fact-sheet-biden-harris-administration-announces-new-standards-and-major-progress-for-a-made-in-america-national-network-of-electric-vehicle-chargers/](https://www.whitehouse.gov/briefing-room/statements-releases/2023/02/15/fact-sheet-biden-harris-administration-announces-new-standards-and-major-progress-for-a-made-in-america-national-network-of-electric-vehicle-chargers/)
11. [https://www.epa.gov/outdoor-air-quality-data/air-data-basic-information](https://www.epa.gov/outdoor-air-quality-data/air-data-basic-information)