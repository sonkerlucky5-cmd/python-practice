# Tuple creation
t = (10, 20, 30, 40, 50)
print("First element:", t[0])
print("Last element:", t[-1])

# Loop through tuple
print("\nLoop:")
for i in t:
    print(i)

# Nested tuple
students = (
    ("Lucky", 20, "ML"),
    ("Rahul", 22, "AI"),
    ("Aman", 19, "DS")
)

print("\nNested Tuple:")
for s in students:
    print("Name:", s[0], "| Age:", s[1], "| Course:", s[2])

# Tuple methods
nums = (1, 2, 3, 2, 4, 2)
print("\nCount of 2:", nums.count(2))
print("Index of 3:", nums.index(3))

# Slicing
print("\nSliced tuple:", nums[1:4])

# Convert tuple to list (modify workaround)
temp = list(nums)
temp.append(10)
nums = tuple(temp)

print("\nUpdated tuple:", nums)

# Tuple inside dictionary
data = {
    "point": (5, 10),
    "range": (1, 100)
}

print("\nTuple in dict:", data)

# sets creation
s = {1, 2, 3, 4, 5}
print("\nSet:", s)
# set operations
s.add(6)
print("After adding 6:", s)
s.remove(3)
print("After removing 3:", s)
s.discard(10)  # No error if element not found
print("After discarding 10:", s)
s.clear()
print("After clearing set:", s) 

# dictionary creation
dict = {
    "name": "Lucky",
    "age": 20,
    "course": "ML"
}
print("\nDictionary:", dict)
# dictionary access
print("Name:", dict["name"])
# dictionary update
dict["age"] = 21
print("Updated Dictionary:", dict)
# dictionary keys and values
print("Keys:", dict.keys())
print("Values:", dict.values())
# dictionary loop
print("\nDictionary Loop:")
for key, value in dict.items():
    print(key, ":", value)  
    