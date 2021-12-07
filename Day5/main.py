class Point():
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)

if __name__ == '__main__':   

    diagram = [[0 for i in range(1000)] for j in range(1000)]
    file_name = 'input.txt'

    with open(file_name, "r") as fd:
        for row in fd.readlines():
            movement = row.rstrip().split(' -> ')
            point_1 = Point(movement[0].split(',')[0],movement[0].split(',')[1])
            point_2 = Point(movement[1].split(',')[0],movement[1].split(',')[1])
            if point_1.x == point_2.x:
                points_sorted = sorted([point_1.y,point_2.y])
                for i in range(points_sorted[0],points_sorted[1]+1):
                    diagram[i][point_1.x] += 1
            if point_1.y == point_2.y:
                points_sorted = sorted([point_1.x,point_2.x])
                for i in range(points_sorted[0],points_sorted[1]+1):
                    diagram[point_1.y][i] += 1
            if abs(point_1.y-point_2.y) == abs(point_1.x - point_2.x):
                if point_1.x > point_2.x:
                    x1 = point_1.x
                    y1 = point_1.y
                    point_1.x = point_2.x
                    point_1.y = point_2.y
                    point_2.x = x1
                    point_2.y = y1
                if point_1.y > point_2.y:
                    result = Point(point_1.x,point_1.y)
                    diagram[point_1.y][point_1.x] += 1
                    while result.x != point_2.x:
                        result.x += 1
                        result.y -= 1
                        diagram[result.y][result.x] += 1
                if point_1.y < point_2.y:
                    result = Point(point_1.x,point_1.y)
                    diagram[point_1.y][point_1.x] += 1
                    while result.x != point_2.x:
                        result.x += 1
                        result.y += 1
                        diagram[result.y][result.x] += 1

    tot = 0
    for row in diagram:
        for column in row:
            if column >= 2:
                tot += 1
    print('result:', tot)