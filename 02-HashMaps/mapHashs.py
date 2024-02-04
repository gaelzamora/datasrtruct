'''
myMap = {}
myMap["Alice"] = 89
myMap["Bob"] = 12

myMap["Alice"] += 1

print(len(myMap))
print(myMap)
myMap = {i:2*i for i in range(3)}
print(myMap)
'''

myMap = {"alice": 90, "bob": 70}
for key in myMap:
    print("Clave: "+key, "Valor: ",myMap[key])

for val in myMap.values():
    print("Valor: ",val)

for key, val in myMap.items():
    print(key, val)