# Import required libraries
import matplotlib.pyplot as plt

# Define the data
votes = ["For", "Against"]
probabilities = [62, 38]

# Create the figure
plt.figure(figsize=(8, 6))

# Draw the bar chart
bars = plt.bar(votes, probabilities, color=['steelblue', 'grey'])

# Beautifying the plot
plt.title('Probability of Each Voting Outcome', fontsize=20)
plt.xlabel('Voting outcome', fontsize=15)
plt.ylabel('Probability (%)', fontsize=15)

# Set axis limits and ticks explicitly
plt.ylim(0, 100)
plt.yticks(range(0, 101, 10), fontsize=12)

# Add the percentage labels on top of the bars
for bar, probability in zip(bars, probabilities):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 2,
        f"{probability}%",
        ha="center",
        va="bottom",
        fontsize=12
    )

# Save and show
plt.tight_layout()
plt.savefig("pics/task1_bernoulli.pdf", dpi=300)
plt.show()