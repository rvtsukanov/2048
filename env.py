import numpy as np

class Game(object):
    def __init__(self, n = 3):
        self.counter = 0
        self.n = n
        self.field = np.zeros((n, n))

    def print(self):
        print(self.field)

    def rand(self, n, val):
        indexes = np.random.choice(self.n ** 2, n, replace=False)
        self.field = np.reshape(self.field, -1)
        for i in indexes:
            self.field[i] = val
        self.field = np.reshape(self.field, (self.n, self.n))

    def __upd(self):
        for i in range(1, self.n):
            for j in range(0, self.n):
                if self.field[i, j] != 0:
                    for i_t in range(i - 1, -1, -1):
                        if i_t == 0 or self.field[i_t, j] != 0:
                            if self.field[i_t, j] == self.field[i, j]:
                                self.field[i_t, j] = self.field[i, j] * 2
                                self.field[i, j] = 0
                                break
                            elif self.field[i_t, j] != 0:
                                tmp = self.field[i, j]
                                self.field[i, j] = 0
                                self.field[i_t + 1, j] = tmp
                                break
                            else:
                                self.field[i_t, j] = self.field[i, j]
                                self.field[i, j] = 0
                                break

    def next_step(self):
        self.field = np.reshape(self.field, -1)
        ind = []
        for num, it in enumerate(self.field):
            if it == 0:
                ind.append(num)
        if len(ind) == 0:
            print("game over")
            pass
        else:
            new_ind = np.random.choice(ind, 1, replace=False)
            self.field[new_ind] = 2
        self.field = np.reshape(self.field, (self.n, self.n))


    def move(self, step):
        if step == "up":
            self.__upd()
        if step == "down":
            self.field = np.rot90(self.field, k = 2)
            self.__upd()
            self.field = np.rot90(self.field, k = 2)
        if step == "right":
            self.field = np.rot90(self.field)
            self.__upd()
            self.field = np.rot90(self.field, k = 3)
        if step == "left":
            self.field = np.rot90(self.field, k = 3)
            self.__upd()
            self.field = np.rot90(self.field)


