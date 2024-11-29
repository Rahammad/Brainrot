from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3

class VRGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load environment model
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add a rotating camera
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

    def spinCameraTask(self, task):
        angle = task.time * 10
        self.camera.setPos(Point3(20 * task.time % 360, -30, 10))
        self.camera.lookAt(self.render)
        return task.cont

# Run the game
game = VRGame()
game.run()
