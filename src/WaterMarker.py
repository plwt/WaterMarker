# install pillow

from PIL import Image, ImageDraw, ImageFont

import os
import sys
from pathlib import Path


def welcome():
    print("""
    Welcome to WaterMarker
    """)

welcome()

def make_watermark():

    width = 512
    height = 512
    message = input("Enter your watermark message (one word is best): ")
    font = ImageFont.truetype("//usr/share/fonts/truetype/freefont/FreeMono.ttf", size=30)
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    imgDraw = ImageDraw.Draw(img)
    textWidth, textHeight = imgDraw.textsize(message, font=font)
    xText = (width - textWidth) / 2
    yText = (height - textHeight) / 2
    imgDraw.text((xText, yText), message, font=font, fill=(0, 0, 0, 1))
    img.save('/opt/WaterMarker/src/watermark.png')

make_watermark()



def watermarker():
    Gonogo=input("Have you saved the file to be watermarked to the the WaterMarker folder in your user documents with filename image.png?(y/n)")
    
    if Gonogo=="n":
        print("Please save the image to be watermarked to the WaterMarker folder in your user documents with the filename image.jpg and run WaterMarker again.")
          

    elif Gonogo=="y":
        
        # Open the original image and save it as temporary.png
        
        from pathlib import Path
        home_path = str(Path.home())
        words=Image.open(home_path + '/WaterMarker/image.jpg')
        words.save("/opt/WaterMarker/images/temp.png")
        
        # Open the temporary .png and set alpha
        words=Image.open("/opt/WaterMarker/images/temp.png")
        words.putalpha(230)
        hmat,wmat = words.size
        mask=Image.open('/opt/WaterMarker/src/watermark.png')
        mask.putalpha(255)
        complete=mask.resize((hmat,wmat))
        complete.paste(words,box=(0,0),mask=words)
        complete.save(home_path + '/WaterMarker/watermarkedimage.png')
        path = "/opt/WaterMarker/images/temp.png"
        os.remove("/opt/WaterMarker/images/temp.png")
        print("Your watermarked file has been saved to the WaterMarker folder in your user documents with the filename watermarkedimage.png.  Thank you for using WaterMarker")
    else:
        print("Please try again.")

watermarker()
