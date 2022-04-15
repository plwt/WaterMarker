# install pillow

from PIL import Image

import OS

print("Welcome to WaterMarker")

while True:
    while imaging:
 print("Have you saved the file to be watermarked to the WaterMarker folder with filename image.png?(y/n)")

Gonogo=input()

while Gonogo=="n":
    print("Have you saved the file to be watermarked to the WaterMarker folder (/opt/WaterMarker/src/images) with filename image.png?(y/n)")
    Gonogo=input()  

if Gonogo=="y":
    words=Image.open('/opt/WaterMarker/images/image.jpg')
    words.save("/opt/WaterMarker/images/temp.png")
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
    print("Your watermarked file has been saved to /opt/WaterMarker/images/watermarkedimage.png")
else:
    print("Thank you for using WaterMarker.")
