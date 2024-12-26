from tkinter import *
from PIL import Image, ImageTk
import time
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By Hamdan")
        self.root.config(bg="white")

        # ========================================== Title ===========================================
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman", 40, "bold"),bg="#010c48",fg="white",anchor="w",padx=20,).place(x=0, y=0, relwidth=1, height=70)

        # ===================================== Logout Button =========================================
        btn_logout = Button(self.root,text="Logout",font=("times new roman", 15, "bold"),bg="yellow",cursor="hand2",).place(x=1150, y=10, height=50, width=150)

        # ========================================== Clock ==============================================
        self.lbl_clock = Label(self.root,text=" Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:ss",font=("times new roman", 15),bg="#4d636d",fg="white",)
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # ========================================== Left Menu ==============================================
        self.MenuLogo = Image.open("images/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.Resampling.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        self.LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.LeftMenu.place(x=0, y=102, width=200, height=565)
        
        
        lbl_menuLogo = Label(self.LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)
        
        # =============================================MENU BAR=================================================
        self.icon_side = PhotoImage(file="images/side.png")
        lbl_menu = Label(self.LeftMenu,text="Menu",font=("times new roman", 20),bg="#009688").pack(side=TOP,fill=X)
        # =============================================Employee-btn=============================================
        btn_employee = Button(self.LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman", 20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        # ================================================Supplier-btn==============================================
        btn_supplier = Button(self.LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman", 20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        # ==================================================category-btn================================================
        btn_category = Button(self.LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman", 20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        # =====================================================product-btn===========================================
        btn_product = Button(self.LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman", 20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        # =======================================================sales-btn============================================
        btn_sales = Button(self.LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman", 20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        # ========================================================exit-btn==============================================
        btn_exit = Button(self.LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman", 20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        
        # ==========================================================content======================================
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style", 20 ,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
        
        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style", 20 ,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        
        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style", 20 ,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)
        
        self.lbl_product=Label(self.root,text="Total Products\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style", 20 ,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        
        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style", 20 ,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        
        # ==========================================================Footer==========================================
        lbl_footer= Label(self.root,text="IMS-Inventory Management System | Developed By Hamdan\nFor any Technical Issue Contact: +92-316-4780493",font=("times new roman", 12),bg="#4d636d",fg="white",).pack(side=BOTTOM,fill=X)
        self.update_date_time()
        
# ==========================================Function for employee enu=======================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
# ===========================================Function for supplier menu======================================================
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
        
# ===========================================Function for Category menu======================================================
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
        
# ===========================================Function for Product menu======================================================
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

# ===========================================Function for sales menu======================================================
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
        
#=================================================SET AUTO DATE AND TIME===========================================================================================
    def update_date_time(self):
        time_= time.strftime("%I:%M:%S")
        date_= time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f" Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)


# ============Initialize the GUI===========
if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
