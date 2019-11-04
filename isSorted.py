def isSorted(list1):
    list2 = list1
    list2.sort()
    print(list1)
    print(list2)
    if(list1 == list2):
        return True
    else:
        return False
    
