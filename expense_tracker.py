expenselist=[]
print("WELCOME TO EXPENSE TRACKER")
while True:
    print("===MENU===")
    print("1.add expense")
    print("2.view expense")
    print("3.total amount")
    print("4.exit")
    choice=int(input("enter the number:"))
    if(choice==1):
        date=input("enter the date:")
        category=input("entrr the category:")
        description=input("enter the description:")
        amount=int(input("enter your amount:"))
        #doubt why we are creating distioary
        expense={
        "date":date,
        "category":category,
        "description":description,
        "amount":amount
        }#keys are there wb value and why we are adding to list only choice 1 wb 2,3 and all
        expenselist.append(expense)
        print("DONE BRO! EXPENSE IS ADDED")
    elif(choice==2):
        print("view the expense")
        count=1
        for item in expenselist:#why for loop
            print(f"item{"count"}--->{item["date"]},{item["category"]},{item["description"]},{item["amount"]}")
            count=count+1
    elif(choice==3):
            total=0
            for item in expenselist:
                total=total+item["amount"]
                print("total amount:",total)
    elif(choice==4):
           print("tq for using expense tracker")
           break
           
             
            
       