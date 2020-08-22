ct_max = 0
ct = 0
for s in list(input()):
    if s == 'R':
        ct += 1
    else:
        ct = 0
    if ct > ct_max:
        ct_max = ct

print(ct_max)
