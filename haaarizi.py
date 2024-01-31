# BY WAEL HARIZI
import tkinter as tk
import webbrowser
window=tk.Tk()
window.title('LSIM1')
window.geometry('780x450')
window.configure(background="#708fa2")
def insta():
    webbrowser.open("https://www.instagram.com/haaarizi?igsh=MzRlODBiNWFlZA==")
def myfunction1():
    exit()

def RES(): 
     try:
         num1 = eval(txtalgebreds.get()) 
         num2 = eval(txtalgebreex.get())
         result1 = num1*0.3 + num2*0.7
         num3 = eval(txtanalyseds.get())  
         num4 = eval(txtanalyseex.get())
         result2 = num3*0.3 + num4*0.7   #You can change the operation as needed

         num5 = eval(txtasdds.get())  
         num6 = eval(txtasdex.get())
         result3 = num5*0.3 + num6*0.7
         num7 = eval(txtprogcds.get())  
         num8 = eval(txtprogcex.get())
         num9 = eval(txtprogctp.get())
         result4 = num7*0.15 + num9*0.15 + num8*0.7

         num10 = eval(txtSEds.get())  
         num11 = eval(txtSEex.get())
         num12 = eval(txtSEtp.get())
         result5 = num10*0.15 + num12*0.15 + num11*0.7
         num13 = eval(txtSYSLOGIQUEds.get())  
         num14 = eval(txtSYSLOGIQUEex.get())
         num15 = eval(txtSYSLOGIQUEtp.get())
         result6 = num13*0.15 + num15*0.15 + num14*0.7

         num16 = eval(txtlfds.get())  
         num17 = eval(txtlfex.get())
         result7 = num16*0.3 + num17*0.7
         num18 = eval(txtMULTIMEDIAds.get())  
         num19 = eval(txtMULTIMEDIAex.get())
         num20 = eval(txtMULTIMEDIAtp.get())
         result8 = num18*0.15 + num20*0.15 + num19*0.7

         num21 = eval(txtanglaisds1.get())  
         num22 = eval(txtanglaisds2.get())
         num23 = eval(txtanglaisoral.get())
         result9 = num21*0.4 + num22*0.4 + num23*0.2
         num24 = eval(txtFRds1.get())  
         num25 = eval(txtFRds2.get())
         num26 = eval(txtFRoral.get())
         result10 = num24*0.4 + num25*0.4 + num26*0.2
         result=(result1*1.5+result2*1.5+result3*2+result4*1.5+result5*1.5+result6*2+result7*1.5+result8*1.5+result9+result10)/15
         #Update the Button with the result
         if result>=10:
             btnRES.config(text=f"{result} MABROUUK")
         else:
             btnRES.config(text=f"{result} GOOD LUCK \U0001F622")
     except (ValueError, SyntaxError):
         # Handle the case where the input is not a valid number
         btnRES.config(text='Please enter valid numbers')


lblalgebreds=tk.Label(text='Algebre DS:',font=('Arial Bold',10),bg='lightgray')
lblalgebreds.grid(pady=5,padx=5,row=0, column=0)
txtalgebreds=tk.Entry(window, width=10)
txtalgebreds.grid(row=0, column=1,pady=5,padx=5)

lblalgebreex=tk.Label(text='Algebre EX:',font=('Arial Bold',10),bg='lightgray')
lblalgebreex.grid(pady=5,padx=5,row=0, column=2)
txtalgebreex=tk.Entry(window, width=10)
txtalgebreex.grid(row=0, column=3,pady=5,padx=5)


lblanalyseds=tk.Label(text='Analyse DS:',font=('Arial Bold',10),bg='lightgray')
lblanalyseds.grid(pady=5,padx=5,row=1, column=0)
txtanalyseds=tk.Entry(window, width=10)
txtanalyseds.grid(row=1, column=1,pady=5,padx=5)

lblanalyseex=tk.Label(text='Analyse EX:',font=('Arial Bold',10),bg='lightgray')
lblanalyseex.grid(pady=5,padx=5,row=1, column=2)
txtanalyseex=tk.Entry(window, width=10)
txtanalyseex.grid(row=1, column=3,pady=5,padx=5)


lblasdds=tk.Label(text='ASD DS:',font=('Arial Bold',10),bg='lightgray')
lblasdds.grid(pady=5,padx=5,row=2, column=0)
txtasdds=tk.Entry(window, width=10)
txtasdds.grid(row=2, column=1,pady=5,padx=5)

lblasdex=tk.Label(text='ASD EX:',font=('Arial Bold',10),bg='lightgray')
lblasdex.grid(pady=5,padx=5,row=2, column=2)
txtasdex=tk.Entry(window, width=10)
txtasdex.grid(row=2, column=3,pady=5,padx=5)


lblprogcds=tk.Label(text='C DS:',font=('Arial Bold',10),bg='lightgray')
lblprogcds.grid(pady=5,padx=5,row=3, column=0)
txtprogcds=tk.Entry(window, width=10)
txtprogcds.grid(row=3, column=1,pady=5,padx=5)

lblprogcex=tk.Label(text='C EX:',font=('Arial Bold',10),bg='lightgray')
lblprogcex.grid(pady=5,padx=5,row=3, column=2)
txtprogcex=tk.Entry(window, width=10)
txtprogcex.grid(row=3, column=3,pady=5,padx=5)

lblprogctp=tk.Label(text='C TP:',font=('Arial Bold',10),bg='lightgray')
lblprogctp.grid(pady=5,padx=5,row=3, column=4)
txtprogctp=tk.Entry(window, width=10)
txtprogctp.grid(row=3, column=5,pady=5,padx=5)


lblSEds=tk.Label(text='SE DS:',font=('Arial Bold',10),bg='lightgray')
lblSEds.grid(pady=5,padx=5,row=4, column=0)
txtSEds=tk.Entry(window, width=10)
txtSEds.grid(row=4, column=1,pady=5,padx=5)

lblSEex=tk.Label(text='SE EX:',font=('Arial Bold',10),bg='lightgray')
lblSEex.grid(pady=5,padx=5,row=4, column=2)
txtSEex=tk.Entry(window, width=10)
txtSEex.grid(row=4, column=3,pady=5,padx=5)

lblSEtp=tk.Label(text='SE TP:',font=('Arial Bold',10),bg='lightgray')
lblSEtp.grid(pady=5,padx=5,row=4, column=4)
txtSEtp=tk.Entry(window, width=10)
txtSEtp.grid(row=4, column=5,pady=5,padx=5)


lblSYSLOGIQUEds=tk.Label(text='SYSLOGIQUE DS:',font=('Arial Bold',10),bg='lightgray')
lblSYSLOGIQUEds.grid(pady=5,padx=5,row=5, column=0)
txtSYSLOGIQUEds=tk.Entry(window, width=10)
txtSYSLOGIQUEds.grid(row=5, column=1,pady=5,padx=5)

lblSYSLOGIQUEex=tk.Label(text='SYSLOGIQUE EX:',font=('Arial Bold',10),bg='lightgray')
lblSYSLOGIQUEex.grid(pady=5,padx=5,row=5, column=2)
txtSYSLOGIQUEex=tk.Entry(window, width=10)
txtSYSLOGIQUEex.grid(row=5, column=3,pady=5,padx=5)

lblSYSLOGIQUEtp=tk.Label(text='SYSLOGIQUE TP:',font=('Arial Bold',10),bg='lightgray')
lblSYSLOGIQUEtp.grid(pady=5,padx=5,row=5, column=4)
txtSYSLOGIQUEtp=tk.Entry(window, width=10)
txtSYSLOGIQUEtp.grid(row=5, column=5,pady=5,padx=5)


lbllfds=tk.Label(text='LOGIQUE FORMELLE DS:',font=('Arial Bold',10),bg='lightgray')
lbllfds.grid(pady=5,padx=5,row=6, column=0)
txtlfds=tk.Entry(window, width=10)
txtlfds.grid(row=6, column=1,pady=5,padx=5)

lbllfex=tk.Label(text='LOGIQUE FORMELLE EX:',font=('Arial Bold',10),bg='lightgray')
lbllfex.grid(pady=5,padx=5,row=6, column=2)
txtlfex=tk.Entry(window, width=10)
txtlfex.grid(row=6, column=3,pady=5,padx=5)


lblMULTIMEDIAds=tk.Label(text='MULTIMEDIA DS:',font=('Arial Bold',10),bg='lightgray')
lblMULTIMEDIAds.grid(pady=5,padx=5,row=7, column=0)
txtMULTIMEDIAds=tk.Entry(window, width=10)
txtMULTIMEDIAds.grid(row=7, column=1,pady=5,padx=5)

lblMULTIMEDIAex=tk.Label(text='MULTIMEDIA EX:',font=('Arial Bold',10),bg='lightgray')
lblMULTIMEDIAex.grid(pady=5,padx=5,row=7, column=2)
txtMULTIMEDIAex=tk.Entry(window, width=10)
txtMULTIMEDIAex.grid(row=7, column=3,pady=5,padx=5)

lblMULTIMEDIAtp=tk.Label(text='MULTIMEDIA TP:',font=('Arial Bold',10),bg='lightgray')
lblMULTIMEDIAtp.grid(pady=5,padx=5,row=7, column=4)
txtMULTIMEDIAtp=tk.Entry(window, width=10)
txtMULTIMEDIAtp.grid(row=7, column=5,pady=5,padx=5)


lblanglaisds1=tk.Label(text='anglais DS1:',font=('Arial Bold',10),bg='lightgray')
lblanglaisds1.grid(pady=5,padx=5,row=8, column=0)
txtanglaisds1=tk.Entry(window, width=10)
txtanglaisds1.grid(row=8, column=1,pady=5,padx=5)

lblanglaisds2=tk.Label(text='anglais DS2:',font=('Arial Bold',10),bg='lightgray')
lblanglaisds2.grid(pady=5,padx=5,row=8, column=2)
txtanglaisds2=tk.Entry(window, width=10)
txtanglaisds2.grid(row=8, column=3,pady=5,padx=5)

lblanglaisoral=tk.Label(text='anglais ORAL:',font=('Arial Bold',10),bg='lightgray')
lblanglaisoral.grid(pady=5,padx=5,row=8, column=4)
txtanglaisoral=tk.Entry(window, width=10)
txtanglaisoral.grid(row=8, column=5,pady=5,padx=5)


lblFRds1=tk.Label(text='FR DS1:',font=('Arial Bold',10),bg='lightgray')
lblFRds1.grid(pady=5,padx=5,row=9, column=0)
txtFRds1=tk.Entry(window, width=10)
txtFRds1.grid(row=9, column=1,pady=5,padx=5)

lblFRds2=tk.Label(text='FR DS2:',font=('Arial Bold',10),bg='lightgray')
lblFRds2.grid(pady=5,padx=5,row=9, column=2)
txtFRds2=tk.Entry(window, width=10)
txtFRds2.grid(row=9, column=3,pady=5,padx=5)

lblFRoral=tk.Label(text='FR ORAL:',font=('Arial Bold',10),bg='lightgray')
lblFRoral.grid(pady=5,padx=5,row=9, column=4)
txtFRoral=tk.Entry(window, width=10)
txtFRoral.grid(row=9, column=5,pady=5,padx=5)

btnRES=tk.Button(text='MOY SEM1',command=RES,font=('Arial Bold',20),bg='#1a4f76',relief=tk.FLAT)
btnRES.grid(row=11, column=2,pady=5,padx=5)

btn1=tk.Button(text='exit',  fg="black",bg="lightblue", command=myfunction1 , padx=10 , pady=3,font=('Arial Bold',15),relief=tk.FLAT)
btn1.grid(row=10, column=0,pady=5,padx=5)

btninsta=tk.Button(text="follow me", command=insta , padx=5, pady=3,font=('Arial Bold',15),bg="lightblue",relief=tk.FLAT)
btninsta.grid(row=10, column=5,pady=5,padx=5)
window.mainloop()


