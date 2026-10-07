"""
COMP 3625
Lab 4
Professor: Eric Chalmers
Group members: Sean Jose, Katrina Bourgeois
Due date: October 16
"""
import numpy as np
import csv
import math
import matplotlib.pyplot as plt

PAYOUT_FAIL = 0

data = []
client_a_plots = []
client_b_plots = []
client_c_plots = []

def calc_perceived_util(payout: int, probability: float):
    return probability*payout + (1-probability)*PAYOUT_FAIL

# Utility functions
def util_client_a(dollars: int):
    return 0.2 * math.log(dollars/1000 + 1)

def util_client_b(dollars: int):
    return 0.14 * math.log(dollars/200 + 1)

def util_client_c(dollars: int):
    return 1.43 * math.log(dollars/100000 + 1)

# read CSV values
with open('investment_data.csv', mode='r', encoding='utf-8') as file:
    # Create the reader object
    csv_reader = csv.reader(file)
    
    # Skip the header row
    header = next(csv_reader)

    for row in csv_reader:
        data.append(row)

# TASK 1: Plot utility functions
for i in range(0, 1000001, 10000): # $0 to $100000, only record every 10000th index
    client_a_plots.append(util_client_a(i))
    client_b_plots.append(util_client_b(i))
    client_c_plots.append(util_client_c(i))

plt.plot(client_a_plots, color='red', label='Client A')
plt.plot(client_b_plots, color='blue', label='Client B')
plt.plot(client_c_plots, color='green', label='Client C')
plt.legend()
plt.show()

# TASk 2: compute percieved values of investment
data = np.array(data)
print(data)

# client A investment 1
# U(success) = 80000
# U(failure) = 0
# P(payout|success) = 0.6
investment_a_1_prob = float(data[0][1])
investment_a_1_payout = int(data[0][2])
investment_a_1_util = calc_perceived_util(investment_a_1_payout,investment_a_1_prob)

print(investment_a_1_util)
