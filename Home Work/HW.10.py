coins = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
i = 0
much = 0

ones = coins.count(1)
zeros = coins.count(0)

if ones <= zeros:
    while i < len(coins):
        if coins[i] == 1:
            coins[i] = 0
            much = much + 1
        else:
            i = i + 1

elif ones > zeros:
    while i < len(coins):
        if coins[i] == 0:
            coins[i] = 1
            much = much + 1
        else:
            i = i + 1

print(much)