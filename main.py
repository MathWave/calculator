from tkinter import *
import math

number_on_field = ''
action = ''
number_in_mind = ''
working = False

root = Tk()
root.title('Calculator by MathWave')
root.geometry('280x335')
root.resizable(height=False, width=False)

canvas = Canvas(root, width=270, height=50, bg='black')
canvas.pack(side='top')

########################################################################################################################

btn_control = Button(root, text='off', background='#FF0000')
btn_control.place(x=5, y=60)

btn_sin = Button(root, text='sin')
btn_sin.place(x=60, y=60)

btn_cos = Button(root, text='cos')
btn_cos.place(x=115, y=60)

btn_ln = Button(root, text='ln')
btn_ln.place(x=170, y=60)

btn_devision = Button(root, text='/')
btn_devision.place(x=225, y=60)

btn_pi = Button(root, text='π')
btn_pi.place(x=5, y=115)

btn_seven = Button(root, text='7')
btn_seven.place(x=60, y=115)

btn_eight = Button(root, text='8')
btn_eight.place(x=115, y=115)

btn_nine = Button(root, text='9')
btn_nine.place(x=170, y=115)

btn_multiply = Button(root, text='*')
btn_multiply.place(x=225, y=115)

btn_e = Button(root, text='e')
btn_e.place(x=5, y=170)

btn_four = Button(root, text='4')
btn_four.place(x=60, y=170)

btn_five = Button(root, text='5')
btn_five.place(x=115, y=170)

btn_six = Button(root, text='6')
btn_six.place(x=170, y=170)

btn_minus = Button(root, text='-')
btn_minus.place(x=225, y=170)

btn_power = Button(root, text='xʸ')
btn_power.place(x=5, y=225)

btn_one = Button(root, text='1')
btn_one.place(x=60, y=225)

btn_two = Button(root, text='2')
btn_two.place(x=115, y=225)

btn_three = Button(root, text='3')
btn_three.place(x=170, y=225)

btn_plus = Button(root, text='+')
btn_plus.place(x=225, y=225)

btn_root = Button(root, text='ʸ√x')
btn_root.place(x=5, y=280)

btn_clear = Button(root, text='©')
btn_clear.place(x=60, y=280)

btn_zero = Button(root, text='0')
btn_zero.place(x=115, y=280)

btn_point = Button(root, text='.')
btn_point.place(x=170, y=280)

btn_answer = Button(root, text='=')
btn_answer.place(x=225, y=280)

########################################################################################################################

def Plus():
    if working:
        global number_on_field
        global number_in_mind
        global action
        number_in_mind = number_on_field
        number_on_field = ''
        canvas.delete('all')
        action = 'plus'

def Minus():
    if working:
        global number_on_field
        global number_in_mind
        global action
        number_in_mind = number_on_field
        number_on_field = ''
        canvas.delete('all')
        action = 'minus'

def Multiply():
    if working:
        global number_on_field
        global number_in_mind
        global action
        number_in_mind = number_on_field
        number_on_field = ''
        canvas.delete('all')
        action = 'multiply'

def Devide():
    if working:
        global number_on_field
        global number_in_mind
        global action
        number_in_mind = number_on_field
        number_on_field = ''
        canvas.delete('all')
        action = 'devide'

def Logorithm():
    global working
    if working:
        global number_on_field
        number_on_field = str(math.log(float(number_on_field), math.e))
        if float(number_on_field) == int(float(number_on_field)):
            number_on_field = int(float(number_on_field))
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)


def Cosinus():
    global working
    if working:
        global number_on_field
        number_on_field = str(math.cos(float(number_on_field)))
        if float(number_on_field) == int(float(number_on_field)):
            number_on_field = int(float(number_on_field))
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Sinus():
    global working
    if working:
        global number_on_field
        number_on_field = str(math.sin(float(number_on_field)))
        if float(number_on_field) == int(float(number_on_field)):
            number_on_field = int(float(number_on_field))
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Control():
    global working
    global btn_control
    if working:
        canvas.delete('all')
        global number_on_field
        global action
        global number_in_mind
        number_on_field = ''
        action = ''
        number_in_mind = ''
        btn_control['text'] = 'off'
        btn_control['background'] = '#FF0000'
    else:
        btn_control['text'] = 'on'
        btn_control['background'] = '#00FF00'
    working = 1 - working

def Clear():
    canvas.delete('all')
    global number_on_field
    global action
    global number_in_mind
    number_on_field = ''
    action = ''
    number_in_mind = ''

def Pi():
    global working
    if working:
        global number_on_field
        number_on_field = str(math.pi)
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def E_num():
    global working
    if working:
        global number_on_field
        number_on_field = str(math.e)
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Power():
    if working:
        global number_on_field
        global number_in_mind
        global action
        number_in_mind = number_on_field
        number_on_field = ''
        canvas.delete('all')
        action = 'power'

def Root():
    if working:
        global number_on_field
        global number_in_mind
        global action
        number_in_mind = number_on_field
        number_on_field = ''
        canvas.delete('all')
        action = 'root'

def One():
    global working
    if working:
        global number_on_field
        number_on_field += '1'
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Two():
    global working
    if working:
        global number_on_field
        number_on_field += '2'
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Three():
    global working
    if working:
        global number_on_field
        number_on_field += '3'
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Four():
    global working
    if working:
        global number_on_field
        number_on_field += '4'
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Five():
    global working
    if working:
        global number_on_field
        number_on_field += '5'
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Six():
    global working
    if working:
        global number_on_field
        number_on_field += '6'
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Seven():
    global working
    if working:
        global number_on_field
        number_on_field += '7'
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Eight():
    global working
    if working:
        global number_on_field
        number_on_field += '8'
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Nine():
    global working
    if working:
        global number_on_field
        number_on_field += '9'
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Zero():
    global working
    if working:
        global number_on_field
        number_on_field += '0'
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Point():
    global working
    if working:
        global number_on_field
        number_on_field += '.'
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

def Answer():
    global working
    global number_on_field
    global number_in_mind
    global  action
    if working:
        if action == 'plus':
            number_on_field = float(number_in_mind) + float(number_on_field)
        elif action == 'minus':
            number_on_field = float(number_in_mind) - float(number_on_field)
        elif action == 'multiply':
            number_on_field = float(number_in_mind) * float(number_on_field)
        elif action == 'devide':
            if number_on_field == '0':
                number_on_field = 'ERROR'
            else:
              number_on_field = float(number_in_mind) / float(number_on_field)
        elif action == 'power':
            number_on_field = float(number_in_mind) ** float(number_on_field)
        else:
            number_on_field = float(number_in_mind) ** (1 / float(number_on_field))
        if '.' in str(number_on_field):
            if float(number_on_field) == int(float(number_on_field)):
                number_on_field = int(float(number_on_field))
        number_on_field = str(number_on_field)
        number_in_mind = ''
        canvas.delete('all')
        canvas.create_text(260, 25, width=250, anchor=E, fill="white", text=number_on_field)

########################################################################################################################


btn_control.bind('<Button-1>', lambda event: Control())

btn_sin.bind('<Button-1>', lambda event: Sinus())

btn_cos.bind('<Button-1>', lambda event: Cosinus())

btn_ln.bind('<Button-1>', lambda event: Logorithm())

btn_devision.bind('<Button-1>', lambda event: Devide())

btn_pi.bind('<Button-1>', lambda event: Pi())

btn_seven.bind('<Button-1>', lambda event: Seven())

btn_eight.bind('<Button-1>', lambda event: Eight())

btn_nine.bind('<Button-1>', lambda event: Nine())

btn_multiply.bind('<Button-1>', lambda event: Multiply())

btn_e.bind('<Button-1>', lambda event: E_num())

btn_four.bind('<Button-1>', lambda event: Four())

btn_five.bind('<Button-1>', lambda event: Five())

btn_six.bind('<Button-1>', lambda event: Six())

btn_minus.bind('<Button-1>', lambda event: Minus())

btn_power.bind('<Button-1>', lambda event: Power())

btn_one.bind('<Button-1>', lambda event: One())

btn_two.bind('<Button-1>', lambda event: Two())

btn_three.bind('<Button-1>', lambda event: Three())

btn_plus.bind('<Button-1>', lambda event: Plus())

btn_root.bind('<Button-1>', lambda event: Root())

btn_clear.bind('<Button-1>', lambda event: Clear())

btn_zero.bind('<Button-1>', lambda event: Zero())

btn_point.bind('<Button-1>', lambda event: Point())

btn_answer.bind('<Button-1>', lambda event: Answer())

root.mainloop()
