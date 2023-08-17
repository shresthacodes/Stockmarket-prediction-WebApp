import datetime as dt
from sklearn.preprocessing import MinMaxScaler
import streamlit as st
from keras.models import load_model
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

<<<<<<< HEAD

=======
# import pandas_datareader as data
# import pandas_datareader.data as web
>>>>>>> 5714200 (changes)

st.title("Stock trend detection")
user_input = st.text_input("Enter stock ticker", 'AAPL')
df = yf.download(user_input, start='2020-01-01', end='2023-7-31')
<<<<<<< HEAD

=======
# df.head()
>>>>>>> 5714200 (changes)

# Description of data
st.subheader("Data from 2021 to 2023")
st.write(df.describe())

# visualisation
st.subheader('Closing price vs Time chart')
fig = plt.figure(figsize=(12, 6))
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing price vs Time chart with 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize=(12, 6))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing price vs Time chart with 100MA & 200MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(12, 6))
plt.plot(ma100)
plt.plot(ma200)
plt.plot(df.Close)
st.pyplot(fig)
# Splitting data into training and testing
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])
print(data_training.shape)
print(data_testing.shape)

scaler = MinMaxScaler(feature_range=(0, 1))
data_training_array = scaler.fit_transform(data_training)


# load the model
model = load_model(
    '/Users/shrestharaj/Desktop/git/potential-potato/keras_model.h5')
# testing part
# data_testing.head()
past_100_days = data_training.tail(100)
final_df = past_100_days._append(data_testing, ignore_index=True)
input_data = scaler.fit_transform(final_df)
x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100: i])
    y_test.append(input_data[i, 0])
x_test, y_test = np.array(x_test), np.array(y_test)
y_predicted = model.predict(x_test)
scaler = scaler.scale_

scale_factor = 1/scaler[0]
y_predicted = y_predicted*scale_factor
y_test = y_test*scale_factor

# Final graph
st.subheader("Prediction Vs Original")
plt.figure(figsize=(12, 6))
plt.plot(y_test, 'b', label='Original Price')
plt.plot(y_predicted, 'r', label='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()
