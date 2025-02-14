class Point:
    def __init__(self, y ,x):
        self.y = y
        self.x = x

def draw_point(p):
    print('.',end='')


class Line:
    def __init__(self,start ,end):
        self.start = start
        self.end = end

class Reqtangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x,y), Point(x+width, y)))
        self.append(Line(Point(x+height,y),Point(x+width,y+height)))
        self.append(Line(Point(x,y),Point(x,y+height)))
        self.append(Line(Point(x,y+height),Point(x+width, y+height)))


class LinetoPoint:
    cache = {}    
    def __init__(self, line):
        self.h = hash(line)
        if self.h in self.cache:
            print('asshole')
            return
        print(f'Generating points for the line '
              f'[{line.start.x},{line.start.y}] -> '
              f'[{line.end.x},{line.end.x}]')
        

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.end.y, line.end.x)
        bottom = min(line.start.y, line.end.y)

        points = []
        if right - left == 0:
            for y in range(top,bottom):
                points.append(Point(left, y))

        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x,top))

        self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h])
                                    

def draw(rcs):
    print('\n\n--- Drawing some stuff ---\n')
    for rc in rcs:
        for line in rc:
            adapter = LinetoPoint(line)
            for p in adapter:
                draw_point(p)


if __name__ == "__main__":
    rcs = [
        Reqtangle(1,1,10,10),
        Reqtangle(3,3,6,6)    
    ]

    draw(rcs)
    draw(rcs)
