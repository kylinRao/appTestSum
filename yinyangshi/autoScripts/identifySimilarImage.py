# coding=utf-8
from PIL import Image
import math
import operator
import heapq

WPIECE = 20
HPIECE = 10
def make_same_lenth(h1,h2):
    a = len(h1)
    b = len(h2)
    if a > b:
        h1 = h1[0:b]
    else:
        h2 = h2[0:a]
    return h1,h2

def compare_and_return_rms(image1filePath,toCompare):
    h1 = Image.open(image1filePath).histogram()
    h2 = Image.open(toCompare).histogram()
    h1,h2 = make_same_lenth(h1,h2)
    rms = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return rms


#返回字典 ，{"picPath":rms[i],"x":x,"y":y}
# 其中x,y为图片的中心地址origImagefilePath为大图，toCompare为小图
def gen_similar_cut_pic_center_x_y(origImagefilePath,toCompare):
    orgimage = Image.open(origImagefilePath)
    (w,h) = orgimage.size
    wa = w/WPIECE
    ha = h/HPIECE
    print wa,ha
    listw = []
    listh = []
    rms = {}
    ll=lambda x: wa*x
    for i in range(1,WPIECE+1):
        listw.append(i*wa)
    for i in range(1,HPIECE+1):
        listh.append(i*ha)
    print listw,listh
    for x in listw:
        for y in listh:
            #print x,y
            data = orgimage.crop((x,y,x+wa,y+ha))
            
            filename = "{x}_{y}pic.png".format(x=x,y=y)
            data.save(filename)
            rms[compare_and_return_rms(filename,toCompare)]={"filename":filename,"x":x,"y":y,"comparefile":toCompare}
    similar =  heapq.nsmallest(1, rms.keys())
    for i in similar:
        print rms[i]

    return {"picPath":rms[i]["filename"],"x":int(rms[i]["x"]+wa/2),"y":int(rms[i]["y"]+ha/2)}
if __name__ == '__main__':
    origImagefilePath = "yinyangshi.png"
    toCompare = "test.png"
    gen_similar_cut_pic(origImagefilePath,toCompare)
