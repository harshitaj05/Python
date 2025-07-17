# i= 1
# while i<= 6:
#     print("Loops" , i)
#     i += 1
# print(i)

# A= 1
# while A <=100 :
#     print(A)
#     A += 1

# print("Loop Ended")

# B = 100
# while B>=1:
#     print(B)
#     B -=1

# print("Loop Ended")


# n= 3
# while n/3 <= 10:
#     print(n)
#     n += 3

# m =1 
# no = int(input("Enternumber"))
# while m<=10:
#     print(no * m)
#     m +=1 


# z = 1
# while z<= 10:
#     print( z**2)
#     z += 1

# list = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx<= len(list)-1:
#     print(list[idx])
#     idx +=1 



# tup  = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x= 36

# i = 0
# while i < len(tup):
#     if(tup[i] == x):
#         print("Found at index", i)
#         break 
#     else:
#         print("Finding...")
# i += 1

# print("End") 

# i=1
# while i<= 10:
#     if(i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i+=1 

# A= "apnacollegelearning"
# for sow in A:
#     if( sow == "o"):
#         print("o found")
#         break
#     print(sow)
# else:
#     print("end")

# list = [ 1,4,9,16,25,36,49,64,81,100]
# for el in list:
#     if(el == 49):
#         print(el, "7square found")
#         break
#     print(el)
# else:
#     print("Searching", el)

seq = range(10)

for el in seq:
    print(el)

    #or

for el in range(1,9):
    print(el)

for el in range(0,15,2):
    print(el)
