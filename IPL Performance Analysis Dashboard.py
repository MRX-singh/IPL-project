import matplotlib.pyplot as plt
import numpy as np


teams = ["MI","CSK","RCB","KKR","SRH","DC"]
matches_won = [10, 12, 8, 9, 7, 6]
runs_scored = [2200, 2400, 2100, 2000, 1800, 1700]
matches_played = [14, 14, 14, 14, 14, 14]

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.bar(teams,matches_won,color="orange",width=0.6)
for i in range(len(teams)):
    plt.text(teams[i],matches_won[i]+0.1,str(matches_won[i]),ha="center",fontsize=10)
plt.xlabel("Teams")
plt.ylabel("Won")
plt.title("Matches won by Teams")
plt.grid(axis="y", linestyle="dotted")


plt.subplot(1,2,2)
plt.scatter(matches_won,runs_scored,c=runs_scored,cmap="viridis", s=50,marker="o")
plt.xlabel("Teams")
plt.ylabel("Runs")
plt.title("win vs runs analysis")
cr=plt.colorbar()
cr.set_label("runs")

data=sorted(zip(matches_won,runs_scored))
x_sorted,y_sorted = zip(*data)
plt.plot(x_sorted,y_sorted,color="red",linestyle="dashed")
plt.grid()

for i in range(len(teams)):
    plt.text(matches_won[i]+0.1,runs_scored[i],str(teams[i]),ha="center",fontsize=10)

plt.tight_layout()
plt.show()
