from tkinter import *

root = Tk()
root.geometry('500x500')
root.title('Billing Table')
# Functions

def Calculate():
    Cust_name  = Name_1.get()
    Idly_Qty = int(Idly_1.get())*5
    Dosa_Qty = int(Dosa_1.get())*15
    Upma_Qty = int(Upma_1.get())*25
    Spl_Dosa_Qty = int(Spl_Dosa_1.get())*30
    Tea_Qty = int(Tea_1.get())*7
    Cofee_Qty = int(Cofee_1.get())*10
    global Total
    Total=Idly_Qty+Dosa_Qty+Upma_Qty+Spl_Dosa_Qty+Tea_Qty+Cofee_Qty
    print('The Total Bill Amount is :',Total)
    



def Generate_bill():
    Cust_name  = Name_1.get()
    Idly_Qty = int(Idly_1.get())*5
    Dosa_Qty = int(Dosa_1.get())*15
    Upma_Qty = int(Upma_1.get())*25
    Spl_Dosa_Qty = int(Spl_Dosa_1.get())*30
    Tea_Qty = int(Tea_1.get())*7
    Cofee_Qty = int(Cofee_1.get())*10
    print()
    print('The Customer Name is :',Cust_name)
    print('The Idly price is :',Idly_Qty)
    print('The Dosa Price is :',Dosa_Qty)
    print('The Upma Price is :',Upma_Qty)
    print('The Spl_Dosa price is :',Spl_Dosa_Qty)
    print('The Tea Price is :',Tea_Qty)
    print('The Cofee price is :',Cofee_Qty)
    print()
    print('The Total Bill Amount is :',Total)

# Name Label
Head = Label(root,text = "Billing Table",relief = 'solid',width = 25,bg = 'gray',font = ('arial',18,'italic')).place(x = 45,y = 15)
Name = Label(root,text = "Customer Name :",font = ('arial',14,'italic')).place(x = 45,y = 65)
Number_1 = Label(root,text = "1 . Idly ",font = ('arial',12,'italic')).place(x =45, y = 120)
Number_2 = Label(root,text = "2 . Dosa ",font = ('arial',12,'italic')).place(x = 45, y = 160)
Number_3 = Label(root,text = "3 . Upma ",font = ('arial',12,'italic')).place(x = 45,y = 200)
Number_4 = Label(root,text = "4 . Spl Dosa " ,font = ('arial',12,'italic')).place(x = 45, y = 240)
Number_5 = Label(root,text= "5 . Tea ",font = ('arial',12,'italic')).place(x = 45, y = 280)
Number_6 = Label(root,text = "6 . Cofee ",font = ('arial',12,'italic')).place(x = 45,y = 320)


va = StringVar()
Terms = Label(root,text = "Terms and Conditions :",font = ('arial',12,'italic')).place(x = 45,y = 360)
Check  = Checkbutton(root,text = "I agree the terms and conditions",variable = va).place(x = 65, y = 400)
Button_1 = Button(root,text = "Calculate Bill ",padx = 5,pady = 5,font = ('arial',12,'italic'),command = Calculate).place(x = 45,y = 440)
Bill = Button(root,text = "Generate Bill",padx = 5,pady = 5,font = ('arial',12,'italic'),command = Generate_bill).place(x = 220,y = 440)

New = StringVar()
# Entry Label
Name_1 = Entry(root,textvar = New,width = 25,borderwidth = 5)
Name_1.place(x = 220,y = 70)

Idly_1 = Entry(root,width = 5)
Idly_1.place(x = 180,y = 120)

Dosa_1 = Entry(root,width = 5)
Dosa_1.place(x = 180,y = 160)

Upma_1 = Entry(root,width = 5)
Upma_1.place(x = 180,y = 200)


Spl_Dosa_1 = Entry(root,width = 5)
Spl_Dosa_1.place(x = 180,y = 240)

Tea_1 = Entry(root,width = 5)
Tea_1.place(x = 180,y = 280)

Cofee_1 = Entry(root,width = 5)
Cofee_1.place(x = 180,y = 320)

#Price
Idly_2 = Label(root,text = "Each Idly Rs = 5/-",font= ('arial',10,'italic')).place(x = 250,y = 120)
Dosa_2 = Label(root,text = "Each Dosa Rs = 15/-",font= ('arial',10,'italic')).place(x = 250,y = 160)
Upma_2 = Label(root,text = "One upma Rs = 25/-",font= ('arial',10,'italic')).place(x = 250,y = 200)
Spl_Dosa_2 = Label(root,text = "Each SPl Dosa Rs = 30/-",font= ('arial',10,'italic')).place(x = 250,y = 240)
Tea_2 = Label(root,text = "Each Tea Rs = 7/-",font= ('arial',10,'italic')).place(x = 250,y = 280)
Cofee_2 = Label(root,text = "Each Cofee Rs = 10/-",font= ('arial',10,'italic')).place(x = 250,y = 320)



root.mainloop()
