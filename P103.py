import plotly.express as px
import pandas as pd
df=pd.read_csv("Copy+of+data+-+data.csv")
fig=px.scatter(df,x="date",y="cases",color="country",size_max=70)
fig.show()