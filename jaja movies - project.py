import webbrowser
from tkinter import *

v = Tk()
v.title("jaja movies")
v.geometry("992x992+230+70")

j = Label(v, text="Hello user welcome to jaja movies. How much are you?", font=("Arial", 17))
j.pack()

def p():
    if uuuu.get() == 2:
        v.destroy()
        tyyyy()
    if uuuu.get() == 3:
        v.destroy()
        tyyyy()
    if uuuu.get() == 4:
        v.destroy()
        tyyyy()
    if uuuu.get() == 5:
        v.destroy()
        tyyyy()
    if uuuu.get() == 6:
        v.destroy()
        tyyyy()
    if uuuu.get() == 7:
        v.destroy()
        tyyyy()
    if uuuu.get() == 8:
        v.destroy()
        tyyyy()
    else:
        v.destroy()
        print("sorry theres only 8 chairs aviable please come tommorow")


    
    
def shjp():

    webbrowser.open("https://youtu.be/g6fMwBP1MfU")


def tyyyy():
    whu = Tk()
    whu.title("movie picker jaja")
    whu.geometry("992x992+230+70")

    def jhp():
        if ploploplou.get() == 1822:
            whu.destroy()

            otherthing = Tk()
            otherthing.title("food in the movie")
            otherthing.geometry("992x992+230+70")


            def ramom():
                if drop.get() == 2621:
                    otherthing.destroy()

                    garon = Tk()
                    garon.title("checkout")
                    garon.geometry("992x992+230+70")

                    ttd = Label(garon, text="it cost 7 shekel")
                    ttd.pack()

                    rr = Button(garon, text =" pay and go to then movie", command=shjp)
                    rr.pack()

                    garon.mainloop()

                elif drop.get() == 68457:
                
                    webbrowser.open("https://youtu.be/g6fMwBP1MfU")


                elif drop.get() == 4:
                    otherthing.destroy()

                    garo8n = Tk()
                    garo8n.title("checkout")
                    garo8n.geometry("992x992+230+70")

                    tt7d = Label(garo8n, text="it cost 15 shekel")
                    tt7d.pack()

                    r8r = Button(garo8n, text =" pay and go to then movie", command=shjp)
                    r8r.pack()


                elif drop.get() == 24:
                    otherthing.destroy()

                    garo88n = Tk()
                    garo88n.title("checkout")
                    garo88n.geometry("992x992+230+70")

                    tt87d = Label(garo88n, text="it cost 7.90 shekel")
                    tt87d.pack()

                    r888r = Button(garo88n, text =" pay and go to then movie", command=shjp)
                    r888r.pack()
                    

                











            tu = Label(otherthing, text="do you want food while watching?")
            tu.pack()


            drop = IntVar()
            drop.set(None)

            sssp = Radiobutton(otherthing, text="water,  7 shekel",value=2621, variable=drop)
            sssp.pack()

            sese = Radiobutton(otherthing, text="coca cola, 7.90 shekel",value=24, variable=drop)
            sese.pack()

            sdro = Radiobutton(otherthing, text="popcorn, 15 shekel", value=4, variable=drop)
            sdro.pack()

            
            sdr61o = Radiobutton(otherthing, text="nothing", value=68457, variable=drop)
            sdr61o.pack()


            han = Button(otherthing, text="next", command=ramom)
            han.pack()




            





            otherthing.mainloop()
    
    
    troo = Label(whu, text="what movie do you want to watch")
    troo.pack()

    ploploplou = IntVar()
    ploploplou.set(None)

    caropp1 = Radiobutton(whu, text="garfield", value=1822, variable=ploploplou)
    caropp1.pack()
    g = Label(whu, text="there is only 1 movie aviable")
    g.pack()
    hj = Button(whu, text="enter", command=jhp)
    hj.pack()
    whu.mainloop()








uuuu = IntVar()
uuuu.set(None)


uu = Radiobutton(v, text="2", value=2, variable=uuuu)
uu.pack()
uu1q1 = Radiobutton(v, text="3", value=3, variable=uuuu)
uu1q1.pack()
uu1111 = Radiobutton(v, text="4", value=4, variable=uuuu)
uu1111.pack()
uu1q2 = Radiobutton(v, text="5", value=5, variable=uuuu)
uu1q2.pack()
uu1 = Radiobutton(v, text="6", value=6, variable=uuuu)
uu1.pack()
uu1q1111 = Radiobutton(v, text="7", value=7, variable=uuuu)
uu1q1111.pack()
puu = Radiobutton(v, text="8", value=8, variable=uuuu)
puu.pack()
u111u = Radiobutton(v, text="9", value=21, variable=uuuu)
u111u.pack()
uu1q1 = Radiobutton(v, text="10", value=31, variable=uuuu)
uu1q1.pack()

tyo = Button(v, text="enter", command=p)
tyo.pack()

v.mainloop()


