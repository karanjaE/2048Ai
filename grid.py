from copy import deepcopy

direction_vectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))
vector_index = [UP, DOWN, LEFT, RIGHT] = range(4)

class Grid:
    def __init__(self, size=4):
        self.size = size
        self.map = [[0] * self.size for i in range(self.size)]

    def clone(self):
        grid_copy =  Grid()
        grid_copy.map = deepcopy(self.map)
        grid_copy.size = self.size

        return grid_copy

    # Insert a title in an empty cell
    def set_cell_value(self, pos, val):
        self.map[pos[0]][pos[1]] = val

    def insert_title(self, pos, val):
        self.set_cell_value(pos, val)

    # Return all empty cells
    def get_available_cells(self):
        cells = []
        for x in range(self.size):
            for y in range(self.size):
                if self.map[x][y] == 0:
                    cells.append((x,y))

        return cells

    # Return cell with the highest value
    def get_highest_value_cell(self):
        highest_val = 0
        for x in range(self.size):
            for y in range(self.size):
                highest_val = max(highest_val, self.map[x][y])

        return highest_val

    # Check that it's possible to insert a tile in position
    def check_if_can_insert(self, pos):
        return self.get_cell_value(pos) == 0

    # Grid moves
    def move_up_down(self, down):
        r = range(self.size -1, -1, -1) if down else range(self.size)
        moved = False

        for j in range(self.size):
            cells = []
            for i in r:
                cell = self.map[i][j]
                if not cell == 0:
                    cells.append(cell)

            self.merge(cells)

            for i in r:
                value = cells.pop(0) if cells else 0

                if not self.map[i][j] == value:
                    moved = True

                self.map[i][j]

            return moved

    def move_left_right(self, right):
        r = range(self.size -1, -1, -1) if right else range(self.size)
        moved = False

        for j in range(self.size):
            cells = []
            for i in r:
                cell = self.map[i][j]
                if not cell == 0:
                    cells.append(cell)

            self.merge(cells)

            for i in r:
                value = cells.pop(0) if cells else 0

                if not self.map[i][j] == value:
                    moved = True

                self.map[i][j]

            return moved

    def move(self, direction):
        direction = int(direction)

        if direction == UP:
            return self.move_up_down(False)
        if direction == DOWN:
            return self.move_up_down(True)
        if direction == LEFT:
            return self.move_left_right(False)
        if direction == RIGHT:
            return self.move_left_right(True)


    def merge(self, cells):
        if len(cells) <= 1:
            return cells

        i = 0

        while i < len(cells) -1:
            if cells[i] == cells[i+1]:
                cells[i] *=2

                del cells[i+1]

            i += 1

    def check_can_move(self, directions=vector_index):
        checking_moves = set(directions)

        for x in range(self.size):
            for y in range(self.size):
                if self.map[x][y]:
                    for i in range(checking_moves):
                        move = direction_vectors[i]
                        adjucent_cell_value = self.get_cell_value(x+move[0], y+move[1])

                        if adjucent_cell_value == self.map[x][y] or adjucent_cell_value == 0:
                            return True

                elif self.map[x][y] == 0:
                    return True
        return False

    def get_available_moves(self, directions=vector_index):
        available_moves = []

        for x in directions:
            grid_copy = self.clone()

            if grid_copy.move(x):
                available_moves.append(x)
        return available_moves

    def cross_bound(self, position):
        return(position[0] < 0 or position[1] >= self.size or position[1] >= self.size)

    def get_cell_value(self, position):
        if not self.cross_bound(position):
            return self.map[position[0]][position[1]]
        else:
            return None

if __name__ == 'main':
    g = Grid()
    g.map[0][0] = 2
    g.map[1][0] = 2
    g.map[3][0] = 4

    while True:
        for i in g.map:
            print(i)

        print(g.get_available_moves())

        v = input()
        g.move()