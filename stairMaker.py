"""
The Stair Maker 3000
By Chase Miller

Instructions: 
1. *Windows- Place script file in: C:\Users\NAME\Documents\maya\2019\scripts
2. copy paste into python console -
    import stairMaker
    reload(stairMaker)
    stairMaker.StairUI().show()
3. Highlight, then middle mouse drag code to shelf
"""

from maya import cmds
import stairCreator as stair

class BaseWindow(object):
    windowName = "BaseWindow"

    def show(self):
        if cmds.window(self.windowName, query=True, exists=True):
            self.close()

        cmds.window(self.windowName)
        self.buildUI()
        cmds.showWindow()

    def reset(self, *arg):
        cmds.intSliderGrp(self.count_value, edit=True, value=20)
        cmds.intSliderGrp(self.height_value, edit=True, value=1)
        cmds.intSliderGrp(self.width_value, edit=True, value=10)
        cmds.intSliderGrp(self.length_value, edit=True, value=24)

    def close(self, *args):
        cmds.deleteUI(self.windowName)

class StairUI(BaseWindow):
    windowName = "The Stair Maker 3000"

    def __init__(self):
        self.stair = None
        self.transform = None
        self.extrude = None
        self.constructor = None

    def buildUI(self):
        column = cmds.columnLayout(adj=True)

        cmds.separator(style=None, bgc=(0.31, 0.31, 0.31), h=3)
        cmds.text(label="   Stair Attributes", align="left", bgc=(0.31, 0.31, 0.31))
        cmds.separator(style=None, bgc=(0.31, 0.31, 0.31), h=3)

        self.count_value = cmds.intSliderGrp(label='Step Count', min=1, max=99, value=20, field=True)
        self.height_value = cmds.intSliderGrp(label='Height', min=1, max=10, value=1, field=True)
        self.width_value = cmds.intSliderGrp(label='Width', min=1, max=999, value=10, field=True)
        self.length_value = cmds.intSliderGrp(label='Length', min=1, max=999, value=24, field=True)
        cmds.button(label="Make Stair", command=self.makeStair)
        cmds.button(label="Reset", align = "right", command=self.reset)

    def makeStair(self, *args):

        # check what the slider value is set to
        steps = cmds.intSliderGrp(self.count_value, query=True, value=True)
        height = cmds.intSliderGrp(self.height_value, query=True, value=True)
        width = cmds.intSliderGrp(self.width_value, query=True, value=True)
        length = cmds.intSliderGrp(self.length_value, query=True, value=True)

        #create stair with set values
        self.stair = stair.Stair()
        self.transform, self.constructor = \
            cmds.polyPlane(n= 'stairCase*', subdivisionsHeight=steps, subdivisionsWidth=1, width=width,height=length)
        self.frontFaces = range(steps)

        for face in self.frontFaces:
            self.extrude = \
            cmds.polyExtrudeFacet('%s.f[%s:%s]' % (self.transform, face, steps - 1), localTranslateZ=height)[0]

        cmds.select(clear=True)

