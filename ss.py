import pandas as pd
import streamlit as st
import plotly.express as px

# Read the data
df1 = pd.read_csv("Day_ahead_prices2")
df2 = pd.read_csv("load_and_forecast")
df3 = pd.read_csv("Winds and solar forecast")

# Combine the data from both DataFrames
combined_data = pd.concat([df1, df2, df3], axis=1)

# Write the combined data to a new CSV file
combined_data.to_csv("combined_data.csv", index=False)

# Read the combined data
df = pd.read_csv('combined_data.csv', parse_dates=True)
df2 = df.rename(columns={"Unnamed: 0": "time", "0": "day_ahead_prices"})
columns_to_keep = ["time","day_ahead_prices", "Forecasted Load","Actual Load","Solar","Wind Offshore","Wind Onshore"]
df1= df2[columns_to_keep]
# Display the data as a table
st.title("Combined Data Table")
st.table(df1.head(20))

# Define the available variables
available_variables = ["day_ahead_prices", "Forecasted Load", "Actual Load", "Solar", "Wind Offshore", "Wind Onshore"]

# Set up the Streamlit app
st.title("Line Plot Dashboard")

# Create the sidebar with checkboxes
selected_variables = st.sidebar.multiselect("Select Variables", available_variables, default=["day_ahead_prices"])

# Filter the dataframe based on the selected variables
filtered_df = df1[["time"] + selected_variables]

# Plot the line charts
for variable in selected_variables:
    fig = px.line(filtered_df, x="time", y=variable)
    fig.update_layout(height=700, width=900)
    st.plotly_chart(fig)
