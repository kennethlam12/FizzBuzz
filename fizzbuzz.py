for x in range(1, 101):
  s = ""
  if not x % 3:
      s += "Fizz"
  if not x % 5:
      s += "Buzz"
  if s == "":
      s = x
  print(s)
