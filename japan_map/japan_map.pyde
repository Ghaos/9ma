import urllib
import math

x = []
y = []
h = []
l = []
def setup():
    global mapImage
    size(700,755)
    mapImage = loadImage("japan_map.gif")
    background(255)
    image(mapImage,0,0)
    
    sql = urllib.quote("""
        SELECT location_table.prefecture_id AS prefecture_id, 
        location_table.location_x AS x,
        location_table.location_y AS y,
        wt.h AS h,
        wt.l AS l
        FROM location_table,
        (SELECT prefecture_id, AVG(highest) AS h, AVG(lowest) AS l
         FROM weather_table GROUP BY prefecture_id) AS wt
        WHERE location_table.prefecture_id = wt.prefecture_id
        """)
    url = "http://course.mpkato.net/scripts/iam/?query=" + sql
    print url
    xml = loadXML(url)
    children = xml.getChildren("item")

    for i,child in enumerate(children):
        prefecture_id = int(child.getChild("prefecture_id").getContent())
        x.append(int(child.getChild("x").getContent()))
        y.append(int(child.getChild("y").getContent()))
        h.append(float(child.getChild("h").getContent()))
        l.append(float(child.getChild("l").getContent()))

def draw():
    pass

def mousePressed():
    image(mapImage,0,0)
    for i in range(0,len(x)):
        if math.hypot(mouseX-x[i], mouseY-y[i])  <= 60:
            fill(0,0,255)
            rect(x[i]-10,y[i]-h[i],10,h[i])
            fill(255,0,0)
            rect(x[i],y[i]-l[i],10,l[i])