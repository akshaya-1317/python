
#python list


def function0():
    print("______________")

#empty list demo

def function1():
    list1 = []
    list2 = list()
    print("type of list1 : ", type(list1))
    print("type of list2 : ", type(list2))

function1()
function0()

#list of elements
def function2():
    nums = [11,22,33,44,55]
    print("type of nums : ", type(nums))
    print("nums : ", nums)

    #list is indexable
    print("nums[2] : ", nums[2])
    nums[3] = 40 # Modified/replaced 44 with 40 - list is mutable.
    print("nums = ", nums)

    print("length of nums : ", len(nums))


function2()
function0()

#access elements one by one from list i.e. Traversing
def function3():
     nums = [11,22,33,44,55]
     #use while loop to traverse from o to 4 index.
     i = 0
     while i < len(nums):
         print("nums[i] = ", nums[i])
         i += 1


     #use for loop to traverse
     for n in nums:
         print("list of ele = ", n)

function3()
function0()


# +ve (fwd) index and -ve (rev) indexing

def function4():
    nums = [11,22,33,44,55]
    print("first ele: ", nums[0])
    print("second ele: ", nums[1])
    print("third ele: ", nums[2])
    print("fourth ele: ", nums[3])
    print("last ele: ", nums[4])

    print("last ele: ", nums[-1])
    print("second last ele: ", nums[-2])
    print("third last ele: ", nums[-3])
    print("fourth last ele: ", nums[-4])
    print("fifth last ele: ", nums[-5])

    i= -1
    while i >= -len(nums):
      print("element is rev order: ", nums[i])
      i -= 1

function4()


#Append method
def function5():
    nums = [11,22,33,44,55]
    print("original list: ",nums)

    nums.append(66)
    print("first append: ", nums)

    nums.append(77)
    print("second append: ", nums)


function5()
function0()


#insert method
def function6():
    nums = [11,22,33,44,55]
    print("original nums list: ", nums)

    nums.insert(5,66)
    print("first insert list: ", nums)

    nums.insert(9,77)  #this will insert at last. not error
    print("at 9 index insert list: ", nums)

    nums.insert(-1,88)
    print("first negative insert list: ", nums)

function6()
function0()


#pop generally deletes last element in list but if index is given it deletes at index.

def function7():
    nums = [11,22,33,44,55]
    print("original nums list: ", nums)

    nums.pop()
    print("after pop: ", nums)

function7()
function0()


#remove() deletes given element
def function8():
    nums = [11,22,33,44,55]
    print("original nums list is: ", nums)
    x = int(input("enter element to delete: "))
    nums.remove(x)

    #nums.remove(33)   #not index, give element.
    print("after remove: ", nums)

#function8()
function0()


# get count of number - how many times repeated.
def function9():
    nums = [11,22,33,65,47,33,22,96,87,96,57,22]
    print("original list: ", nums)

    x = int(input("Enter number of which you want a count: "))
    cnt = nums.count(x)
    print(x, "repeated", cnt, "times")

#function9()
function0()


#element is present or not
def function10():
    nums = [11,58,69,97,84,51,26,23,47,49,48,64]
    print("original list: ", nums)

    n = int(input("Enter element you want: "))

   # if nums.count(n) > 0:
    #    print("Element is present")
   # else:
    #    print("Element is not present")
    if n in nums:
        print("Element is present")
    else:
        print("Element is not present")

#function10()
function0()


#to delete element
def function11():
    nums = [15,87,98,98,65,26,24,84,87,59,89,26,26]
    print("original nums list: ", nums)

    n = int(input("Enter element to delete: "))
    cnt = nums.count(n)
    i = 1
    while i <= cnt:
        nums.remove(n)
        i += 1
        print("nums = ",nums)

#function11()
function0()


#delete using del operator
def function12():
    nums = [12,54,47,89,98,98,68,25,68,25,58]
    print("nums = ", nums)
  #  idx = 5
  #  del nums[idx]
  #  print("after deleting index",idx)
  #  print("nums = ",nums)

    n = int(input("give index you want to delete: "))
    del nums[n]
    print("after deleting index", n)
    print("new nums: ", nums)


#function12()
function0()


#Append, extend, +=, +
def function13():
    nums1 = [10,20,30,40]
    print("nums1= ",nums1)
    nums1.append([50,60])
    print("after append() nums1= ", nums1)

    nums2 = [10,20,30,40]
    print("nums2= ", nums2)
    nums2.extend([50,60])
    print("after extend() nums2= ", nums2)

    nums3 = [10,20,30,40]
    print("nums3= ", nums3)
    nums3 += [50,60]
    print("after += ", nums3)

    nums4 = [10,20,30,40]
    print("nums4= ", nums4)
    nums5 = nums4 + [50,60]
    print("after +", nums5)
    print("nums4= ", nums4)

function13()
function0()


#reverse list
def function14():
    nums = [10,20,30,40,50]
    print("original list: ", nums)
    nums.reverse()
    print("nums= ",nums)

function14()
function0()


#sort list
def function15():
    nums = [60,40,10,20,30,50]
    nums.sort()
    print("sorted = ", nums)
    nums.sort(reverse=True)
    print("s2= ",nums)

function15()
function0()


def function16():
    def add(x,y):
        print("add: ", x+y)

    def subtract(x,y):
        print("sub: ", x-y)

    def multiply(x,y):
        print(("multiply: ", x*y))

    def divide(x,y):
        print("division: ", x/y)

    list1 =[add, subtract, multiply, divide]
    for ele in list1:
        print("list1 ele ", ele, "of type", type(ele))
        ele(22,7)
        print()

function16()


#LIST SLICING
#   list[start:end] -- start index included and end index is excluded
#       if end is not given, default end = len(list)
#       if start is not given, default start = 0
#   list[start:end:step] -- from start access element stepwise (end excluded)
#       step is optional and default is 1
#start must be less than end

def function17():
    nums = [0,1,2,3,4,5,6,7,8,9]
    print("num of elements: ", len(nums))
    print("nums[2:5]", nums[2:5])
    print("nums[3:9]", nums[3:9])
    print("nums[-4:-8]", nums[-4:-8])
    print("nums[7:]", nums[7:])
    print("nums[:4]", nums[:4])
    print("nums[:]", nums[:])

 # access alternate elements
    print("nums[0:10:2]= ", nums[0:10:2])
    print("nums[1:10:2]= ",nums[1:10:2])

function17()
function0()


# advanced slicing -- can be used to insert, update or delete slice from list
def function18():
    nums1 = [0,1,2,3,4,5,6,7,8,9]

    # update a slice of a list
    print("before update: nums1 =", nums1) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums1[3:6] = [30, 40, 50]
    print(" after update: nums1 =", nums1) # [0, 1, 2, 30, 40, 50, 6, 7, 8, 9]

    # insert a list into another list
    nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("before insert: nums2 =", nums2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums2[3:3] = [11, 22, 33]
    print(" after insert: nums2 =", nums2)  # [0, 1, 2, 11, 22, 33, 3, 4, 5, 6, 7, 8, 9]

    # delete a slice of list
    nums3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("before delete: nums3 =", nums3)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums3[3:6] = []
    print(" after delete: nums3 =", nums3)  # [0, 1, 2, 6, 7, 8, 9]

function18()














