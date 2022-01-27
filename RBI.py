from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import datetime
import os

def main():
    win = Tk()
    app = Window1(win)
    win.mainloop()

class Window1:
    def __init__(self,win):
        self.win = win
        self.win.title("Restraunt Billing System")
        self.win.geometry("1350x700+0+0")

        # self.title_frame = Frame(self.win,border=4,relief=GROOVE,background="lightgrey")
        self.title_label = ttk.Label(self.win,text="Restraunt Billing System",font=('sans-serif',40,'bold'),anchor=CENTER,background="lightgrey",border=4,relief=GROOVE)
        # self.title_label.grid(row=0,column=0,padx=4,pady=2)     
        self.title_label.pack(side=TOP,fill=X)   
        self.title_label.config(anchor=CENTER)             
        # self.title_frame.pack(side=TOP,fill=X)

        self.main_frame = Frame(self.win,border=5,relief=GROOVE,background="lightgrey")
        self.main_frame.place(x=120,y=120,width=1000,height=500)

        # self.lgl_fr = Frame(self.main_frame,border=5,relief=GROOVE,background="lightgrey")
        # self.lgl_fr.pack(side=TOP,fill=X)

        self.login_lbl = ttk.Label(self.main_frame,text="Login",anchor=CENTER,border=7,relief=GROOVE,font=('sans-serif',30,'bold'),background="lightgrey")
        # self.login_lbl.grid(row=0,column=0,padx=2,pady=2)
        self.login_lbl.pack(side=TOP, fill=X)

        self.button_frame = Frame(self.main_frame,border=5,relief=GROOVE,background="lightgrey")
        self.button_frame.pack(fill=BOTH,expand=True)

        self.username_lbl = Label(self.button_frame,font=('sans-serif',20,'bold'),text="Enter username: ",background="lightgrey")
        self.username_lbl.grid(row=0,column=0,padx=2,pady=2)

        #======================================================#
        #                Text Variables                        #

        username = StringVar()
        password = StringVar()

        #======================================================#

        def check_login():
            # if username.get() == "shashank" and password.get() == "vishu@200427":
            if username.get() == "@Eleen" and password.get() == "12345":
                self.billing_button.config(state='normal')
            elif username.get() == "" and password.get() == "":
                messagebox.showinfo("Nothing entered","Please enter the fields.")
            else:
                self.billing_button.config(state="disabled")
                reset_func()
                messagebox.showerror("Invalid Login","Please enter valid credentials.")

        def reset_func():
            username.set("")
            password.set("")
            self.billing_button.config(state="disabled")

        self.username_enter = Entry(self.button_frame,width=25,font=('sans-serif',14),textvariable=username,border=5,relief=GROOVE)
        self.username_enter.grid(row=0,column=1,padx=2,pady=2)

        self.password_lbl = Label(self.button_frame,font=('sans-serif',20,'bold'),text="Enter password: ",background="lightgrey")
        self.password_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.password_enter = Entry(self.button_frame,width=25,font=('sans-serif',14),textvariable=password,border=5,relief=GROOVE)
        self.password_enter.grid(row=1,column=1,padx=2,pady=2)

        self.inside_frame = Frame(self.button_frame,border=5,relief=GROOVE,background="lightgrey")
        self.inside_frame.place(x=50,y=100,width=785,height=110)

        self.submit_button = Button(self.inside_frame,background="lightgrey",text="Submit",font=('sans-serif',15,'bold'),width=20,height=3,command=check_login)
        self.submit_button.grid(row=0,column=0,padx=4,pady=4)

        def open_billing():
            self.newWindow = Toplevel(self.win)
            self.app = Window2(self.newWindow)

        self.billing_button = Button(self.inside_frame,background="lightgrey",text="Billing",font=('sans-serif',15,'bold'),width=20,height=3,command=open_billing)
        self.billing_button.grid(row=0,column=1,padx=4,pady=4)
        self.billing_button.config(state="disabled")

        self.reset_button = Button(self.inside_frame, text="Reset",background="lightgrey",font=('sans-serif',15,'bold'),width=20,height=3,command=reset_func)
        self.reset_button.grid(row=0,column=2,padx=4,pady=4)



class Window2:
    def __init__(self,win):
        self.win = win
        self.win.title("Billing")
        self.win.geometry("1350x700+0+0")

        #=============== Variables ===================

        bill_no = IntVar()
        cust_nm = StringVar()
        cust_cot = StringVar()
        date = StringVar()
        items_pur = StringVar()
        item_qty = IntVar()
        cost_one = IntVar()
        calc_var = StringVar()

        # self.operator = ""
        op_tk = StringVar()

        bill_no_gen = random.randint(1000,9999)
        bill_no.set(bill_no_gen)

        date_gen = datetime.datetime.now()
        # date_gen.strftime(fmt="%D-%m-%Y")
        date.set(date_gen)

        #=============================================

        # self.title_frame = Frame(self.win,border=4,relief=GROOVE,background="lightgrey")
        self.title_label = ttk.Label(self.win,text="Restaurant Billing System",font=('sans-serif',40,'bold'),border=4,relief=GROOVE,anchor=CENTER,background="lightgrey")
        # self.title_label.grid(row=0,column=0,padx=4,pady=2)     
        self.title_label.pack(side=TOP, fill=X)   
        self.title_label.config(anchor=CENTER)             
        # self.title_frame.pack(side=TOP,fill=X)

        self.entry_frame = Frame(self.win,border=5,relief=GROOVE,background="lightgrey")
        self.entry_frame.place(x=15,y=90,width=500,height=600)

        self.mlbl1_frame = Frame(self.entry_frame,border=4,relief=GROOVE,background="lightgrey")
        # self.mlbl1_frame.grid(row=0,column=0,pady=2)
        # self.mlbl1_frame.place(x=12,y=5,width=470)
        self.mlbl1_frame.pack(fill=X,side=TOP)

        self.mlbl1 = Label(self.mlbl1_frame,background="lightgrey",text="Enter Details",anchor=CENTER,font=('sans-serif',20,'bold'))
        self.mlbl1.pack(fill=X,side=TOP)

        self.prime_frame = Frame(self.entry_frame,border=4,relief=GROOVE,background="lightgrey")
        self.prime_frame.pack(fill=BOTH,expand=True)

        self.bill_no_lb = Label(self.prime_frame,text="Bill Number :",font=('sans-serif',17,'bold'),background="lightgrey")
        self.bill_no_lb.grid(row=0,column=0,padx=2,pady=2)

        self.bill_no_ent = Entry(self.prime_frame,font=('sans-serif',16),border=3,relief=GROOVE,textvariable=bill_no,state=DISABLED)
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        # self.bill_no_ent.config(state=DISABLED, background="lightgrey")

        self.cust_nm_lb = Label(self.prime_frame,text="Customer name :",font=('sans-serif',17,'bold'),background="lightgrey")
        self.cust_nm_lb.grid(row=1,column=0,padx=2,pady=2)

        self.cust_nm_ent = Entry(self.prime_frame,font=('sans-serif',16),border=3,relief=GROOVE,textvariable=cust_nm)
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)

        self.cust_cot_lb = Label(self.prime_frame,text="Customer contact :",font=('sans-serif',17,'bold'),background="lightgrey")
        self.cust_cot_lb.grid(row=2,column=0,padx=2,pady=2)

        self.cust_cot_ent = Entry(self.prime_frame,font=('sans-serif',16),border=3,relief=GROOVE,textvariable=cust_cot)
        self.cust_cot_ent.grid(row=2,column=1,padx=2,pady=2)

        self.date_lb = Label(self.prime_frame,text="Date :",font=('sans-serif',17,'bold'),background="lightgrey")
        self.date_lb.grid(row=3,column=0,padx=2,pady=2)

        self.date_ent = Entry(self.prime_frame,font=('sans-serif',16),border=3,relief=GROOVE,textvariable=date,state=DISABLED)
        self.date_ent.grid(row=3,column=1,padx=2)

        self.items_pur_lb = Label(self.prime_frame,text="Items purchased :",font=('sans-serif',17,'bold'),background="lightgrey")
        self.items_pur_lb.grid(row=4,column=0,padx=2,pady=2)

        self.items_pur_ent = Entry(self.prime_frame,font=('sans-serif',16),border=3,relief=GROOVE,textvariable=items_pur)
        self.items_pur_ent.grid(row=4,column=1,padx=2,pady=2)

        self.items_qty_lb = Label(self.prime_frame,text="Item quantity :",font=('sans-serif',17,'bold'),background="lightgrey")
        self.items_qty_lb.grid(row=5,column=0,padx=2,pady=2)

        self.items_qty_ent = Entry(self.prime_frame,font=('sans-serif',16),border=3,relief=GROOVE,textvariable=item_qty)
        self.items_qty_ent.grid(row=5,column=1,padx=2,pady=2)

        self.items_cost_lb = Label(self.prime_frame,text="Cost of one :",font=('sans-serif',17,'bold'),background="lightgrey")
        self.items_cost_lb.grid(row=6,column=0,padx=2,pady=2)

        self.items_cost_ent = Entry(self.prime_frame,font=('sans-serif',16),border=3,relief=GROOVE,textvariable=cost_one)
        self.items_cost_ent.grid(row=6,column=1,padx=2,pady=2)

        #====================== functions ======================

        def clear_ent():
            messagebox.showinfo("Success","Entries cleared successfully!")
            cust_nm.set("")
            cust_cot.set("")
            items_pur.set("")
            item_qty.set("")
            cost_one.set("")


        #=======================================================

        #================== Calculator ===================

        # self.operator = ""

        self.calc_frame = Frame(self.win,border=4,background="lightgrey")
        self.calc_frame.place(x=560,y=90,width=620,height=280)

        self.txtDisplay = Entry(self.calc_frame,font=('sans-serif',16),textvariable=calc_var,bd=20,bg="lightgrey",insertwidth=4,justify='right',width=47)
        self.txtDisplay.grid(row=0,column=0,padx=2,columnspan=4)

        def click(event):
            text = event.widget.cget("text")
            if text == "=":
                if calc_var.get().isdigit():
                    value = int(calc_var.get())
                else:
                    try:
                        value = eval(self.txtDisplay.get())          
                    except:             
                        messagebox.showerror("Error","Only digits are allowed.")
                calc_var.set(value)    
                self.txtDisplay.update()
            elif text == "C":
                pass
            else:
                calc_var.set(calc_var.get() + text)
                txtDisplay.update()

        self.btn7 = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="7",bg="lightgrey",width=11)
        self.btn7.grid(row=2,column=0)
        self.btn7.bind('<Button-1>',click)

        self.btn8 = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="8",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btn8.grid(row=2,column=1)
        self.btn8.bind('<Button-1>',click)

        self.btn9 = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="9",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btn9.grid(row=2,column=2)
        self.btn9.bind('<Button-1>',click)

        self.btnAdd = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="+",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btnAdd.grid(row=2,column=3)
        self.btnAdd.bind('<Button-1>',click)

        self.btn4 = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="4",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btn4.grid(row=3,column=0)
        self.btn4.bind('<Button-1>',click)

        self.btn5 = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="5",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btn5.grid(row=3,column=1)
        self.btn5.bind('<Button-1>',click)

        self.btn6 = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="6",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btn6.grid(row=3,column=2)
        self.btn6.bind('<Button-1>',click)

        self.btnSubs = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="-",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btnSubs.grid(row=3,column=3)
        self.btnSubs.bind('<Button-1>',click)

        self.btn1 = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="1",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btn1.grid(row=4,column=0)
        self.btn1.bind('<Button-1>',click)

        self.btn2 = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="2",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btn2.grid(row=4,column=1)
        self.btn2.bind('<Button-1>',click)

        self.btn3 = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="3",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btn3.grid(row=4,column=2)
        self.btn3.bind('<Button-1>',click)

        self.btnMult = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="*",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btnMult.grid(row=4,column=3)
        self.btnMult.bind('<Button-1>',click)

        self.btn0 = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="0",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btn0.grid(row=5,column=0)
        self.btn0.bind('<Button-1>',click)

        self.btnDot = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text=".",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btnDot.grid(row=5,column=1)
        self.btnDot.bind('<Button-1>',click)

        self.btnDiv = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="/",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btnDiv.grid(row=5,column=2)
        self.btnDiv.bind('<Button-1>',click)

        self.btnEq = Button(self.calc_frame,padx=2,pady=2,bd=8,font=('sans-serif',14),text="=",bg="lightgrey",command =lambda: btnClick(7),width=11)
        self.btnEq.grid(row=5,column=3)
        self.btnEq.bind('<Button-1>',click)

        #=================================================

        #================== Bill ===========================

        self.bill1fr = Frame(self.win,border=4,background="lightgrey")
        # self.bill1fr.place(x=560,y=90,width=620,height=600)
        self.bill1fr.place(x=560,y=380,width=620,height=300)

        self.bill_lbl = Label(self.bill1fr,text="Bill Area",font=('sans-serif',20,'bold'),background="lightgrey",border=4,relief=GROOVE,anchor=CENTER)
        self.bill_lbl.pack(fill=X,side=TOP)

        self.scroll_y = Scrollbar(self.bill1fr,orient=VERTICAL)

        self.bill_txt = Text(self.bill1fr, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=True)

        self.scroll_y.config(command=self.bill_txt.yview)

        def default_bill():
            self.bill_txt.insert(END,"\t\t\t\tRestraunt Name ELEEN's CAFE")
            self.bill_txt.insert(END,"\n\t\t\tAYODHYA street, near ghat, Faizabad")
            self.bill_txt.insert(END,"\n\t\t\t\tContact: +91954545456")
            self.bill_txt.insert(END,"\n=========================================================================")
            self.bill_txt.insert(END,"\nBill number : {}".format(bill_no.get()))
            
        #===== Generate bill function has been moved =====#
        

        totlist = []

        def addbill():
            if item_qty.get() == "" or items_pur.get() == "" or cost_one == "":
                messagebox.showerror("Error!","Please enter all the fields.")
            itemqt = item_qty.get()
            itemqt = int(itemqt)
            itemcost = cost_one.get()
            itemcost = int(itemcost)
            total_calc = itemqt * itemcost
            totlist.append(total_calc)
            # self.bill_txt.insert(END,"\n{}\t\t\t\t{}\t\t\t\tRs. {}".format(items_pur.get(),item_qty.get(),itemcost))
            self.bill_txt.insert(END,"\n{}\t\t\tRs.{}\t\t  {}\t\t  Rs.{}".format(items_pur.get(),itemcost,item_qty.get(),total_calc))

        def totalgen():
            totalget = 0
            for item in totlist:
                totalget = totalget + item
            
            self.bill_txt.insert(END,"\n=========================================================================")
            self.bill_txt.insert(END,"\t\t\t\t\t\tTotal : Rs. {} (inc. GST)".format(totalget))
            gst_price = 18/100*totalget
            self.bill_txt.insert(END,"\n\t\t\t\t\tGST : 18%"+" of Rs. {} = {}".format(totalget,gst_price))
            grand_total = totalget + gst_price
            self.bill_txt.insert(END,"\n\t\t\t\t\tGrand Total: Rs. {}".format(grand_total))
            self.bill_txt.insert(END,"\n=========================================================================")

        def save_bill():
            self.bill_data = self.bill_txt.get('1.0',END)
            curd = os.curdir
            # f1 = open("F:\\Programming here\\Python\\Tkinter here\\Restraunt Management System\\bills\\"+str(bill_no.get())+".txt","w")
            f1 = open("D:\\Python learn proj2\\Restraunt Management System\\bills\\"+str(bill_no.get())+".txt","w")
            # f1 = open("bills/"+str(bill_no.get())+".txt","w")
            # f1 = open("bills\\"+str(bill_no.get())+".txt","w")
            try:
                f1.write(self.bill_data)
                messagebox.showinfo("Success!","Bill saved successfully!")
            except:
                messagebox.showerror("Error","Bill unable to save")
            f1.close()

        def genbill():
            if cust_nm.get() == "" or cust_cot.get() == "":
                messagebox.showerror("Error!","Please enter all the fields")
            elif len(cust_cot.get()) > 10 or len(cust_cot.get()) < 10:
                messagebox.showerror("Error!","Contact number must be of 10 digits")
                cust_cot.set("")
            else:
                self.bill_txt.insert(END,"\nCustomer Name : {}".format(cust_nm.get()))
                self.bill_txt.insert(END,"\nCustomer contact : {}".format(cust_cot.get()))
                self.bill_txt.insert(END,"\nDate : {}".format(date.get()))
                self.bill_txt.insert(END,"\n=========================================================================")
                self.bill_txt.insert(END,"\nItem Name\t\t\tper unit\t\t  Quantity\t\t  Total")
                self.bill_txt.insert(END,"\n=========================================================================")
                self.add_btn.config(state="normal")
                self.total_btn.config(state="normal")
                self.save_bill_btn.config(state="normal")

        default_bill()

        #===================================================

        def reset():
            self.bill_txt.delete("1.0",END)
            messagebox.showinfo("Success!","Bill has been reset.")
            default_bill()

        #====================== Buttons ========================

        '''
        Add, clear, reset, generate bill, total
        '''

        self.button_frame = Frame(self.prime_frame, border=4,relief=GROOVE,background="lightgrey")
        self.button_frame.place(x=15,y=280,width=450,height=230)

        self.add_btn = Button(self.button_frame, text="Add", font=('sans-serif',14),width=12,height=2,background="lightgrey",command=addbill)
        self.add_btn.grid(row=0,column=0,padx=2,pady=2)

        self.clear_btn = Button(self.button_frame, text="Clear", font=('sans-serif',14),width=12,height=2,background="lightgrey",command=clear_ent)
        self.clear_btn.grid(row=0,column=1,padx=2,pady=2)

        self.reset_btn = Button(self.button_frame, text="Reset", font=('sans-serif',14),width=12,height=2,background="lightgrey",command=reset)
        self.reset_btn.grid(row=0,column=2,padx=2,pady=2)

        self.gen_bill_btn = Button(self.button_frame, text="Generate Bill", font=('sans-serif',14),width=12,height=2,background="lightgrey",command=genbill)
        self.gen_bill_btn.grid(row=1,column=0,padx=2,pady=2)

        self.total_btn = Button(self.button_frame, text="Total", font=('sans-serif',14),width=12,height=2,background="lightgrey",command=totalgen)
        self.total_btn.grid(row=1,column=1,padx=2,pady=2)

        self.save_bill_btn = Button(self.button_frame, text="Save Bill", font=('sans-serif',14),width=12,height=2,background="lightgrey",command=save_bill)
        self.save_bill_btn.grid(row=1,column=2,padx=2,pady=2)

        #===== Default button configurations =========#

        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_bill_btn.config(state="disabled")

        #============================================#

        


        #=======================================================

        


if __name__ == "__main__":
    main()