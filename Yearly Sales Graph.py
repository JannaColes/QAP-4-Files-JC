# Title: Yearly Sales Report 2023
# Program Description: The program allows users to enter monthly sales then creates a graph to display results.
# Written By: Janna Coles
# Stared On: July 17, 2023
# Finished On: July 26, 2023

# Import necessary modules
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Initialize empty lists for x and y values
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = []

# Get the sales input from the user for each month
for month in months:
    sales_amount = float(input(f"Enter the sales amount for {month}: $ "))
    sales.append(sales_amount)

# Create the graph with fonts and colors
plt.plot(months, sales, marker='p', color='teal', linewidth=2, linestyle='-', label='Sales', markersize=6)
plt.xlabel("Months", fontsize=16, fontweight='bold', color='orange')
plt.ylabel("Total Sales", fontsize=16, fontweight='bold', color='orange')
plt.title("Yearly Sales Report - 2023", fontsize=20, fontweight='bold', color='orange')
plt.grid(True, linestyle='--', alpha=0.7)

# Customize the legend
plt.legend(loc='upper right', fontsize=10)

# Add some background color
plt.gca().set_facecolor('whitesmoke')

# Set custom formatting for y-axis values with a dollar sign
plt.gca().get_yaxis().set_major_formatter(mticker.StrMethodFormatter('${x:,.0f}'))

# Display the graph
plt.tight_layout()
plt.show()