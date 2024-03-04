import cv2
import pandas as pd


# img = cv2. // Click image from video
img_path = './imagefile.jpeg' # Image in which color detection happens
img = cv2.imread(img_path)
im = img.copy()

cv2.imshow("image", img) 

font = cv2.FONT_HERSHEY_TRIPLEX 
clicked = False
r=g=b=x_pos=y_pos=0

index = ["color","color_name","hex","R","G","B"]
csv = pd.read_csv("colors.csv",names=index,header=None)


def getColorName(R,G,B):
    minimum = 200000
    for i in range(len(csv)):
        d = (R-int(csv.loc[i,"R"]))**2+(G-int(csv.loc[i,"G"]))**2+(B-int(csv.loc[i,"B"]))**2
        if d<=minimum:
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

window_size = cv2.getWindowImageRect("image")
m = window_size[2]
def drawFun(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global b,g,r,x_pos,y_pos,clicked,im,img
        if clicked==True:
            img = im.copy()
            # print("sa")
            # cv2.imshow(im)
        clicked = True
        x_pos = x
        y_pos = y
        if(y_pos<=window_size[3]*13/100): # if clicked on top text is shifted 50 pixels down
            y_pos+=50
        if(x_pos>=window_size[2]*50/100): # if clicked on right text is shown on left otherwise right
            x_pos -= 300

        # if(x)
        print(x,y)
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
        cname = getColorName(r,g,b)
        # print(getColorName(r,g,b))
        # cv2.putText(cv2.imread variable,Text,(x coordinate,y coordinate),font, fontsize, (rgb color pixels), font weight)
        if r+g+b >= 600:
            cv2.putText(img,cname,(x_pos,y_pos),font, 1, (0, 0, 0), 2)
        else:
            cv2.putText(img,cname,(x_pos,y_pos),font, 0.8, (0, 255, 255), 2)

        cv2.imshow('image', img)
        
        print(window_size)
        # cv2.imshow('im', im)
        
        # print("Clicked")


cv2.setMouseCallback('image',drawFun)
cv2.waitKey(0) 
cv2.destroyAllWindows() 

