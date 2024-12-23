from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System | Developed By Hamdan")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # ====Search Frame====
        SearchFrame=LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=250,y=20,width=600,height=70)
        
        # ====options====
        cmb_search=ttk.Combobox(SearchFrame,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        
        txt_search=Entry(SearchFrame,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
        # time: 17:44 






if __name__=="__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()