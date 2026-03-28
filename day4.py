# List syntax
list = ["lucky","shnopi","Ayush","Jitendra","shivam","satyarth","shubham","satyam"]
print(list[0:8])
# list append 
list.append("Movies")
print(list)
# list insert 
list.insert(0,"Python")
print(list)
# list remove
list.remove("satyarth")
print(list)
# list pop
list.pop(0)
print(list)
# list sort
list.sort()
print(list)
# list reverse
list.reverse()
print(list)
# basic list loops operations
list = [1,2,3,4,5]
for i in list:
    print(i)
# list sum using for loop
nums = [1,2,3,4,5,6,7]
sum = 0
for n in nums:
    sum += n
    print(sum)