print("Hello")

import pandas as pd
import numpy as np

# Read the csv file from the location
input_path = "C:/Users/Kaushik Acharya/Documents/Python Scripts/Traffic-Prediction/data/traffic-violations-in-maryland-county/"

input_file = input_path + "Traffic_Violations.csv"

traffic_data = pd.read_csv(input_file)
traffic_data.shape


traffic_data_short = traffic_data.iloc[1:1000,]
traffic_data_short.shape
traffic_data_short.head()

# check for missing values per column
traffic_data_short.isna().sum()

# overall misisng values
traffic_data_short.isna().sum().sum()

# check for duplicates
traffic_data_short.duplicated().sum()