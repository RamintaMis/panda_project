from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor


class WalkingPanda(ShowBase):
    def __init__(self, no_rotate=False, scale=False, change_color=False, disappear_panda=False, change_scenery=False):
        ShowBase.__init__(self)

        # Load the environment model.
        if change_scenery is False:
            self.scene = self.loader.loadModel("models/environment")
        else:
            self.scene = self.loader.loadModel("walking_panda/OldWestTerrain/OldWestTerrain")

        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        if no_rotate is False:
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        else:
            self.taskMgr.add(self.no_spinCameraTask, "NoSpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})

        # Change Panda's color
        if change_color is True:
            self.pandaActor.setColor(0.8, 0.4, 0.6, 1)

        # Make panda disappear
        if disappear_panda is True:
            self.pandaActor.hide()

        # Changing panda's size
        if scale is False:
            self.pandaActor.setScale(0.005, 0.005, 0.005)
        else:
            self.pandaActor.setScale(0.001, 0.001, 0.001)

        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")
        # Adding sound effects
        mySound = self.loader.loadSfx("walking_panda/sound/sound_effect.mp3")
        mySound.play()

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont


    def no_spinCameraTask(self, task):
        angleDegrees = task.time * 0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
