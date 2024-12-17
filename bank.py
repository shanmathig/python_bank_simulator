#Bank Simulation!
def solution(balances, requests):
    def isValidAcc(i):
        return 1 <= i <= len(balances)
        
    for reqNum, request in enumerate(requests):
        parts = request.split()
        if parts[0] == "withdraw":
            i = int(parts[1])
            amt = int(parts[2])
            if not isValidAcc(i) or amt > balances[i-1]: return [-reqNum - 1]
            balances[i-1] -= amt
        elif parts[0] == "transfer":
            i = int(parts[1])
            j = int(parts[2])
            amt = int(parts[3])
            if not isValidAcc(i) or not isValidAcc(j) or amt > balances[i-1]: return [-reqNum - 1]
            balances[i-1] -= amt
            balances[j-1] += amt
        elif parts[0] == "deposit":
            i = int(parts[1])
            amt = int(parts[2])
            if not isValidAcc(i): return False
            balances[i-1] += amt
    return balances


def main():
    # Test case 1: Valid operations
    balances = [100, 200, 300]
    requests = [
        "withdraw 1 50",   
        "deposit 2 30",     
        "transfer 2 3 50"
    ]
    print(solution(balances, requests))  # Output: [50, 180, 350]

    # Test case 2: Invalid withdraw (insufficient funds)
    balances = [100, 200, 300]
    requests = [
        "withdraw 1 150" 
    ]
    print(solution(balances, requests))  # Output: [-1]

    # Test case 3: Invalid account number
    balances = [100, 200, 300]
    requests = [
        "withdraw 4 50" 
    ]
    print(solution(balances, requests))  # Output: [-1]

main()
