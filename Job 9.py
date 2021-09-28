#Job 9
def draw_rectange(width:int, height:int) -> str:
    print("|"+(width-2)*"-"+"|")
    for i in range(0,height-2):
        print("|"+" "*(width-2)+"|")
    print("|"+(width-2)*"-"+"|")
#Job 9.5
def draw_triangle(height:int) -> str:
    for i,j in zip(range(height-1,0,-1),range(0,height-1)):
        print(" "*i+"/"+" "*j*2+"\\"+" "*i)
    print("/"+"_"*((height*2)-2)+"\\")