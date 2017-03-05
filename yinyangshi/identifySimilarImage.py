from PIL import Image
import math
import operator
import heapq
WPIECE = 20
HPIECE = 10
def compare_and_return_rms(image1filePath,toCompare):
    h1 = Image.open(image1filePath).histogram()
    h2 = Image.open(toCompare).histogram()
    rms = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return rms



def gen_similar_cut_pic(origImagefilePath,toCompare):
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
            rms[compare_and_return_rms(filename,toCompare)]=[filename,toCompare]
    similar =  heapq.nsmallest(1, rms.keys())
    for i in similar:
        print rms[i]
    return rms[i]

origImagefilePath = "yinyangshi.png"
toCompare = "test.png"
gen_similar_cut_pic(origImagefilePath,toCompare)
