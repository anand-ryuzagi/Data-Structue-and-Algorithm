#Greedy algorithm - Minimum coin exchange solution

result = []

def bubbleSort(coins):
    size = len(coins)
    for i in range(size-1):
        for j in range(size-1-i):
            if coins[j]<coins[j+1]:
                swap(j,j+1,coins)

def swap(a,b,arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def minimumCoinExchange(coins,size,value):
    count = 0
    for i in range(size):
        while value >= coins[i]:
            value = value - coins[i]
            result.append(coins[i])
            count += 1
        if value == 0:
            break

    return count

if __name__ == "__main__":
    coins = [25,20,10,5]
    bubbleSort(coins)
    print(coins)
    print(minimumCoinExchange(coins,4,55))
    print(result)
