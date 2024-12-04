# How many different ways can £2 be made using any number of coins?
coins_worth = [1, 2,5,10,20,50,100,200] #in pence

def count_ways(value:int, coins_to_use:list[int])->int:
    if value ==0:
        return 1
    coins_to_use = coins_to_use.copy()
    coins_to_use.sort()
    if len(coins_to_use) == 1:
        return 1
    max_coin = coins_to_use.pop()
    ways_count = 0
    while value >= 0:
        ways_count+= count_ways(value, coins_to_use)
        value-=max_coin
    return ways_count

print(3, [1], count_ways(3, [1]))
print(3, [2], count_ways(3, [2]))
print(3, [1,2], count_ways(3, [1,2]))
print(4, [1,2], count_ways(4, [1,2]))
print(10, [1, 2,5], count_ways(10, [1, 2,5]))
print(200, coins_worth,count_ways(200, coins_worth))