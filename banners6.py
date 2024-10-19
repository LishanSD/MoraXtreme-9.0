def min_operations(n, s, themes):
    # Check for the length
    if len(s) != n or any(len(t) != n for t in themes):
        return -1

    # Check for lowercase English letters
    if not all(c.islower() for c in s) or any(not all(c.islower() for c in t) for t in themes):
        return -1
    
    # Check for the correct range of n
    if not (1 <= n <= 100):
        return -1

    total_operations = 0
    
    for i in range(n):
        min_ops = float('inf')  # Initialize min operations as infinity
        
        for theme in themes:
            forward_diff = (ord(theme[i]) - ord(s[i]) + 26) % 26  # Forward rotation
            backward_diff = (ord(s[i]) - ord(theme[i]) + 26) % 26  # Backward rotation
            
            min_ops = min(min_ops, forward_diff, backward_diff)  # Get the minimum operation
            
            # Debugging info (can be toggled off if needed)
            print(f"i: {i}, theme: {theme}, forward_diff: {forward_diff}, backward_diff: {backward_diff}, min_ops: {min_ops}")

        total_operations += min_ops  # Add the minimum operations for this character

    return total_operations

# Example usage:
n = int(input())  
s = input().strip()  
m = int(input())       
themes = [input().strip() for i in range(m)] 

result = min_operations(n, s, themes)
print(result)
