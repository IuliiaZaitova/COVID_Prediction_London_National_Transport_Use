# COVID Prediction of London National Transport Use


In the times of global lockdown, public transportation became one of the most affected industries. Transport for London (TfL)'s fares income, for example, has fallen by 90% during lockdown. At the end of May, TfL has secured a £1.6bn (US$2bn) bailout from the government.
A partial service has been operating only since the UK first went into lockdown on 23 March 2020. No service cuts were made prior to that down, even though the number of passengers has been crashing significantly since the beginning of March.

*The current repository contains all the material used for predicting the London TfL Tube
and the UK National Rail Use during a pandemic using **Polynomial Regression Model**.*
 
to run the Bokeh app representing the predictors and the results, run the following command in the current directory via the command line:

   > bokeh serve --show bokeh_app


## Submitted Files

- `UK_transport.ipynb` (Jupyter Notebook file) is the notebook used for exploratory analysis, implementing, testing and scoring the Polynomial Regression.

The `bokeh_app` directory contains all the files required for generating and running the Bokeh visualization app:

- `PredictionVisualization.py` is a module with a class 'PredictionVisualization' that allows to call both the data required for visualization and the trained model.

- `main.py` is a script to generate and run the Bokeh app.

### Bokeh data files

The `bokeh_app/data` directory contains the data required for interactive prediction and visualization:

- `Cases_Transport.csv` is the dataset prepared for visualizing n of cases (infection and death) and use of transport.

- `London_mobility.csv` is the dataset prepared for visualizing mobility change in London.

- `UK_mobility.csv` is the dataset prepared for visualizing mobility change in UK.

- `rail_poly_model.pkl` is the Polynomial Regression ML model for predicting National Rail use saved using `Pickle`.

- `tfl_poly_model.pkl` is the Polynomial Regression ML model for predicting TfL Use use saved using `Pickle`.

### Notebook data files
The `data` directory contains the data required for TfL and National Rail use prediction:

- `Covid_Deaths_Global.csv` is the dataset showing COVID-19 daily new death cases globally by countries. Source: [European Centre for Disease Prevention and Control](https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases)

- `New_Cases.csv` is the dataset of COVID-19 daily new infections cases globally by countries. Source: [Our World in Data](https://ourworldindata.org/coronavirus-source-data)

- `New_Cases_London.csv` is the dataset showing COVID-19 daily new infection cases in London. Source: [Gov.uk](https://www.gov.uk/government/publications/slides-to-accompany-coronavirus-press-conference-30-march-2020)

- `Covid_Deaths_UK_Regions.csv`  is the dataset showing COVID-19 daily new death cases in different UK regions, among them London. Source: [Gov.uk](https://coronavirus.data.gov.uk/)

- `Transport_Use_feb_mar.csv` is the dataset showing COVID-19 pandemic transport use change from the baseline in the UK during end of Feb-March. Source: [Gov.uk](https://www.gov.uk/government/publications/slides-to-accompany-coronavirus-press-conference-30-march-2020) 

- `Global_Mobility_Report.csv` is the dataset showing COVID-19 pandemic mobility change from the baseline globally, by countries, and by regions. Source: [Google COVID-19 Community Mobility Reports](https://www.google.com/covid19/mobility/)

- `Transport_Use_mar_may.csv` is the dataset showing COVID-19 pandemic transport use change from the baseline in the UK during March-May. Source: [Gov.uk](https://www.gov.uk/government/publications/slides-to-accompany-coronavirus-press-conference-30-march-2020)

+ All the data required by the Bokeh app (`Cases_Transport.csv`  `rail_poly_model.pkl`  `UK_mobility.csv`
`London_mobility.csv`  `tfl_poly_model.pkl`)

## System requirements 
The Python version used for implementing the model is **3.7.3**.

### Python libraries required to run the modules:
- numpy
- pandas
- sklearn
- matplotlib
- seaborn
- bokeh
