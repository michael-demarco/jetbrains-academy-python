import math

edge_length = abs(int(input()))

area = float(round((2 * math.sqrt(3) * math.pow(edge_length, 2)), 2))

volume = float(round(((1 / 3) * math.sqrt(2) * math.pow(edge_length, 3)), 2))

print(f"{area} {volume}")
