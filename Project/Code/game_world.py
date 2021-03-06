
# layer 0: Background Objects
# layer 1: Foreground Objects
# layer 2: Bullet Objects
objects = [[],[]]

def add_object(o, layer):
    objects[layer].append(o)


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break

def clear():
    for o in objects:
        o.clear()



def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

def get_sky():
    for o in objects[0]:
        yield o
