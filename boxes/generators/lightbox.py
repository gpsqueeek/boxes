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

class LightBox(_TopEdge):
    """Advanced decorative lamp with creatively laser cut plates"""

    ui_group = "Misc"
    description = "This is an advanced light box with options for LED positionning on the different modules."

    def __init__(self) -> None:
        Boxes.__init__(self)
        self.addSettingsArgs(edges.FingerJointSettings, surroundingspaces=.5)
        self.addSettingsArgs(edges.StackableSettings)
        self.addSettingsArgs(edges.HingeSettings)
        self.addSettingsArgs(edges.CabinetHingeSettings)
        self.addSettingsArgs(lids.LidSettings)
        self.buildArgParser(bottom_edge="s", top_edge="i")
        self.argparser.add_argument(
            "--PlateVisibleWidth",  action="store", type=float, default=200.0,
            help="width of the window in the front panel in mm")
        self.argparser.add_argument(
            "--PlateVisibleHeight",  action="store", type=float, default=100.0,
            help="height of the window in the front panel in mm")
        self.argparser.add_argument(
            "--WoodPlatesWithHLedsCount",  action="store", type=int, default=1,
            help="Number of wood plates with horizontal LEDs support")
        self.argparser.add_argument(
            "--WoodPlatesWithoutHLedsCount",  action="store", type=int, default=2,
            help="Number of wood plates without horizontal LEDs support")
        self.argparser.add_argument(
            "--WoodPlateThickness",  action="store", type=float, default=3.0,
            help="Thickness of the wood plates in mm")
        self.argparser.add_argument(
            "--AcrylicPlatesCount",  action="store", type=int, default=1,
            help="Number of acrylic plates (except background)")
        self.argparser.add_argument(
            "--AcrylicPlateThickness",  action="store", type=float, default=5.0,
            help="Thickness of the acrylic plates in mm")
        self.argparser.add_argument(
            "--ThickModuleDepth",  action="store", type=float, default=40.0,
            help="Depth of the thick modules (background, acrylic, wood with LEDs) in mm")
        self.argparser.add_argument(
            "--ThinModuleDepth",  action="store", type=float, default=20.0,
            help="Depth of the thin modules (wood without LEDs) in mm")
        self.argparser.add_argument(
            "--Margin",  action="store", type=float, default=0.2,
            help="Margin for moving parts in mm")
        self.argparser.add_argument(
            "--BoxDepthMargin",  action="store", type=float, default=1.0,
            help="Margin for box depth in per cent")
        self.argparser.add_argument(
            "--HasLateralLeds",  action="store", type=boolarg, default=True,
            help="Modules have support for lateral LEDs")
        
        

    def railSlots(self, xSize, ySize):
        if self.HasLateralLeds:
            self.fingerHolesAt(self.thickness*4.5 + self.Margin, self.thickness + self.Margin, ySize - self.thickness*2)
            self.fingerHolesAt(xSize - (self.thickness*4.5 + self.Margin), self.thickness + self.Margin, ySize - self.thickness*2)
        else:
            self.fingerHolesAt(self.thickness*1.5 + self.Margin, self.thickness + self.Margin, ySize - self.thickness*2)
            self.fingerHolesAt(xSize - (self.thickness*1.5 + self.Margin), self.thickness + self.Margin, ySize - self.thickness*2)
    
    def plate(self, IsAcrylic, IsBackplane, move=None, label=""):
        if self.HasLateralLeds:
            if self.move(self.PlateVisibleWidth + self.thickness*8, self.PlateVisibleHeight + self.thickness*4, move, True):
                return
        else:
            if self.move(self.PlateVisibleWidth + self.thickness*2, self.PlateVisibleHeight + self.thickness*4, move, True):
                return
        # visible zone
        if not IsBackplane:
            if self.HasLateralLeds:
                self.rectangularHole(self.thickness*4, self.thickness*2, self.PlateVisibleWidth, self.PlateVisibleHeight, center_x=False, center_y=False, color=Color.ANNOTATIONS)
            else:
                self.rectangularHole(self.thickness, self.thickness*2, self.PlateVisibleWidth, self.PlateVisibleHeight, center_x=False, center_y=False, color=Color.ANNOTATIONS)
        # bottom
        if (IsAcrylic and not IsBackplane):
            # with slot for bottom LEDs
            if self.HasLateralLeds:
                self.edge(self.thickness*4)
            else:
                self.edge(self.thickness)
            self.corner(90)
            self.edge(self.thickness*2 - self.Margin/2)
            self.corner(-90)
            self.edge(self.PlateVisibleWidth)
            self.corner(-90)
            self.edge(self.thickness*2 - self.Margin/2)
            self.corner(90)
            if self.HasLateralLeds:
                self.edge(self.thickness*4)
            else:
                self.edge(self.thickness)
        else:
            # without slot for bottom LEDs
            if self.HasLateralLeds:
                self.edge(self.thickness*8 + self.PlateVisibleWidth)
            else:
                self.edge(self.thickness*2 + self.PlateVisibleWidth)
        self.corner(90)
        # right side
        if self.HasLateralLeds:
            # slot for latteral LEDs and its attachement
            self.edge(self.thickness - self.Margin/2)
            self.corner(90)
            self.edge(self.thickness + self.Margin/2)
            self.corner(-90)
            self.edge(self.thickness + self.Margin/2)
            self.corner(90)
            self.edge(self.thickness*2 - self.Margin/2)
            self.corner(-90)
            self.edge(self.PlateVisibleHeight)
            self.corner(-90)
            self.edge(self.thickness*2 - self.Margin/2)
            self.corner(90)
            self.edge(self.thickness + self.Margin/2)
            self.corner(-90)
            self.edge(self.thickness + self.Margin/2)
            self.corner(90)
            self.edge(self.thickness - self.Margin/2)
            self.corner(90)
            # slot for plate attachement
            self.edge(self.thickness*2 - self.Margin)
            self.corner(90)
            self.edge(self.thickness + self.Margin)
            self.corner(-90)
            self.edge(self.thickness + self.Margin)
            self.corner(-90)
            self.edge(self.thickness + self.Margin)
        else:
            self.edge(self.thickness*4 + self.PlateVisibleHeight)
        self.corner(90)
        # top
        if (IsAcrylic and not IsBackplane):
            # with slot for top LEDs
            self.edge(self.thickness)
            self.corner(90)
            self.edge(self.thickness*2 - self.Margin/2)
            self.corner(-90)
            self.edge(self.PlateVisibleWidth)
            self.corner(-90)
            self.edge(self.thickness*2 - self.Margin/2)
            self.corner(90)
            self.edge(self.thickness)
        else:
            # without slot for top LEDs
            self.edge(self.thickness*2 + self.PlateVisibleWidth)
        self.corner(90)
        # left side
        if self.HasLateralLeds:
            # slot for plate attachement
            self.edge(self.thickness + self.Margin)
            self.corner(-90)
            self.edge(self.thickness + self.Margin)
            self.corner(-90)
            self.edge(self.thickness + self.Margin)
            self.corner(90)
            self.edge(self.thickness*2 - self.Margin)
            self.corner(90)
            # slot for latteral LEDs and its attachement
            self.edge(self.thickness - self.Margin/2)
            self.corner(90)
            self.edge(self.thickness + self.Margin/2)
            self.corner(-90)
            self.edge(self.thickness + self.Margin/2)
            self.corner(90)
            self.edge(self.thickness*2 - self.Margin/2)
            self.corner(-90)
            self.edge(self.PlateVisibleHeight)
            self.corner(-90)
            self.edge(self.thickness*2 - self.Margin/2)
            self.corner(90)
            self.edge(self.thickness + self.Margin/2)
            self.corner(-90)
            self.edge(self.thickness + self.Margin/2)
            self.corner(90)
            self.edge(self.thickness - self.Margin/2)
        else:
            self.edge(self.thickness*4 + self.PlateVisibleHeight)
        self.corner(90)
        # move plate
        if self.HasLateralLeds:
            self.move(self.PlateVisibleWidth + self.thickness*8, self.PlateVisibleHeight + self.thickness*4, move, label=label)
        else:
            self.move(self.PlateVisibleWidth + self.thickness*2, self.PlateVisibleHeight + self.thickness*4, move, label=label)
    
    def genericPlateSupport(self, IsThinModule, IsBackplane, move=None, label=""):
    # TODO : add side holes in case of latteral LEDs for wiring
        if IsThinModule :
            if self.move(self.PlateVisibleHeight + self.thickness * 10, self.ThinModuleDepth, move, True):
                return
        else:
            if self.move(self.PlateVisibleHeight + self.thickness * 10, self.ThickModuleDepth, move, True):
                return
        # plate hole
        if IsBackplane:
            self.rectangularHole(self.thickness*2 - self.Margin/2, self.thickness - self.Margin/2, self.PlateVisibleHeight + self.thickness*4 + self.Margin, self.AcrylicPlateThickness + self.Margin, center_x=False, center_y=False)
        else:
            self.rectangularHole(self.thickness*2 - self.Margin/2, self.thickness - self.Margin/2, self.PlateVisibleHeight + self.thickness*4 + self.Margin, self.WoodPlateThickness + self.Margin, center_x=False, center_y=False)
        # bottom LED plate hole
        if not IsThinModule:
            self.rectangularHole(self.PlateVisibleHeight + self.thickness*6, self.thickness*2 + self.WoodPlateThickness, self.thickness + self.Margin, self.thickness + self.Margin, center_x=False, center_y=False)
        
        # bottom
        if self.HasLateralLeds:
            self.edge(self.thickness*8.5 + self.PlateVisibleHeight)
            self.corner(90)
            self.edge(self.thickness*1.5)
            self.corner(-90)
            self.edge(self.thickness*1.5)
        else:
            self.edge(self.thickness*10 + self.PlateVisibleHeight)
        self.corner(90)
        # right side
        if self.HasLateralLeds:
            if IsThinModule:
                self.edge(self.ThinModuleDepth - self.thickness*1.5)
            else:
                self.edge(self.ThickModuleDepth - self.thickness*1.5)
        else:
            if IsThinModule:
                self.edge(self.ThinModuleDepth)
            else:
                self.edge(self.ThickModuleDepth)
        self.corner(90)
        # top
        if IsBackplane:
            self.edge(self.thickness*9 + self.PlateVisibleHeight)
            self.corner(90)
            self.edge(self.thickness*2)
            self.corner(-90)
            self.edge(self.thickness)
        else:
            self.edge(self.thickness*10 + self.PlateVisibleHeight)
        self.corner(90)
        # left side
        if IsThinModule:
            self.edge(self.ThinModuleDepth - max(self.thickness, self.WoodPlateThickness) - self.thickness - self.Margin/2)
            self.corner(90)
            self.edge(self.thickness + self.Margin)
            self.corner(-90)
            self.edge(self.thickness + self.Margin)
            self.corner(-90)
            self.edge(self.thickness + self.Margin)
            self.corner(90)
            self.edge(max(self.thickness, self.WoodPlateThickness) - self.Margin/2)
        else:
            if IsBackplane:
                self.edge(self.ThickModuleDepth - self.thickness*5 - self.AcrylicPlateThickness - self.Margin/2)
            else:
                self.edge(self.ThickModuleDepth - self.thickness*3 - self.WoodPlateThickness - self.Margin/2)
            self.corner(90)
            self.edge(self.thickness + self.Margin)
            self.corner(-90)
            self.edge(self.thickness + self.Margin)
            self.corner(-90)
            self.edge(self.thickness + self.Margin)
            self.corner(90)
            if IsBackplane:
                self.edge(self.thickness*2 + self.AcrylicPlateThickness - self.Margin/2)
            else:
                self.edge(self.thickness*2 + self.WoodPlateThickness - self.Margin/2)
        self.corner(90)
        # move plate
        if IsThinModule :
            self.move(self.PlateVisibleHeight + self.thickness * 10, self.ThinModuleDepth, move, label=label)
        else:
            self.move(self.PlateVisibleHeight + self.thickness * 10, self.ThickModuleDepth, move, label=label)
        
    def acrylicPlateSupport(self, move=None, label=""):
    # TODO : add side holes in case of latteral LEDs for wiring
        if self.move(self.PlateVisibleHeight + self.thickness * 10, self.ThickModuleDepth, move, True):
            return
        # plate hole
        self.rectangularHole(self.thickness*2 - self.Margin/2, self.thickness*3 - self.Margin/2, self.PlateVisibleHeight + self.thickness*4 + self.Margin, self.AcrylicPlateThickness + self.Margin, center_x=False, center_y=False)
        # bottom LED plate hole
        self.rectangularHole(self.PlateVisibleHeight + self.thickness*7 - self.Margin/2, self.thickness*2.5 + self.AcrylicPlateThickness*0.5 - self.Margin/2, self.thickness + self.Margin, self.thickness + self.Margin, center_x=False, center_y=False)
        # top and bottom light limiters
        self.moveTo(self.thickness*3, self.thickness*1.5, 45)
        self.rectangularHole(0,0, self.thickness + self.Margin, self.thickness + self.Margin)
        self.moveTo(0,0,-45)
        self.moveTo(0, self.AcrylicPlateThickness + self.thickness*3, 45)
        self.rectangularHole(0, 0, self.thickness + self.Margin, self.thickness + self.Margin)
        self.moveTo(0,0,-45)
        self.moveTo(self.PlateVisibleHeight + self.thickness*2, 0, 45)
        self.rectangularHole(0, 0, self.thickness + self.Margin, self.thickness + self.Margin)
        self.moveTo(0,0,-45)
        self.moveTo(0, -self.AcrylicPlateThickness - self.thickness*3, 45)
        self.rectangularHole(0, 0, self.thickness + self.Margin, self.thickness + self.Margin)
        self.moveTo(0,0,-45)
        self.moveTo(-self.PlateVisibleHeight - self.thickness*5, -self.thickness*1.5,0)
        # bottom
        if self.HasLateralLeds:
            self.edge(self.thickness*8.5 + self.PlateVisibleHeight)
            self.corner(90)
            self.edge(self.thickness*1.5)
            self.corner(-90)
            self.edge(self.thickness*1.5)
        else:
            self.edge(self.thickness*10 + self.PlateVisibleHeight)
        self.corner(90)
        # right side
        if self.HasLateralLeds:
            self.edge(self.ThickModuleDepth - self.thickness*1.5)
        else:
            self.edge(self.ThickModuleDepth)
        self.corner(90)
        # top
        self.edge(self.thickness*10 + self.PlateVisibleHeight)
        self.corner(90)
        # left side
        self.edge(self.ThickModuleDepth - self.thickness*3.5 - self.AcrylicPlateThickness*0.5 - self.Margin/2)
        self.corner(90)
        self.edge(self.thickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin)
        self.corner(90)
        self.edge(self.thickness*2.5 + self.AcrylicPlateThickness*0.5 - self.Margin/2)
        self.corner(90)
        # move plate
        self.move(self.PlateVisibleHeight + self.thickness * 10, self.ThickModuleDepth, move, label=label)
        
    def horizontalLedSupport(self, move=None, label=""):
        if self.move(self.thickness*2 + self.PlateVisibleWidth, self.thickness*3, move, True):
            return
        # bottom
        self.edge(self.PlateVisibleWidth - self.Margin)
        self.corner(90)
        self.edge(self.thickness)
        self.corner(-90)
        self.edge(self.thickness + self.Margin/2)
        self.corner(90)
        # right side
        self.edge(self.thickness)
        self.corner(90)
        self.edge(self.thickness + self.Margin/2)
        self.corner(-90)
        self.edge(self.thickness)
        self.corner(90)
        # top
        self.edge(self.PlateVisibleWidth - self.Margin)
        self.corner(90)
        self.edge(self.thickness)
        self.corner(-90)
        self.edge(self.thickness + self.Margin/2)
        self.corner(90)
        # left side
        self.edge(self.thickness)
        self.corner(90)
        self.edge(self.thickness + self.Margin/2)
        self.corner(-90)
        self.edge(self.thickness)
        self.corner(90)
        # move plate
        self.move(self.thickness*2 + self.PlateVisibleWidth, self.thickness*3, move, label=label)
        
    def verticalLedSupport(self, IsAcrylic, move=None, label=""):
        if IsAcrylic :
            if self.move(self.thickness*4 + self.PlateVisibleHeight, self.thickness*3 + self.AcrylicPlateThickness, move, True):
                return
        else:
            if self.move(self.thickness*4 + self.PlateVisibleHeight, self.thickness*3 + self.WoodPlateThickness, move, True):
                return
        # bottom
        self.edge(self.thickness * 4 + self.PlateVisibleHeight)
        self.corner(90)
        # right side
        self.edge(self.thickness - self.Margin/2)
        self.corner(90)
        self.edge(self.thickness + self.Margin/2)
        self.corner(-90)
        if IsAcrylic :
            self.edge(self.AcrylicPlateThickness + self.Margin)
        else :
            self.edge(self.WoodPlateThickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin/2)
        self.corner(90)
        self.edge(self.thickness * 2 - self.Margin/2)
        self.corner(90)
        # top
        self.edge(self.thickness * 4 + self.PlateVisibleHeight)
        self.corner(90)
        # left side
        self.edge(self.thickness * 2 - self.Margin/2)
        self.corner(90)
        self.edge(self.thickness + self.Margin/2)
        self.corner(-90)
        if IsAcrylic :
            self.edge(self.AcrylicPlateThickness + self.Margin)
        else :
            self.edge(self.WoodPlateThickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin/2)
        self.corner(90)
        self.edge(self.thickness - self.Margin/2)
        self.corner(90)
        # move plate
        if IsAcrylic :
            self.move(self.thickness*4 + self.PlateVisibleHeight, self.thickness*3 + self.AcrylicPlateThickness, move, label=label)
        else:
            self.move(self.thickness*4 + self.PlateVisibleHeight, self.thickness*3 + self.WoodPlateThickness, move, label=label)
        
    def plateAttachement(self, IsAcrylic, move=None, label=""):
        if IsAcrylic :
            if self.move(self.thickness*2 + self.AcrylicPlateThickness + self.Margin, self.thickness*2 + self.Margin, move, True):
                return
        else:
            if self.move(self.thickness*2 + self.WoodPlateThickness + self.Margin, self.thickness*2 + self.Margin, move, True):
                return
        # bottom
        self.edge(self.thickness)
        self.corner(90)
        self.edge(self.thickness + self.Margin)
        self.corner(-90)
        if IsAcrylic :
            self.edge(self.AcrylicPlateThickness + self.Margin)
        else :
            self.edge(self.WoodPlateThickness + self.Margin)
        self.corner(-90)
        self.edge(self.thickness + self.Margin)
        self.corner(90)
        self.edge(self.thickness)
        self.corner(90)
        # right side
        self.edge(self.thickness*2 + self.Margin)
        self.corner(90)
        # top
        if IsAcrylic :
            self.edge(self.thickness*2 + self.AcrylicPlateThickness + self.Margin)
        else :
            self.edge(self.thickness*2 + self.WoodPlateThickness + self.Margin)
        self.corner(90)
        # left side
        self.edge(self.thickness*2 + self.Margin)
        self.corner(90)
        # move plate
        if IsAcrylic :
            self.move(self.thickness*2 + self.AcrylicPlateThickness + self.Margin, self.thickness*2 + self.Margin, move, label=label)
        else:
            self.move(self.thickness*2 + self.WoodPlateThickness + self.Margin, self.thickness*2 + self.Margin, move, label=label)
        
    def render(self):
        # define box inner depth ; "+1" corresponds to the backplane module
        y = ((self.WoodPlatesWithHLedsCount + self.AcrylicPlatesCount + 1) * self.ThickModuleDepth + self.WoodPlatesWithoutHLedsCount * self.ThinModuleDepth) * (1 + self.BoxDepthMargin/100)
        # define box inner width
        x = self.thickness * 8 + self.PlateVisibleWidth + self.Margin if self.HasLateralLeds else self.thickness * 2 + self.PlateVisibleWidth + self.Margin
        #define box inner height
        h = self.PlateVisibleHeight + self.thickness * 10 + self.Margin
        
        b = self.bottom_edge
        t1, t2, t3, t4 = self.topEdges(self.top_edge)
        #if top_edge is t put the handle on the x walls
        if(self.top_edge=='t'):
            t1,t2,t3,t4=(t2,t1,t4,t3)
        self.ctx.save()

        # sides
        self.rectangularWall(y, h, [b, "F", t1, "F"], move="mirror", label="right")
        self.rectangularWall(y, h, [b, "F", t3, "F"], move="left up", label="left")

        #rails
        self.rectangularWall(y - self.thickness*2, self.thickness*2, "feee", move="up", label="rail")
        self.rectangularWall(y - self.thickness*2, self.thickness*2, "feee", move="up", label="rail")
        
        # floor
        if b != "e":
            self.rectangularWall(x, y, "ffff", callback=[lambda:self.railSlots(x, y)], move="up", label="bottom")
        
        # back
        self.rectangularWall(x, h, [b, "f", t2, "f"], move="up", label="back")
        
        # front
        if self.HasLateralLeds:
            self.rectangularWall(x, h, [b, "f", t2, "f"], callback=[lambda:self.rectangularHole(self.PlateVisibleWidth/2 + self.thickness*4,self.PlateVisibleHeight/2 + self.thickness*6,self.PlateVisibleWidth, self.PlateVisibleHeight)], move="up", label="front")
        else:
            self.rectangularWall(x, h, [b, "f", t2, "f"], callback=[lambda:self.rectangularHole(self.PlateVisibleWidth/2 + self.thickness,self.PlateVisibleHeight/2 + self.thickness*6,self.PlateVisibleWidth, self.PlateVisibleHeight)], move="up", label="front")

        # top / lid
        self.drawLid(x, y, self.top_edge)
        self.lid(x, y, self.top_edge)
        #self.ctx.restore()
        
        # backplane plate
        self.plate(True, True, move="up", label="Backplane")
        
        # acrylic plates
        for i in range(self.AcrylicPlatesCount):
            self.plate(True, False, move="up", label="Acrylic\nInsert engraved art here")
        
        # wood plates with horizontal LEDs
        for i in range(self.WoodPlatesWithHLedsCount):
            self.plate(False, False, move="up", label="Wood with LEDs\nInsert cut and\nengraved art here")
        
        # wood plates without horizontal LEDs
        for i in range(self.WoodPlatesWithoutHLedsCount):
            self.plate(False, False, move="up", label="Wood without LEDs\nInsert cut and\nengraved art here")
        
        # Backplane plate supports
        self.genericPlateSupport(False, True, "up", label="B")
        self.genericPlateSupport(False, True, "up", label="B")
        
        # wood plates with horizontal LEDs supports
        for i in range(self.WoodPlatesWithHLedsCount * 2):
            self.genericPlateSupport(False, False, "up", label="W")
        
        # wood plates without horizontal LEDs supports
        for i in range(self.WoodPlatesWithoutHLedsCount * 2):
            self.genericPlateSupport(True, False, "up", label="w")
        
        # acrylic plates supports
        for i in range(self.AcrylicPlatesCount * 2):
            self.acrylicPlateSupport("up", label="A")
        
        # Horizontal LED supports
        for i in range(self.AcrylicPlatesCount * 6 + (1 + self.WoodPlatesWithHLedsCount) * 2 +  + self.WoodPlatesWithoutHLedsCount):
            self.horizontalLedSupport("up", label="")
        
        # Vertical LED supports
        if self.HasLateralLeds:
            for i in range((self.AcrylicPlatesCount + 1) * 2):
                self.verticalLedSupport(True, "up", label="A")
            for i in range((self.WoodPlatesWithHLedsCount + self.WoodPlatesWithoutHLedsCount) * 2):
                self.verticalLedSupport(False, "up", label="W")
        
        # Plate attachements
        if self.HasLateralLeds:
            for i in range((self.AcrylicPlatesCount + 1) * 2):
                self.plateAttachement(True, "up", label="A")
            for i in range((self.WoodPlatesWithHLedsCount + self.WoodPlatesWithoutHLedsCount) * 2):
                self.plateAttachement(False, "up", label="W")
        
        
