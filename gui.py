from tkinter import *
from collections import defaultdict
from queue import PriorityQueue
from tkinter import messagebox

data = defaultdict(list)

NutGoc = []
Duyet = [] #Chua cac Node da duyet
N = []
KhoangCach = []
#----------------------------------------------------------------- Best First Search  -----------------------------------------------------------

class Node:
    def __init__(self, name, par = None, h = 0):
        self.name = name
        self.par = par
        self.h = h
    
    def display(self):
        print(self.name, self.h)
        
    def __lt__(self, other):
        if other == None:
            return False
        return self.h < other.h
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.name == other.name        

def equal(O, G):
    if O.name == G.name:
        return True
    return False

def checkInPriority(tmp, c):
    if tmp == None:
        return False
    return (tmp in c.queue)

def getPath(O, distance):
    NutGoc.append(O.name)
    print(O.name)
    distance += O.h
    KhoangCach.append(distance)
    if O.par != None:
        getPath(O.par, distance)
    else:
        print('distance: ', distance)
    return

def BestFS(S = Node('A'), G = Node('N')):
    Duyet.clear()
    NutGoc.clear()
    N.clear()

    Open = PriorityQueue()
    Closed = PriorityQueue()
    S.h = data[S.name][-1]
    Open.put(S)
    while True:
        if Open.empty() == True:
            print('tim kiem that bai')
            messagebox.showinfo("Thong bao","Tim kiem that bai")
            return
        O = Open.get()
        Closed.put(O)
        a = str(O.name) + ' ' + str(O.h)
        Duyet.append(a)
        N.append(O.h)
        print('duyet: ', O.name, O.h)
        if equal(O, G) == True:
            print('Tim kiem thanh cong')
            distance = 0
            getPath(O, distance)
            return
        i = 0
        while i < len(data[O.name]) -1:
            name = data[O.name][i]
            h = data[name][-1]
            
            tmp = Node(name = name, h = h)
            tmp.par = O
            
            ok1 = checkInPriority(tmp, Open)
            ok2 = checkInPriority(tmp, Closed)
            
            if not ok1 and not ok2:
                Open.put(tmp)
            i += 1

#------------------------------------------------------------- Best First Searh ---------------------------------------------------------------

#------------------------------------------------------------------- GUI -----------------------------------------------------------------------

# Them data vao dict
def add_funct(text):
    text_1 = text
    text_1 = text.split(',')
    text_key = text_1[0].upper()
    text_2 = text_1[1]
    text_item = text_2.upper().strip().split(' ')
    data[text_key] = [x for x in text_item]
    data[text_key][-1] = int(data[text_key][-1])
    print(data[text_key])

# Hien thi dict len label
def print_dict():
    lists = []
    for x in data:
        a = str(x) + ': ' + str(data[x])
        lists.append(a)
    data_list = '\n'.join(lists)
    label3['text'] = data_list

# Chay BestFS
def run_funct(text):
    text = text.upper().split(' ')
    BestFS(Node(text[0]), Node(text[1]))
    str_Duyet = []
    for x in Duyet:
        a = 'Duyet: ' + str(x)
        str_Duyet.append(a)
    str_Duyet1 = '\n'.join(str_Duyet)
    label1['text'] = str_Duyet1
    str_NutGoc = ' <-- '.join(NutGoc)
    label2['text'] = str_NutGoc + '     Distance: ' +  str(KhoangCach[-1])

# KHi chon menu Add_dict
def Add_dict():
    frame1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
    frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')
    frame.place_forget()
    lower_frame.place_forget()
# Khi chon menu BestFS
def BFS():
    frame1.place_forget()
    frame2.place_forget()
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')


root = Tk()
root.title('Best First Search')
canvas = Canvas(root, height=500, width=800)
canvas.pack()

bg_img = PhotoImage(file='images/bg_img2.png')
bg_label = Label(root, image=bg_img)
bg_label.place(relwidth=1, relheight=1)


menu = Menu(root)
menu.add_command(label="add dict", command=Add_dict)
menu.add_command(label="BFS", command=BFS)

frame = Frame(root, bg='#3AAACF', bd=5)

frame1 = Frame(root, bg='#3AAACF', bd=5)
frame1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
frame2 = Frame(root, bg='#3AAACF', bd=10)
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')

entry = Entry(frame, font=('courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text ='Run', font=('courier', 18), bg='#06799F', fg='white', command = lambda: run_funct(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = Frame(root, bg='#3AAACF', bd=10)

label1 = Label(lower_frame, font=('courier', 10), anchor='nw', justify='left', bd=4, bg='white', fg='black')
label1.place(relx=0.5, rely=0.02, relwidth=0.8, relheight=0.8, anchor='n')

label2 = Label(lower_frame, font=('courier', 12), anchor='nw', justify='left', bd=4, bg='white', fg='black')
label2.place(relx=0.5, rely=0.85, relwidth=0.8, relheight=0.15, anchor='n')


entry_ = Entry(frame1, font=('courier', 18))
entry_.place(relwidth=0.65, relheight=1)

button1 = Button(frame1, text ='Add', font=('courier', 18), bg='#06799F', fg='white', command = lambda:add_funct(entry_.get()))
button1.place(relx=0.7, relwidth=0.3, relheight=1)

button2 = Button(frame2, text ='Update Dict', font=('courier', 18), bg='#06799F', fg='white', command = lambda:print_dict())
button2.pack(side=BOTTOM)
label3= Label(frame2, text=data, font=('courier', 8), anchor='nw', justify='left', bd=4, bg='white', fg='black')
label3.place(relx=0.5, rely=0.05, relwidth=1, relheight=0.8, anchor='n')
root.config(menu=menu)
root.mainloop()

#------------------------------------------------------------------ GUI -----------------------------------------------------------------------
