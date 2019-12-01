Shares=1000
PricePerShareBought=32.87
Commission=0.02
PricePerShareSell=33.92

ShareCost=Shares*PricePerShareBought
print('1.')
print(ShareCost)

Commission_Price_1=Commission*ShareCost
print('2.')
print(Commission_Price_1)

ShareSold=Shares*PricePerShareSell
print('3.')
print(ShareSold)

Commission_Price_2=Commission*ShareSold
print('4.')
print(Commission_Price_2)

TotalMoneyLeft=ShareSold-Commission_Price_2-Commission_Price_1-ShareCost
print('5.')
print(TotalMoneyLeft)
print('Joe lost money :( ')






