type = str(input())
if type == "triangle":
  a = float(input())
  b = float(input())
  c = float(input())
  p = float((a + b + c) / 2)
  print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif type == "rectangle":
  a = float(input())
  b = float(input())
  print(a * b)
elif type == "circle":
  r = float(input())
  print(3.14 * r ** 2)
else:
  print("Incorrect value")