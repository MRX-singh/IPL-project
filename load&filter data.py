import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel, title, ylabel
from sympy import false
from sympy.codegen.fnodes import kind

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

print(matches.head())
print(deliveries.head())

print(matches.shape)
print(deliveries.shape)

print(matches.info())
print(deliveries.info())
print((matches.isnull()).sum())
print((deliveries.isnull()).sum())

# # Fill missing winners
# matches["winner"].fillna("No Result", inplace=True)
#
# # Fill missing city (optional)
# matches["city"].fillna("Unknown", inplace=True)
#
# # Remove rows where batsman is missing
# deliveries.dropna(subset=["batsman"], inplace=True)

wins= matches["winner"].value_counts()
wins.head(10).plot(kind="bar",color="orange")

plt.xticks(rotation=25, ha="right")
for i , v in enumerate(wins):
    plt.text(i,v+1,str(v),ha="center")
plt.grid(axis="y", linestyle="--")
plt.ylabel("total wins")
# topbatsman
# runs= deliveries.groupby("batter")["batsman_runs"].sum()
# top_batsman=runs.sort_values(ascending=False).head(10)
# top_batsman.plot(kind="bar",color="skyblue")
# for i, v in enumerate(top_batsman):
#     plt.text(i,v+1,str(v),ha="center")
# plt.xticks(rotation=30)
# plt.title("High Run score Batsman")
# plt.ylabel("Number of runs")

# topstrike_rate
# balls=deliveries.groupby("batter")["ball"].count()
# strike_rate= (runs /balls)*100
# filter_sr=strike_rate[balls>200]
# top_sr= filter_sr.sort_values(ascending=False).head(10)
# for i ,v in enumerate(top_sr):
#     plt.text(i,v+1,round(v,1),ha='center')
# title("Top strike rate > 200",color='blue')
# ylabel("strike rate")
# top_sr.plot(kind="bar")

#runs_per over analysis
# runs_over=deliveries.groupby('over')["total_runs"].mean()
# runs_over = runs_over.sort_index()
#
# plt.plot(runs_over, marker=6, linestyle="--", color="red"
# )
plt.show()


