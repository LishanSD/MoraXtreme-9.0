def enigmatic_rune_cipher(s):
    # Step 1: Remove surrounding quotes if present
    if s.startswith('"') and s.endswith('"'):
        s = s[1:-1]  # Remove the surrounding quotes
    
    # Step 2: Prime number assignments for each letter 'a' to 'z'
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
              47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    
    # Step 3: Frequency mapping
    freq = {}
    for char in s:
        if not ('a' <= char <= 'z'):  # Check for invalid characters
            return -1  # Return an error code if invalid
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Step 4: Calculate the final hash value
    MOD = 10**9 + 7
    total_hash = 0

    for index, char in enumerate(s):
        # 1-based index
        pos = index + 1
        # Get the prime number for the current character
        prime_value = primes[ord(char) - ord('a')]
        # Calculate transformed value
        transformed_value = prime_value * freq[char] * (pos ** 2)
        total_hash = (total_hash + transformed_value) % MOD

    # Step 5: Return the total hash value
    return total_hash

# Input reading
s = input().strip()  # Read the input string and remove extra spaces

# Call the function and print the result
print(enigmatic_rune_cipher(s))
