list1 = [10,20,30,40,50]
rev_list = ""
for i in list1:
    rev_list = list1 + " " +str(i) 
    i = i -1
    print(rev_list)
