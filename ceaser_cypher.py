import tkinter
class A():
    def __init__(self, size, basliq):
       
        self.win=tkinter.Tk()
       
        self.win.geometry(size)
       
        self.win.title(basliq)  
def sifrele():
    metn=[]
    metn=metn_e.get()
    s=''
    for i in metn:
        if i=='z':
            s=s+(chr(ord('a')+3))
        else:     
            s=s+(chr(ord(i)+3))
    netice.insert(0,s)        
def desifrele():
    metn=[]
    metn=metn_e.get()
    d=''
    for i in metn:
        if i=='a':
            d=d+(chr(ord('z')-3))
        else:    
            d=d+(chr(ord(i)-3)) 
    netice.insert(0,d)    
def delete():       
    netice.delete(0, 'end')
    metn_e.delete(0, 'end')
def cixis():
    t.win.destroy()
t=A('400x400', 'Caesar')
metn=tkinter.Label(t.win, text='metni daxil edin: ')
metn.place(x=120, y=0, width=160, height=30)
metn.config(background='black', fg='white', font='arial-12')
metn_e=tkinter.Entry(t.win)
metn_e.place(x=0, y=30, width=400, height=110)
sifrele=tkinter.Button(t.win, text='Sifrele', command=sifrele)
sifrele.place(x=10, y=320, width=60, height=50)
sifrele.config(background='black', fg='white', font='arial-12')
desifrele=tkinter.Button(t.win, text='DeSifrele', command=desifrele)
desifrele.place(x=300, y=320, width=90, height=50)
desifrele.config(background='black', fg='white', font='arial-12')
n2=tkinter.Label(t.win, text='Netice: ')
n2.place(x=120, y=140, width=160, height=30)
n2.config(background='black', fg='white', font='arial-12')
netice=tkinter.Entry(t.win)
netice.place(x=0, y=170, width=409, height=110)
sil=tkinter.Button(t.win, text='Yenile', command=delete)
sil.place(x=170, y=280, width=60, height=40)
sil.config(background='black', fg='white', font='arial-12')
chixish=tkinter.Button(t.win, text='chixish', command=cixis)
chixish.place(x=170, y=340, width=60, height=50)
chixish.config(background='black', fg='white', font='arial-12')
t.win.mainloop()