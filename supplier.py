from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System | Developed By Hamdan")
        self.root.config(bg="white")
        self.root.focus_force()
        # =====================================================
        # ========================All Variables====================================================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        
        # ================================Search Frame===============================================
        SearchFrame=LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=250,y=20,width=600,height=70)
        
        # ================================options========================================================
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","CNIC","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        # ================================Search Btn and txt Entry=============================================
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
        
        
        # ====================================title=================================================
        title=Label(self.root,text="Supplier Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
        
        # ========================================content============================================
        # ============================================Row 1============================================
        lbl_supplier_invoice=Label(self.root,text="Invoice No",font=("goudy old style",15),bg="white").place(x=50,y=150)
        
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)

        # ============================================Row 2=============================================
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        
        # ==============================================Row 3=========================================
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=230)
        
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        
        
        # =========================================Row 4===============================================
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=270)

        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=150,y=270,width=300,height=60)
        
        
        # ======================================================Buttons============================================
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)


        # =======================================================Employee Details====================================
        # ========================================frame where details name are shown=============================
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        
        # ====================================================Scrol Details========================================
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("invoice",text="INVOICE ID")
        self.supplierTable.heading("name",text="NAME")
        self.supplierTable.heading("contact",text="CONTACT")
        self.supplierTable.heading("desc",text="DESCRIPTION")
        
        self.supplierTable["show"]="headings"
        
        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=100)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)   
        self.supplierTable.pack(fill=BOTH,expand=1)
        # self.show()
        
# =========================================================================================================================================================
# ======================Add function to (ADD) Button===============================================================================================================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Invoice no. already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                    self.var_sup_invoice.get(),
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.txt_desc.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
# ==================================================================================================================================================
# ===============To show all the data on Entry fields==========================================================================================================
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
#====================================to get access of data on entry fields==================================================================================
    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        # ======to set data on entry details=========
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_cnic.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[9])
        self.var_salary.set(row[10])
# =========================================================================================================================================================================================
# =========UPDATE FUNCTION SETUP============================================================================================================================================================
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("Update Employee set name=?,cnic=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                                    self.var_name.get(),
                                    self.var_cnic.get(),
                                    self.var_gender.get(),
                                    self.var_contact.get(),
                                    self.var_dob.get(),
                                    self.var_doj.get(),
                                    self.var_pass.get(),
                                    self.var_utype.get(),
                                    self.txt_desc.get('1.0',END),
                                    self.var_salary.get(),
                                    self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
                    self.show()  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
# ==================================================================================================================================================
# ==============================Add function to Delete Button=============================================================================================
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

# ========================Add function to Clear Button==============================================================================================================================
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_cnic.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Select")
        self.txt_desc.delete('1.0',END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
# ==================Add function to Search Bar and Search Button=============================================================================================================
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Select input should be required",parent=self.root)
            else:
                cur.execute("Select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in rows:
                        self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)






# ===========================================================================================================================================================================
if __name__=="__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()
    # 16:14  part 4