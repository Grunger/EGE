data = open('24-153.txt').readline().strip()
print(len([s for s in [data[i:i + j] for i in range(len(data) - 6) for j in range(6, 10 + 1)] if
           s[0] == 'A' and s[-1] == 'F']))
