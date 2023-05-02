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

def pl_bar(df):
    fig = px.bar(data_frame=df,
        x="date",
        y="amount",
        color="won",
        hover_data=["name", "category"]
        )
    return fig

df = preprocess()
fig = pl_bar(df=df)
fig.show()