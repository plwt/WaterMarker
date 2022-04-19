# install pillow

from PIL import Image, ImageDraw, ImageFont

import os

def welcome():
    print("""
    Welcome to WaterMarker
    """)

welcome()

def make_watermark():

    width = 512
    height = 512
    message = input("Enter your message (one word is best): ")
    font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansElbasan-Regular.ttf", size=30)
    img = Image.new('RGBA', (width, height), (255, 0, 0, 0))
    imgDraw = ImageDraw.Draw(img)
    textWidth, textHeight = imgDraw.textsize(message, font=font)
    xText = (width - textWidth) / 2
    yText = (height - textHeight) / 2

    imgDraw.text((xText, yText), message, font=font, fill=(255, 255, 255, 250))

    img.save('/opt/WaterMarker/src/watermark.png')

make_watermark()



def watermarker():
    Gonogo=input("Have you saved the file to be watermarked to the the WaterMarker folder in your user documents with filename image.png?(y/n)")
    
    if Gonogo=="n":
        print("Please save the image to be watermarked to the WaterMarker folder in your user documents with the filename image.jpg and run WaterMarker again.")
          

    elif Gonogo=="y":
        
        # Open the original image and save it as temporary.png
        words=Image.open('/opt/WaterMarker/images/image.jpg')
        words.save("/opt/WaterMarker/images/temp.png")
        
        # Open the temporary .png and set alpha
        words2=Image.open("/opt/WaterMarker/images/temp.png")
        words2.putalpha(250)
        hmat,wmat = words2.size
        mask=Image.open('/opt/WaterMarker/src/watermark.png')
        mask.putalpha(255)
        complete=mask.resize((hmat,wmat))
        complete.paste(words2,box=(0,0),mask=words2)
        complete.save("/opt/WaterMarker/images/watermarkedimage.png")
        path = "/opt/WaterMarker/images/temp.png"
        os.remove("/opt/WaterMarker/images/temp.png")
        print("Your watermarked file has been saved to the WaterMarker folder in your user documents with the filename watermarkedimage.png")
    else:
        print("Thank you for using WaterMarker.")

watermarker()
