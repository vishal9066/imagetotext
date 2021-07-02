from tkinter import *
import img
import Image_Location

root = Tk()
root.geometry("800x800")
e = Entry(root,width = 200)
e.pack(padx = 300,pady = 30)
myLabel = Label(root)
def onLinkclick():
    try:
        obj = Image_Location.Find_Image()
        location = obj.download_image(e.get())
        string = img.Extract_data().return_string(location)
        myLabel = Label(root, text = string)
        myLabel.pack()
    except:
        myLabel = Label(root, text="The Link is broken or empty.")
        myLabel.pack()
def onclick():
    try:
        obj = Image_Location.Find_Image()
        location = obj.find_location()
        string = img.Extract_data().return_string(location)
        myLabel = Label(root, text = string)
        myLabel.pack()
    except:
        myLabel = Label(root, text="Nothing is chosen or may be the file is of invalid format.")
        myLabel.pack()
myButton2 = Button(root, text = "Open Image Link", command = onLinkclick)
myButton2.pack(padx = 300, pady = 20)
myButton1 = Button(root, text = "Open Image File", command = onclick)
myButton1.pack(padx = 300, pady = 20)

root.mainloop()