# list = [1,2,3,4,5]
# print(list)


# ###to change the element 
# list =[1,2,3,4,5]
# list[1] = 10   ##list is updated
# print(list)


###inserted method 
list = [1,2,3,4,5,6]
list.insert(3,10)  ##we can't store the insert method in a variable because it can update the list but not return the values 
print(list)


##extened list 
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list1.extend(list2)
print(list1)