from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System | Developed By Hamdan")
        self.root.config(bg="white")
        self.root.focus_force()
        # ===============================variables defined======================================
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        
        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)
        
        # =================================================================TITLE ADDED=======================================================================
        title=Label(product_Frame,text="Manage Product Details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        
        
        # =======================LABELS ADDED======================================================================
        lbl_category=Label(product_Frame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=110)
        lbl_product_name=Label(product_Frame,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=160)
        lbl_price=Label(product_Frame,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=210)
        lbl_qty=Label(product_Frame,text="Quantity",font=("goudy old style",18),bg="white").place(x=30,y=260)
        lbl_status=Label(product_Frame,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=310)

#======================================ENTRY FIELS FOR LABELS, WE ADDED ON #LABELS ADDED======================================================
        txt_category=Label(product_Frame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=("Select"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=10,y=10,width=180)
        cmb_cat.current(0)
        
# 11:03 , To be continued

# ===========================================================================================================================================================================
if __name__=="__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()