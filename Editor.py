from PIL import Image ,ImageFilter
import os
def black():
	c= input("PATH OF FILE >>")
	os.chdir("/"+c)
	a = input("FILE NAME >>")
	b = Image.open(a)
	b.convert(mode = 'L').save(a+"_black.jpg")
def blur():
	c= input("PATH OF FILE >>")
	os.chdir("/"+c)
	a = input("NAME OF FILE >>")
	b = Image.open(a)
	d = int(input("BLUR SIZE (btwn 1 and 20)"))
	b.filter(ImageFilter.GaussianBlur(d)).save(a+"_blur.jpg")
print("[1]*BLACK AND WHITE\n[2]*BLUR ")

try:
	r = int(input(">>"))
	while r != "1" and "2":
		print("PICK A NUMBER")
		#if r == 2:
#			break
		break
	else:
	
		pass
	
	if r == 1:
		black()
	elif r == 2:
		blur()
except:
	print("ERROR")
