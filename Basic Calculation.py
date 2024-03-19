import matplotlib.pyplot as plt
import numpy as np

# Time Period
years = np.arange(1, 31, 1)

# Future Value Calculation
fv_goal_1 = goal_1_pv * (1 + annual_interest_rate)**years
fv_goal_2 = goal_2_pv * (1 + annual_interest_rate)**years

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(years, fv_goal_1, label='Goal 1 (15 Crores in 10 Years)')
plt.plot(years, fv_goal_2, label='Goal 2 (50 Crores in 30 Years)')

# Adding Labels and Title
plt.xlabel('Years')
plt.ylabel('Future Value (INR)')
plt.title('Growth of Savings Over Time')
plt.legend()
plt.grid(True)
plt.show()
