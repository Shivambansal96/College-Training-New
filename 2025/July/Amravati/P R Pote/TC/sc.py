import matplotlib.pyplot as plt
import numpy as np

# Sample input sizes
n = np.linspace(1, 100, 100)

# Space complexity functions (scaled for visibility)
O_1 = np.ones_like(n)
O_log_n = np.log2(n)
O_n = n
O_n2 = n**2

# Plot
plt.figure(figsize=(12, 7))
plt.plot(n, O_1, label='O(1) — Constant Space')
plt.plot(n, O_log_n, label='O(log n) — Logarithmic Space')
plt.plot(n, O_n, label='O(n) — Linear Space')
plt.plot(n, O_n2, label='O(n²) — Quadratic Space')

plt.title('Space Complexity Growth Rates')
plt.xlabel('Input size (n)')
plt.ylabel('Memory Usage (scaled units)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save and show the plot
plt.savefig("space_complexity_chart.png")
plt.show()
