import tkinter as tk
root = tk.Tk()
root.resizable(False,False)
root.title("Tic Tac Toe")

tk.Label(root , text="Tic Tac Toe", font=('Ariel', 25)).pack()
current_chr = "X"

play_area = tk.Frame(root,height=300,width=300,bg="white")
X_point=[]
O_point=[]
class XO_point:
    def __init__(self,x,y):
        self.x= x
        self.y= y
        self.value= None
        self.button = tk.Button(play_area,height=5,width=10,text="",command=self.set)
        self.button.grid(row=x,column=y)

    def set(self):
        global current_chr
        if not self.value:
            self.button.config(text = current_chr, bg="snow",fg="black")
            self.value = current_chr
            if current_chr =="X":
                X_point.append(self)
                current_chr == "O"
            elif current_chr =="O":
                X_point.append(self)
                current_chr == "X"
            

    def reset(self):
        self.button.configure(text="",bg="white")
        self.value= None
for x in range(1,4):
    for y in range(1,4):
        XO_point(x,y)

play_area.pack(padx=10,pady=10)




















root.mainloop()
