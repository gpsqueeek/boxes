# Copyright (C) 2013-2014 Florian Festi
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from boxes import *
from boxes.lids import _TopEdge

class NightLightBox(_TopEdge):
    """Simple decorative lamp with creatively laser cut plates"""

    ui_group = "Misc"
    description = "This is a simple light box with a closed compartment for electronics and the backlighting."

    def __init__(self) -> None:
        Boxes.__init__(self)
        self.addSettingsArgs(edges.FingerJointSettings, surroundingspaces=.5)
        self.addSettingsArgs(edges.StackableSettings)
        self.addSettingsArgs(edges.HingeSettings)
        self.argparser.add_argument(
            "--PlateVisibleWidth",  action="store", type=float, default=150.0,
            help="width of the window in the front panel in mm")
        self.argparser.add_argument(
            "--PlateVisibleHeight",  action="store", type=float, default=75.0,
            help="height of the window in the front panel in mm")
        self.argparser.add_argument(
            "--WoodPlatesCount",  action="store", type=int, default=3,
            help="Number of decorative wood plates")
        self.argparser.add_argument(
            "--WoodPlateThickness",  action="store", type=float, default=5.0,
            help="Thickness of the wood plates in mm")
        self.argparser.add_argument(
            "--DiffuserPlateThickness",  action="store", type=float, default=5.0,
            help="Thickness of the background acrylic diffuser plate in mm")
        self.argparser.add_argument(
            "--BackgroundDepth",  action="store", type=float, default=40.0,
            help="Depth of the background zone for the electronics and LEDs in mm")
        self.argparser.add_argument(
            "--InterPlateSpacing",  action="store", type=float, default=10,
            help="Space between the decorative plates in mm")
        self.argparser.add_argument(
            "--Margin",  action="store", type=float, default=0.5,
            help="Margin for moving parts in mm")
    
    def railSlots(self, xSize, ySize):
        # to be updated
        self.fingerHolesAt(self.thickness*1.5, self.InterPlateSpacing - self.thickness - self.Margin/2, self.thickness*2 + self.DiffuserPlateThickness + (self.InterPlateSpacing + self.WoodPlateThickness) * self.WoodPlatesCount)
        self.fingerHolesAt(xSize - (self.thickness*1.5), self.InterPlateSpacing - self.thickness - self.Margin/2, self.thickness*2 + self.DiffuserPlateThickness + (self.InterPlateSpacing + self.WoodPlateThickness) * self.WoodPlatesCount)
            
    def woodPlate(self, move=None, label=""):
        if self.move(self.PlateVisibleWidth + self.thickness*6, self.PlateVisibleHeight + self.thickness*4, move, True):
            return
        # visible zone
        self.rectangularHole(self.thickness*3, self.thickness*2, self.PlateVisibleWidth, self.PlateVisibleHeight, center_x=False, center_y=False, color=Color.ANNOTATIONS)
        # bottom
        self.moveTo(self.thickness + self.Margin/2, 0, 0)
        self.edge(self.thickness - self.Margin)
        self.corner(90)
        self.edge(self.thickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin)
        self.corner(90)
        self.edge(self.PlateVisibleWidth - self.Margin)
        self.corner(90)
        self.edge(self.thickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin)
        self.corner(90)
        self.edge(self.thickness - self.Margin)
        self.corner(90)
        # right side
        self.edge(self.PlateVisibleHeight + self.thickness*2 + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin/2)
        self.corner(90)
        self.edge(self.thickness*2 - self.Margin*2)
        self.corner(90)
        # top
        self.edge(self.PlateVisibleWidth + self.thickness*6)
        self.corner(90)
        # left side
        self.edge(self.thickness*2 - self.Margin*2)
        self.corner(90)
        self.edge(self.thickness + self.Margin/2)
        self.corner(-90)
        self.edge(self.PlateVisibleHeight + self.thickness*2 + self.Margin)
        self.corner(90)
        # move plate
        self.move(self.PlateVisibleWidth + self.thickness*6, self.PlateVisibleHeight + self.thickness*4, move, label=label)
    
    def diffuserPlate(self, move=None, label=""):
        if self.move(self.PlateVisibleWidth + self.thickness*4, self.PlateVisibleHeight + self.thickness*4, move, True):
            return
        # bottom
        self.edge(self.thickness - self.Margin)
        self.corner(90)
        self.edge(self.thickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin)
        self.corner(90)
        self.edge(self.PlateVisibleWidth - self.Margin)
        self.corner(90)
        self.edge(self.thickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin)
        self.corner(90)
        self.edge(self.thickness - self.Margin)
        self.corner(90)
        # right side
        self.edge(self.thickness*6 - 1)
        self.corner(90)
        self.edge(self.thickness)
        self.corner(-90)
        self.edge(2)
        self.corner(-90)
        self.edge(self.thickness)
        self.corner(90)
        self.edge(self.PlateVisibleHeight - self.thickness*2 - self.Margin - 1)
        self.corner(90)
        # top
        self.edge(self.PlateVisibleWidth + self.thickness*4 - self.Margin)
        self.corner(90)
        # left side
        self.edge(self.PlateVisibleHeight - self.thickness*2 - self.Margin - 1)
        self.corner(90)
        self.edge(self.thickness)
        self.corner(-90)
        self.edge(2)
        self.corner(-90)
        self.edge(self.thickness)
        self.corner(90)
        self.edge(self.thickness*6 - 1)
        self.corner(90)
        # move plate
        self.move(self.PlateVisibleWidth + self.thickness*4, self.PlateVisibleHeight + self.thickness*4, move, label=label)
    
    def elecCompartmentTop(self, move=None, label=""):
        if self.move(self.thickness * 4 + self.PlateVisibleWidth + self.Margin, self.BackgroundDepth - self.thickness*2.5 - self.Margin, move, True):
            return
        # bottom
        self.edge(self.thickness * 4 + self.PlateVisibleWidth + self.Margin)
        self.corner(90)
        # right side
        self.edge(self.thickness)
        self.edges["f"](self.BackgroundDepth - self.thickness*3.5 - self.Margin)
        self.corner(90)
        # top
        self.edge(self.thickness * 4 + self.PlateVisibleWidth + self.Margin)
        self.corner(90)
        # left side
        self.edges["f"](self.BackgroundDepth - self.thickness*3.5 - self.Margin)
        self.edge(self.thickness)
        self.corner(90)
        # move plate
        self.move(self.thickness * 4 + self.PlateVisibleWidth + self.Margin, self.BackgroundDepth - self.thickness*2.5 - self.Margin, move, label=label)
        
    def side(self, ySize, hSize, bEdge, tEdge, move=None, label=""):
        if self.move(ySize + self.thickness, hSize + self.thickness*4, move, True):
            return
        # rectangular hole for background guiding
        self.rectangularHole(ySize - self.BackgroundDepth - self.DiffuserPlateThickness - self.thickness - self.Margin*1.5, self.PlateVisibleHeight + self.thickness*4, self.thickness, self.thickness, center_x=False, center_y=False)
        # round hole for background lock screw
        self.hole(ySize - self.BackgroundDepth - self.DiffuserPlateThickness/2 - self.Margin/2, self.thickness*10, 0.5)
        # bottom
        self.edges[bEdge](ySize)
        self.corner(90)
        # right side
        self.edge(self.thickness*4) # stackable feet height, to be replaced woth actual parameter
        self.edges["f"](hSize)
        self.corner(90)
        # top
        self.edges["i"](self.thickness*3.5)
        self.edges["F"](self.BackgroundDepth - self.thickness*3.5 - self.Margin/2)
        self.edge(self.DiffuserPlateThickness + self.InterPlateSpacing + self.Margin/2)
        for i in range(self.WoodPlatesCount):
            self.corner(90)
            self.edge(self.thickness*2 + self.Margin)
            self.corner(-90)
            self.edge(self.WoodPlateThickness + self.Margin)
            self.corner(-90)
            self.edge(self.thickness*2 + self.Margin)
            self.corner(90)
            self.edge(self.InterPlateSpacing - self.Margin)
        self.corner(90)
        # left side
        self.edges["f"](hSize)# + self.thickness*2)self.corner(90)
        self.edge(self.thickness*4)
        # move plate
        self.move(ySize + self.thickness, hSize + self.thickness*8, move, label=label)
    
    def rail(self, move=None, label=""):
        if self.move(self.WoodPlatesCount * (self.InterPlateSpacing + self.WoodPlateThickness) + self.DiffuserPlateThickness + self.thickness*2, self.thickness*3, move, True):
            return
        # bottom
        self.edges["f"](self.thickness*2 + self.DiffuserPlateThickness + (self.InterPlateSpacing + self.WoodPlateThickness) * self.WoodPlatesCount)
        self.corner(90)
        # right side
        self.edge(self.thickness*2)
        self.corner(90)
        # top
        self.edge(self.thickness - self.Margin/2)
        self.corner(90)
        for i in range(self.WoodPlatesCount):
            self.edge(self.thickness + self.Margin)
            self.corner(-90)
            self.edge(self.WoodPlateThickness + self.Margin)
            self.corner(-90)
            self.edge(self.thickness + self.Margin)
            self.corner(90)
            self.edge(self.InterPlateSpacing - self.Margin)
            self.corner(90)
        self.edge(self.thickness + self.Margin)
        self.corner(-90)
        self.edge(self.DiffuserPlateThickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin)
        self.corner(90)
        self.edge(self.thickness - self.Margin/2)
        self.corner(90)
        # left side
        self.edge(self.thickness*2)
        self.corner(90)
        # move plate
        self.move(self.WoodPlatesCount * (self.InterPlateSpacing + self.WoodPlateThickness) + self.DiffuserPlateThickness + self.thickness*2, self.thickness*3, move, label=label)
            
    def render(self):
        # define box inner depth
        y = self.BackgroundDepth + self.DiffuserPlateThickness + (self.WoodPlateThickness + self.InterPlateSpacing) * self.WoodPlatesCount + self.InterPlateSpacing #+ self.thickness*2
        # define box inner width
        x = self.thickness * 4 + self.PlateVisibleWidth + self.Margin
        #define box inner height
        h = self.PlateVisibleHeight + self.thickness * 4 + self.Margin
        
        b = "s"
        t1, t2, t3, t4 = self.topEdges("i")
        #if top_edge is t put the handle on the x walls
        self.ctx.save()

        # sides
        self.side(y, h, b, t1, move="mirror", label="right")
        self.side(y, h, b, t1, move="left up", label="left")
        
        # simple sides for debug
        #self.rectangularWall(y, h, [b, "F", t1, "F"], move="mirror", label="right dbg")
        #self.rectangularWall(y, h, [b, "F", t1, "F"], move="left up", label="left dbg")
        
        #rails
        self.rail(move="up", label="rail")
        self.rail(move="up mirror", label="rail")
        
        # floor
        if b != "e":
            self.rectangularWall(x, y, "ffff", callback=[lambda:self.railSlots(x, y)], move="up", label="bottom")
        
        # back
        self.rectangularWall(x, h, [b, "F", t2, "F"], move="up", label="back")
        
        # front
        self.rectangularWall(x, h, [b, "F", t2, "F"], callback=[lambda:self.rectangularHole(self.PlateVisibleWidth/2 + self.thickness*2,self.PlateVisibleHeight/2 + self.thickness*2,self.PlateVisibleWidth, self.PlateVisibleHeight)], move="up", label="front")
        
        # electronics compartment top
        self.elecCompartmentTop(move="up", label="elec. comp.")
        
        # difuser guides
        self.rectangularWall(self.thickness*2, self.thickness, "eeee", move="up", label="guide")
        self.rectangularWall(self.thickness*2, self.thickness, "eeee", move="up", label="guide")
        
        # top / lid
        self.drawLid(x, y, "i")
        self.lid(x, y, "i")
        #self.ctx.restore()
        
        # diffuser plate
        self.diffuserPlate(move="up", label="Diffuser")
        
        # wood plates with horizontal LEDs
        for i in range(self.WoodPlatesCount):
            self.woodPlate(move="up", label="Insert cut and\nengraved art here")
        
        
