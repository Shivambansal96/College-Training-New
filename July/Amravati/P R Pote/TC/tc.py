import matplotlib.pyplot as plt
import numpy as np
import math

# Sample input sizes
n = np.linspace(1, 10, 100)

# Time complexity functions
O_1 = np.ones_like(n)
O_log_n = np.log2(n)
O_n = n
O_n_log_n = n * np.log2(n)
O_n2 = n**2
O_2n = 2**n
O_nf = [math.factorial(int(i)) if i <= 10 else float('nan') for i in n]

# Plot
plt.figure(figsize=(12, 7))
plt.plot(n, O_1, label='O(1) — Constant')
plt.plot(n, O_log_n, label='O(log n) — Logarithmic')
plt.plot(n, O_n, label='O(n) — Linear')
plt.plot(n, O_n_log_n, label='O(n log n) — Log-linear')
plt.plot(n, O_n2, label='O(n²) — Quadratic')
plt.plot(n, O_2n, label='O(2ⁿ) — Exponential')
plt.plot(n, O_nf, label='O(n!) — Factorial')

plt.ylim(0, 100)
plt.title('Time Complexity Growth Rates')
plt.xlabel('Input size (n)')
plt.ylabel('Operations (scaled)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save and show the plot
plt.savefig("time_complexity_chart.png")
plt.show()
