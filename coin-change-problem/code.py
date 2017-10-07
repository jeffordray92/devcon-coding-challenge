coins = [2,3,5,6]
change = 10


def solution (coins, change):
  combo = []
  for coin in coins:
    if (change%coin) == 0:
      temp = []
      for x in range(change//coin):
        temp.append(coin)  
      combo.append(temp)

    print combo
    # if remainder == 0:

solution(coins, change)
