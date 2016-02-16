list1=[1,2,3,1,3]
list2=[1,2,3,4,5]
list3=[5,5,5,5,5]
list4=[10,9,10,10,9,8]
main_list=[]

def appendingToMainList(a,b,c,d):
    for x in a,b,c,d:
        for y in range(len(x)):
            if x[y] not in main_list:
                main_list.append(x[y])
    main_list.sort()
    return main_list

print appendingToMainList(list1,list2,list3,list4)
