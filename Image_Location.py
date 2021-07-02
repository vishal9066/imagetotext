import requests
import tkinter as tk
import urllib.request
from tkinter import filedialog

class Find_Image:
    def find_location(self):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()
        return file_path
    def download_image(self,image_url):
        if image_url == "":
            return "Please provide a link."
        filename = "testfile.jpg"
        urllib.request.urlretrieve(image_url,filename)
        return filename
