import cv2
image_paths=['Pic1.jpg','Pic2.jpg']
# initialized a list of images
imgs = []

for i in range(len(image_paths)):
	imgs.append(cv2.imread(image_paths[i]))
	imgs[i]=cv2.resize(imgs[i],(0,0),fx=1,fy=1)

# showing the original pictures
cv2.imshow('1',imgs[0])
cv2.imshow('2',imgs[1])

stitchy=cv2.Stitcher.create()
(dummy,output)=stitchy.stitch(imgs)

if dummy != cv2.STITCHER_OK:
# done successfully
	print("stitching ain't successful")
else:
	print('Your Panorama is ready!!!')

# final output
cv2.imshow('final result',output)

cv2.waitKey(0)
