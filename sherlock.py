def find_longest_suffix(note, hints):
    note_len = len(note)
    results = []
    
    for hint in hints:
        hint_len = len(hint)
        longest_suffix_length = 0
        
        
        for suffix_len in range(hint_len, 0, -1):
            suffix = hint[-suffix_len:] 
            
          
            note_pointer = 0
            suffix_pointer = 0
            
            while note_pointer < note_len and suffix_pointer < suffix_len:
                if note[note_pointer] == suffix[suffix_pointer]:
                    suffix_pointer += 1
                note_pointer += 1
            
            if suffix_pointer == suffix_len:
                longest_suffix_length = suffix_len
                break 
        
        results.append(longest_suffix_length)
    
    return results


# Input
note = input().strip() 
n = int(input()) 
hints = [input().strip() for _ in range(n)] 


results = find_longest_suffix(note, hints)
for res in results:
    print(res)
