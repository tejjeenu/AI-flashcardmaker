from tkinter import *               # importing all the widgets and modules from tkinter  
from tkinter import messagebox as mb    # importing the messagebox module from tkinter  
from tkinter import filedialog as fd    # importing the filedialog module from tkinter  
import os                               # importing the os module  
import shutil
from tkinter import messagebox
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import cv2
import numpy
import openai
import csv
import time
#openai.api_key = open ai key here


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


def converttoq(specpoint:str):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user", "content": "can you turn '" + specpoint + "' into a question that can be used for a flashcard"}]
    )
    return str(completion.choices[0].message.content)

def btn_clicked():
    print("Button Clicked")
    messagebox.showinfo("showinfo", "making your flashcards now, please wait")
    #entry0 = file path for pdf
    #entry1 = start page for scanning
    #entry2 = end page for scanning
    #entry3 = file path for csv file for saving
    model = YOLO("newspecextract.pt")
    images = convert_from_path(entry0.get())

    data = []
    count = 0
    for j in range(int(entry2.get())):
      # Save pages as images in the pdf
       if(j >= int(entry1.get()) - 1):
          images[j].save('page'+ str(j) +'.png', 'PNG')
          results = model.predict(source='page'+ str(j) +'.png', show=False)
          img = cv2.imread('page'+ str(j) +'.png')
          for result in results:
             boxes = result.boxes.cpu().numpy()
             for i, box in enumerate(boxes):
               r = box.xyxy[0].astype(int)
               crop = img[r[1]:r[3], r[0]:r[2]]
               cv2.imwrite(str(i) + ".png", crop)
               speccontent = str(pytesseract.image_to_string(Image.open(str(i) + ".png")))
        
               rawqlist = speccontent.split(".")
               qlist = []

               for spec in rawqlist:
                  spec = spec.replace("\n\n","\n")
                  #use the converttoq() method here for the q
                  q = converttoq(spec)
                  q = q.replace('"','') #usually q qould be here
                  print(q)
                  messagebox.showinfo("showinfo", "potential flashcard " + str(count) + ": " + q + " please wait a few minutes to make the next one")
                  qlist.append(q.strip())#replace q with the actual rephrased spec point as a q
                  time.sleep(70)
                  count = count + 1

               qlist.remove(qlist[len(qlist)-1])
        
               os.remove(str(i) + ".png")
        
               for q in qlist:
                  data.append([q, 'Enter answer here'])
          os.remove('page'+ str(j) +'.png')

    with open(entry3.get(), 'w', encoding='UTF8', newline='') as f:
       writer = csv.writer(f)
       writer.writerows(data)
       f.close()
    
    messagebox.showinfo("showinfo", "all flashcards made succesfully!")



def getspecification(something):  
   # selecting the file using the askopenfilename() method of filedialog  
   the_file = fd.askopenfilename(  
      title = "Select a file of any type",  
      filetypes = [("pdf files", "*.pdf*")]  
      )
   
   entry0.delete(0,END)
   entry0.insert(0, str(the_file))
   # opening a file using the startfile() method of the os module

def selectdestination(something):
   the_file = fd.askopenfilename(  
      title = "Select a file of any type",  
      filetypes = [("select csv file", "*.csv*")]  
      )
   
   entry3.delete(0,END)
   entry3.insert(0, str(the_file))

   


window = Tk()

window.geometry("999x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 999,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    430.5, 281.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 500, y = 480,
    width = 244,
    height = 79)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    765.5, 140.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 636, y = 117,
    width = 259,
    height = 45)

entry0.bind('<Button-1>', getspecification)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    419.5, 140.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 365, y = 120,
    width = 109,
    height = 39)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    419.5, 374.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry2.place(
    x = 365, y = 354,
    width = 109,
    height = 39)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    765.5, 371.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry3.place(
    x = 636, y = 348,
    width = 259,
    height = 45)

entry3.bind('<Button-1>', selectdestination)

entry0.insert(0,"specification file here")
entry1.insert(0,"first page number")
entry2.insert(0,"last page number")
entry3.insert(0,"flashcard file here(csv)")

window.resizable(False, False)
window.mainloop()
