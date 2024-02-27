# def concat():
#     '''Function to Concatenate strings'''
#     fname = input("Enter First Name: ")
#     lname = input("Enter last Name: ")
#     print("Name:  "+fname+" "+lname)
# concat()
# def calc(num1,num2):
#     '''Function to calculate sum,prod,difference'''    
#     add = num1+num2
#     sub1 = num1-num2
#     sub2 = num2-num1
#     multiply = num1*num2
#     print(f"Sum: {add}\nDifference(First Num - Second Num):{sub1}\nDifference(Second Num - First Num ): {sub2}\nProduct: {multiply}"  )

# num1= int(input("Enter First Number "))
# num2= int(input("Enter Second Number "))

# calc(num1,num2)

# import tkinter
# from tkinter import *
# from PIL import ImageTk,Image
# import time

# root = Tk()
# root.title("Tower Of Hanoi")
# root.minsize(width=600, height=450)
# root.attributes("-alpha", 0.9)
# root.configure(background="#9AD0EC")

# title = Label(root, text='Tower Of Hanoi', fg="white",font="Helveca 30",bg="#9AD0EC")
# title.pack()

# movescount=0

# def elem_start_pos():
#     global img1,img2,img3,img4,movescount,all_posx,all_posy,canvas,pole,moves
#     all_posx=[]
#     all_posy=[]
    
#     moves = Label(root, text=f'{movescount} Moves', fg="white",font="Helveca 20",bg="#9AD0EC")
#     moves.place(relx=0.5, rely=0.12, anchor=CENTER)

#     canvas = Canvas(root, width =550, height = 350,background="#9AD0EC",bd=0, highlightthickness=0)  
#     canvas.place(relx=0.5, rely=0.55, anchor=CENTER)

#     pole = ImageTk.PhotoImage(Image.open("poles.png"))
#     canvas.create_image(-20, -20, anchor=NW, image=pole)
    
#     restart_game = Button(root,text ="Restart", fg="white", font="Helveca 30 bold",bg='white',activebackground='white',highlightbackground="#71cad3",justify=CENTER,command=lambda:restart_tower_game(),width=13,bd=0)
#     restart_game.configure(bg='#85F4FF')
#     restart_game.place(relx=0.5,rely=0.92, anchor=SE)

#     enter = Button(root,text ="Start", fg="white", font="Helveca 30 bold",bg='white',activebackground='white',highlightbackground="#71cad3",justify=CENTER,command=lambda:TowerOfHanoi(4 , 0, 360, 180),width=13,bd=0)
#     enter.configure(bg='#85F4FF')
#     enter.place(relx=0.5, rely=0.92, anchor=SW)

#     img1 = ImageTk.PhotoImage(Image.open("1.png"))
#     all_posx.append(10)
#     all_posy.append(0)
#     canvas.create_image(all_posy[0], all_posx[0], anchor=NW, image=img1)

#     img2 = ImageTk.PhotoImage(Image.open("2.png"))
#     all_posx.append(55)
#     all_posy.append(0)
#     canvas.create_image(all_posy[1], all_posx[1], anchor=NW, image=img2)

#     img3 = ImageTk.PhotoImage(Image.open("3.png"))
#     all_posx.append(100)
#     all_posy.append(0)
#     canvas.create_image(all_posy[2], all_posx[2], anchor=NW, image=img3)

#     img4 = ImageTk.PhotoImage(Image.open("4.png"))
#     all_posx.append(145)
#     all_posy.append(0)
#     canvas.create_image(all_posy[3], all_posx[3], anchor=NW, image=img4)    

# def TowerOfHanoi(n , source, destination, auxiliary):
#     global moves,movescount
#     if n==1:
#         movescount+=1
#         moves.configure(text=str(movescount) +" Moves")
#         time.sleep(0.4)
#         move(0,destination)
#         time.sleep(0.4)
#         return
#     TowerOfHanoi(n-1, source, auxiliary, destination)
#     movescount+=1
#     moves.configure(text=str(movescount) +" Moves")
#     time.sleep(0.4)
#     move(n-1,destination)
#     time.sleep(0.4)
#     TowerOfHanoi(n-1, auxiliary, destination, source)

# def move(item,destination):
#     global img1,img2,img3,img4
    
#     if(item ==0):
        
#         if(all_posy[0]!=destination):
#             img1 = ImageTk.PhotoImage(Image.open("1.png"))
#             canvas.create_image(destination, 145-(45*all_posy.count(destination)), anchor=NW, image=img1)
#             all_posy[0]=destination
#             all_posx[0]=145-(45*all_posy.count(destination))
#             Tk.update(root) 
#             return
    
#     elif(item ==1):
        
#         if(all_posy[1]!=destination):
#             img2 = ImageTk.PhotoImage(Image.open("2.png"))
#             canvas.create_image(destination, 145-(45*all_posy.count(destination)), anchor=NW, image=img2)
#             all_posy[1]=destination
#             all_posx[1]=145-(45*all_posy.count(destination))
#             Tk.update(root) 
#             return
    
#     elif(item ==2):
        
#         if(all_posy[2]!=destination):
#             img3 = ImageTk.PhotoImage(Image.open("3.png"))
#             canvas.create_image(destination, 145-(45*all_posy.count(destination)), anchor=NW, image=img3)
#             all_posy[2]=destination
#             all_posx[2]=145-(45*all_posy.count(destination))
#             Tk.update(root) 
#             return
#     else:
#         if(all_posy[3]!=destination):
#             img4 = ImageTk.PhotoImage(Image.open("4.png"))
#             print(all_posx.count(destination))
#             canvas.create_image(destination, 145-(45*all_posy.count(destination)), anchor=NW, image=img4)
#             all_posy[3]=destination
#             all_posx[3]=145-(45*all_posy.count(destination))
#             Tk.update(root) 
#             return

# def restart_tower_game():
#     global img1,img2,img3,img4,all_posx,all_posy,movescount
#     movescount=0
#     Label.destroy(moves)
#     elem_start_pos()

# elem_start_pos()
# root.mainloop()

#LAB 3 Question 1

# #tower of hanoi (code only)
# def hanoi(n, source, dest, aux):
#   if n == 1:
#     print(f"Move disk 1 from {source} to {dest}")
#   else:
#     hanoi(n-1, source, aux, dest)
#     print(f"Move disk {n} from {source} to {dest}")
#     hanoi(n-1, aux, dest, source)

# # Example usage
# hanoi(3, 'A', 'C', 'B')

# #LAB 3 Question 2
# def is_palindrome(string):
#     if len(string) <= 1:
#         return True
#     if string [0] == string [-1]:
#         return is_palindrome(string[1:-1])
#     return False

# print(is_palindrome("Huzaifa"))
# print(is_palindrome("madam"))
# print(is_palindrome("racecar"))
# #LAB 3 Question 3
# #Create a Python class BankAccount that models a bank account. The class should have attributes for account_number, balance, and owner_name. Implement methods for deposit, withdrawal, and displaying account information. Class must have a constructor that needs to be destroyed at the end.

# class BankAccount:
#     def __init__(self, account_number, owner_name, balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "Insufficient balance"
#         self.balance -= amount
#         return self.balance

#     def display(self):
#         return f"Account Number: {self.account_number}\nOwner Name: {self.owner_name}\nBalance: {self.balance}"

#     def __del__(self):
#         print("Object Destroyed")

# account = BankAccount(1234, "Huzaifa", 1000)
# print(account.display())
# print(account.deposit(500))
# print(account.display())
# print(account.withdraw(200))
# print(account.display())
# del account

#LAB 3 Question 4
class Shape:
    def __init__(self):
        self.area = 0.0

    def calculate_area(self):
        pass

    def on_area_change(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.pi = 3.141592653589793
        self.calculate_area()

    def calculate_area(self):
        self.area = self.pi * self.radius * self.radius

    def on_area_change(self):
        print("The area of the circle has changed.")

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
        self.calculate_area()

    def calculate_area(self):
        self.area = 0.5 * self.base * self.height

    def on_area_change(self):
        print("The area of the triangle has changed.")

class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length
        self.calculate_area()

    def calculate_area(self):
        self.area = self.width * self.length

    def on_area_change(self):
        print("The area of the rectangle has changed.")


def main():
    circle = Circle(5.0)
    print(circle.area)

    triangle = Triangle(3.0, 4.0)
    print(triangle.area)

    rectangle = Rectangle(2.0, 5.0)
    print(rectangle.area)

    circle.radius = 10.0
    circle.calculate_area()
    circle.on_area_change()
    print(circle.area)

    triangle.base = 5.0
    triangle.height = 5.0
    triangle.calculate_area()
    triangle.on_area_change()
    print(triangle.area)

    rectangle.width = 2.0
    rectangle.length = 10.0
    rectangle.calculate_area()
    rectangle.on_area_change()
    print(rectangle.area)

if __name__ == "__main__":
    main()



