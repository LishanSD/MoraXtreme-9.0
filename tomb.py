def count_ways_to_forge(n, s):  
    length = len(s)

    dp = [0] * (length + 1)
    dp[0] = 1  # Base case: 1 way to split an empty string

    # Iterate through the string
    for i in range(1, length + 1):
        current_num = 0
        power = 1

        # Check all possible segments ending at i
        for j in range(i, max(0, i - len(str(n)))-1, -1):
            # Build the number without converting full substring to integer
            current_num = current_num + (ord(s[j-1]) - ord('0')) * power
            power *= 10
            
            if s[j-1] == '0':  # Skip numbers starting with '0'
                continue

            if current_num > n:  # No need to check further
                break

            dp[i] += dp[j-1]

    return dp[length]

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])  # Number of test cases
    idx = 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        S = data[idx + 1]
        results.append(str(count_ways_to_forge(N, S)))
        idx += 2
    
    # Output all results at once for efficiency
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
