import pandas as pd
import matplotlib.pyplot as plt

def ShowStock():
    inv=pd.read_csv("InventoryData.csv")
    l=list(inv["Quantity"])
    l0=list(inv["Item"])
    length=len(l)
    i=0
    while(i<length):
        if l[i]==0:
            l.pop(i)
            l0.pop(i)
            i=i-1
            length=length-1
        i=i+1    
    plt.bar(l0,l,width=0.4,color='lightblue')
    plt.xlabel("Inventory Items")
    plt.ylabel("Quantity")
    plt.title("INVENTORY STOCK")
    print("\n****Displaying Inventory****")
    plt.show()

    
    

def UpdateInv():
    inv=pd.read_csv("InventoryData.csv")
    pur=pd.read_csv("PurchaseData.csv")
    l=list(inv['Item'])
    p=list(inv['Item'])  
    i = input("\nEnter Item to Update: ")
    q = input("Enter Quantity: ")
    q=int(q)
    if i in l:
        pos=l.index(i)
        inv.loc[pos,'Quantity']=inv.at[pos,'Quantity']+q
    else:
        print("enter cost of unit")
        c=int(input())
        pos=len(l)
        inv.loc[pos,'Item']=i
        inv.at[pos,'Quantity']=q  
        pos=len(p)
        pur.loc[pos,'Item']=i
        pur.loc[pos,'Quantity']=0
        pur.loc[pos,'CPU']=c
        pur.loc[pos,'Revenue']=0
    print("****Updating Item****")
    inv.to_csv("InventoryData.csv",index=False)
    pur.to_csv("PurchaseData.csv",index=False)
    print("Inventory is Updated")

def purchaseItem():
    inv=pd.read_csv("InventoryData.csv")
    pur=pd.read_csv("PurchaseData.csv")
    l=list(inv['Item'])
    p=list(pur['Item'])
    print("\n***Items Available***\n")
    print(inv)
    i = input("\nEnter Item to Purchase: ")
    q = input("Enter Quantity: ")
    q=int(q)
    if i in l and q<=inv.at[l.index(i),"Quantity"]:
        pos=l.index(i)
        inv.loc[pos,'Quantity']=inv.at[pos,'Quantity']-q
        pos=p.index(i)
        pur.loc[pos,'Quantity']=pur.at[pos,'Quantity']+q
        pur.loc[pos,'Revenue']=pur.at[pos,'Quantity']*pur.at[pos,'CPU']
        print("Purchasing Item.....")
        inv.to_csv("inventory.csv",index=False)
        pur.to_csv("PurchaseData.csv",index=False)
        print("Item Purchased, Thank You")
    elif inv.at[l.index(i),"Quantity"]==0:
        print("***Item not Available***") 
    else:
        print("***Quantity not Available***")      
   
def ShowRevenue():
    pur=pd.read_csv("PurchaseData.csv")
    l=list(pur["Revenue"])
    l0=list(pur["Item"])
    length=len(l)
    i=0
    while(i<length):
        if l[i]==0:
            l.pop(i)
            l0.pop(i)
            i=i-1
            length=length-1
        i=i+1    
    plt.bar(l0,l,width=0.4,color='cyan')
    plt.xlabel("Items")
    plt.ylabel("Revenue (Rs.)")
    plt.title("REVENUE REPORT")
    print("Displaying Revenue Report....")
    plt.show()

def main():
    print("\n\n********INVENTORY MANAGEMENT SYSTEM********")
    y=1
    while(y==1):
        print("\nChoose Option:\n1.Show Inventory Stock\n2.Show Revenue\n3.Update Inventory\n4.Purchase Item\n5.Exit")    
        i=int(input("\nChoice: "))
        if i==1:
            ShowStock()
        elif i==2:
            ShowRevenue()
        elif i==3:
            UpdateInv()
        elif i==4:
            purchaseItem()
        elif i==5:
            print("****Exiting System****")
            y=0
        else:
            print("Incorrect Option, Enter Again!!!")

if __name__=="__main__":
    main()




