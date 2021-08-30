import sqlite3
cursor=sqlite3.connect('crop_data.sqlite3')


#states
def states():
    cursor=sqlite3.connect('crop_data.sqlite3')
    l=[]
    states=cursor.execute("SELECT State_Name from crop_production")
    for i in states:
        if i[0] not in l: l.append(i[0])
    #print(*l)
    cursor.close()
    return(l)

def districts(state):
    cursor=sqlite3.connect('crop_data.sqlite3')
    l=[]
    #print(state)
    districts=cursor.execute("SELECT District_Name from crop_production WHERE State_Name LIKE (?)",(state,))
    for i in districts:
        if i[0] not in l: l.append(i[0])
    #print(*l)
    cursor.close()
    return(l)

def seasons(state,district):
    cursor=sqlite3.connect('crop_data.sqlite3')
    l=[]
    #print(state,district)
    seasons=cursor.execute("SELECT Season from crop_production WHERE State_Name LIKE (?) AND District_Name LIKE (?)",(state,district))
    for i in seasons:
        if i[0] not in l: l.append(i[0])
    #print(*l)
    cursor.close()
    return(l)

def crops(state,district,season):
    cursor=sqlite3.connect('crop_data.sqlite3')
    l=[]
    #print(state,district,season)
    crops=cursor.execute("SELECT Crop from crop_production WHERE State_Name LIKE (?) AND District_Name LIKE (?) AND Season LIKE (?)",(state,district,season,))
    for i in crops:
        if i[0] not in l: l.append(i[0])
    #print(*l)
    cursor.close()
    return(l)


def images(croppredict):
    cursor=sqlite3.connect('crop_data.sqlite3')
    image=cursor.execute("SELECT images from crops WHERE crops LIKE (?)",(croppredict,))
    l=[]
    for i in image:
        l.append(i)
    image=l[0][0]
    cursor.close()
    return(image)