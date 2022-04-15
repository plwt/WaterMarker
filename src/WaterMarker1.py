# install pillow

from PIL import Image

import OS

# Introduction
print(" ")
print("Welcome to WaterMarker")
print(" ")

while True:
    while imaging:
    
        # Get the image
        new_image = input("Have you saved the file to be watermarked to the WaterMarker folder with filename image.png? (y/n)")
        
            # If no, end the program
            if new_image=="n":
                print("Please save your file to (/opt/WaterMarker/src/images) and re-run WaterMarker")
                break  
        
            # If yes, continue
            else new_image=="y":
                words=Image.open('/opt/WaterMarker/images/image.jpg')
                # Save the image as a png
                words.save("/opt/WaterMarker/images/temp.png")
                words2=Image.open("/opt/WaterMarker/images/temp.png")
            
                # Set image alpha to 250
                words2.putalpha(250)
            
                # Get the image size
                hmat,wmat = words2.size
            
                # Open the watermark image
                mask=Image.open('/opt/WaterMarker/src/watermark.png')
            
                # Set the watermark alpha to 255
                mask.putalpha(255)
            
                # Resize the watermark image
                complete=mask.resize((hmat,wmat))
            
                # Paste the watermark image onto the image
                complete.paste(words2,box=(0,0),mask=words2)
            
                # Save the watermarked image
                complete.save("/opt/WaterMarker/images/watermarkedimage.png")
            
                # Delete the temp image
                path = "/opt/WaterMarker/images/temp.png"
                os.remove("/opt/WaterMarker/images/temp.png")
            
                #Notify user
                print("Your watermarked file has been saved to /opt/WaterMarker/images/watermarkedimage.png")
        

    # Ask to play again
    another_image = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if another_image[0].lower()=='y':
        imaging=True
        continue

    else:
        print("Thank yous for using WaterMarker.")
        break