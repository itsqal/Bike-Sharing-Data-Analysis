import streamlit as st
import pandas as pd
import dataframes
import visualization as vs
from format import clean_category, set_date_dtype
import pathlib

current_dir = pathlib.Path(__file__).parent.resolve()

day_file_path = current_dir.parent / 'data' / 'day.csv'
hour_file_path = current_dir.parent / 'data' / 'hour.csv'

# Membuat dataframe
day_df = pd.read_csv(day_file_path)
hour_df = pd.read_csv(hour_file_path)

# Bersihkan kedua data
clean_category(day_df)
set_date_dtype(day_df)

clean_category(hour_df)
set_date_dtype(hour_df)

# Set filter waktu
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

# Sidebar for date input
with st.sidebar:
    selected_dates = st.date_input(
        label='Time Range',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter data based on selected date range
filtered_day_df = day_df[(day_df["dteday"] >= str(selected_dates[0])) & 
                         (day_df["dteday"] <= str(selected_dates[1]))]

filtered_hour_df = hour_df[(hour_df["dteday"] >= str(selected_dates[0])) & 
                           (hour_df["dteday"] <= str(selected_dates[1]))]

# Create dataframes from filtered data
season_user_df = dataframes.create_season_user_df(filtered_day_df)
month_user_df = dataframes.create_monthly_user(filtered_day_df)
casual_registered_hour_df = dataframes.create_casual_registered_hour_df(filtered_hour_df)
casual_registered_workingday_df = dataframes.create_casual_registered_workingday_df(filtered_hour_df)
casual_registered_season_df = dataframes.create_casual_registered_season_df(filtered_hour_df)

st.title('Dashboard Bikesharing System Historical Log 2011-2012')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Bike Rentals per Season',
                                        'Bike Rentals per Month',
                                        'Casual vs Registered User by Hour',
                                        'Casual vs Registered User by Workingdays',
                                        'Casial vs Registered User by Season'])

with tab1:
    fig = vs.season_user_lineplot(season_user_df)
    st.pyplot(fig)

with tab2:
    fig = vs.monthly_user_lineplot(month_user_df)
    st.pyplot(fig)

with tab3:
    fig = vs.casual_registered_hour_lineplot(casual_registered_hour_df)
    st.pyplot(fig)

with tab4:
    fig = vs.casual_registered_workingday_barplot(casual_registered_workingday_df)
    st.pyplot(fig)

with tab5:
    fig = vs.casual_registered_season_barplot(casual_registered_season_df)
    st.pyplot(fig)