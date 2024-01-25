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
doplay=1
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


def drawplayer(x, y):
  set_color(255,140,0)
  fill_circle(x+5,y+5,8)
  set_color(200,0,0)
  fill_circle(x,y,10)
  set_color(0,0,0)
  draw_line(x+9,y+12,x+18,y+9)
  draw_line(x+9,y+6,x+18,y+9)

try:
  hs = recall_value("hsbird")
  #if it works it works
except Exception as e:
   print("no hs, setting to 0")
   store_value("hsbird",0)
   hs=0


print(get_screen_dim())  
debag = 0
set_window(0,317,0,211)
while True:
  use_buffer()
  clear()
  
  drawplayer(50,160)
  drawplayer(230,150)
  
  set_color(117,216,230)
  draw_text(110,100,"Bird game v1.0")
  set_color(0,0,0)
  draw_text(110,80,"High score: "+str(hs))
  draw_text(80,20,"esc – quit          enter – play")
  paint_buffer()
  key=get_key()
  
  if key=="esc":
    doplay=0
    break
  if key=="enter":
    break
  if key=="8":
    debag=1
    break


print("Assume TPS is 100 on emulator")
#CreateWindow not needed

def makeref(obj):
  ref=obj

x,y=159,106
#main loop
while key != "esc":
  tps=ticks_cpu()/clock()
  if debag:
    fpse=get_time_ms()
    makeref(fpse)
  use_buffer()
  #basedraw
  clear()
  #cant win no more
  
  
  #Draw Green map
  set_color(0,200,0)
  fill_rect(0,0,317,11)
  #Draw player
  drawplayer(plx,ply)
  
  
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
    fps=float(1000/(get_time_ms()-fpse))
    draw_text(2,70,"FPS:"+str(fps))
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
       ply=ply+15
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
        
if doplay==1:
  set_color(255,0,0)
  if debag == 0:
    if score > hs:
      hs=score
      store_value("hsbird",hs)
    draw_text(90,100,"Score: "+str(score)+" High Score: "+str(hs))
    print("Game was played")
  else:
    draw_text(190,100,"You Lost")
    print("Game was lost")
  print("Score: "+str(score))
