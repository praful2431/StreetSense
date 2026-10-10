from entities import Position, Road
from simulator import Grid

def bfsPath(grid: Grid, house: Position, office: Position):
    visited = []
    for i in range(grid.rows): visited.append([0] * grid.cols)

    queue = [0] * grid.rows * grid.cols
    front = 0
    rear = -1

    distance = []
    for i in range(grid.rows):
        distance.append([-1] * grid.cols)

    src = house
    visited[house.row][house.col] = 1
    distance[house.row][house.col] = 0

    rear+=1
    queue[rear] = house

    destFound = False

    while(front <= rear and not destFound):
        cR = queue[front].row
        cC = queue[front].col
        front+=1


        for i in [(-1,0), (0,-1), (1,0), (0,1)]:
            x = cR+i[0]
            y = cC+i[1]

            #check if not within grid
            if(grid.rows <= x or x < 0 or grid.cols <= y or y < 0): continue

            if(Position(x,y) == office):
                print("Dest. Node Found")
                visited[x][y] = 1
                distance[x][y] = distance[cR][cC] + 1
                rear+=1
                queue[rear] = Position(x,y)
                print(queue)
                for row in visited:
                    for col in row:
                        print(col, end = " ")
                    print("\n")
                print("\n\n\n")
                for row in distance:
                    for col in row:
                        print(col, end = " ")
                    print("\n")
                destFound = True
                break
            
            if(visited[x][y] == 0 and grid.is_empty(Position(x,y))):
                visited[x][y] = 1
                distance[x][y] = distance[cR][cC] + 1
                rear+=1
                queue[rear] = Position(x,y)

    if distance[office.row][office.col] == -1:
        print("No path found")
        return None

    path = []
    cur = office
    steps = 0

    while(cur != house):
        steps += 1
        if steps > grid.rows * grid.cols:
            print("Reconstruction is stuck at:", cur)
            break

        path.append(cur)

        curDist = distance[cur.row][cur.col]

        for i in [(-1,0), (0,-1), (1,0), (0,1)]:
            x = cur.row+i[0]
            y = cur.col+i[1]

            if (0 <= x < grid.rows and 0 <= y < grid.cols and distance[x][y] == curDist - 1):
                cur = Position(x,y)
                break

    path.append(house)
    path.reverse()
    print(path, sep=" /t ")
    return path