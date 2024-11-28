from direct.showbase.ShowBase import ShowBase


class VRGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.scene=self.loader.loadModel("models/environment")

        self.scene.reparentTo(self.render)
        self.scene.setScale(0.5,0.5,0.5)
vr_game=VRGame()
vr_game.run()
