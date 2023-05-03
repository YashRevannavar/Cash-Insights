import pandas as pd
import plotly.express as px
import numpy as np
# from sql import convert_to_df

def preprocess():
    df = pd.read_csv("data.csv", dtype={
            'category': str,
            'won': str,
            'name': str,
            'amount': np.float16})
    df['name'] = df['name'].astype('category')
    df['won'] = df['won'].astype('category')
    df['category'] = df['category'].astype('category')
    df['date'] = pd.to_datetime(df['date'],dayfirst=True)
    df = df.sort_values(by='date')
    return df

def won_bar(df):
    fig = px.bar(data_frame=df,
        x="date",
        y="amount",
        color="won",
        hover_data=["name", "category"],
        title="Psychology Desires Bar graph"
        )
    return fig

def cat_bar(df):
    fig = px.bar(data_frame=df,
        x="date",
        y="amount",
        color="category",
        hover_data=["name", "won"],
        title="Category Bar graph"
        )
    return fig

def won_pie(df):
    fig = px.pie(data_frame=df,
        values="amount",
        names="won",
        hole=0.25,
        hover_data=["won"],
        title="Psychology Desires Pie Chart" 
        )
    return fig

def cat_pie(df):
    fig = px.pie(data_frame=df,
        values="amount",
        names="category",
        hole=0.25,
        hover_data=["category"],
        title="Category Pie"
        )
    return fig

# df = preprocess()
# fig = pl_bar(df=df)
# fig.show()
