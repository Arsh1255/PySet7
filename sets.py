set1 = []
set2 = []
msg1 = "THIS IS A PYTHON PROGRAM"


def add(cur_set):
    print("=============================================",end = "")
    print(msg1,"==========================================",end = "")
    print("\n \n")
    parameter = int(input("Enter the amount of elements the set has: "    ))
    for i in range(0,parameter):
        result = int(input())
        cur_set.append(result)
    print("\n \n")        
def Operations():
    state = True
    while state == True:
        print(" 1.Union of Sets \n 2.Intersection of Sets \n 3.Get the Complement of set2 \n 4.Get the Complement of set1 \n 5.Get the Union of Sets by deleting Intersecting elements: \n 6.Clear both the sets \n 7.Exit \n")
        choice = int(input(" Please enter your operation number: "))
        if choice == 1:
            print("\n The Union of the two sets entered is {0}\n".format(set1 | set2))
        elif choice == 2:
            print("\n The Intersection of the two sets entered is {0} \n".format(set1 & set2))            
        elif choice == 3:
            print("\n The Complement of the set2 is {0} \n ".format(set1 - set2))            
        elif choice == 4:
            print("\n The Complement of the set1 is {0} \n ".format(set2 - set1))            
        elif choice == 5:
            print("\n The Union of the Sets by deleting the Intersecting elements is {0} \n".format(set1 ^ set2))          
            print("\n")
        elif choice == 7:
            state = False                
        else:
            print("\n Sorry, wrong choice entered ! \n")   
               
                
            
        
add(set1)        
add(set2)
set1 = set(set1)       
set2 = set(set2)
Operations()
            
        

