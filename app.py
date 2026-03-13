import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the processed dataset
df = pd.read_csv("data/formatted_salesdata.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    labels={
        "date": "Date",
        "sales": "Sales ($)",
        "region": "Region"
    },
    title="Pink Morsel Sales Over Time"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    
    html.H1(
        "Soul Foods Pink Morsel Sales Visualizer",
        style={"textAlign": "center"}
    ),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )

])

if __name__ == "__main__":
    app.run(debug=True)