import pyxel
import random

class App:

    def __init__(self):
        self.cells = [[0 for j in range(10)] for i in range(10)]#mineが埋まっている場所
        self.mine_serch = [[0 for j in range(10)] for i in range(10)] #周り8マスにmineが何個 あるかどうか
        self.mine_check = [[0 for j in range(10)] for i in range(10)] #そのマスが既に開かれてるかどうか
        self.flag_set = [[0 for j in range(10)] for i in range(10)]# position of flags
        self.mine_num = 0
        self.mine_left = 0
        self.put_mines()
        self.check_mine()
        self.play_game = True

        pyxel.init(220, 220)
        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def put_mines(self):
        self.mine_num = 0
        for j in range(0, 10):
            for i in range(0, 10):
                if (random.randint(0,5) == 0): #1/5の確率でmineを置く(mine == 1)
                    self.cells[j][i] = 1
                    self.mine_num += 1
                else:
                    self.cells[j][i] = 0

    def check_mine(self):
        for j in range(0, 10):
            for i in range(0, 10):
                for h in range(-1, 2):
                    for w in range(-1, 2):
                        if (0 <= j + h < 10 and 0 <= i + w < 10 ):
                            if (self.cells[j][i] == 1):
                                self.mine_serch[j][i] = 10 #反応させないように書き換える
                            else:
                                if(self.cells[j + h][i + w] == 1):
                                    self.mine_serch[j][i] += 1
                            #else:
                                #self.mine_serch[j][i] = self.cells[j + h][i + w] #glitchが0,1で成り立っているから

    def check_lclick(self):
        if(self.cells[self.cells_x][self.cells_y] == 1): #mineを掘り当てたら
            self.open_all()
        else:
            self.mine_check[self.cells_x][self.cells_y] = 1

    def open_all(self):
        for j in range(0, 10):
            for i in range(0, 10):
                self.mine_check[j][i] = 1

    def check_rclick(self):
        self.flag_set[self.cells_x][self.cells_y] = 1

    def game_over(self):

        self.open_all()
        self.play_game = False
        pyxel.text(100, 100,"Game is over", 0)

    def game_clear(self):

        self.open_all()
        self.play_game = False
        pyxel.text(100, 100, "You dit it !!", 0)


    def update(self):
        if (self.play_game == True):
            self.cells_x = int((pyxel.mouse_x - 10) / 20)  # cast変換
            self.cells_y = int((pyxel.mouse_y - 10) / 20)
            if (self.cells_x > 0 or self.cells_y > 0 or self.cells_x < 10 or self.cells_y < 10):
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                    self.check_lclick()
                if pyxel.btnp(pyxel.MOUSE_RIGHT_BUTTON):
                    self.check_rclick()


    def draw(self):

        pyxel.cls(7)
        for i in range(10, 220, 20):
                pyxel.line(10, i, 210, i, 0)
                pyxel.line(i, 10, i, 210, 0)
        for k in range(0,10):
            for j in range(0, 10):
                if(self.mine_check[k][j] == 1):
                    pyxel.rect((k + 1) * 20 - 10, (j + 1) * 20 - 10, 20, 20, 12)
                    pyxel.text((k + 1) * 20, (j + 1) * 20, str(self.mine_serch[k][j]), 0)
        for k in range(0,10):
            for j in range(0, 10):
                if(self.flag_set[k][j] == 1):
                    pyxel.rect((k + 1) * 20 - 10, (j + 1) * 20 - 10, 20, 20, 8)
        for i in range(10, 220, 20):
                pyxel.line(10, i, 210, i, 0)
                pyxel.line(i, 10, i, 210, 0)

App()
