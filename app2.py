import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load processed data
df = pd.read_csv("data/formatted_salesdata.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div(

    style={
        "backgroundColor": "#F4F6F7",
        "fontFamily": "Arial",
        "padding": "30px"
    },

    children=[

        # Header
        html.H1(
            "Soul Foods Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2C3E50",
                "marginBottom": "10px"
            }
        ),

        html.P(
            "Analyze sales trends before and after the January 15, 2021 price increase.",
            style={
                "textAlign": "center",
                "color": "#566573",
                "marginBottom": "40px"
            }
        ),

        # Radio Buttons
        html.Div(

            style={
                "textAlign": "center",
                "marginBottom": "30px"
            },

            children=[

                html.Label(
                    "Filter by Region:",
                    style={
                        "fontWeight": "bold",
                        "marginRight": "10px"
                    }
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"}
                    ],
                    value="all",
                    inline=True
                )
            ]
        ),

        # Graph
        dcc.Graph(id="sales-chart")

    ]
)

# Callback
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region",
        labels={
            "date": "Date",
            "sales": "Total Sales ($)",
            "region": "Region"
        },
        title="Pink Morsel Sales Over Time"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#F4F6F7",
        title_x=0.5
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)