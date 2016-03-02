from OpenGL.GL import *

'''
Draws an arrow

pos2f - x,y position as Vector2f
scale1f - 1.0 gives an arrow that fills the screen
angle1f - degrees counter clockwise with arrow initially pointing right
'''
def drawArrow(pos2f, scale1f, angle1f):
    glLoadIdentity()
    glTranslatef(pos2f.x, pos2f.y, 0.0)
    glRotatef(angle1f, 0.0, 0.0, 1.0)
    glScalef(scale1f, scale1f, scale1f)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0); glVertex2f(-1.0, 0.8)
    glColor3f(1.0, 0.0, 0.0); glVertex2f(-0.4, 0.0)
    glColor3f(1.0, 0.0, 0.0); glVertex2f( 1.0, 0.0)
    glColor3f(1.0, 0.0, 0.0); glVertex2f( 1.0, 0.0)
    glColor3f(1.0, 0.0, 0.0); glVertex2f(-0.4, 0.0)
    glColor3f(1.0, 0.0, 0.0); glVertex2f(-1.0,-0.8)
    glEnd()
