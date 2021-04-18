from tkinter import *
from tkinter import filedialog
import csv
import clipboard

filename=""
target="Cell size"
debug=""

def Load():
    global filename
    global text
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("csv files", "*.csv"),
                                          ("all files", "*.*")))
    text1=Text(root,width=18, height=4)
    text1.place(x=40,y=85)
    text1.insert(END,filename)
    
    text.configure(state='normal')
    text.delete("1.0","end")
    text.configure(state='disabled')
    
def show_index():
    global debug
    debug="y"
def unshow_index():
    global debug
    debug="n"

def sort_size():
    global text
    global filename
    global target
    global debug
    try :
        f = open(filename, 'r', encoding='utf-8')
        rdr = csv.reader(f)
        
    except:
        text2.insert(END,"file name error"+"\n")
        rdr=[]
    
    text.configure(state='normal')
    text.delete("1.0","end")

    text2=Text(root,width=18, height=10)
    text2.place(x=40,y=230)
    
    
    pr=0
    count={}
    size=[]
    expt=[]
    
    for line in rdr:
        if target in line:
            pr=1
            idx=line.index(target)
        elif line==[] or '':
            pr=0
        else:
            pass
        if pr==1:
            if line[idx]=='':
                pass
            elif target == line[idx]:
                pass
            elif not target == line[idx]:
                try : size.append(int(float(line[idx])))
                except : expt.append(line[idx])
            else:
                expt.append(line[idx])
    try: f.close()
    except: text2.insert(END,"file doesn't opened correctly"+"\n")
    size.sort()
    for i in size:
        try: count[i] += 1
        except: count[i]=1
    s=0
    for i in range (90):
        if debug=='y':
            try:
                text.insert(END,i+1)
                text.insert(END,":")
                text.insert(END,count[i+1])
                text.insert(END,"\n")
                s=s+count[i+1]
            except :
                text.insert(END,0)
                text.insert(END,"\n")
        else:        
            try:
                text.insert(END,count[i+1])
                text.insert(END,"\n")
                s=s+count[i+1]
            except :
                text.insert(END,0)
                text.insert(END,"\n")
                
    text.configure(state='disabled')

    if not s==len(size):
        text2.insert(END,"error : total counted size doesn't match"+"\n")
    elif not expt==[]:
        text2.insert(END,"counting is unsuccesfully completed."+"\n")
        text2.insert(END,"there is an exception"+"\n")
        text2.insert(END,"total counted :"+str(s)+"\n")
        text2.insert(END,"===== this is an excption list start ====="+"\n")

        for i in expt:
            text2.insert(END,str(i)+"\n")
            pass

        text2.insert(END,"===== this is an excption list end ====="+"\n")
    else:
        text2.insert(END,"counting is succesfully completed."+"\n")
        text2.insert(END,"total counted :"+str(s)+"\n")
    text2.configure(state='disabled')
 
    

def copy():
    global text
    clipboard.copy(text.get("1.0", "end"))

def change_target():
    pass
        
root = Tk()

root.geometry("300x400")

btn1 = Button(root, text='sort start',command=sort_size) 
btn3 = Button(root, text='open file',command=Load) 
btn4 = Button(root, text='change target string',command=change_target)
btn2 = Button(root, text='copy',command=copy) 

r1 = Radiobutton(root, text = "show index", value = 1,command=show_index)
r2 = Radiobutton(root, text = "unshow index", value = 2,command=unshow_index)  

text = Text(root)

label1=Label(root, text="target string: "+target)
label1.place(x=170,y=3)


"""
btn1.pack(side='bottom',fill='x')
btn2.pack(side='right') 
btn3.pack(side='top',fill='x')
btn4.pack(side='top') 
r1.pack(side='left')
r2.pack(side='top')
text.pack(side='right')
"""
btn1.place(x=25,y=175)#sort
btn2.place(x=230,y=370)#copy
btn3.place(x=25,y=50)#open
btn4.place(x=180,y=20)#change

r1.place(x=100,y=160)
r2.place(x=100,y=190)

text.place(x=200,y=50)#


text.configure(state='disabled')
root.mainloop()
