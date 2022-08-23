#simple calculator app 
from tkinter import *
from time import sleep
Formula=''
root=Tk()
root.title('Calculator.exe')
root.geometry('500x600')
root.config(bg='#6E6E6E')
root.resizable(False,False)
Display_Label=Label(text='',fg='black',font=('arial',20),bg='#6E6E6E',width=30,height=10,anchor='w',wraplength=480)
Display_Label.place(x=1,y=-35)
Buttons_Frame=Frame(root,bg='#525252',height=700,width=505)
Buttons_Frame.place(x=0,y=190)
#Theme changing function :
dark_light = 0
def change_color():
  global dark_light
  if dark_light==0:
    Buttons_Frame.config(bg="#E6E6E6")
    Display_Label.config(bg="#E6E6E6")
    change_color_btn.config(text="Dark")
    root.config(bg='#E6E6E6')
    dark_light=dark_light+1
  else :
    dark_light=dark_light-1
    Buttons_Frame.config(bg='#525252')
    Display_Label.config(bg='#6E6E6E')
    root.config(bg='#6E6E6E')
    change_color_btn.config(text="Light")
#slide bar for options :
state=0
def slide():
    global state
    if state==1:
        for i in range(150):
            Slide_Frame.place(x=351+i)
            sleep(10**(-350))
            Slide_Frame.update()
        state=state-1
    else:
        for i in range(140):
            Slide_Frame.place(x=490-i,y=29)
            sleep(10**(-350))
            Slide_Frame.update()
        state=state+1
Slide_Frame=Frame(root,width=150,height=2000,bg='#757575')
Slide_Frame.place(x=500,y=29)
#Buttons : 
class Buttons :
    def __init__(self,name,x,y,w,h):
        self.name = name 
        self.x = x
        self.y = y
        self.w=w 
        self.h=h 
    def selected(self):
     try :
        global Formula
        if self.name=="C" :
            Formula=""
        elif self.name =='Rmv':
            if "Sqr" in Formula and Formula.index('Sqr')==len(Formula)-3:
                Formula=Formula[:-3]
            else :
                 Formula=Formula[:-1]
        elif self.name=="=":Formula=Formula.replace('Sqr',"**");Formula=Formula.replace('x',"*");Formula=str(eval(Formula))
        else :
         Formula+=self.name
        Display_Label.config(text=Formula)
     except :
        Display_Label.config(text="Error -_-")
    def make__button(self):
        Funs=Button(Buttons_Frame,relief=FLAT,activebackground='#4A4A4A',activeforeground='#4A4A4A',text=self.name,fg='black',font='arial',bg='#A3A3A3',width=self.w,height=self.h,highlightthickness=6,command=self.selected)
        Funs.place(x=self.x,y=self.y)
        root.bind(str(self.name),lambda event :self.selected())
        if self.name =='Rmv':
         root.bind('<BackSpace>',lambda event :self.selected())
        elif self.name =="=":
         root.bind('<Return>',lambda event :self.selected())
        elif self.name=="C":
         root.bind('<Escape>',lambda event :self.selected())
        elif self.name=="Sqr":
         root.bind('<KP_2>',lambda event :self.selected())
options_btn=Button(root,text="Options",width=10,height=0,command=slide,bg='#757575',relief=FLAT)
options_btn.place(x=417,y=3)

Modulo_btn=Buttons('%',10,10,4,2).make__button()
Clear_btn=Buttons("C",90,10,4,2).make__button()
Sqr_btn=Buttons('Sqr',170,10,4,2).make__button()
Remove_Button=Buttons('Rmv',260,10,4,2).make__button()

Bracket_left=Buttons('(',340,10,4,2).make__button()
Bracket_right=Buttons(')',420,10,4,2).make__button()

Add_Btn=Buttons("+",370,90,8,2).make__button()
Subs_btn=Buttons('-',370,170,8,2).make__button()
Multi_btn=Buttons('x',370,250,8,2).make__button()
Div_btn=Buttons('/',370,330,8,2).make__button()
Equal_btn=Buttons('=',150,330,15,2).make__button()
xs=10
ys=90
counter=0
numbers=[str(i)for i in range(0,10)]
for i in numbers :
    Nms=Buttons(str(i),xs,ys,8,2).make__button()
    counter+=1
    xs+=120
    if counter==3:
       ys+=80
       xs=10
       counter=0
#slide bar options :
change_color_btn=Button(Slide_Frame,relief=FLAT,text="Light",width=10,height=1,bg='white',command=change_color)
change_color_btn.place(x=30,y=40)
root.mainloop()