#!/usr/bin/env python


print('D1 = {"a":1, "b":2}')
print('D2 = {"c":6, "a":2}')
print("Merge D1 and D2 in D3")

D1 = {"a":1, "b":2}
D2 = {"c":6, "a":2}

D3 = {**D1, **D2}

print(D3)

