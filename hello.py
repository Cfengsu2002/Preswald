from preswald import connect, get_df, table, text, plotly
import pandas as pd
import plotly.express as px

connect()

df = pd.read_csv("data/titanic.csv")
filtered_df = df[df["Age"] < 18]

text("# Titanic Data Analysis App")
text("This app explores Titanic passenger data 🚢\n")
text(f"Total passengers in dataset: {len(df)}")
text(f"Number of children (Age < 18): {len(filtered_df)}\n")

table(filtered_df, title="Children Passengers (under 18)")

fig = px.scatter(
    filtered_df,
    x="Age",
    y="Fare",
    color="Sex",
    title="Titanic: Age vs Fare (Children Only)",
    labels={
        "Age": "Passenger Age",
        "Fare": "Ticket Fare (USD)"
    }
)

fig.update_traces(
    textposition="top center",
    marker=dict(size=10, line=dict(width=1))
)

fig.update_layout(template="plotly_white")

plotly(fig)
