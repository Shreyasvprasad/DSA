def calculate_killed_soldiers_and_power(arr, power):
    count = 0
    total_power = 0

    for soldier_power in arr:
        if soldier_power <= power:
            count += 1
            total_power += soldier_power
        else:
            break
    
    return count, total_power

def main():
    n = int(input("Enter the number of soldiers: "))
    arr = list(map(int, input("Enter the powers of soldiers: ").split()))
    q = int(input("Enter the number of rounds: "))
    
    arr.sort()
    
    for _ in range(q):
        bishu_power = int(input("Enter Bishu's power for the round: "))
        killed_soldiers, total_power = calculate_killed_soldiers_and_power(arr, bishu_power)
        print("Killed soldiers:", killed_soldiers)
        print("Total power of killed soldiers:", total_power)

if __name__ == "__main__":
    main()
