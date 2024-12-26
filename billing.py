from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import time
import sqlite3
class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By Hamdan")
        self.root.config(bg="white")
#====================================Variables===========================
        self.cart_list= []

        # ========================================== Title ===========================================
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman", 40, "bold"),bg="#010c48",fg="white",anchor="w",padx=20,).place(x=0, y=0, relwidth=1, height=70)

        # ===================================== Logout Button =========================================
        btn_logout = Button(self.root,text="Logout",font=("times new roman", 15, "bold"),bg="yellow",cursor="hand2",).place(x=1150, y=10, height=50, width=150)

        # ========================================== Clock ==============================================
        self.lbl_clock = Label(self.root,text=" Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:ss",font=("times new roman", 15),bg="#4d636d",fg="white",)
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        
        
#==============================================Product_Frame=================================================================================================
        self.var_search=StringVar()
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)
        
#==============================================Top Label for Product Frame========================================================================
        pTitle=Label(ProductFrame1,text="All Prododucts",font=("goudy old style",20,"bold"),bg="teal",fg="black").pack(side=TOP,fill=X)
        
#======================================Box inside Product Frame for Entry field, Labels and Buttons========================================================
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)
# =========================================Search Label and Name Label inside Box=========================================================================
        lbl_search=Label(ProductFrame2,text="Search Product  |  By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        lbl_name=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=45)
        
#==========================================Search label, Search Entry and Search Button=========================================================================
        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)

# =====================================SHOW ALL BUTTON==========================================================================================================================
        btn_show_all=Button(ProductFrame2,text="Show All",command=self.show,font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)

# =======================================================Supplier Details=========================================================================================================================
        # ========================================frame where details name are shown======================================================================================================================
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)
        
        # ====================================================Scroll Details==============================================================================================================================
        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)
        # =====================================================Tree View DETAILS==========================================================================================================================
        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        self.product_Table.heading("pid",text="P-ID")
        self.product_Table.heading("name",text="NAME")
        self.product_Table.heading("price",text="PRICE")
        self.product_Table.heading("qty",text="QTY")
        self.product_Table.heading("status",text="STATUS")
        self.product_Table["show"]="headings"
        
        self.product_Table.column("pid",width=40)
        self.product_Table.column("name",width=90)
        self.product_Table.column("price",width=90)
        self.product_Table.column("qty",width=40)
        self.product_Table.column("status",width=90)   
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        
        lbl_note=Label(ProductFrame1,text="Note: 'Enter 0 QTY to Remove the Product From Cart' ",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
#===========================================================VARIABLES FOR CUSTOMER SECTION=================================================================
        self.var_cname=StringVar()
        self.var_contact=StringVar()
#============================================CUSTOMER FRAME=====================================================================================
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)
        
#==========================================Title inside Customer Frame======================================================================================
        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
#==============================================Add LABEL AND ENTRY FIELD OF NAME INSIDE CUSTOMER FRAME==============================================================
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180)
#==============================================Add LABEL AND ENTRY FIELD OF CONTaCT INSIDE CUSTOMER FRAME===========================================================
        lbl_contact=Label(CustomerFrame,text="Contact No.",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)

#============================================CALCULATOR AND CART FRAME=====================================================================================
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)
#==============================================MAKE FRAME INSIDE Cal_Cart_Frame=======================================================================================
        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)
#==========================================VARIABLES DEFINED FOR CALCULATOR==================================================================================================
        self.var_cal_input=StringVar()
#=================================MAKE CALCULATOR LAYOUT AND FUNCTIONS INSIDE Cal_Cart_Frame===============================================================================
        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        
#===========================================ADD BUTTONS FOR CALCULATOR=====================================================================================
        btn_7=Button(Cal_Frame,text='7',font=("arial",15,"bold"),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=("arial",15,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=("arial",15,"bold"),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text="+",font=("arial",15,"bold"),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)
        
        btn_4=Button(Cal_Frame,text='4',font=("arial",15,"bold"),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=("arial",15,"bold"),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=("arial",15,"bold"),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text="-",font=("arial",15,"bold"),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)
        
        btn_1=Button(Cal_Frame,text='1',font=("arial",15,"bold"),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=("arial",15,"bold"),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text='3',font=("arial",15,"bold"),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text="*",font=("arial",15,"bold"),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)
        
        
        btn_0=Button(Cal_Frame,text='0',font=("arial",15,"bold"),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='C',font=("arial",15,"bold"),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',font=("arial",15,"bold"),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text="/",font=("arial",15,"bold"),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)
        
        
#===============================================MAKING CART FRAME INSIDE Cal_Cart_Frame=========================================================================
        cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=280,y=8,width=245,height=342)
#==========================================Title inside  Cal_Cart_Frame======================================================================================
        self.cartTitle=Label(cart_Frame,text="Cart \t Total Product: 0",font=("goudy old style",15),bg="lightgray")
        self.cartTitle.pack(side=TOP,fill=X)
        # ====================================================Scroll Details==============================================================================================================================
        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)
        # =====================================================Tree View DETAILS==========================================================================================================================
        self.CartTable=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        self.CartTable.heading("pid",text="P-ID")
        self.CartTable.heading("name",text="NAME")
        self.CartTable.heading("price",text="PRICE")
        self.CartTable.heading("qty",text="QTY")
        self.CartTable["show"]="headings"
        
        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=100)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=40)
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)
        
#========================================DEFINE VARIABLES FOR ADD CART WIDGET FRAME===================================================
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
#===========================================Add CART FRAME WIDGETS========================================================================
        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550,width=530,height=110)
#==============================================LABEL AND ENTRY FIELD OF NAME INSIDE CART_FRAME===================================================================
        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=5,y=35,width=190,height=22)
#==============================================LABEL AND ENTRY FIELD OF PRICE INSIDE CART_FRAME===================================================================

        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=230,y=35,width=150,height=22)
        
#==============================================LABEL AND ENTRY FIELD OF QUANTITY INSIDE CART_FRAME===================================================================

        lbl_p_qty=Label(Add_CartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)
        
        
        self.lbl_inStock=Label(Add_CartWidgetsFrame,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
        
        
#===============================================Buttons For Clear Cart============================================================
        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear",font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
#===============================================Buttons For Add | update  Cart============================================================
        btn_add_cart=Button(Add_CartWidgetsFrame,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
        
#============================================MAKE FRAME FOR BILL AREA SECTION===========================================================================================================
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=953,y=110,width=410,height=410)
#==============================================Top Label for CUSTOME BILL Frame===============================================================================================================
        BTitle=Label(billFrame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="lime",fg="black").pack(side=TOP,fill=X)
#=================================================ADD SCROLL FUNCTION TO CUSTOMER BILL FRAME=======================================================================================================
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)     
        
#=====================================================BILLING BUTTONS ADDED HERE================================================================================================================================
#============================================FRAME ADDED FOR BILLING BUTTONS===========================================================================================================================================
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=953,y=520,width=410,height=140)

#=============================================LABEL IN WHICH AMOUNT OF BILL IS SHOWN=======================================================================================================================================
        self.lbl_amnt=Label(billMenuFrame,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=430,height=70)
        
#=============================================LABEL IN WHICH DISCOUNT  OF BILL IS SHOWN=======================================================================================================================================
        # self.lbl_discount=Label(billMenuFrame,text="Discount \n[5%]",font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        # self.lbl_discount.place(x=124,y=5,width=120,height=70)
        
#=============================================LABEL IN WHICH TOTAL AMOUNT OF BILL IS SHOWN=======================================================================================================================================
        # self.lbl_net_pay=Label(billMenuFrame,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
        # self.lbl_net_pay.place(x=246,y=5,width=160,height=70)
        
#=============================================BUTTON FOR PRINT RECEIPT ======================================================================================================================================
        btn_print=Button(billMenuFrame,text="Print",font=("goudy old style",15,"bold"),bg="blue",fg="white",cursor="hand2")
        btn_print.place(x=2,y=80,width=120,height=50)
        
#=============================================BUTTON FOR CLEAR GENERATED ALL=======================================================================================================================================
        btn_clear_all=Button(billMenuFrame,text="Clear All",font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2")
        btn_clear_all.place(x=124,y=80,width=120,height=50)
        
#=============================================BUTTON FOR GENERATE BILL=======================================================================================================================================
        btn_generate=Button(billMenuFrame,text="Generate/Save Bill",command=self.generate_bill,font=("goudy old style",15,"bold"),bg="#009688",fg="white",cursor="hand2")
        btn_generate.place(x=246,y=80,width=160,height=50)
                
#================================================FOOTER=========================================================================================================================================================
        footer=Label(self.root,text="IMS-Inventory Management System | Developed By Hamdan\nFor any Technical Issue Contact: +92-316-4780493",font=("times new roman",11),bg="#4d636d",fg="white",cursor="hand2").pack(side=BOTTOM,fill=X)
        self.show()
        # self.bill_top()
#================================All Functions Defined Under=======================================================================
#===============================functions defined for calculator==============================================================
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        
    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        
        self.var_cal_input.set(eval(result))
        
#==========================================================OTHER PAGE FUNCTIONS DEFINED===================================================
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select pid,name,price,qty,status from product where status='Active'")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        
        
# ==================Add function to Search Bar and Search Button=============================================================================================================
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Select input should be required",parent=self.root)
            else:
                cur.execute("Select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        
#====================================to get access of data on entry fields==================================================================================
    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        # ======to set data on entry details=========
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')
        
#====================================to get access of data on entry fields==================================================================================
    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        # ======to set data on entry details=========
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        self.var_qty.set('1')

#===========================================================FUNCTION FOR ADD TO CART================================================================================================================================================================
    def add_update_cart(self):
            if self.var_pid.get()=='':
                messagebox.showerror("Error","Please Select Product From List",parent=self.root)
            elif self.var_qty.get()=='':
                messagebox.showerror("Error","Quantity is Required",parent=self.root)
            elif int(self.var_qty.get())>int(self.var_stock.get()):
                    messagebox.showerror("Error","Invalid Quantity",parent=self.root)
            else:
                # price_cal=int(self.var_qty.get()) * float(self.var_price.get())
                # price_cal=float(price_cal)
                price_cal=self.var_price.get()
                cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
#========================FUNCTION FOR UPDATE CART============================================================================================================================================================================================================
                present='no'
                index_=0
                for row in self.cart_list:
                    if self.var_pid.get()==row[0]:
                        present='yes'
                        break
                    index_+=1
                if present=='yes':
                    op=messagebox.askyesno('Confirm',"Product already Present\nDo you want to Update| Remove from the Cart List",parent=self.root)
                    if op==True:
                        if self.var_qty.get()=="0":
                            self.cart_list.pop(index_)
                        else:
                        #     self.cart_list[index_][2]=price_cal #PRICE
                            self.cart_list[index_][3]=self.var_qty.get() #qty
                else:
                    self.cart_list.append(cart_data)
                    
                self.show_cart()
                self.bill_updates()
#===================================================FUNCTION FOR UPDATE BILL==================================================================================================================================================================================================================
    def bill_updates(self):
        self.bill_amnt=0
        self.net_pay=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
        # self.discount=(bill_amnt*5)/100
        # net_pay=bill_amnt-self.discount
        self.lbl_amnt.config(text=f'Bill Amount\n{str(self.bill_amnt)}')
        # self.lbl_net_pay.config(text=f'Net Pay\n{str(net_pay)}')
        self.cartTitle.config(text=f"Cart \t Total Product: {str(len(self.cart_list))}")

#===================================================FUNCTIONS FOR SHOW ITEMS IN CART FRAME==================================================================================================================================================================================================================
     
    def show_cart(self):
            try:  
                self.CartTable.delete(*self.CartTable.get_children())
                for row in self.cart_list:
                    self.CartTable.insert('',END,values=row)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

#================================GENERATING BILL LAYOUT AND FUNCTIONALITY=============================================================================================================
    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are Required",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error",f"Please Add Product To The Cart!!!",parent=self.root)
        else:
            #====Bill Top======
            self.bill_top()
            #=====Bill Middle===
            self.bill_middle()
            #====Bill Bottom
            self.bill_bottom()

    def bill_top(self):
        invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tXYZ-Inventory
\t Phone No. 98725*****, Lahore-50040
{str("="*47)}
 Customer Name: {self.var_cname.get()}
 Ph no.: {self.var_contact.get()}
 Bill No. {str(invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)
        
    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Net Pay\t\t\t\tRs.{self.bill_amnt}
{str("="*47)}\n
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
        
    def bill_middle(self):
        for row in self.cart_list:
            name=row[1]
            qty=row[3]
            price=float(row[2]*int(row[3]))#*int(row[3])
            price=str(price)
            self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+qty+"\tRs."+price)

# ============Initialize the GUI===========
if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()
