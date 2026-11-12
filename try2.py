arr_gas = [763061, 63491, 32829, 31163, 102544]
arr_price = [0] * 5
gas_to_gwei = 0.9526
eth_to_usd = 2394.84

for i in range(len(arr_gas)):
    arr_price[i] = arr_gas[i] * gas_to_gwei / 10**9 * eth_to_usd

print(arr_price)