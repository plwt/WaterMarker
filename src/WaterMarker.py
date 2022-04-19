# install required packages
from PIL import Image, ImageDraw, ImageFont
import os
import sys
from pathlib import Path


# Welcome message
def welcome():
    print("""
    Welcome to WaterMarker
    """)

welcome()


# Make watermark image
def make_watermark():

    # set width and height of watermark
    width = 512
    height = 512
    
    # set the message to be watermarked
    message = input("Enter your watermark message (one word is best): ")
    
    # set the font to be used
    font = ImageFont.truetype("//usr/share/fonts/truetype/freefont/FreeMono.ttf", size=30)
    
    # make the watermark
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    imgDraw = ImageDraw.Draw(img)
    textWidth, textHeight = imgDraw.textsize(message, font=font)
    xText = (width - textWidth) / 2
    yText = (height - textHeight) / 2
    imgDraw.text((xText, yText), message, font=font, fill=(0, 0, 0, 1))
    
    # save the watermark
    img.save('/opt/WaterMarker/src/watermark.png')

make_watermark()


# Watermark the image
def watermarker():
    # Ask the user to confirm the image has been saved
    Gonogo=input("Have you saved the file to be watermarked to the the WaterMarker folder in your user documents with filename image.png?(y/n)")
    
    if Gonogo=="n":
        print("Please save the image to be watermarked to the WaterMarker folder in your user documents with the filename image.jpg and run WaterMarker again.")
          

    elif Gonogo=="y":
        
        # Open the original image and save it as temporary.png
        from pathlib import Path
        home_path = str(Path.home())
        words=Image.open(home_path + '/WaterMarker/image.jpg')
        words.save("/opt/WaterMarker/images/temp.png")
        
        # Open the temporary .png, set alpha and get image size
        words=Image.open("/opt/WaterMarker/images/temp.png")
        words.putalpha(225)
        hmat,wmat = words.size
        
        # Open the watermark and resize it to the size of the original image
        mask=Image.open('/opt/WaterMarker/src/watermark.png')
        mask.putalpha(255)
        complete=mask.resize((hmat,wmat))
        
        # Open the temporary .png and paste the watermark on top of it
        complete.paste(words,box=(0,0),mask=words)
        
        # Save the watermarked image to the WaterMarker folder
        complete.save(home_path + '/WaterMarker/watermarkedimage.png')
        
        # Remove the temporary .png
        path = "/opt/WaterMarker/images/temp.png"
        os.remove("/opt/WaterMarker/images/temp.png")
        
        # Confirm the watermarked image has been saved
        print("Your watermarked file has been saved to the WaterMarker folder in your user documents with the filename watermarkedimage.png.  Thank you for using WaterMarker")
    else:
        print("Please try again.")

watermarker()
