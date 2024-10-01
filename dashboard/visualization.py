import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style='dark') 

def season_user_lineplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.lineplot(x='season', y='cnt', data=df, marker="o", linewidth=2.5, color='b')

    ax.set_title('Bike Sharing Rentals per Season', fontsize=14, fontweight='bold')
    ax.set_xlabel('')
    ax.set_ylabel('Count of Rentals', fontsize=12)

    # Format y-axis dengan ribuan
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    ax.grid(True, linestyle='--', alpha=0.6)
    
    return fig

def monthly_user_lineplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.lineplot(x='mnth', y='cnt', data=df, marker="o", linewidth=2.5, color='b')

    ax.set_title('Bike Sharing Rentals per Month', fontsize=14, fontweight='bold')
    ax.set_xlabel('')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_ylabel('Count of Rentals', fontsize=12)

    # Format y-axis dengan ribuan
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.grid(True, linestyle='--', alpha=0.6)

    return fig

def casual_registered_hour_lineplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.lineplot(x='hr', y='casual', data=df, label='Casual Users', marker='o')
    sns.lineplot(x='hr', y='registered', data=df, label='Registered Users', marker='o')

    ax.set_title('Bike Rentals by Hour (Casual vs Registered)', fontsize=14)
    ax.set_xlabel('Hour of the Day', fontsize=12)
    ax.set_ylabel('Number of Rentals', fontsize=12)

    ax.grid(True)

    # Format y-axis dengan separator ribuan
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    ax.legend(title='User Type')

    return fig

def casual_registered_workingday_barplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))

    df.set_index('workingday')[['casual', 'registered']].plot(kind='bar', ax=ax, color=['skyblue', 'salmon'])

    ax.set_title('Average Bike Rentals by User Type on Working Days and Non-Working Days', fontsize=14)
    ax.set_xlabel('Working Day', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.set_ylabel('Average Number of Rentals', fontsize=12)

    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    # Format y-axis dengan separator ribuan
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    ax.legend(title='User Type')

    return fig


def casual_registered_season_barplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))

    df.set_index('season')[['casual', 'registered']].plot(kind='bar', ax=ax, color=['skyblue', 'salmon'])

    ax.set_title('Bike Rentals by User Type in Different Seasons', fontsize=14)
    ax.set_xlabel('')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.set_ylabel('Number of Rentals', fontsize=12)

    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    # Format y-axis with thousand separators
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    ax.legend(title='User Type')

    return fig