print("Financial Analysis")
print("-----------------")

import os
import csv
import pandas as pd

budget_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

df = pd.read_csv(budget_csv)

number_of_months = len(df)
print(f"Total months: {number_of_months}")

total_amount = df["Profit/Losses"].sum()
print(f"Total: ${total_amount:,.0f}")

df['Change'] = df['Profit/Losses'].diff()

average_change = df['Change'].mean()
print(f"Average Change: ${average_change:.2f}")

max_increase = df.loc[df['Change'].idxmax()]
print(f"Greatest Increase in Profits: {max_increase['Date']} (${max_increase['Change']:,.0f})")

max_decrease = df.loc[df['Change'].idxmin()]
print(f"Greatest Decrease in Profits: {max_decrease['Date']} (${max_decrease['Change']:,.0f})")
