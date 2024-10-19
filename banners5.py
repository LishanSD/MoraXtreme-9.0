n = int(input())
word = input().strip()

if len(word) != n or not word.islower() or not word.isalpha():
    print(-1)
    exit()

m = int(input())
if m < 1 or m > 3: 
    print(-1)
    exit()

themes = [input().strip() for _ in range(m)]
if any(len(theme) != n or not theme.islower() or not theme.isalpha() for theme in themes):
    print(-1)
    exit()

if not (1 <= n <= 100):
    print(-1)
    exit()

L = {chr(i + 97): i for i in range(26)}
total_ops = []

for theme in themes:
    ops = [min((L[word[i]] - L[theme[i]]) % 26, (L[theme[i]] - L[word[i]]) % 26) for i in range(n)]
    total_ops.append(sum(ops))

print(min(total_ops))