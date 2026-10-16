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

data = []
client_a_plots = []
client_b_plots = []
client_c_plots = []

def calc_perceived_util(payout: int, probability: float, client: str):
    if client == 'clientA':
        return probability*util_client_a(payout) + (1-probability)*util_client_a(0)
    elif client == 'clientB':
        return probability*util_client_b(payout) + (1-probability)*util_client_b(0)
    elif client == 'clientC':
        return probability*util_client_c(payout) + (1-probability)*util_client_c(0)
    else:
        return -1

def util_inverse (eu: float, client: str):
    if client == 'clientA':
        return 1000 * (math.exp(eu/0.2) - 1)
    elif client == 'clientB':
        return 200 * (math.exp(eu/0.14) - 1)
    elif client == 'clientC':
        return 100000 * (math.exp(eu/1.43) - 1)
    else:
        return -1

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

# TASK 2: compute perceived values of investment
data = np.array(data)
print(data)
perceived_values = []

clients = ['clientA', 'clientB', 'clientC']

#part 1
for i in data:
    investment_client = str(i[0])
    investment_prob = float(i[1])
    investment_payout = int(i[2])

    for client in clients :
        investment_perceived_util = calc_perceived_util(investment_payout, investment_prob, client)
        perceived_values.append([investment_perceived_util, client, f'owner: {investment_client}'])

print(f'Each client’s perceived utility of each investment: {perceived_values}')

#part 2
indifferent_offers = []

for i in perceived_values:
    dollars_offer = util_inverse(i[0], i[1])
    indifferent_offers.append([dollars_offer, i[1], i[2]])

print(f'\nAmount that you could offer each client for each investment for them to be indifferent: {indifferent_offers}')

#TASK 3: Reflection
#1. To whom should each of the 6 investments be sold? Why?

#Investment 1: It should be sold to client C. This client values investment 1 the most out of each client
# since they have the largest indifference value at $42286.44

#Investment 2: It should be sold to client C. This client values investment 2 the most out of each client
# since they have the largest indifference value at $9544.51

#Investment 3: It should be sold to client C. This client values investment 3 the most out of each client
# since they have the largest indifference value at $86606.60

#Investment 4: It should be sold to client C. This client values investment 4 the most out of each client
# since they have the largest indifference value at $14406.64

#Investment 5: Client C should keep their investment. This client values investment 5 the most out of each client
# since they have the largest indifference value at $957.66

#Investment 6: Client C should keep their investment. This client values investment 6 the most out of each client
# since they have the largest indifference value at $3261.32


#2. Pick one investment that should be sold. Who should it be sold to, and what is the maximum price it could be sold for? What utility gain is provided to each party at that price?
# Let's choose client A's first investment. P = 0.6 and payout = 80000

# Find the utility for all clients if they took the first investment
invest_payout_a1 = int(data[0][2])
invest_prob_a1 = float(data[0][1])
investment_utils = []
for i in range(0, 6, 2):
    if i <= 1:
        client = 'clientA'
    elif i <= 3:
        client = 'clientB'
    else:
        client = 'clientC'
    investment_utils.append(calc_perceived_util(invest_payout_a1,invest_prob_a1, client))
investment_utils = np.array(investment_utils)

# Calculate the indifference price based off the utilities we found
investment_prices = []
for utility in investment_utils:
    if i <= 0:
        client = 'clientA'
    elif i <= 1:
        client = 'clientB'
    else:
        client = 'clientC'
    investment_prices.append(util_inverse(utility,client))

print(f'Utilities of each client for the first investment: {investment_utils}')
print(f'Prices of first investment for each client: {investment_prices}')

# get the maximum price it could be sold for
max_price = np.max(investment_prices)

# calculate utility of first investment but the payout is max_price
investment_utils_max_price = []
for i in range(0, 6, 2):
    if i <= 1:
        client = 'clientA'
    elif i <= 3:
        client = 'clientB'
    else:
        client = 'clientC'
    investment_utils_max_price.append(calc_perceived_util(max_price,invest_prob_a1, client))

investment_utils_max_price = np.array(investment_utils_max_price)
#Find the difference betwwen utility scores of different payouts
investment_util_diff = investment_utils_max_price - investment_utils

print(f'Utility gain for each client: {investment_util_diff}')

print(calc_perceived_util())