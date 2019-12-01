cover_price=24.95
discount=0.5
shipping_costs_1=3
shipping_costs_2=0.75
copies=100

total_cost=(1-discount)*(cover_price*copies)+shipping_costs_1+shipping_costs_2*(copies-1)

print(total_cost)
