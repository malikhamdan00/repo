from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System | Developed By Hamdan")
        self.root.config(bg="white")
        self.root.focus_force()
        
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        
        # ===========================Title=============================
        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
# ==========================================LABEL NAME and name Entry bar for adding category===========================================================================================
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",30),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightyellow").place(x=50,y=170,width=300)
# =========================================Adding "ADD" button and "DELETE" button======================================================================================================
        txt_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        txt_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)

# =======================================CATEGORY DETAILS=================TREE VIEW ADDED =================================================================================================================
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)
        self.category_table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)
        # ===============HEADINGS===============================
        self.category_table.heading("cid",text="CATEGORY ID")
        self.category_table.heading("name",text="NAME")
        # ==============Function to show headings=====================
        self.category_table["show"]="headings"
        # ============columns=======================
        self.category_table.column("cid",width=90)
        self.category_table.column("name",width=100)
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)   
        
# ===================================================ADD 1st IMAGES=================================================================================
        self.im1=Image.open("images/cat.jpg")
        self.im1=self.im1.resize((500,250),Image.Resampling.LANCZOS)
        self.im1=ImageTk.PhotoImage(self.im1)
# ==================================================ADD FUNCTION TO DISPLAY 1st IMAGE=================================================================
        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)
        
        
# ==================================================ADD 2nd IMAGE===========================================================================================
        self.im2=Image.open("images/category.jpg")
        self.im2=self.im2.resize((500,250),Image.Resampling.LANCZOS)
        self.im2=ImageTk.PhotoImage(self.im2)
#====================================================ADD FUNCTION TO DISPLAY 2nd IMAGE=========================================================================
        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)
        
        self.show()
# ==============================================Adding Function to "ADD" Button=========================================================================================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category Name Should Be Required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category Already Present , try different",parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Category Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

#==============================================To show all the data on Entry fields, Adding Show function====================================================================
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        
#=====================================to get access of data on entry fields=========================================================================
    def get_data(self,ev):
            f=self.category_table.focus()
            content=(self.category_table.item(f))
            row=content['values']
        # ======to set data on entry details=========
            self.var_cat_id.set(row[0])
            self.var_name.set(row[1])
            
# ==============================================Add function to Delete Button=======================================================================
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Please Select Category From The List",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error, please try again",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
# ===========================================================================================================================================================================
if __name__=="__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()