
# Press the green button in the gutter to run the script.
#from guizero import App ,Text ,TextBox, PushButton , Picture ,ButtonGroup


   #  def say_my_name():
  #      if int(my_name.value) > 5000 :
    #            app.warn("warning", "Bitte eine Gültige Geschwindigkeit eingeben")
    #        else:
    #            welcome_message.value = my_name.value +"min-1"
 #def limit():
    #if int(name.value)>5000:
      #  app.info("info", "valeur incorrect")
   # else:
    #    welcome_message.value= my.name.value + "min-1"

#app define
  #  app = App(title="Motor Geschwindigkeit app",width=600, height=600 )
#picture insert
  #  picture = Picture(app, image="uni-rostock.png",width=400, height=200)
#text insert
  #  Text(app, text="Universität Rostock", size=40, font="Times New Roman", color="#ff100d")
#second text that will be changed
   # welcome_message = Text(app, text="0"+"min-1", size=40, font="Times New Roman", color="Black")
#create textbox
  #  my_name = TextBox(app,text=0,width=30)
#create botton

    #Button = ButtonGroup(app, options=[ ["Geschw Richtung 1", "M"], ["Geschw Richtung 2", "B"]] ,selected="M", horizontal=False,  align="middle")
#refraich the second text  (must be controlled)
#
  #  update_text = PushButton(app, command=limit, text="Geschwindigkeit einreichen", width=30, height=5)

   # if button==true and my_name < string(5000)
  #      message_m

#app.display()

from guizero import App ,Text ,TextBox, PushButton , Picture ,ButtonGroup

def limit():
    if  name.value.isalpha() or int(name.value) >5000 :
        app.warn("warning", "Bitte eine Gültige Geschwindigkeit eingeben")
    else:
        message.value= name.value + "min-1"

#def update():
#    message.value = name.value +"min-1"

app = App(title="RasberryPi")

picture = Picture(app, image="uni-rostock.png",width=400, height=200)

message = Text(app, text="0"+"min-1", size=40, font="Times New Roman", color="Black")

name = TextBox(app,text=0 )

choice = ButtonGroup(app, options=[ ["Geschw Richtung 1", "M"], ["Geschw Richtung 2", "B"]] ,selected="M", horizontal=False,  align="middle")

button = PushButton(app, text="Geschwindigkeit einreichen", command=limit, width=30, height=5)

app.display()