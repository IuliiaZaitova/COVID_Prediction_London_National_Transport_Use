# Qualification_task_S2E

*The current repository contains all the material used for predicting the London TfL Tube
and the UK National Rail Use during a pandemic.*
 
to run the Bokeh app representing the predictors and the results, run the following command in the current directory via the command line:

   > bokeh serve --show bokeh_app


## Submitted Files

- `UK_transport.ipynb` (Jupyter Notebook file) is the notebook used for exploratory analysis, implementing, testing and scoring the Polynomial Regression.
- 
=================================================================
The `bokeh_app` directory contains all the files required for generating and running the Bokeh visualization app:

-`PredictionVisualization.py` is a module with a class 'PredictionVisualization' that allows to call both the data required for visualization and the trained model.

-`main.py` is a script to generate and run the Bokeh app.

=================================================================
        The `bokeh_app/data` directory contains the data required for interactive prediction and visualization:

        -`Cases_Transport.csv` is the dataset prepared for visualizing n of cases (infection and death) and use of transport.

        -`London_mobility.csv` is the dataset prepared for visualizing mobility change in London.

        -`UK_mobility.csv` is the dataset prepared for visualizing mobility change in UK.

        -`rail_poly_model.pkl` is the Polynomial Regression ML model for predicting National Rail use saved using `Pickle`.

        -`tfl_poly_model.pkl` is the Polynomial Regression ML model for predicting TfL Use use saved using `Pickle`.

=================================================================
The `data` directory contains the data required for TfL and National Rail use prediction:

-`Covid_Deaths_Global.csv` is the dataset showing COVID-19 daily new death cases globally by countries.

-`New_Cases.csv` is the dataset of COVID-19 daily new infections cases globally by countries.

-`New_Cases_London.csv` is the dataset showing COVID-19 daily new infection cases in London.

-`Covid_Deaths_UK_Regions.csv`  is the dataset showing COVID-19 daily new death cases in different UK regions, among them London.

-`Transport_Use_feb_mar.csv` is the dataset showing COVID-19 pandemic transport use change from the baseline in the UK during end of Feb-March.

-`Global_Mobility_Report.csv` is the dataset showing COVID-19 pandemic mobility change from the baseline globally, by countries, and by regions. 

-`Transport_Use_mar_may.csv` is the dataset showing COVID-19 pandemic transport use change from the baseline in the UK during March-May.

+ All the data required by the Bokeh app (Cases_Transport.csv  rail_poly_model.pkl  UK_mobility.csv
London_mobility.csv  tfl_poly_model.pkl)
=================================================================
The Python version used for implementing the model is **3.7.3**.

### Python libraries required to run the modules:
~ numpy
~ pandas
~ sklearn
~ matplotlib
~ seaborn
~ bokeh

