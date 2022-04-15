# install pillow

from PIL import Image

import OS

print(" ")
print("Welcome to WaterMarker")
print(" ")

Gonogo=input("Have you saved the file to be watermarked to the WaterMarker folder with filename image.png?(y/n)")

if Gonogo=="n":
    print("Please save the image to be watermarked to /opt/WaterMarker/images with the filename image.jpg and run WaterMarker again.")
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
    print("Your watermarked file has been saved to /opt/WaterMarker/images/watermarkedimage.png")
else:
    print("Thank you for using WaterMarker.")