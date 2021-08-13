from tkinter import*                                     
from tkinter import filedialog,messagebox
import random
import time
import requests


# Functions


def reset():                                   ##this is function of reset button I mean all reset button work
   textReceipt.delete(1.0,END)

   e_roti.set('0')
   e_daal.set('0')
   e_fish.set('0')
   e_egg.set('0')
   e_chicken.set('0')
   e_mutton.set('0')
   e_biryani.set('0')
   e_paneer.set('0')
   e_chawal.set('0')


   e_lassi.set('0')
   e_coffee.set('0')
   e_tea.set('0')
   e_milk.set('0')
   e_faluda.set('0')
   e_jaljeera.set('0')
   e_roohafza.set('0')
   e_masalatak.set('0')
   e_cocacola.set('0')


   e_oreo.set('0')
   e_apple.set('0')
   e_kitkat.set('0')
   e_vanilla.set('0')
   e_banana.set('0')
   e_pista.set('0')
   e_pineapple.set('0')
   e_chocolate.set('0')
   e_blackforest.set('0')

   textroti.config(state=DISABLED)
   textdaal.config(state=DISABLED)
   textfish.config(state=DISABLED)
   textegg.config(state=DISABLED)
   textchicken.config(state=DISABLED)
   textmutton.config(state=DISABLED)
   textbiryani.config(state=DISABLED)
   textpaneer.config(state=DISABLED)
   textchawal.config(state=DISABLED)

   textlassi.config(state=DISABLED)
   textcoffee.config(state=DISABLED)
   texttea.config(state=DISABLED)
   textmilk.config(state=DISABLED)
   textfaluda.config(state=DISABLED)
   textjaljeera.config(state=DISABLED)
   textroohafza.config(state=DISABLED)
   textmasalatak.config(state=DISABLED)
   textcocacola.config(state=DISABLED)

   textoreo.config(state=DISABLED)
   textapple.config(state=DISABLED)
   textkitkat.config(state=DISABLED)
   textvanilla.config(state=DISABLED)
   textbanana.config(state=DISABLED)
   textpista.config(state=DISABLED)
   textpineapple.config(state=DISABLED)
   textchocolate.config(state=DISABLED)
   textblackforest.config(state=DISABLED)

   var1.set(0)
   var2.set(0)
   var3.set(0)
   var4.set(0)
   var5.set(0)
   var6.set(0)
   var7.set(0)
   var8.set(0)
   var9.set(0)
   var10.set(0)
   var11.set(0)
   var12.set(0)
   var13.set(0)
   var14.set(0)
   var15.set(0)
   var16.set(0)
   var17.set(0)
   var18.set(0)
   var19.set(0)
   var20.set(0)
   var21.set(0)
   var22.set(0)
   var23.set(0)
   var24.set(0)
   var25.set(0)
   var26.set(0)
   var27.set(0)
   costofdrinksvar.set('')
   costoffoodvar.set('')
   costofcakesvar.set('')
   subtotalvar.set('')
   servicetaxvar.set('')
   totalcostvar.set('')



def send():                                           ##this is function of send button I mean all Send button work
   if textReceipt.get(1.0,END)=='\n':
      pass
   else:
      def send_msg():
         message=textarea.get(1.0,END)
         number=numberfield.get()
         auth='EAC43FbwDuih1nmr9aPYIsBSRLZVfU8TtzokeJK6l7NpcHXMqxMgZzD7mScxyFbT6lo1WKGaLhQY5J2O'
         url = "https://www.fast2sms.com/dev/bulkV2"
         querystring = {"authorization":"EAC43FbwDuih1nmr9aPYIsBSRLZVfU8TtzokeJK6l7NpcHXMqxMgZzD7mScxyFbT6lo1WKGaLhQY5J2O","message":message,"language":"english","route":"q","numbers":number}
         headers = {
                 'cache-control': "no-cache"
                   }
         response = requests.request("GET", url, headers=headers, params=querystring)
         print(response.text)

         
         dic=response.json()
         result=dic.get('return')
         if result==True:
            messagebox.showinfo('Send Successfully','Message Send Successfully')

         else:
            messagebox.showerror('Error','Something went wrong')
            

                                
      root2=Toplevel()

      root2.title=("SEND BILL")
      root2.config(bg="#0C89FE")
      root2.geometry('485x620+50+50')


      logoImage=PhotoImage(file='sender.png')
      label=Label(root2,image=logoImage,bg='#0C89FE')
      label.pack()

      numberLabel=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='#0C89FE',fg='white')
      numberLabel.pack(pady=4)

      numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=4,width=24)
      numberfield.pack(pady=4)

      billLabel=Label(root2,text='Bill Details',font=('arial',18,'bold underline'),bg='#0C89FE',fg='white')
      billLabel.pack(pady=4)

      textarea=Text(root2,font=('arial',12,'bold'),bd=4,width=42,height=14)
      textarea.pack(pady=4)

      sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='White',fg='blue4',bd=7,relief=GROOVE,command=send_msg)
      sendButton.pack(pady=5)

      textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')

      if costoffoodvar.get()!='0 Rs':
         textarea.insert(END,f'Cost Of Food\t\t\t{priceofFood}Rs\n')
      if costofdrinksvar.get()!='0 Rs':
         textarea.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n')
      if costofcakesvar.get()!='0 Rs':
         textarea.insert(END,f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n')

      textarea.insert(END,f'Sub Total\t\t\t{subtotalofItems}Rs\n')
      textarea.insert(END,f'Service Tax\t\t\t{50}Rs\n')
      textarea.insert(END,'***************************************************************\n')
      textarea.insert(END,f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')
      

      root2.mainloop()







def save():                                           ##this is function of Save button I mean all save button work
   if textReceipt.get(1.0,END)=='\n':
      pass
   else:
      url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
      if url==None:
         pass
      else:
         bill_data=textReceipt.get(1.0,END)
         url.write(bill_data)
         url.close()
         messagebox.showinfo("Information","Your Bill Successfully Saved")
   



def receipt():                                     ##this is function of receipt button I mean all receipt button work
   if costoffoodvar.get() !='' or costofdrinksvar.get() !='' or costofcakesvar.get() !='':
      global billnumber,date
      textReceipt.delete(1.0,END)
      x=random.randint(100,10000)
      billnumber='BILL'+str(x)
      date=time.strftime('%d/%m/%Y')
      textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
      textReceipt.insert(END,'***************************************************************\n')
      textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
      textReceipt.insert(END,'***************************************************************\n')
      if e_roti.get()!='0':
         textReceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*10}\n\n')

      if e_daal.get()!='0':
         textReceipt.insert(END,f'Daal\t\t\t{int(e_daal.get())*80}\n\n')

      if e_fish.get()!='0':
         textReceipt.insert(END,f'Fish\t\t\t{int(e_fish.get())*180}\n\n')

      if e_egg.get()!='0':
         textReceipt.insert(END,f'Egg\t\t\t{int(e_egg.get())*90}\n\n')

      if e_chicken.get()!='0':
         textReceipt.insert(END,f'Chicken\t\t\t{int(e_chicken.get())*210}\n\n')

      if e_mutton.get()!='0':
         textReceipt.insert(END,f'Mutton\t\t\t{int(e_mutton.get())*250}\n\n')

      if e_biryani.get()!='0':
         textReceipt.insert(END,f'Biryani\t\t\t{int(e_biryani.get())*140}\n\n')

      if e_paneer.get()!='0':
         textReceipt.insert(END,f'Paneer\t\t\t{int(e_paneer.get())*80}\n\n')

      if e_chawal.get()!='0':
         textReceipt.insert(END,f'Chawal\t\t\t{int(e_chawal.get())*40}\n\n')

      if e_lassi.get()!='0':
         textReceipt.insert(END,f'Lassi\t\t\t{int(e_lassi.get())*30}\n\n')

      if e_coffee.get()!='0':
         textReceipt.insert(END,f'Coffee\t\t\t{int(e_coffee.get())*10}\n\n')

      if e_tea.get()!='0':
         textReceipt.insert(END,f'Tea\t\t\t{int(e_tea.get())*10}\n\n')

      if e_milk.get()!='0':
         textReceipt.insert(END,f'Milk\t\t\t{int(e_milk.get())*20}\n\n')

      if e_faluda.get()!='0':
         textReceipt.insert(END,f'Faluda\t\t\t{int(e_faluda.get())*40}\n\n')

      if e_jaljeera.get()!='0':
         textReceipt.insert(END,f'Jaljeera\t\t\t{int(e_jaljeera.get())*20}\n\n')

      if e_roohafza.get()!='0':
         textReceipt.insert(END,f'Roohafza\t\t\t{int(e_roohafza.get())*20}\n\n')

      if e_masalatak.get()!='0':
         textReceipt.insert(END,f'Masala Tak\t\t\t{int(e_masalatak.get())*15}\n\n')

      if e_cocacola.get()!='0':
         textReceipt.insert(END,f'Coca-Cola\t\t\t{int(e_cocacola.get())*30}\n\n')

      if e_oreo.get()!='0':
         textReceipt.insert(END,f'Oreo\t\t\t{int(e_oreo.get())*250}\n\n')

      if e_apple.get()!='0':
         textReceipt.insert(END,f'Apple\t\t\t{int(e_apple.get())*240}\n\n')

      if e_kitkat.get()!='0':
         textReceipt.insert(END,f'Kitkat\t\t\t{int(e_kitkat.get())*260}\n\n')

      if e_vanilla.get()!='0':
         textReceipt.insert(END,f'Vanilla\t\t\t{int(e_vanilla.get())*270}\n\n')

      if e_banana.get()!='0':
         textReceipt.insert(END,f'Banana\t\t\t{int(e_banana.get())*280}\n\n')

      if e_pista.get()!='0':
         textReceipt.insert(END,f'Pista\t\t\t{int(e_pista.get())*270}\n\n')

      if e_pineapple.get()!='0':
         textReceipt.insert(END,f'Pineapple\t\t\t{int(e_pineapple.get())*260}\n\n')

      if e_chocolate.get()!='0':
         textReceipt.insert(END,f'Chocolate\t\t\t{int(e_chocolate.get())*290}\n\n')

      if e_blackforest.get()!='0':
         textReceipt.insert(END,f'Black Forest\t\t\t{int(e_blackforest.get())*300}\n\n')

      textReceipt.insert(END,'***************************************************************\n')

      if costoffoodvar.get()!='0 Rs':
         textReceipt.insert(END,f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
      if costoffoodvar.get()!='0 Rs':
         textReceipt.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
      if costoffoodvar.get()!='0 Rs':
         textReceipt.insert(END,f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')

      textReceipt.insert(END,f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
      
      textReceipt.insert(END,f'Service Tax\t\t\t{50}Rs\n\n')
      textReceipt.insert(END,'***************************************************************\n')
      textReceipt.insert(END,f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')

   else:
      messagebox.showerror("Error","No ! Item is Selected")

   
   

   


   
      
   





def totalcost():                                ##this is function of total cost label I mean all total cost label working
   global priceofFood,priceofDrinks,priceofCakes,subtotalofItems
   if var1.get()!=0 or var2.get()!=0 or var3.get()!=0 or var4.get()!=0 or var5.get()!=0 or var6.get()!=0 \
      or var7.get()!=0 or var8.get()!=0 or var9.get()!=0 or var10.get()!=0 or var11.get()!=0 or var12.get()!=0 \
      or var13.get()!=0 or var14.get()!=0 or var15.get()!=0 or var16.get()!=0 or var17.get()!=0 or var18.get()!=0 \
      or var19.get()!=0 or var20.get()!=0 or var21.get()!=0 or var22.get()!=0 or var23.get()!=0 or var24.get()!=0 \
      or var25.get()!=0 or var26.get()!=0 or var27.get()!=0:
      
      item1=int(e_roti.get())
      item2=int(e_daal.get())
      item3=int(e_fish.get())
      item4=int(e_egg.get())
      item5=int(e_chicken.get())
      item6=int(e_mutton.get())
      item7=int(e_biryani.get())
      item8=int(e_paneer.get())
      item9=int(e_chawal.get())


      item10=int(e_lassi.get())
      item11=int(e_coffee.get())
      item12=int(e_tea.get())
      item13=int(e_milk.get())
      item14=int(e_faluda.get())
      item15=int(e_jaljeera.get())
      item16=int(e_roohafza.get())
      item17=int(e_masalatak.get())
      item18=int(e_cocacola.get())


      item19=int(e_oreo.get())
      item20=int(e_apple.get())
      item21=int(e_kitkat.get())
      item22=int(e_vanilla.get())
      item23=int(e_banana.get())
      item24=int(e_pista.get())
      item25=int(e_pineapple.get())
      item26=int(e_chocolate.get())
      item27=int(e_blackforest.get())



      priceofFood=(item1*10)+(item2*80)+(item3*180)+(item4*90)+(item5*210)+(item6*250)+(item7*140)+(item8*80)+(item9*40)


      priceofDrinks=(item10*30)+(item11*10)+(item12*10)+(item13*20)+(item14*40)+(item15*20)+(item16*20)+(item17*15)+(item18*30)


      priceofCakes=(item19*250)+(item20*240)+(item21*260)+(item22*270)+(item23*280)+(item24*270)+(item25*260)+(item26*290)+(item27*300)


      costoffoodvar.set(str(priceofFood)+' Rs')
      costofdrinksvar.set(str(priceofDrinks)+' Rs')
      costofcakesvar.set(str(priceofCakes)+' Rs')




      subtotalofItems=priceofFood+priceofDrinks+priceofCakes
      subtotalvar.set(str(subtotalofItems)+' Rs')


      servicetaxvar.set('50 Rs')

      tottalcost=subtotalofItems+50
      totalcostvar.set(str(tottalcost)+' Rs')
   else:
      messagebox.showerror("Error","No ! Item is Selected")

   


   


def roti():
   if var1.get()==1:
      textroti.config(state=NORMAL)
      textroti.delete(0,END)
      textroti.focus()
   else:
      textroti.config(state=DISABLED)
      e_roti.set('0') 


def daal():
   if var2.get()==1:
      textdaal.config(state=NORMAL)
      textdaal.delete(0,END)
      textdaal.focus()
   else:
      textdaal.config(state=DISABLED)
      e_daal.set('0')


def fish():
   if var3.get()==1:
      textfish.config(state=NORMAL)
      textfish.delete(0,END)
      textfish.focus()
   else:
      textfish.config(state=DISABLED)
      e_fish.set('0')


def egg():
   if var4.get()==1:
      textegg.config(state=NORMAL)
      textegg.delete(0,END)
      textegg.focus()
   else:
      textegg.config(state=DISABLED)
      e_egg.set('0')


def chicken():
   if var5.get()==1:
      textchicken.config(state=NORMAL)
      textchicken.delete(0,END)
      textchicken.focus()
   else:
      textchicken.config(state=DISABLED)
      e_chicken.set('0')


def mutton():
   if var6.get()==1:
      textmutton.config(state=NORMAL)
      textmutton.delete(0,END)
      textmutton.focus()
   else:
      textmutton.config(state=DISABLED)
      e_mutton.set('0')


def biryani():
   if var7.get()==1:
      textbiryani.config(state=NORMAL)
      textbiryani.delete(0,END)
      textbiryani.focus()
   else:
      textbiryani.config(state=DISABLED)
      e_biryani.set('0')


def paneer():
   if var8.get()==1:
      textpaneer.config(state=NORMAL)
      textpaneer.delete(0,END)
      textpaneer.focus()
   else:
      textpaneer.config(state=DISABLED)
      e_paneer.set('0')


def chawal():
   if var9.get()==1:
      textchawal.config(state=NORMAL)
      textchawal.delete(0,END)
      textchawal.focus()
   else:
      textchawal.config(state=DISABLED)
      e_chawal.set('0')

def lassi():
   if var10.get()==1:
      textlassi.config(state=NORMAL)
      textlassi.delete(0,END)
      textlassi.focus()
   else:
      textlassi.config(state=DISABLED)
      e_lassi.set('0')

def coffee():
   if var11.get()==1:
      textcoffee.config(state=NORMAL)
      textcoffee.delete(0,END)
      textcoffee.focus()
   else:
      textcoffee.config(state=DISABLED)
      e_coffee.set('0')


def tea():
   if var12.get()==1:
      texttea.config(state=NORMAL)
      texttea.delete(0,END)
      texttea.focus()
   else:
      texttea.config(state=DISABLED)
      e_tea.set('0')


def milk():
   if var13.get()==1:
      textmilk.config(state=NORMAL)
      textmilk.delete(0,END)
      textmilk.focus()
   else:
      textmilk.config(state=DISABLED)
      e_milk.set('0')


def faluda():
   if var14.get()==1:
      textfaluda.config(state=NORMAL)
      textfaluda.delete(0,END)
      textfaluda.focus()
   else:
      textfaluda.config(state=DISABLED)
      e_faluda.set('0')


def jaljeera():
   if var15.get()==1:
      textjaljeera.config(state=NORMAL)
      textjaljeera.delete(0,END)
      textjaljeera.focus()
   else:
      textjaljeera.config(state=DISABLED)
      e_jaljeera.set('0')


def roohafza():
   if var16.get()==1:
      textroohafza.config(state=NORMAL)
      textroohafza.delete(0,END)
      textroohafza.focus()
   else:
      textroohafza.config(state=DISABLED)
      e_roohafza.set('0')



def masalatak():
   if var17.get()==1:
      textmasalatak.config(state=NORMAL)
      textmasalatak.delete(0,END)
      textmasalatak.focus()
   else:
      textmasalatak.config(state=DISABLED)
      e_masalatak.set('0')


def cocacola():
   if var18.get()==1:
      textcocacola.config(state=NORMAL)
      textcocacola.delete(0,END)
      textcocacola.focus()
   else:
      textcocacola.config(state=DISABLED)
      e_cocacola.set('0')


def oreo():
   if var19.get()==1:
      textoreo.config(state=NORMAL)
      textoreo.delete(0,END)
      textoreo.focus()
   else:
      textoreo.config(state=DISABLED)
      e_oreo.set('0')


def apple():
   if var20.get()==1:
      textapple.config(state=NORMAL)
      textapple.delete(0,END)
      textapple.focus()
   else:
      textapple.config(state=DISABLED)
      e_apple.set('0')


def kitkat():
   if var21.get()==1:
      textkitkat.config(state=NORMAL)
      textkitkat.delete(0,END)
      textkitkat.focus()
   else:
      textkitkat.config(state=DISABLED)
      e_kitkat.set('0')


def vanilla():
   if var22.get()==1:
      textvanilla.config(state=NORMAL)
      textvanilla.delete(0,END)
      textvanilla.focus()
   else:
      textvanilla.config(state=DISABLED)
      e_vanilla.set('0')


def banana():
   if var23.get()==1:
      textbanana.config(state=NORMAL)
      textbanana.delete(0,END)
      textbanana.focus()
   else:
      textbanana.config(state=DISABLED)
      e_banana.set('0')


def pista():
   if var24.get()==1:
      textpista.config(state=NORMAL)
      textpista.delete(0,END)
      textpista.focus()
   else:
      textpista.config(state=DISABLED)
      e_pista.set('0')



def pineapple():
   if var25.get()==1:
      textpineapple.config(state=NORMAL)
      textpineapple.delete(0,END)
      textpineapple.focus()
   else:
      textpineapple.config(state=DISABLED)
      e_pineapple.set('0')




def chocolate():
   if var26.get()==1:
      textchocolate.config(state=NORMAL)
      textchocolate.delete(0,END)
      textchocolate.focus()
   else:
      textchocolate.config(state=DISABLED)
      e_chocolate.set('0')



def blackforest():
   if var27.get()==1:
      textblackforest.config(state=NORMAL)
      textblackforest.delete(0,END)
      textblackforest.focus()
   else:
      textblackforest.config(state=DISABLED)
      e_blackforest.set('0')







root=Tk()                  ##window


root.geometry('1270x690+0+0')         ##window size
root.resizable(0,0)


root.title("Restaurant Management System")    ##Window Title
root.config(bg="firebrick3")


######################

topFrame=Frame(root,bd=10,relief=RIDGE,bg="green")
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text="Restaurant Billing System",font=("Times New Roman",30,"bold"),fg="yellow",bd=9,bg="red4",width=51)
labelTitle.grid(row=0,column=0)

######################################

#Frames

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg="Yellow",pady=10)
costFrame.pack(side=BOTTOM)


foodFrame=LabelFrame(menuFrame,text="Food",font=('arial',19,"bold"),bd=10,relief=RIDGE,fg='green')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text="Drinks",font=('arial',19,"bold"),bd=10,relief=RIDGE,fg='green')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text="Cakes",font=('arial',19,"bold"),bd=10,relief=RIDGE,fg='green')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg="red4")
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg="red4")
calculatorFrame.pack()

receiptFrame=Frame(rightFrame,bd=2,relief=RIDGE,bg="red4")
receiptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg="Yellow")
buttonFrame.pack()


#Variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()


#variable for food

e_roti=StringVar()
e_daal=StringVar()
e_fish=StringVar()
e_egg=StringVar()
e_chicken=StringVar()
e_mutton=StringVar()
e_biryani=StringVar()
e_paneer=StringVar()
e_chawal=StringVar()


#variables for drinks

e_lassi=StringVar()
e_coffee=StringVar()
e_tea=StringVar()
e_milk=StringVar()
e_faluda=StringVar()
e_jaljeera=StringVar()
e_roohafza=StringVar()
e_masalatak=StringVar()
e_cocacola=StringVar()

#variables for Cakes

e_oreo=StringVar()
e_apple=StringVar()
e_kitkat=StringVar()
e_vanilla=StringVar()
e_banana=StringVar()
e_pista=StringVar()
e_pineapple=StringVar()
e_chocolate=StringVar()
e_blackforest=StringVar()

#variables for cost

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()


# Zero keli sarvanchi value

e_roti.set('0')
e_daal.set('0')
e_fish.set('0')
e_egg.set('0')
e_chicken.set('0')
e_mutton.set('0')
e_biryani.set('0')
e_paneer.set('0')
e_chawal.set('0')


e_lassi.set('0')
e_coffee.set('0')
e_tea.set('0')
e_milk.set('0')
e_faluda.set('0')
e_jaljeera.set('0')
e_roohafza.set('0')
e_masalatak.set('0')
e_cocacola.set('0')


e_oreo.set('0')
e_apple.set('0')
e_kitkat.set('0')
e_vanilla.set('0')
e_banana.set('0')
e_pista.set('0')
e_pineapple.set('0')
e_chocolate.set('0')
e_blackforest.set('0')




#Food

roti=Checkbutton(foodFrame,text="Roti",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(foodFrame,text="Daal",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var2,command=daal)
daal.grid(row=1,column=0,sticky=W)

fish=Checkbutton(foodFrame,text="Fish",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var3,command=fish)
fish.grid(row=2,column=0,sticky=W)

egg=Checkbutton(foodFrame,text="Egg",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var4,command=egg)
egg.grid(row=3,column=0,sticky=W)

chicken=Checkbutton(foodFrame,text="Chicken",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var5,command=chicken)
chicken.grid(row=4,column=0,sticky=W)

muttton=Checkbutton(foodFrame,text="Mutton",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var6,command=mutton)
muttton.grid(row=5,column=0,sticky=W)

biryani=Checkbutton(foodFrame,text="Biryani",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var7,command=biryani)
biryani.grid(row=6,column=0,sticky=W)

paneer=Checkbutton(foodFrame,text="Paneer",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var8,command=paneer)
paneer.grid(row=7,column=0,sticky=W)

chawal=Checkbutton(foodFrame,text="Chawal",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var9,command=chawal)
chawal.grid(row=8,column=0,sticky=W)



# Entry Box For Food Items

textroti=Entry(foodFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(foodFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textfish=Entry(foodFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)

textegg=Entry(foodFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_egg)
textegg.grid(row=3,column=1)

textchicken=Entry(foodFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=4,column=1)

textmutton=Entry(foodFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_mutton)
textmutton.grid(row=5,column=1)

textbiryani=Entry(foodFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_biryani)
textbiryani.grid(row=6,column=1)

textpaneer=Entry(foodFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=7,column=1)

textchawal=Entry(foodFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_chawal)
textchawal.grid(row=8,column=1)



##################
# Drinks

lassi=Checkbutton(drinksFrame,text="Lassi",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var10,command=lassi)
lassi.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text="Coffee",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var11,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

tea=Checkbutton(drinksFrame,text="Tea",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var12,command=tea)
tea.grid(row=2,column=0,sticky=W)

milk=Checkbutton(drinksFrame,text="Milk",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var13,command=milk)
milk.grid(row=3,column=0,sticky=W)

faluda=Checkbutton(drinksFrame,text="Faluda",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var14,command=faluda)
faluda.grid(row=4,column=0,sticky=W)

jaljeera=Checkbutton(drinksFrame,text="Jaljeera",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var15,command=jaljeera)
jaljeera.grid(row=5,column=0,sticky=W)

roohafza=Checkbutton(drinksFrame,text="Roohafza",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var16,command=roohafza)
roohafza.grid(row=6,column=0,sticky=W)

masalatak=Checkbutton(drinksFrame,text="Masala Tak",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var17,command=masalatak)
masalatak.grid(row=7,column=0,sticky=W)

cocacola=Checkbutton(drinksFrame,text="Coca-Cola",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var18,command=cocacola)
cocacola.grid(row=8,column=0,sticky=W)




########################

# Entry Fields for Drinks items

textlassi=Entry(drinksFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=0,column=1)

textcoffee=Entry(drinksFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1,column=1)

texttea=Entry(drinksFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_tea)
texttea.grid(row=2,column=1)

textmilk=Entry(drinksFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_milk)
textmilk.grid(row=3,column=1)

textfaluda=Entry(drinksFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=4,column=1)

textjaljeera=Entry(drinksFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_jaljeera)
textjaljeera.grid(row=5,column=1)

textroohafza=Entry(drinksFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_roohafza)
textroohafza.grid(row=6,column=1)

textmasalatak=Entry(drinksFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_masalatak)
textmasalatak.grid(row=7,column=1)

textcocacola=Entry(drinksFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_cocacola)
textcocacola.grid(row=8,column=1)



########################################

# Cakes

oreocake=Checkbutton(cakesFrame,text="Oreo",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var19,command=oreo)
oreocake.grid(row=0,column=0,sticky=W)

applecake=Checkbutton(cakesFrame,text="Apple",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var20,command=apple)
applecake.grid(row=1,column=0,sticky=W)

kitkatcake=Checkbutton(cakesFrame,text="Kitkat",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var21,command=kitkat)
kitkatcake.grid(row=2,column=0,sticky=W)

vanillacake=Checkbutton(cakesFrame,text="Vanilla",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var22,command=vanilla)
vanillacake.grid(row=3,column=0,sticky=W)

bananacake=Checkbutton(cakesFrame,text="Banana",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var23,command=banana)
bananacake.grid(row=4,column=0,sticky=W)

pistacake=Checkbutton(cakesFrame,text="Pista",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var24,command=pista)
pistacake.grid(row=5,column=0,sticky=W)

pineapplecake=Checkbutton(cakesFrame,text="Pineapple",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var25,command=pineapple)
pineapplecake.grid(row=6,column=0,sticky=W)

chocolatecake=Checkbutton(cakesFrame,text="Chocolate",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var26,command=chocolate)
chocolatecake.grid(row=7,column=0,sticky=W)

blackforestcake=Checkbutton(cakesFrame,text="Black Forest",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var27,command=blackforest)
blackforestcake.grid(row=8,column=0,sticky=W)

# Entry Box for Cakes

textoreo=Entry(cakesFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=0,column=1)

textapple=Entry(cakesFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_apple)
textapple.grid(row=1,column=1)

textkitkat=Entry(cakesFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=2,column=1)

textvanilla=Entry(cakesFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=3,column=1)

textbanana=Entry(cakesFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_banana)
textbanana.grid(row=4,column=1)

textpista=Entry(cakesFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_pista)
textpista.grid(row=5,column=1)

textpineapple=Entry(cakesFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=6,column=1)

textchocolate=Entry(cakesFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_chocolate)
textchocolate.grid(row=7,column=1)

textblackforest=Entry(cakesFrame,font=("arial",10,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8,column=1)



######################################################################################################

# Cost Labels and their Entry Box

labelCostofFood=Label(costFrame,text="Cost of Food",font=("arial",16,"bold"),fg="blue",bg="yellow")
labelCostofFood.grid(row=0,column=0)

labelCostofFood=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=costoffoodvar)
labelCostofFood.grid(row=0,column=1)



labelCostofDrinks=Label(costFrame,text="Cost of Drinks",font=("arial",16,"bold"),fg="blue",bg="yellow")
labelCostofDrinks.grid(row=1,column=0)

labelCostofDrinks=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=costofdrinksvar)
labelCostofDrinks.grid(row=1,column=1)



labelCostofCakes=Label(costFrame,text="Cost of Cakes",font=("arial",16,"bold"),fg="blue",bg="yellow")
labelCostofCakes.grid(row=2,column=0)

labelCostofCakes=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=costofcakesvar)
labelCostofCakes.grid(row=2,column=1)


labelSubTotal=Label(costFrame,text="Sub Total",font=("arial",16,"bold"),fg="blue",bg="yellow")
labelSubTotal.grid(row=0,column=2)

labelSubTotal=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=subtotalvar)
labelSubTotal.grid(row=0,column=3)


labelServiceTax=Label(costFrame,text="Service Tax",font=("arial",16,"bold"),fg="blue",bg="yellow")
labelServiceTax.grid(row=1,column=2)

labelServiceTax=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=servicetaxvar)
labelServiceTax.grid(row=1,column=3)

labelTotalCost=Label(costFrame,text="Total Cost",font=("arial",16,"bold"),fg="blue",bg="yellow")
labelTotalCost.grid(row=2,column=2)

labelTotalCost=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=totalcostvar)
labelTotalCost.grid(row=2,column=3,padx=26)


###########################################################################################################

# Buttons

buttonTotal=Button(buttonFrame,text="Total",font=("arial",10,"bold"),fg="white",bg="green",bd=6,padx=12,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text="Receipt",font=("arial",10,"bold"),fg="white",bg="green",bd=6,padx=12,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text="Save",font=("arial",10,"bold"),fg="white",bg="green",bd=6,padx=12,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text="Send",font=("arial",10,"bold"),fg="white",bg="green",bd=6,padx=12,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text="Reset",font=("arial",10,"bold"),fg="white",bg="Red",bd=6,padx=12,command=reset)
buttonReset.grid(row=0,column=4)



#############################################################

# Text Area for Receipt


textReceipt=Text(receiptFrame,font=("arial",12,"bold"),bd=5,width=42,height=14)
textReceipt.grid(row=0,column=0)


##############################################################


# Calculator Function

operator=''
def buttonClick(numbers):
   global operator
   operator=operator+numbers
   calculatorField.delete(0,END)
   calculatorField.insert(END,operator)

def clear():
   global operator
   operator=''
   calculatorField.delete(0,END)
   

def answer():
   global operator
   result = str(eval(operator))
   calculatorField.delete(0,END)
   calculatorField.insert(0,result)
   operator=''
   
   
   

# Calculator

calculatorField=Entry(calculatorFrame,font=("arial",16,"bold"),width=32,bd=5)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text="7",font=("arial",16,"bold"),fg="Yellow",bg="red4",bd=6,width=6,command=lambda:buttonClick("7"))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text="8",font=("arial",16,"bold"),fg="Yellow",bg="red4",bd=6,width=6,command=lambda:buttonClick("8"))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text="9",font=("arial",16,"bold"),fg="Yellow",bg="red4",bd=6,width=6,command=lambda:buttonClick("9"))
button9.grid(row=1,column=2)

buttonplus=Button(calculatorFrame,text="+",font=("arial",16,"bold"),fg="Yellow",bg="red4",bd=6,width=6,command=lambda:buttonClick("+"))
buttonplus.grid(row=1,column=3)

button4=Button(calculatorFrame,text="4",font=("arial",16,"bold"),fg="Yellow",bg="red4",bd=6,width=6,command=lambda:buttonClick("4"))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text="5",font=("arial",16,"bold"),fg="black",bg="white",bd=6,width=6,command=lambda:buttonClick("5"))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text="6",font=("arial",16,"bold"),fg="black",bg="white",bd=6,width=6,command=lambda:buttonClick("6"))
button6.grid(row=2,column=2)

buttonminus=Button(calculatorFrame,text="-",font=("arial",16,"bold"),fg="Yellow",bg="red4",bd=6,width=6,command=lambda:buttonClick("-"))
buttonminus.grid(row=2,column=3)

button1=Button(calculatorFrame,text="1",font=("arial",16,"bold"),fg="Yellow",bg="red4",bd=6,width=6,command=lambda:buttonClick("1"))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text="2",font=("arial",16,"bold"),fg="black",bg="white",bd=6,width=6,command=lambda:buttonClick("2"))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text="3",font=("arial",16,"bold"),fg="black",bg="white",bd=6,width=6,command=lambda:buttonClick("3"))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text="*",font=("arial",16,"bold"),fg="Yellow",bg="red4",bd=6,width=6,command=lambda:buttonClick("*"))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text="Ans",font=("arial",16,"bold"),fg="Yellow",bg="red4",bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text="Clear",font=("arial",16,"bold"),fg="Yellow",bg="red4",bd=6,width=6,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text="0",font=("arial",16,"bold"),fg="Yellow",bg="red4",bd=6,width=6,command=lambda:buttonClick("0"))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text="/",font=("arial",16,"bold"),fg="Yellow",bg="red4",bd=6,width=6,command=lambda:buttonClick("/"))
buttonDiv.grid(row=4,column=3)








root.mainloop()



#######################################################################################################################################
##                            ##
## Created By : Nikhil Falke  ##
## Contact    : 7499105910    ##
##                            ##
################################
