# install pillow

from PIL import Image

print("Welcome to WaterMarker")
print("Have you saved the file to be watermarked to the WaterMarker folder with filename image.png?(y/n)")

Gonogo=input()

while Gonogo=="n":
    print("Have you saved the file to be watermarked to the WaterMarker folder with filename image.png?(y/n)")
    Gonogo=input()  

if Gonogo=="y":
    words=Image.open('/opt/WaterMarker/src/home/WaterMark/image.png')
    words.putalpha(50)
    hmat,wmat = words.size
    mask=Image.open('/opt/WaterMarker/src/watermark.png')
    mask.putalpha(100)
    complete=mask.resize((hmat,wmat))
    complete.paste(words,box=(0,0),mask=words)
    complete.save("/opt/WaterMarker/src/home/WaterMark/watermarkedimage.png")
    print("Your watermarked file has been saved to your desktop with filename watermarkedimage.png")
else:
    print("Thank you for using WaterMarker.")
