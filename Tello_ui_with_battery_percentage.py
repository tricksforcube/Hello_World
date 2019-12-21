import tkinter as tki
import threading 
import time 
from tkinter import Toplevel, Scale
#import tello_working


class Tello_updated:
    
    def __init__(self):
        
        #self.tello=tello # tello class object 
        
        self.root=tki.Tk() # main tkinter ui class call
        
        self.distance_bar = Scale(self.root, from_=100, to=-100, tickinterval=0.01, digits=3, label='U-D(cm) ',

                                  resolution=0.02)
        self.distance_bar.set(0)

        self.distance_bar.pack(side="left")

        #self.btn_distance = tki.Button(self.root, text="Reset Distance", relief="raised",command=self.updateDistancebar)

        #self.btn_distance.pack(side="left", fill="both", expand="yes", padx=10, pady=5)
            
        
        self.angle_bar = Scale(self.root, from_=-180, to=180, tickinterval=0.01, digits=3, label='Angle(Degree)',

                                  resolution=0.02,orient = 'horizontal')

        self.angle_bar.set(0)

        self.angle_bar.pack(side="right")
        

        
        self.lr_bar = Scale(self.root, from_=-150, to=150, tickinterval=0.01, digits=3, label='L-R(cm)',

                                  resolution=0.02,orient = 'horizontal')

        self.lr_bar.set(0)

        self.lr_bar.pack(side="right")
        
        
        self.fb_bar = Scale(self.root, from_=150, to=-150, tickinterval=0.01, digits=3, label='F-R(cm) ',

                                  resolution=0.02)
        self.fb_bar.set(0)

        self.fb_bar.pack(side="left")
        
        
        self.thread = threading.Thread(target=self.cc)
        self.thread.start()
        #ourMessage ='This is our Message'
        #messageVar = Message(self.root, text = self.cc()) 
        #messageVar.config(bg='lightgreen') 
        #messageVar.pack( ) 
        

        
              
    def cc(self):
        c=0
        while True:
            
            c+=1
            print(c)
            
            msg="Bat: "+str(c)+ "%"
            messageVar = tki.Message(self.root, text = msg,borderwidth=5 )
            messageVar.pack()
            time.sleep(3)
            messageVar.destroy()
            
        
        
        
        
def main():
    
    #drone = tello_working.Tello()  
    tu=Tello_updated()
    tu.root.mainloop()
    
    
if __name__ == "__main__":

    main()         
