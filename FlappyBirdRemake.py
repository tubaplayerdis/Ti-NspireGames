print("STARTING Game")
from ti_draw import *
from ti_system import *
from time import *
from random import *



key=""


#playervars
plx=15
ply=70
score = 0
didwin = 0
hs=-1
#debugvars
colls = 0#this does not work, but it dosent matter since it only taker one to fail
#enemyvars
catx = 312
caty = 11
catsize = 30
dogx = 312
dogy = 212
dogsize = 30
speed = 1.5
dif = 80
mindif = 30

print(get_screen_dim())  
debag = input("Mode: ")
print("Running In debug: "+debag)
debag = int(debag)




try:
  hs = recall_value("hsbird")
  #if it works it works
except Exception as e:
   print("no hs, setting to 0")
   store_value("hsbird",0)
   hs=0



print("Assume TPS is 100 on emulator")
#CreateWindow
set_window(0,317,0,211)
x,y=159,106
#main loop
while key != "esc":
  tps=ticks_cpu()/clock()
  use_buffer()
  #basedraw
  clear()
  #cant win no more
  
  
  #Draw Green map
  set_color(0,200,0)
  fill_rect(0,0,317,11)
  #Draw player
  set_color(255,140,0)
  fill_circle(plx+5,ply+5,8)
  set_color(200,0,0)
  fill_circle(plx,ply,10)
  set_color(0,0,0)
  draw_line(plx+9,ply+12,plx+18,ply+9)
  draw_line(plx+9,ply+6,plx+18,ply+9)
  
  
  #Enemys
  set_color(26,51,125)
  fill_rect(catx,caty,20,catsize)
  fill_rect(dogx,dogy-dogsize,20,dogsize)
  dogx = dogx-speed
  catx = catx-speed
  speed = speed+0.0005
  if catx < 8:
    catsize =uniform(mindif,dif)
    catx = 312
    score = score+1
    dif=dif+0.3
    mindif=mindif+0.3
  if dogx < 8:
    dogsize = uniform(mindif,dif)
    dogx = 312
  #LOGIC
  #enemy collison
  if plx >= catx-3:
    if debag == 1:
      draw_text(150,170,"Interpreting collision")
    if ply < 11+int(catsize)+5 or ply >212-int(dogsize)-5:
      if debag == 0:
        break
      else:
        colls = colls+1
  #ground collison
  if ply < 14:
    break
  
  #Counters
  set_color(0,0,0)
  #DEBUG
  if debag == 1:
    draw_text(2,190,"TPS: "+str(tps))
    draw_text(2,175,"Score: "+str(score))
    draw_text(2,160,"ccol: "+str(11+catsize))
    draw_text(2,145,"dcol: "+str(212-dogsize))
    draw_text(2,130,"ply: "+str(ply))
    draw_text(2,115,"colls: "+str(colls))
    draw_text(2,100,"speed: "+str(speed))
    draw_text(2,85,"catx: "+str(catx))
  else:
    draw_text(2,190,"Score: "+str(score))
  #VERY IMPORTANT NO MORE DRAWS
  paint_buffer()
  if debag == 0:
    ply=ply-0.5
  
  
  #input
  key=get_key()
  
  
#CONTROL
  if debag == 0:
    if key=="up":
      if ply >210 or ply < 10:
       ply = 100
      else:
       ply=ply+10
  else:
    if key=="up":
     if ply >210 or ply < 10:
       ply = 100
     else:
       ply=ply+1
    if key=="down":
      if ply >210 or ply < 10:
        ply = 100
      else:
        ply=ply-1
set_color(255,0,0)
if debag == 0:
  if score > hs:
    hs=score
    store_value("hsbird",hs)
  draw_text(90,100,"Score: "+str(score)+"High Score: "+str(hs))
  print("Game was played")
else:
  draw_text(170,100,"You Lost")
  print("Game was lost")
print("Score: "+str(score))
