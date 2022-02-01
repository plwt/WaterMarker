# python3 pip install pillow in the bash terminal

# run the script in the terminal

# python3 pip remove pillow in the bash terminal



from PIL import Image

print("Have you saved the file to be watermarked to your desktop with filename image.png?(y/n)")
Gonogo=input()

if Gonogo=="y":
    baseimage=Image.open('/home/path/filename.png')
    baseimage.putalpha(100)
    hmat,wmat = baseimage.size
    watermark=Image.open('/home/path/filename.png')
    complete=watermark.resize((hmat,wmat))
    complete.paste(baseimage,box=(0,0),watermark=baseimage)
    complete.save("/home/path/watermarkedfile.png")
    print("Your watermarked file has been saved to your desktop with filename watermarkedfile.png")
else:
    print("Thank you for trying WaterMarker.")