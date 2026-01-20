# # s = {65,34,76,87,23,65,87}

# # print(type(s))
# # print(s)

# # s = {1,2,1,1,1,1,1,4,5,7,6,8,7,9}
# # print(s)


# s = {10,20,45,65}

# print(s)
# # add - single 
# s.add(100)
# print(s)

# # multiple add 
# s.update([90,80])
# print(s)


# #remove(element)
# s.remove(10)
# print(s)

# #remove the random element
# s.pop()
# print(s)


# #clear
# s.clear()
# print(s)

# union -> join -> all element but jo duplicate honge woh only once

A = {1,2,3,4}
B = {5,6,7,3,45,2,4,2,1}

# print(A | B)
# print(A.union(B))


#intersection - only comman - intersect

print(A.intersection(B))
print(A & B)


#difference -> 
print(B - A)
print(B.difference(A))