import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame from the provided data
data = {
    "Regressor": ["LinearRegression", "DecisionTreeRegressor", "RandomForest"],
    "Tuned Parameters": [
        "{'fit_intercept': True}", 
        "{'min_samples_leaf': 2, 'min_samples_split': 2}", 
        "{'min_samples_leaf': 2, 'min_samples_split': 3, 'n_estimators': 100}"
    ],
    "Best Score": [0.7539420804197905, 0.7548737080840036, 0.7605306297813516],
    "MAE": [0.7153119740251251, 0.6498545108306477, 0.6466399218342249],
    "MSE": [1.7357713929975975, 1.7032186770377924, 1.6741250134251238],
    "R2 Score": [0.755062349421775, 0.7596559184823672, 0.7637613747888534]
}

df = pd.DataFrame(data)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
df.plot(x='Regressor', y=['Best Score', 'MAE', 'MSE', 'R2 Score'], kind='bar', ax=ax)
plt.title('Comparison of Regression Models')
plt.ylabel('Scores and Errors')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.close()


import plotly.graph_objects as go
import pandas as pd

# Your data with values rounded to two decimal places
data = {
    "Regressor": ["LinearRegression", "DecisionTreeRegressor", "RandomForest"],
    "Tuned Parameters": [
        "{'fit_intercept': True}", 
        "{'min_samples_leaf': 2, 'min_samples_split': 2}", 
        "{'min_samples_leaf': 2, 'min_samples_split': 3, 'n_estimators': 100}"
    ],
    "Best Score": [0.75, 0.75, 0.76],
    "MAE": [0.72, 0.65, 0.65],
    "MSE": [1.74, 1.70, 1.67],
    "R2 Score": [0.76, 0.76, 0.76]
}
df_rounded = pd.DataFrame(data)

# Creating a Plotly table
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df_rounded.columns),
                fill_color='paleturquoise',
                align='center'),
    cells=dict(values=[df_rounded.Regressor, df_rounded['Tuned Parameters'], df_rounded['Best Score'], df_rounded.MAE, df_rounded.MSE, df_rounded['R2 Score']],
               fill_color='lavender',
               align='center'))
])

fig.update_layout(width=1200, height=600)
fig.show()


