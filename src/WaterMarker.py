# install pillow

from PIL import Image, ImageDraw, ImageFont

import OS

def welcome():
    print("""
    Welcome to WaterMarker
    """)

welcome()



def make_watermark():

    width = 512
    height = 512
    message = input("Enter your message (one word is best): ")
    font = ImageFont.truetype("arial.ttf", size=30)
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
        break  

    elif Gonogo=="y":
        original=Image.open('/opt/WaterMarker/images/image.jpg')
        original.save("/opt/WaterMarker/images/temp.png")
        original2=Image.open("/opt/WaterMarker/images/temp.png")
        original2.putalpha(250)
        hmat,wmat = original2.size
        watermark=Image.open('/opt/WaterMarker/src/watermark.png')
        watermark.putalpha(255)
        complete=watermark.resize((hmat,wmat))
        complete.paste(original2,box=(0,0),watermark=original2)
        complete.save("/opt/WaterMarker/images/watermarkedimage.png")
        path = "/opt/WaterMarker/images/temp.png"
        os.remove("/opt/WaterMarker/images/temp.png")
        print("Your watermarked file has been saved to the WaterMarker folder in your user documents with the filename watermarkedimage.png")
    else:
        print("Thank you for using WaterMarker.")

watermarker()
