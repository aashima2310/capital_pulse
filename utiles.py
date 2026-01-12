def find_max(list1):
    max= list1[0]
    for val in list1:
        if(val>max):
            max=val
    print("The max value is : ",max)