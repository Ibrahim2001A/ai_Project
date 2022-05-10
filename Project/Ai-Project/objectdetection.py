import cv2
import tkinter 

top = tkinter.Tk()
top.title("Object Detection")

top.config(bg='white')
def noramlfacedetect():
   trained = cv2.CascadeClassifier('face2.xml')
   webcam = cv2.VideoCapture(1)
   while True:
      succesfram_read, frame = webcam.read()
      greyimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     
      facecourd = trained.detectMultiScale(greyimg)
      for(x,y,w,h) in facecourd:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(124,252,0))
      cv2.imshow("hello",frame)
      cv2.waitKey(1)
def catfacedetect():
   trained = cv2.CascadeClassifier('cat.xml')
   webcam = cv2.VideoCapture(0)
   while True:
      succesfram_read, frame = webcam.read()
      greyimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     
      facecourd = trained.detectMultiScale(greyimg)
      for(x,y,w,h) in facecourd:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(124,252,0))
      cv2.imshow("hello",frame)
      cv2.waitKey(1)
def smiledtect():
   trained = cv2.CascadeClassifier('face2.xml')
   smile = cv2.CascadeClassifier('smile.xml')
   webcam = cv2.VideoCapture(1)
   while True:
      succesfram_read, frame = webcam.read()
      greyimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     
      facecourd = trained.detectMultiScale(greyimg)
      for(x,y,w,h) in facecourd:
         theface =  frame[y:y+h,x:x+w]
         greyface = cv2.cvtColor(theface,cv2.COLOR_BGR2GRAY)
         smilecourd = smile.detectMultiScale(greyface,scaleFactor = 1.7,minNeighbors = 20)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(124,252,0))
         for(x,y,w,h) in smilecourd:
            cv2.rectangle(theface,(x,y),(x+w,y+h),(124,252,0))
         
      cv2.imshow("hello",frame)
      cv2.waitKey(1)
      
      
top.minsize(500,500)
B = tkinter.Label(top, text ="Object Detection",fg='black',bg='white',width=50,font=("Arial", 25)).pack()
# B.pack()
# B.grid(column=3,row=0,)
# z = tkinter.Label(top, text ="Hello",fg='red',bg='yellow')
facebutton = tkinter.Button(top ,text="Face Detection",command= noramlfacedetect, width=40)
facebutton.place(x=350, y=150, anchor="center")

# facebutton.pack()
smilebutton = tkinter.Button(top ,text="Smile Detection",command=  smiledtect, width=40)
smilebutton.place(x=350, y=250, anchor="center")
catbutton = tkinter.Button(top ,text="Cat Face Detection",command=  catfacedetect, width=40)
catbutton.place(x=350, y=350, anchor="center")
# smilebutton.pack()
# z.pack()

top.mainloop()