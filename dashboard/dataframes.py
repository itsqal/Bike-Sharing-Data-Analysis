import pandas as pd

def create_season_user_df(df):
    season_user_df = df.groupby('season')['cnt'].sum().reset_index()
    return season_user_df

def create_monthly_user(df):
    monthly_user_df = df.groupby('mnth')['cnt'].sum().reset_index()
    return monthly_user_df

def create_casual_registered_hour_df(df):
    casual_registered_hour_df = df.groupby('hr').agg({
    'casual': 'sum',
    'registered': 'sum'
    }).reset_index()
    return casual_registered_hour_df

def create_casual_registered_workingday_df(df):
    casual_registered_workingday_df = df.groupby('workingday').agg({
    'casual': 'sum',
    'registered': 'sum'
    }).reset_index()
    return casual_registered_workingday_df

def create_casual_registered_season_df(df):
    casual_registered_season_df = df.groupby('season').agg({
    'casual': 'sum',
    'registered': 'sum'
    }).reset_index()
    return casual_registered_season_df

