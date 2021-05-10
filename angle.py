import cv2
import math
import numpy as np

cx = 604.1289
cy = 525.4418
w = 77.8029
h = 87.506
angle = 0.54

center = [cx,cy]
hpoint = [
    626.6238920427987,
    487.9144720642886]

def getAngle(center,hpoint):
    x1,y1 = center[0],center[1]
    x2,y2 = hpoint[0],hpoint[1]

    # 求斜率
    k = -(y2-y1)/(x2-x1)
    # 求反正切，在从弧度转到角度
    result = np.arctan(k) #* 57.29577

    print("直线倾斜角度为：" + str(result) + "度")

def getAngle(center, p1, p2):
    dx1 = p1[0] - center[0]
    dy1 = p1[1] - center[1]

    dx2 = p2[0] - center[0]
    dy2 = p2[1] - center[1]

    c = math.sqrt(dx1*dx1 + dy1*dy1) * math.sqrt(dx2*dx2 + dy2*dy2)
    if c == 0: return 0
    y = (dx1*dx2+dy1*dy2)/c
    if y>1: return 0
    angle = math.acos(y)

    if (dx1*dy2-dx2*dy1)>0:
        return angle
    else:
        return -angle

def rotatePoint(xc, yc, xp, yp, theta):
    xoff = xp - xc
    yoff = yp - yc

    cosTheta = math.cos(theta)
    sinTheta = math.sin(theta)
    pResx = cosTheta * xoff + sinTheta * yoff
    pResy = - sinTheta * xoff + cosTheta * yoff
    return xc + pResx, yc + pResy

rp = rotatePoint(cx,cy,cx,(cy-0.5*h),-angle)
# rp_bak = rotatePoint(cx,cy,cx,(cy+0.5*h),-angle)


point_size = 1
point_color = (0, 0, 255) # BGR
thickness = 4
# image input
img = cv2.imread('C:/Users/maggie/Desktop/work/R-CenterNet/data/airplane/images/001.jpg')

# roated point
# cv2.circle(img, (int(rp[0]),int(rp[1])), point_size, (0, 255, 0), thickness)
# cv2.circle(img, (int(rp_bak[0]),int(rp_bak[1])), point_size, (0, 255, 0), thickness)

# dxdy
# dx = 423
# dy = 570
# cv2.circle(img, (int(dx),int(dy)), point_size, (0, 255, 0), thickness)

# center
# cv2.circle(img, (int(cx),int(cy)), point_size, (0, 0, 255), thickness)
# cv2.imwrite('ret/angle_test.png',img)

if __name__ == '__main__':
    # getAngle(center,hpoint)
    getAngle(center, [cx,(cy-0.5*h)], rp)

    # image input
    img = cv2.imread('C:/Users/maggie/Desktop/work/R-CenterNet/data/airplane/images/001.jpg')

    # center
    cv2.circle(img, (int(cx), int(cy)), point_size, (0, 0, 255), thickness)
    cv2.circle(img, (int(cx), int(cy-0.5*h)), point_size, (0, 255, 0), thickness)
    cv2.circle(img, (int(rp[0]), int(rp[1])), point_size, (0, 255, 0), thickness)
    # cv2.circle(img, (int(rp_bak[0]), int(rp_bak[1])), point_size, (0, 255, 0), thickness)

    # save image
    cv2.imwrite('ret/angle.png', img)