


# # print("jai shree ram");






# # # sum of natural number

# # sum = 0;
# # for i in range(5):
# #     sum+=i;
# # print("the sum of first n natural number is : ",sum)





# # i = 1;

# # while i<=10:
# #     print("i am while loop ", i)
# #     i+=1;






# # def CheckValues(a):
# #     if(a==10):
# #         print("yes it is correct the value is : ", a)
# #     else:
# #          print("no it is not correct")




# # CheckValues(10);
  


# # a = 90

# # if(a==10):
# #     print("yes it is correct the value is : ", a)
# # else:
# #     print("no it is not correct")





# # data structure

# ✅ 1. LIST

# Ordered → Items have a fixed position (index).

# Mutable → You can change values (add, remove, update).

# Allows duplicates.

# Syntax: []
# # # list
# user_list = ["Arbind", "Aryan", "Jai", "Bhim"];



# user_list.append("Abhisekh")
# user_list.append("Abhisekh")


# # user_list.sort()
# # user_list.remove("Arbind")


# user_list.reverse()
# for i in user_list:
#     print(i)





#set
# ✅ 3. SET

# Unordered → No index, no fixed position.

# Mutable → You can add/remove items.

# Does NOT allow duplicates.

# Syntax: {} or set()


# user_set =  { "arbind", "jai" , "rama"};

# # user_set.add("ram")
# for i in user_set:
#     print(i)







# ✅ 2. TUPLE

# Ordered → Items have index.

# Immutable → Cannot change after creation.

# Allows duplicates.

# Syntax: () or tuple()
# tuple_example = (1, 2, 3, 4, 5 , 2)



# for i in tuple_example:
#     print(i)





# 4. DICTIONARY (dict)

# Ordered (Python 3.7+ maintains insertion order)

# Mutable → You can add, remove, update key-value pairs.

# Does NOT allow duplicate keys (values can duplicate)

# Stores data in key–value form.

# Syntax: { key: value }

my_dict = {
    "name": "Arbind",
    "age": 22,
    "city": "Kathmandu"
}

print(my_dict["name"])  # Output: Arbind

my_dict["age"] = 23     # Update
my_dict["country"] = "Nepal"  # Add new pair
