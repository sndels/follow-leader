from OpenGL.GL import *
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtOpenGL import *
from vector import Vector2f
from parameters import PLeader, PFollower
from leader import Leader
from follower import Follower


class OGLWidget(QGLWidget):
    def __init__(self):
        super(OGLWidget, self).__init__()
        self.xres = 1280
        self.yres = 720
        self.setMinimumSize(self.xres,self.yres)

        leaderParams = PLeader()
        self.leader = Leader(leaderParams)
        followerParams = PFollower()
        self.follower = Follower(self.leader, followerParams)

        # set compute timer
        self.computeTimer = QtCore.QTimer()
        self.computeTimer.setInterval(16)
        self.computeTimer.timeout.connect(self.compute)
        self.computeTimer.start()
        # set render timer
        self.renderTimer = QtCore.QTimer()
        self.renderTimer.setInterval(16)
        self.renderTimer.timeout.connect(self.updateGL)
        self.renderTimer.start()

    def compute(self):
        self.leader.move()
        self.follower.move()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        self.leader.render()
        self.follower.render()

    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glOrtho(-w/h, w/h, -1, 1, -1.0, 1.0)
        glViewport(0, 0, w, h)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

if __name__ == '__main__':
    app = QtGui.QApplication(["Lol, ikkuna"])
    window = OGLWidget()
    window.show()

    app.exec_()
