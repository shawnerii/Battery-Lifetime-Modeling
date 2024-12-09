In this research, we have completed an incomplete project using its dataset and the data collected by the original authors to finalize the project.

This project is a tool that can determine the remaining lifespan of your battery based on its usage pattern. It takes into account if you only partially charge and discharge the battery. The tool analyzes the discharge or charge curve of your battery’s current cycle, whether it is partially charged and discharged, and determines the cycle and capacity of the battery. Finally, it calculates the percentage of your battery’s remaining lifespan based on its capacity.

Dataset Details

The dataset for this project consists of binary files stored in MATLAB format, including information such as the charge and discharge times of the battery and other related data. The dataset is organized into two folders: Data and Test. The Data folder contains the files used for training and testing the MATLAB scripts and their construction. The Test folder is used to validate and ensure the correct functionality of the project.

Software Dependencies

This project utilizes Python version 3.6. The following packages have been used:
	•	fastdtw
	•	h5py
	•	hdf5storage
	•	matplotlib
	•	numpy
	•	pandas
	•	scipy
	•	tqdm

Modules in the Provided Tool

The tool includes the following modules:
	•	Import_data
	•	sort_data
	•	Predict_capacity


## Data Cleaning Packages

This packages are used to import the charge/discharge cycle infomation inside a Matlab file and load it into two dictionaries sorted by the number of cycle. 

The modules included are:

### 1.  The ``import_data.py`` package

The main function in this package is called ``single_pd_matlab_data``, that generates a dataframe with the data store in a Matlab file using HDF5 format.

### 2.  The ``sort_data.py`` package

This package generates two dictionaries, one for the charge cycles data and the other for the discharge cycles data..


### 3.  The "predict_capacity.py" package

This module is used for predicting the remaining life of lithium batteries. 

There are two main functions in this module. One is called ``partial_to_full``, which links the partial cycle curve to one full cycle curve. The other is called ``get_lifetime``, which gives all the parameters to diagnose the battery using the full cycle curve information. 
This module also includes a set of auxiliar functions that include:

1. ``curve_distance``: Calculates the dynamic time wraping distance between two time series
2. ``distance_cycle_to_full``: Calculates the distances between one partial cycle curve and a set of full cycle curves. 
3. ``life_plot``: This is a visualization function, that plots the results from the prediction method.



