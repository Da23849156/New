from tkinter import*
root = Tk()

    
l1 =Label(root, text="Monday")
l2 =Label(root, text="Tuesday")
l3=Label(root, text="Wednesday")
l4=Label(root, text="Thursday")
l5=Label(root, text="Saturday")

t1=Label(root, text="16:00-17:00")
t2=Label(root, text="17:00-18:00")
t3=Label(root, text="18:00-19:00")
t4=Label(root, text="19:00-20:00")
t5=Label(root, text="20:00-21:00")
t6=Label(root, text="21:00-22:00")


l1.grid(row=0, column=1)
l2.grid(row=0, column=2)
l3.grid(row=0, column=3)
l4.grid(row=0, column=4)
l5.grid(row=0, column=5)

t1.grid(row=1, column=0)
t2.grid(row=2, column=0)
t3.grid(row=3, column=0)
t4.grid(row=4, column=0)
t5.grid(row=5, column=0)

def click(row, col):
        print(row, col)
        label.configure(text="you clicked row %s column %s" % (row, col))
        buttons[row-1][col-1].config(relief=SUNKEN, state=DISABLED)
            
            
def relief(row, col):
    print(row, col)
    label.configure(text="you relief row %s column %s" % (row, col))
    buttons[row-1][col-1].config(relief=RAISED,state=ACTIVE)

test_text = "select"


buttons = []
for row in range(1,6):
    button_row = []
    for col in range(1,6):
        button = Button(root, text=test_text)
        button.bind("<Button-1>",lambda event,row=row,col=col: click(row,col))
        button.bind("<Double-1>",lambda event,row=row,col=col: relief(row,col))
        button.grid(row=row, column=col, sticky="nsew")
        button_row.append(button)
    buttons.append(button_row)


label = Label(root, text="")
label.grid(row=8, column=1, columnspan=8, sticky="new")

fi=[]
li=[]
def check(row,col):
        global fi,li
        for row in range(1,6):
                print()
                for col in range(1,6):
                        ans=buttons[row-1][col-1]['state']=='disabled'
                        if ans==True :
                                print(1,end=',')
                                li.append(1)
                        else:
                                print(0,end=',')
                                li.append(0)
                fi.append(li)
                li=[]
                        
                             

Final=Button(root,text='Finish',command=lambda row=row,col=col: check(row,col))
Final.grid(row=10,column=3,sticky='nsew')

root.grid_rowconfigure(12, weight=1)
root.grid_columnconfigure(12, weight=1)






root.mainloop()
