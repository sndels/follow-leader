import sys
import os
import random
from OpenGL.GL import *
from PyQt4 import Qt, QtGui, QtCore
from PyQt4.QtOpenGL import *
from vector import Vector2f
from parameters import PLeader, PFollower, PGlobal, PInfo
from leader import Leader
from follower import Follower
from grid import Grid

class GLWidget(QGLWidget):
    def __init__(self):
        super(GLWidget, self).__init__()
        self.xres = 1024
        self.yres = 768
        self.setMinimumSize(self.xres,self.yres)
        self.info = PInfo()
        self.globalParams = PGlobal()

        self.leaderParams = PLeader()
        self.leader = Leader(self.leaderParams, self.globalParams)
        self.followerParams = PFollower()

        self.grid = Grid()
        self.followers = []
        self.setFollowers()

        # set info timer
        self.infoTimer = QtCore.QTime()
        self.infoTimer.start()
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

    def setFollowers(self):
        num = self.followerParams.num - len(self.followers)
        if num > 0:
            for i in range(0,num):
                self.followers.append(Follower(self.leader, self.followerParams,\
                                               self.globalParams, self.grid))
        elif num < 0:
            num *= -1
            for i in range(0, num):
                popd = self.followers.pop()
                self.grid.remove(popd, popd.loc.x, popd.loc.y)

    def compute(self):
        # compTime = self.infoTimer.elapsed()
        self.setFollowers()
        self.leader.move()
        collisions = 0
        for i in self.followers:
            collisions += i.move(self.followers)
        self.info.collisionChecks = collisions
        # self.info.computeTime.pop(0)
        # compTime = self.infoTimer.elapsed() - compTime
        # self.info.computeTime.append(compTime)

    def paintGL(self):
        self.info.computeTime.pop(0)
        compTime = self.infoTimer.elapsed() - self.info.lastFrame
        self.info.computeTime.append(compTime)
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        self.leader.render()
        for i in self.followers:
            i.render()
        curTime = self.infoTimer.elapsed()
        self.info.frameTime.pop(0)
        self.info.frameTime.append(curTime - self.info.lastFrame)
        self.info.lastFrame = curTime
        self.updateInfo()

    def updateInfo(self):
        print("FPS: " + str(1 / (sum(self.info.frameTime)/1000/len(self.info.frameTime))))
        print("Collision checks: " + str(self.info.collisionChecks))
        print("RendToRend: " + str(sum(self.info.computeTime)/len(self.info.computeTime)) + 'ms\n')

    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glOrtho(-w/h, w/h, -1, 1, -1.0, 1.0)
        glViewport(0, 0, w, h)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space and not event.isAutoRepeat():
            self.leader.toggleControl()
        elif self.leader.isControlled():
            if event.key() == QtCore.Qt.Key_Left:
                self.leader.turn('L')
            elif event.key() == QtCore.Qt.Key_Right:
                self.leader.turn('R')

    def setLeaderTarget(self, target):
        vecTarget = Vector2f(target.x(), target.y())
        vecTarget.x -= 16
        vecTarget.y = 768 - (vecTarget.y - 23)
        if vecTarget.x > 0 and vecTarget.x < 1024 and vecTarget.y > 0 and vecTarget.y < 768:
            self.leader.goTo(vecTarget)

class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        random.seed(100)
        self.glWidget = GLWidget()
        self.globalSpeedLabel = self.createLabel("Global Speed")
        self.globalSpeedSlider = self.createSlider(0, 20, 1)
        self.globalSpeedSlider.valueChanged.connect(self.glWidget.globalParams.setSpeed)

        self.leaderSpeedLabel = self.createLabel("Leader Speed")
        self.leaderSpeedSlider = self.createSlider(1, 15, 1)
        self.leaderSpeedSlider.valueChanged.connect(self.glWidget.leaderParams.setMaxV)

        self.followerAmountLabel = self.createLabel("Follower Amount")
        self.followerAmountSlider = self.createSlider(10, 150, 5)
        self.followerAmountSlider.valueChanged.connect(self.glWidget.followerParams.setNum)

        self.followerSpeedLabel = self.createLabel("Follower Speed")
        self.followerSpeedSlider = self.createSlider(1, 15, 1)
        self.followerSpeedSlider.valueChanged.connect(self.glWidget.followerParams.setMaxV)

        self.followerSeparationLabel = self.createLabel("Follower Separation")
        self.followerSeparationSlider = self.createSlider(20, 50, 5)
        self.followerSeparationSlider.valueChanged.connect(self.glWidget.followerParams.setSeparation)

        self.followDistanceLabel = self.createLabel("Follow Distance")
        self.followDistanceSlider = self.createSlider(20, 160, 20)
        self.followDistanceSlider.valueChanged.connect(self.glWidget.followerParams.setFollowDist)

        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(self.glWidget, 0, 0, 30, 1)
        mainLayout.addWidget(self.globalSpeedLabel, 0, 1, 1, 20)
        mainLayout.addWidget(self.globalSpeedSlider, 1, 1, 1, 20)
        mainLayout.addWidget(self.leaderSpeedLabel, 3, 1, 1, 20)
        mainLayout.addWidget(self.leaderSpeedSlider, 4, 1, 1, 20)
        mainLayout.addWidget(self.followerAmountLabel, 6, 1, 1, 20)
        mainLayout.addWidget(self.followerAmountSlider, 7, 1, 1, 20)
        mainLayout.addWidget(self.followerSpeedLabel, 9, 1, 1, 20)
        mainLayout.addWidget(self.followerSpeedSlider, 10, 1, 1, 20)
        mainLayout.addWidget(self.followerSeparationLabel, 12, 1, 1, 20)
        mainLayout.addWidget(self.followerSeparationSlider, 13, 1, 1, 20)
        mainLayout.addWidget(self.followDistanceLabel, 15, 1, 1, 20)
        mainLayout.addWidget(self.followDistanceSlider, 16, 1, 1, 20)
        self.setLayout(mainLayout)

        self.globalSpeedSlider.setValue(self.glWidget.globalParams.speed * 10)
        self.leaderSpeedSlider.setValue(self.glWidget.leaderParams.maxV * 10)
        self.followerAmountSlider.setValue(self.glWidget.followerParams.num)
        self.followerSpeedSlider.setValue(self.glWidget.followerParams.maxV * 10)
        self.followerSeparationSlider.setValue(self.glWidget.followerParams.separationD)
        self.followDistanceSlider.setValue(self.glWidget.followerParams.followDist)

        self.setWindowTitle("Follow the leader")

    def createSlider(self, minValue, maxValue, step):
        slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        slider.setRange(minValue, maxValue)
        slider.setTickInterval(step)
        slider.setTickPosition(QtGui.QSlider.TicksBelow)
        return slider

    def createLabel(self, text):
        label = QtGui.QLabel(text)
        label.setAlignment(QtCore.Qt.AlignHCenter)
        return label

    def keyPressEvent(self, event):
        self.glWidget.keyPressEvent(event)

    def mousePressEvent(self, event):
        self.glWidget.setLeaderTarget(event.pos())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())
