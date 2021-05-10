
# -*- coding:utf-8 -*-
import os
import cv2
import math
import xml.etree.ElementTree as ET

Base_dir = r"C:\Users\maggie\Desktop\dir_points"


rootdir = './r_xml'  # 存有xml的文件夹路径
img_path = './JPEGImages'
new_xml_path = './Annotations'

def file_name (file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.xml':
                L.append(os.path.join(root, file))
    return L

def rotatePoint(xc, yc, xp, yp, theta):

    xoff = xp - xc
    yoff = yp - yc

    cosTheta = math.cos(theta)
    sinTheta = math.sin(theta)
    pResx = cosTheta * xoff + sinTheta * yoff
    pResy = - sinTheta * xoff + cosTheta * yoff
    return xc + pResx, yc + pResy

xml_dirs = file_name(os.path.join(Base_dir + rootdir))


def pretty_xml(element, indent, newline, level=0):  # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
    if element:  # 判断element是否有子元素
        if (element.text is None) or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
            # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
            # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element)  # 将element转成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
            subelement.tail = newline + indent * level

        pretty_xml(subelement, indent, newline, level=level + 1)  # 对子元素进行递归操作


# 循环
for ind, item in enumerate(xml_dirs):
    print(item)
    xml = ET.parse(item)
    root = xml.getroot()
    for obj in root.findall("object"):
        cx = obj.find('robndbox').find('cx').text
        cy = obj.find('robndbox').find('cy').text
        h = obj.find('robndbox').find('h').text
        angle = obj.find('robndbox').find('angle').text
        rp = rotatePoint(float(cx), float(cy), float(cx), (float(cy) - 0.5 * float(h)), -float(angle))
        # 在节点robndbox下面创建子节点dx和dy
        robndbox = obj.find('robndbox')

        dx = ET.SubElement(robndbox, 'dx')
        dx.text = str(rp[0])

        dy = ET.SubElement(robndbox, 'dy')
        dy.text = str(rp[1])
    # 美化xml
    pretty_xml(root, '\t', '\n')
    xml.write(os.path.join(Base_dir,new_xml_path,item.split("\\")[-1]), encoding="utf-8")

