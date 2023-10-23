a = float(input("zadejte koeficient a"))
b = float(input("zadejte koeficient b"))
c = float(input("zadejte koeficient c"))

diskriminant = b * b - 4*a*c

if diskriminant > 0:
  x1 = (-b + (diskriminant ** 0.5)) / (2 * a)
  x2 = (-b - (diskriminant ** 0.5)) / (2 * a)
  print("rovnice má 2 kořeny")
  print(f"kořen x1 je {x1} kořen x2 je {x2}")
elif diskriminant == 0:
  x = (-b)/ (2 * a)
  print(f"kořen je x je {x}")
else:
  print("rovnice nemá realný kořen")