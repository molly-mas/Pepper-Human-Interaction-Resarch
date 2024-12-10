import naoqi

def explore_room(ip_address="192.168.3.137",port=9559, radius = 1.0):
    '''returns a map based on the given radius, its an image of the room pepper made (Idk how to look at the image) '''
    from naoqi import ALProxy
    exploration = ALProxy("ALNavigation", ip_address, port)
    exploration.explore(radius)
    path = exploration.saveExploration()
    return exploration.getMetricalMap()

#map =explore_room(radius=2.0)
#print map


# you can make your own modules so I could make one for my proj 
#once I have the methods hashed out its called ALModule


