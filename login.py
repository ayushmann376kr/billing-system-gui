from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox
import sys 

def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()
    
class LoginPage:
    def __init__(self,win):
        self.win = win 
        self.win.geometry("1370x750+0+0")
        self.win.title("Billing System")
        
        self.title_label = Label(self.win,text="Billing System", font=('Arial',35,'bold'),bg="lightblue",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        
        self.main_frame = Frame(self.win,bg="lightgrey",bd=6,relief=GROOVE)
        self.main_frame.place(x=250,y=150,width=800,height=400)
        
        self.login_lbl = Label(self.main_frame,text="Login",bd=5,relief=GROOVE,anchor=CENTER,bg="lightblue",font=('sans-serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)
        
        self.entry_frame = LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg="lightgrey",font=('sans-serif',25))
        self.entry_frame.pack(fill=BOTH,expand=True)
        
        self.entus_lbl = Label(self.entry_frame,text="Enter Username:",bg="lightgrey",font=('sans-serif',15))
        self.entus_lbl.grid(row=0,column=0,padx=2,pady=2)
        
        #================variables=================
        
        username = StringVar()
        password = StringVar()
        
        
        #==========================================    
        self.entus_ent = Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)
        
        self.entpass_lbl = Label(self.entry_frame,text="Enter Password:",bg="lightgrey",font=('sans-serif',15),)
        self.entpass_lbl.grid(row=1,column=0,padx=2,pady=2)
        
        self.enpass_ent = Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=password,show="*")
        self.enpass_ent.grid(row=1,column=1,padx=2,pady=2)
        
        #===========Functions===============
        '''this will check login'''
        def check_login():
            if username.get() == "ayushmann" and password.get() == "N12nikhil376":    #username, pass
                self.billing_btn.config(state="normal")
            else:
                pass #------> message box
            
        def reset():
            username.set("")
            password.set("")
            
        
            
        def billing_sect():
            self.newWindow = Toplevel(self.win)
            self.app = window2(self.newWindow)
        
        #===================================
        
        #===========Buttons=================
        
        self.button_frame = LabelFrame(self.entry_frame,text="Options",font=('Arial',15),bg="lightgrey",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=80)
        
        self.login_btn = Button(self.button_frame,text="Login",font=('Arial',15),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)
        
        self.billing_btn = Button(self.button_frame,text="Billing",font=('Arial',15),bd=5,width=15,command=billing_sect)
        self.billing_btn.grid(row=0,column=1,padx=20,pady=2)
        self.billing_btn.config(state="disabled")
        
        self.reset_btn = Button(self.button_frame,text="Reset",font=('Arial',15),bd=5,width=15,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)
        
        #===================================
        
class window2:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1370x750+0+0")
        self.win.title("Billing System")
        
        self.title_label = Label(self.win,text="Billing System", font=('Arial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        
        self.win.resizable(0,0)
        
        #=============variables============
        
        bill_no= random.randint(100,9999)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)
        
        calc_var = StringVar()
        
        cust_nm = StringVar()
        cust_con = StringVar()
        date = StringVar()
        item_pur = StringVar()
        item_qan = StringVar()
        cost = StringVar()
        
        date.set(datetime.now())
        
        #==================================
        
        #=============Entry================
        
        self.entry_frame = LabelFrame(self.win,text="Enter Details ",background="lightgrey",font=("arial",20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=500,height=650)
        
        self.bill_no_lbl = Label(self.entry_frame,text= "Bill Number: ",font=('arial',15),bg= "lightgrey")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)
        
        self.bill_no_ent = Entry(self.entry_frame,bd=5,font=('arial',15),textvariable=bill_no_tk) #check this part
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        
        self.cust_nm_lbl = Label(self.entry_frame,text= "Customer Name: ",font=('arial',15),bg= "lightgrey")
        self.cust_nm_lbl.grid(row=1,column=0,padx=2,pady=2)
        
        self.cust_nm_ent = Entry(self.entry_frame,bd=5,textvariable=cust_nm,font=('arial',15))
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)
        
        self.cust_con_lbl = Label(self.entry_frame,text= "Customer Contact: ",font=('arial',15),bg= "lightgrey")
        self.cust_con_lbl.grid(row=2,column=0,padx=2,pady=2)
        
        self.cust_con_ent = Entry(self.entry_frame,bd=5,textvariable=cust_con,font=('arial',15))
        self.cust_con_ent.grid(row=2,column=1,padx=2,pady=2)
        
        self.date_lbl = Label(self.entry_frame,text= "Date: ",font=('arial',15),bg= "lightgrey")
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2)
        
        self.date_ent = Entry(self.entry_frame,bd=5,textvariable=date,font=('arial',15))
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)
        
        self.item_pur_lbl = Label(self.entry_frame,text= "Item Purchased: ",font=('arial',15),bg= "lightgrey")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)
        
        self.item_pur_ent = Entry(self.entry_frame,bd=5,textvariable=item_pur,font=('arial',15))
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)
        
        self.item_qan_lbl = Label(self.entry_frame,text= "Item Quantity",font=('arial',15),bg= "lightgrey")
        self.item_qan_lbl.grid(row=5,column=0,padx=2,pady=2)
        
        self.item_qan_ent = Entry(self.entry_frame,bd=5,textvariable=item_qan,font=('arial',15))
        self.item_qan_ent.grid(row=5,column=1,padx=2,pady=2)
        
        self.cost_lbl = Label(self.entry_frame,text= "Cost of One",font=('arial',15),bg= "lightgrey")
        self.cost_lbl.grid(row=6,column=0,padx=2,pady=2)
        
        self.cost_ent = Entry(self.entry_frame,bd=5,textvariable=None,font=('arial',15))
        self.cost_ent.grid(row=6,column=1,padx=2,pady=2)
        
        #============functions======================
        
        total_list = []
        self.grd_total = 0
        def default_bill():
            self.bill_txt.insert(END,"\t\t\t\t Monginis Cafe")
            self.bill_txt.insert(END,"\n\t\t\t 7 street, Near Railway Lines, Dadar")
            self.bill_txt.insert(END,"\n\t\t\t\t +91 7658902311")
            self.bill_txt.insert(END,"\n=====================================================================================")
            self.bill_txt.insert(END,f"\nBill Number: {bill_no_tk.get()}")
            
        def genbill():
            self.bill_txt.insert(END,f"\nCustomer Name : {cust_nm.get()}")
            self.bill_txt.insert(END,f"\nCustomer Contact : {cust_con.get()}")
            self.bill_txt.insert(END,f"\nDate : {date.get()}")
            self.bill_txt.insert(END,"\n=====================================================================================")
            self.bill_txt.insert(END,"   Item           Quantity \t\t           Per Cost \t\t             Total")
            self.bill_txt.insert(END,"\n=====================================================================================")
            
            self.add_btn.config(state="normal")
            self.total_btn.config(state="normal")
            self.save_btn.config(state="normal")
            
        
        
        def clear_func():
            cust_con.set("")
            cust_nm.set("")
            item_pur.set("")
            item_qan.set("")
            cost.set("")
        
        def reset_func():
            total_list.clear()
            self.grd_total = 0
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
            self.bill_txt.delete("1.0",END)
            default_bill()
            
        def add_func():
            qty = int(item_qan.get())
            costs = int(cost.get())
            total = qty * costs
            self.bill_txt.insert(END,f"\n{item_pur.get()}\t\t    {item_qan.get()}\t\t            Rs. {cost.get()}\t\t           Rs. {total}")
            
        def total_func():
            for item in total_list:
                self.grd_total = self.grd_total +item  
            self.bill_txt.insert(END,"\n=====================================================================================")
            self.bill_txt.insert(END,"\t\t\t\t\tGrand Total : {self.grd_total}") 
            self.bill_txt.insert(END,"\n=====================================================================================")
            
        def save_func():
            user_choice = messagebox.askyesno("confirm",f"Do You Want To Save the Bill {bill_no_tk.get()}",parent = self.win)
            if user_choice > 0:
                self.bill_content = self.bill_txt.get("1.0",END)
                try:
                    con = open(f"{sys.path[0]}/bills/"+str(self.bill_no_tk.get())+".txt","w")
                except Exception as e:
                    messagebox.showerror("Error!",f"Error due to {e}")
                    con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Success!",f"Bill {bill_no_tk.get()} has been saved successfully",parent= self.win)
            else:
                return
            
            
        #==========================================

    #===============button=====================
    
        self.button_frame =LabelFrame(self.entry_frame,bd=5,text="Options",bg="lightgrey",font=('arial',15))
        self.button_frame.place(x=20,y=280,width=395,height=300)
        
        self.add_btn = Button(self.button_frame,bd=2,text="Add",font=('arial',12),width=12,height=3,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=2,pady=2)
        
        self.generate_btn = Button(self.button_frame,bd=2,text="Generate",font=('arial',12),width=12,height=3,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=2,pady=2)
        
        self.clear_btn = Button(self.button_frame,bd=2,text="Clear",font=('arial',12),width=12,height=3,command=clear_func)
        self.clear_btn.grid(row=0,column=2,padx=2,pady=2)
        
        self.total_btn = Button(self.button_frame,bd=2,text="Total",font=('arial',12),width=12,height=3,command=total_func)
        self.total_btn.grid(row=1,column=0,padx=2,pady=2)
        
        self.save_btn = Button(self.button_frame,bd=2,text="Save",font=('arial',12),width=12,height=3,command=save_func)
        self.save_btn.grid(row=1,column=1,padx=2,pady=2)
        
        self.reset_btn = Button(self.button_frame,bd=2,text="Reset",font=('arial',12),width=12,height=3,command=reset_func)
        self.reset_btn.grid(row=1,column=2,padx=2,pady=2)
        
        
        
        
        #==================================================
        
        
        #===================calculator=====================
        
        self.calc_frame = Frame(self.win,bd=8,background="lightgrey",relief=GROOVE)
        self.calc_frame.place(x=570,y=95,width=730,height=295)
        
        self.num_ent = Entry(self.calc_frame,bd=15,background="lightgrey",textvariable=calc_var,font=('arial',15),width=64,justify='right')
        self.num_ent.grid(row=0,column=0,columnspan=7)
         
        def press_btn(event):
            text = event.widget.cget("text")
            if text == "=":
                if calc_var.get().isdigit():
                    value= int(calc_var.get())
                else:
                    try:
                        value= eval(self.num_ent.get())
                    except:
                        print("Error")
                calc_var.set(value)
                self.num_ent.update()
            elif text == "C":
                pass
            else:
                calc_var.set(calc_var.get() + text)
                self.num_ent.update()
            
            
        
            
        self.but1 = Button(self.calc_frame,bg="lightgrey",text="7",bd=8,width=13,height=1,font=('arial',15))
        self.but1.grid(row=1,column=0,padx=1,pady=2)
        self.but1.bind("<Button-1>",press_btn)
        
        self.but2 = Button(self.calc_frame,bg="lightgrey",text="8",bd=8,width=13,height=1,font=('arial',15))
        self.but2.grid(row=1,column=1,padx=1,pady=2)
        self.but2.bind("<Button-1>",press_btn)
       
        self.but3 = Button(self.calc_frame,bg="lightgrey",text="9",bd=8,width=13,height=1,font=('arial',15))
        self.but3.grid(row=1,column=2,padx=1,pady=2)
        self.but3.bind("<Button-1>",press_btn)
        
        self.but4 = Button(self.calc_frame,bg="lightgrey",text="/",bd=8,width=13,height=1,font=('arial',15))
        self.but4.grid(row=1,column=3,padx=1,pady=2)
        self.but4.bind("<Button-1>",press_btn)
          
        self.but5 = Button(self.calc_frame,bg="lightgrey",text="4",bd=8,width=13,height=1,font=('arial',15))
        self.but5.grid(row=2,column=0,padx=1,pady=2)
        self.but5.bind("<Button-1>",press_btn)
        
        self.but6 = Button(self.calc_frame,bg="lightgrey",text="5",bd=8,width=13,height=1,font=('arial',15))
        self.but6.grid(row=2,column=1,padx=1,pady=2)
        self.but6.bind("<Button-1>",press_btn)
    
        self.but7 = Button(self.calc_frame,bg="lightgrey",text="6",bd=8,width=13,height=1,font=('arial',15))
        self.but7.grid(row=2,column=2,padx=1,pady=2)
        self.but7.bind("<Button-1>",press_btn)
        
        self.but8 = Button(self.calc_frame,bg="lightgrey",text="*",bd=8,width=13,height=1,font=('arial',15))
        self.but8.grid(row=2,column=3,padx=1,pady=2)
        self.but8.bind("<Button-1>",press_btn)
        
        self.but9 = Button(self.calc_frame,bg="lightgrey",text="1",bd=8,width=13,height=1,font=('arial',15))
        self.but9.grid(row=3,column=0,padx=1,pady=2)
        self.but9.bind("<Button-1>",press_btn)
        
        self.but10 = Button(self.calc_frame,bg="lightgrey",text="2",bd=8,width=13,height=1,font=('arial',15))
        self.but10.grid(row=3,column=1,padx=1,pady=2)
        self.but10.bind("<Button-1>",press_btn)
       
        self.but11 = Button(self.calc_frame,bg="lightgrey",text="3",bd=8,width=13,height=1,font=('arial',15))
        self.but11.grid(row=3,column=2,padx=1,pady=2)
        self.but11.bind("<Button-1>",press_btn)
        
        self.but12 = Button(self.calc_frame,bg="lightgrey",text="-",bd=8,width=13,height=1,font=('arial',15))
        self.but12.grid(row=3,column=3,padx=1,pady=2)
        self.but12.bind("<Button-1>",press_btn)
        
        self.but13 = Button(self.calc_frame,bg="lightgrey",text="0",bd=8,width=13,height=1,font=('arial',15))
        self.but13.grid(row=4,column=0,padx=1,pady=2)
        self.but13.bind("<Button-1>",press_btn)
        
        self.but14 = Button(self.calc_frame,bg="lightgrey",text=".",bd=8,width=13,height=1,font=('arial',15))
        self.but14.grid(row=4,column=1,padx=1,pady=2)
        self.but14.bind("<Button-1>",press_btn)
       
        self.but15 = Button(self.calc_frame,bg="lightgrey",text="=",bd=8,width=13,height=1,font=('arial',15))
        self.but15.grid(row=4,column=2,padx=1,pady=2)
        self.but15.bind("<Button-1>",press_btn)
        
        self.but16 = Button(self.calc_frame,bg="lightgrey",text="+",bd=8,width=13,height=1,font=('arial',15))
        self.but16.grid(row=4,column=3,padx=1,pady=2)
        self.but16.bind("<Button-1>",press_btn)
   
        #==================================================

    #=================bill frame========================
    
        self.bill_frame = LabelFrame(self.win,text="Bill Area ", font=("Arial",18),background="lightgrey",bd=8,relief=GROOVE)
        self.bill_frame.place(x=585,y=420,width=720,height=320)
                
        self.y_scroll = Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt = Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side="right",fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=TRUE)
        
        default_bill()
    
    #===================================================

if __name__ == "__main__":
    
    main()
    