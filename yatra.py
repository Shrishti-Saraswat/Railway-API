from tkinter import*

class YATRA:
    def __init__(self):
        self.root=Tk()

        self.root.title("Train route")
        self.root.minsize(400,600)
        self.root.maxsize(400,600)
        self.root.configure(background="#2c3e50")
        label1=Label(self.root,text="Train Route",bg="#2c3e50",fg="#ecf0f1")
        label1.configure(font=("Constaltia",22,"bold"))
        label1.pack(pady=(30,10))

        self.train_no=Entry(self.root)
        self.train_no.pack(ipadx=30,ipady=5)

        click=Button(self.root,text="Fetch",bg="#bdc3c7",width=28,height=2,command=lambda:self.fetch())
        click.pack(pady=(10,20))

        self.result=Label(self.root,bg="#e67e22",fg="#e67e22")
        self.result.configure(font=("Constantia",14))
        self.result.pack(pady=(5,10))

        self.root.mainloop()
    def fetch(self):
        print("Hello")
obj=YATRA()
