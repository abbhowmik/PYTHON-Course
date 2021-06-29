class Remote():
    pass


class Player:
    def moveright(self):
        pass

    def moveleft(self):
        pass

    def moveTop(self):
        pass


remote1 = Remote()
player1 = Player()

if (remote1.isLeftPressed()):
    Player.moveLeft()
# it is just an example that how we used class as real word as possible
