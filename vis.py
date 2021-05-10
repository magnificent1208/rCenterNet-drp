import math

cx = 604.12890625
cy = 437.93580627441406
# w = 77.8029
# h = 87.506
angle = 1.21

def rotatePoint(xc, yc, xp, yp, theta):
    xoff = xp - xc
    yoff = yp - yc

    cosTheta = math.cos(theta)
    sinTheta = math.sin(theta)
    pResx = cosTheta * xoff + sinTheta * yoff
    pResy = - sinTheta * xoff + cosTheta * yoff
    return xc + pResx, yc + pResy

# rp = rotatePoint(cx,cy,cx,(cy-0.5*h),-angle)
# bp = rotatePoint(cx,cy,cx,(cy+0.5*h),-angle)

import cv2

point_size = 1
point_color = (0, 0, 255) # BGR
thickness = 4

# img = cv2.imread(r"C:\Users\maggie\Desktop\work\rCenterNet-drp\data\airplane\images\001.jpg")
img = cv2.imread(r"data/airplane/images/001.jpg")
# roated point
# cv2.circle(img, (int(bp[0]),int(bp[1])), point_size, (0, 255, 0), thickness)

#dxdy
dx = 626.6239
dy = 487.91446
cv2.circle(img, (int(dx),int(dy)), point_size, (0, 255, 0), thickness)

# center
cx = 604.12890625
cy = 525.4418182373047
cv2.circle(img, (int(cx),int(cy)), point_size, (0, 0, 255), thickness)

cv2.imwrite('ret/vis.png',img)
