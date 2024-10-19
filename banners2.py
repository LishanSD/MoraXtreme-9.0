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
    final_s = list(s) 

    
    for i in range(n):
        min_ops = float('inf')  
        best_char = s[i]  
        
        theme = themes[0]
        
        forward_diff = (ord(theme[i]) - ord(s[i]) + 26) % 26
        backward_diff = (ord(s[i]) - ord(theme[i]) + 26) % 26
        
        if forward_diff < min_ops:
            min_ops = forward_diff
            best_char = chr((ord(s[i]) - ord('a') + forward_diff) % 26 + ord('a'))  # Apply forward rotation

        if backward_diff < min_ops:
            min_ops = backward_diff
            best_char = chr((ord(s[i]) - ord('a') - backward_diff + 26) % 26 + ord('a'))  # Apply backward rotation
        
        print(f"i: {i}, theme: {theme}, forward_diff: {forward_diff}, backward_diff: {backward_diff}, min_ops: {min_ops}, best_char: {best_char}")
    
        
        final_s[i] = best_char
        total_operations += min_ops

    
    final_s = ''.join(final_s)
    
    
    print(f"Final string: {final_s}")
    
    return total_operations


n = int(input())  
s = input().strip()  
m = int(input())       
themes = [input().strip() for i in range(m)] 

#print(n, s, m, themes)


result = min_operations(n, s, themes)
print(result)
