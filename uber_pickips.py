import streamlit as st 
import pandas as pd 
import numpy as np

st.title('Uber pickups in NY')

#-- Fecht Data --#

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache 
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace = True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

#This creates a text element and let the reader know the data is loading. 
data_load_state = st.text('Loading data...')
#Now load 10.000 rows of data into the dataframe. 
data = load_data(10000)
#This notify the reader that the data was successfully loaded. 
data_load_state.text('Loading data...done!!')

#-- Using a button to toggle data --#
if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(data)

#--Drawing a Histogram--#

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)


#--Pltting the data on a map--#

#We are gonna filtered the data because we deteremined that the busiest hour for Uber pickups was 17:00.
hour_to_filter = st.slider('hour', 0, 23, 17) #This strealit's widget allow us to filter the results by hour. (min: 0h, max: 23h, default: 17h)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data) #This scripts allow us to plot the data on the mapself.


