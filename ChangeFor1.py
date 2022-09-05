

for p in range(0,101,1):
  for n in range(0,21,1):
    for q in range(0,5,1):
      for d in range (0,11,1):
        if 1*p + 5*n + 25*q + 10*d == 100:
          print(f'{p} pennies , {n} nickels, {q} quarters, {d} dimes')
