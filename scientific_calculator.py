import random
from tkinter import *
import math



class Calculator:
    def __init__(self, window):

        self.root=window
        self.root.configure(bg='black')

        self.disply=Entry(self.root , width=25, bg='white' , font=('arial',20))
        self.disply.place(x=15, y=60)
 
        #core_oprator
        self.actions_butten=Button(self.root, text='(', command=lambda : self.num_click('(') , anchor=CENTER, width=4 , height=1 , font=('times new roman',14) , bg='black' , fg='white'  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=15 , y=445)

        self.actions_butten=Button(self.root, text=')', command=lambda : self.num_click(')') , anchor=CENTER, width=4 , height=1 , font=('times new roman',14) , bg='black' , fg='white'  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=65 , y=445)

        self.actions_butten=Button(self.root, text='÷', command=lambda : self.op_click('÷') ,  anchor=CENTER, width=4 , height=1 , font=('times new roman',14) , bg='black' , fg='orange'  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=115 , y=445)

        self.actions_butten=Button(self.root, text='×', command=lambda : self.op_click('×') ,  anchor=CENTER, width=4 , height=1 , font=('times new roman',14) , bg='black' , fg='orange'  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=165 , y=445)

        self.actions_butten=Button(self.root, text='-', command=lambda : self.op_click('-') , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , bg='black' , fg='orange' , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=215 , y=445)

        self.actions_butten=Button(self.root, text='+', command=lambda : self.op_click('+') ,  anchor=CENTER, width= 4, height= 1 , font=('times new roman',14) , bg='black' , fg='orange' , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=265 , y=445)

        self.actions_butten=Button(self.root, text='=',command=self.equal_btn ,  anchor=CENTER, width= 7 , height=1 , font=('times new roman',14)  , bg='black' , fg='orange'  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=315 , y=445)
        
        #numbers
        self.one_butten=Button(self.root, text='1', bg='black' ,fg='white' , anchor=CENTER, command=lambda : self.num_click(1), width=4 , height=1 , font=('times new roman',14)  , relief=FLAT, cursor='hand2')
        self.one_butten.place(x=15 , y=405)

        self.actions_butten=Button(self.root, text='2' , bg='black' ,fg='white' ,command=lambda : self.num_click(2),anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=70 , y=405)

        self.actions_butten=Button(self.root, text='3', bg='black' ,fg='white' ,anchor=CENTER,command=lambda : self.num_click(3), width=4 , height=1 , font=('times new roman',14)  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=125 , y=405)

        self.actions_butten=Button(self.root, text='4', bg='black' ,fg='white' , anchor=CENTER,command=lambda : self.num_click(4), width=4 , height=1 , font=('times new roman',14)  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=15 , y=365)

        self.actions_butten=Button(self.root, text='5', bg='black' ,fg='white' , anchor=CENTER,command=lambda : self.num_click(5), width=4 , height=1 , font=('times new roman',14)  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=70 , y=365)

        self.actions_butten=Button(self.root, text='6', bg='black' ,fg='white' ,  anchor=CENTER,command=lambda : self.num_click(6), width=4 , height=1 , font=('times new roman',14)  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=125 , y=365)

        self.actions_butten=Button(self.root, text='7', bg='black' ,fg='white' ,anchor=CENTER,command=lambda : self.num_click(7), width=4 , height=1 , font=('times new roman',14)  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=15 , y=325)

        self.actions_butten=Button(self.root, text='8', bg='black' ,fg='white' , anchor=CENTER,command=lambda : self.num_click(8), width=4 , height=1 , font=('times new roman',14)  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=70 , y=325)

        self.actions_butten=Button(self.root, text='9', bg='black' ,fg='white' ,  anchor=CENTER,command=lambda : self.num_click(9), width=4 , height=1 , font=('times new roman',14)  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=125 , y=325)

        self.actions_butten=Button(self.root, text='0', bg='black' ,fg='white' ,anchor=CENTER,command=lambda : self.num_click(0), width=4 , height=1 , font=('times new roman',14)  , relief=FLAT, cursor='hand2')
        self.actions_butten.place(x=15 , y=285)


        #other_functions
        
        self.actions_butten=Button(self.root, text='h', bg='black' ,fg='gray' , command=lambda : self.op_click('h') , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=235 , y=365)

        self.actions_butten=Button(self.root, text='| z |', bg='black' ,fg='gray' , command=self.Absolute_value , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2') 
        self.actions_butten.place(x=180 , y=405)

        self.actions_butten=Button(self.root, text='Rad', bg='black' ,fg='gray' , command=self.radians , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=290 , y=365)

        self.actions_butten=Button(self.root, text='%' ,command=lambda : self.op_click('%') ,  anchor=CENTER, width=4 , height=1 , font=('times new roman',14) , bg='black' ,fg='orange' , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=345 , y=405)

        self.actions_butten=Button(self.root, text='e', bg='black' ,fg='gray' , command=self.e , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=180 , y=365)

        self.actions_butten=Button(self.root, text='n!', bg='black' ,fg='gray' , command=self.factorial , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=235 , y=405)

        self.actions_butten=Button(self.root, text='Rnd', bg='black' ,fg='gray' , command=self.random , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=290 , y=405)

        self.actions_butten=Button(self.root, text='log', bg='black' ,fg='gray' , command=self.log , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=180 , y=245)

        self.actions_butten=Button(self.root, text='ln', bg='black' ,fg='gray' , command=self.ln , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=125 , y=245)

        self.actions_butten=Button(self.root, text='Deg', bg='black' ,fg='gray' , command=self.degrees , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=345 , y=365)

        self.actions_butten=Button(self.root, text='√', bg='black' ,fg='gray' , command=self.squared , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=180 , y=325)

        self.actions_butten=Button(self.root, text='x^y', bg='black' ,fg='gray' , command=lambda : self.op_click('^'), anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=70 , y=245)

        self.actions_butten=Button(self.root, text='.', bg='black' ,fg='white' ,command=lambda : self.num_click('.') , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=70 , y=285)

        self.actions_butten=Button(self.root, text='π', bg='black' ,fg='gray' , command=self.pi , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=125 , y=285)

        self.actions_butten=Button(self.root, text='trunc', bg='black' ,fg='gray' , command=self.trunc , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=235 , y=325)

        self.actions_butten=Button(self.root, text='asinh', bg='black' ,fg='gray' , command=self.asinh, anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=345 , y=325)

        self.actions_butten=Button(self.root, text='acosh', bg='black' ,fg='gray' , command=self.acosh, anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=290 , y=325)

        self.actions_butten=Button(self.root, text='Γ', bg='black' ,fg='gray' , command=self.gamma , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=180 , y=285)

        self.actions_butten=Button(self.root, text='sinh', bg='black' ,fg='gray' , command=self.sinh , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=345 , y=245)

        self.actions_butten=Button(self.root, text='cosh', bg='black' ,fg='gray' , command=self.cosh , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=290 , y=245)

        self.actions_butten=Button(self.root, text='tanh', bg='black' ,fg='gray' , command=self.tanh, anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=235 , y=245)

        self.actions_butten=Button(self.root, text='asin', bg='black' ,fg='gray' , command=self.asin, anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=345 , y=285)

        self.actions_butten=Button(self.root, text='acos', bg='black' ,fg='gray' , command=self.acos, anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=290 , y=285)

        self.actions_butten=Button(self.root, text='atan', bg='black' ,fg='gray' , command=self.atan, anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=235 , y=285)

        self.actions_butten=Button(self.root, text='sin', bg='black' ,fg='gray' , command=self.sin , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=345 , y=205)

        self.actions_butten=Button(self.root, text='cos', bg='black' ,fg='gray' , command=self.cos , anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=290 , y=205)

        self.actions_butten=Button(self.root, text='tan', bg='black' ,fg='gray' , command=self.tan, anchor=CENTER, width=4 , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=235 , y=205)

        #delete and clean
        self.actions_butten=Button(self.root, text='Del', command=self.delete , anchor=CENTER, width=4 ,  bg='black' ,fg='orange' , height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=15 , y=245)

        self.actions_butten=Button(self.root, text='AC', command=self.all_clear , anchor=CENTER, width=4 , bg='black' ,fg='orange' ,  height=1 , font=('times new roman',14)  , relief=FLAT , cursor='hand2')
        self.actions_butten.place(x=15 , y =205)


        self.empty_entry=True   
        self.current_num = ''
        self.op_press= False
        self.type_op =''
        self.total = 0
        

    def num_click(self, num):
        first_number=self.disply.get()
        second_number= str(num)
        if self.empty_entry:
            self.current_num =num
            self.empty_entry = False
        else:
            if second_number == '.':
                if second_number in first_number:
                    return
            self.current_num = first_number + second_number
        self.display(self.current_num)



    def op_click(self,op):
        
        self.current_num =float(self.disply.get())

        if not self.op_press:
            self.total = self.current_num
            self.empty_entry = True
            
        else:
            self.valid_function()
        self.op_press = True
        self.type_op = op


    def valid_function(self):
        if self.type_op == "+":
            self.total = float(self.total) + float(self.current_num)
        if self.type_op == "-":
            self.total =float(self.total) - float(self.current_num)
        if self.type_op == "×":
            self.total=float(self.total) *  float(self.current_num)
        if self.type_op == "÷":
            self.total =float(self.total)/float(self.current_num)
        if self.type_op == "%":
            self.total =float(self.total) % float(self.current_num)
        if self.type_op == "^":
            self.total = math.pow(float(self.total),float(self.current_num))
        if self.type_op == "h":
            self.total = math.hypot(float(self.total),float(self.current_num))

        self.empty_entry = True
        self.op_press = False
        self.display(self.total)

    def display(self , value):
        self.disply.delete('0' , END)
        self.disply.insert(END , value)

    def delete(self):
        self.disply.get()
        self.disply.delete(len(self.disply.get())-1 , END)
        

    def all_clear(self):
        self.empty_entry=True   
        self.current_num = ''
        self.op_press= False
        self.type_op =''
        self.total = 0
        self.disply.delete('0', END)
        
    
    def equal_btn(self):
        self.current_num =float(self.disply.get())
        if self.op_press:
            self.valid_function()
        else:
            self.total = float(self.disply.get())
        

    def squared(self):
        self.current_num = math.sqrt(float(self.disply.get()))
        self.display(self.current_num)


    def cos(self):
        self.current_num=math.cos(float(self.disply.get()))
        self.display(self.current_num)

    def e(self):
        self.current_num=math.e
        self.display(self.current_num)
    
    def tanh(self):
        self.current_num = math.tanh(float(self.disply.get()))
        self.display(self.current_num)

    def cosh(self):
        self.current_num = math.cosh(float(self.disply.get()))
        self.display(self.current_num)

    def tan(self):
        self.current_num = math.tan(float(self.disply.get()))
        self.display(self.current_num)

    def sin(self):
        self.current_num = math.sin(float(self.disply.get()))
        self.display(self.current_num)

    def sinh(self):
        self.current_num = math.sinh(float(self.disply.get()))
        self.display(self.current_num)

    def log(self):
        self.current_num = math.log10(float(self.disply.get()))
        self.display(self.current_num)

    def atan(self):
        self.current_num = math.atan(float(self.disply.get()))
        self.display(self.current_num)

    def asin(self):
        self.current_num = math.asin(float(self.disply.get()))
        self.display(self.current_num)

    def acos(self):
        self.current_num = math.acos(float(self.disply.get()))
        self.display(self.current_num)

    def acosh(self):
        self.current_num = math.acosh(float(self.disply.get()))
        self.display(self.current_num)

    def asinh(self):
        self.current_num = math.asinh(float(self.disply.get()))
        self.display(self.current_num)
    
    def ln(self):
        self.current_num = math.log(float(self.disply.get()))
        self.display(self.current_num)
    
    def factorial(self):
        self.current_num = math.factorial(int(self.disply.get()))
        self.display(self.current_num)

    def random(self):
        self.current_num = random.uniform(0, 1)
        self.display(self.current_num)

    def Absolute_value(self):
        self.current_num = abs(float(self.disply.get()))
        self.display(self.current_num)

    def pi(self):
        self.current_num = math.pi
        self.display(self.current_num)


    def degrees(self):
        self.current_num = math.degrees(float(self.disply.get()))
        self.display(self.current_num)


    def radians(self):
        self.current_num = math.radians(float(self.disply.get()))
        self.display(self.current_num)

    def gamma(self):
        self.current_num = math.gamma(float(self.disply.get()))
        self.display(self.current_num)


    def trunc(self):
        self.current_num = math.trunc(float(self.disply.get()))
        self.display(self.current_num)



if __name__=='__main__':
    window=Tk()
    window.title('Scientific Calculator')
    window.geometry('410x500')
    window.wm_iconbitmap('img/calculator_icon.ico')

    x=Calculator(window)

    window.mainloop()