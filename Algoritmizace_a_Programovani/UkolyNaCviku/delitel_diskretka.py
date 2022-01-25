
cntr = 0
for i in range(1, 1801):
    if i % 10 == 0 or i % 12 == 0 or i % 15 == 0:
        cntr += 1

print(cntr)
