from tabulate import tabulate

halving = 32
reward = 50
total_supply = 0
blocks = 210000
capped = 21000000

datos = []


initial_reward = reward *100000000 #convertidos a SATS directamente
total_supply_i = blocks * reward
percentage_i = (total_supply_i/capped) * 100
datos.append([f"Initial", initial_reward, total_supply_i, percentage_i])

total_supply += total_supply_i
for i in range(31):
    b_reward = reward / pow(2,i+1)
    reward_sats = b_reward * 100000000 #convert BTC to SATS
    supply = blocks * b_reward
    total_supply += supply

    percentage = (total_supply/capped)*100
    datos.append([f"{i + 1} halving", reward_sats, total_supply, percentage])
    

print("\n Monetary Policy of Bitcoin")
print(tabulate(datos, headers=["Halving", "Reward (SATS)", "Total Supply (BTC)", "Percentage (%)"], floatfmt=".2f"))





