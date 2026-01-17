test_dict = {"Codingal": 3, "is": 2, "best": 2, "for": 2, "Coding": 1}

R = 2

res = 0
for key in test_dict:
    if test_dict[key] == R:
        res += 1

print(" The number of keys with value R : " + str(res))