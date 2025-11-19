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
    description = """
    This is a multiplate light box with a closed compartment for electronics and the backlighting.
    The box offers thte possibility to be either definitively mounted (glued or forced in), or screwed
    (if the LockScrewDiameter is more than 0 mm).
    For assembling the box, please follow the following steps:
    1. Insert the rails in the bottom plate
    2. Insert the diffuser plate
    3. Insert one side
    4. Insert the electronics comparment top in the side
    5. Add (and glue if needed) the hinge rings to the lid top and insert it in the side
    6. Add the other side
    7. Insert the front plate
    8. Mount the eletronics in the electronics compartment and / or on the back plate
    9. Insert the back plate
    10. Add the nuts and screws to hold everything together if needed
    """

    def __init__(self) -> None:
        Boxes.__init__(self)
        self.addSettingsArgs(edges.FingerJointSettings, surroundingspaces=1)
        self.addSettingsArgs(edges.StackableSettings)
        self.addSettingsArgs(edges.HingeSettings, outset=True, pinwidth=0.4, style="flush", axle=2.5)
        self.argparser.add_argument(
            "--BoxStyle",  action="store", type=str, default="large face",
            choices=["minimalist", "large face", "extra customizable face"],
            help="style of the front lock")
        self.argparser.add_argument(
            "--PlateVisibleWidth",  action="store", type=float, default=150.0,
            help="width of the window in the front panel in mm")
        self.argparser.add_argument(
            "--PlateVisibleHeight",  action="store", type=float, default=75.0,
            help="height of the window in the front panel in mm")
        self.argparser.add_argument(
            "--WindowCorner",  action="store", type=float, default=5.0,
            help="radius of the corners of the window in the front panel in mm")
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
            "--hooks",  action="store", type=boolarg, default=False,
            help="add hooks to decorative plates (allowing one sides plates)")
        self.argparser.add_argument(
            "--Margin",  action="store", type=float, default=0.5,
            help="Margin for moving parts in mm")
        BackSideOptions_group = self.argparser.add_argument_group("Night lightbox options for the back side (holes for connectors, marking)")
        BackSideOptions_group.add_argument(
            "--BackExtraHoles",  action="store", type=str, default="R 20 10 11.5 8\nC 11.58 10 3\nC 28.42 10 3",
            help="extra holes for connectors or buttons ; enter one line per hole ; first parameter should be R for rectangle or C for circle ; then X and Y position for the center of the hole, and then the X and Y size of the rectangle or the circle diameter, all in mm ; parameters should be separated by spaces")
        ScrewsLocking_group = self.argparser.add_argument_group("Screws parameters for attaching the pieces together")
        ScrewsLocking_group.add_argument(
            "--LockScrewDiameter",  action="store", type=float, default=0.0,
            help="Diameter of the screw holes in mm (set to 0 for no screws)")
        ScrewsLocking_group.add_argument(
            "--LockScrewLength",  action="store", type=float, default=16.0,
            help="Length of the locking screws in mm")
        ScrewsLocking_group.add_argument(
            "--LockNutThickness",  action="store", type=float, default=2.4,
            help="Thickness of the locking nuts in mm")
        ScrewsLocking_group.add_argument(
            "--LockNutWidth",  action="store", type=float, default=5.5,
            help="Width of the locking nuts in mm")

    def screwAttachement (self):
        self.polyline(0, 90, self.thickness, 90, self.LockNutWidth/2 - self.LockScrewDiameter/2, -90,
                        self.LockNutThickness, -90, self.LockNutWidth/2 - self.LockScrewDiameter/2, 90,
                        self.LockScrewLength - self.LockNutThickness - self.thickness, -90, self.LockScrewDiameter, -90,
                        self.LockScrewLength - self.LockNutThickness - self.thickness, 90, self.LockNutWidth/2 - self.LockScrewDiameter/2, -90,
                        self.LockNutThickness, -90, self.LockNutWidth/2 - self.LockScrewDiameter/2, 90, self.thickness, 90)

    def railSlots(self, xSize, ySize):
        # to be updated
        t = self.thickness
        self.fingerHolesAt(t*1.5, self.InterPlateSpacing - t - self.Margin/2, t*2 + self.DiffuserPlateThickness + (self.InterPlateSpacing + self.WoodPlateThickness) * self.WoodPlatesCount)
        self.fingerHolesAt(xSize - (t*1.5), self.InterPlateSpacing - t - self.Margin/2, t*2 + self.DiffuserPlateThickness + (self.InterPlateSpacing + self.WoodPlateThickness) * self.WoodPlatesCount)

    def woodPlate(self, move=None, label=""):
        t = self.thickness
        if self.move(self.PlateVisibleWidth + t*(6 if self.BoxStyle == "minimalist" else 10), self.PlateVisibleHeight + t*(4 if self.BoxStyle == "minimalist" else 8), move, True):
            return
        # visible zone
        if self.BoxStyle == "minimalist" :
            self.rectangularHole(t*3, t*2, self.PlateVisibleWidth, self.PlateVisibleHeight, center_x=False, center_y=False, color=Color.ANNOTATIONS)
        else :
            self.rectangularHole(t*5, t*4, self.PlateVisibleWidth, self.PlateVisibleHeight, center_x=False, center_y=False, color=Color.ANNOTATIONS)
        self.moveTo(t + self.Margin/2, 0, 0)
        # bottom
        self.polyline(t - self.Margin, 90, t + self.Margin, -90, t + self.Margin, -90, t + self.Margin, 90,
                        self.PlateVisibleWidth + t*(0 if self.BoxStyle == "minimalist" else 4) - self.Margin, 90,
                        t + self.Margin, -90, t + self.Margin, -90, t + self.Margin, 90, t - self.Margin, 90)
        # right side
        self.polyline(self.PlateVisibleHeight + t*(2 if self.BoxStyle == "minimalist" else 6) + self.Margin, -90,
                        t + self.Margin/2)
        if self.hooks:
            self.polyline(0, -90, t, 90, 0, (90, t), t, (90, t))
        else:
            self.polyline(0, 90, t*2 - self.Margin*2, 90)
        # top
        self.polyline(self.PlateVisibleWidth + t*(6 if self.BoxStyle == "minimalist" else 10))
        # left side
        if self.hooks:
            self.polyline(0, (90, t), t, (90, t), 0, 90, t, -90)
        else:
            self.polyline(0, 90, t*2 - self.Margin*2, 90)
        self.polyline(t + self.Margin/2, -90,
                        self.PlateVisibleHeight + t*(2 if self.BoxStyle == "minimalist" else 6) + self.Margin, 90)
        # move plate
        self.move(self.PlateVisibleWidth + t*(6 if self.BoxStyle == "minimalist" else 10), self.PlateVisibleHeight + t*(4 if self.BoxStyle == "minimalist" else 8), move, label=label)

    def diffuserPlate(self, move=None, label=""):
        t = self.thickness
        if self.move(self.PlateVisibleWidth + t*(6 if self.BoxStyle == "minimalist" else 10), self.PlateVisibleHeight + t*(4 if self.BoxStyle == "minimalist" else 8), move, True):
            return
        # bottom
        self.polyline(t - self.Margin, 90, t + self.Margin, -90, t + self.Margin, -90, t + self.Margin, 90,
                        self.PlateVisibleWidth + t*(0 if self.BoxStyle == "minimalist" else 4) - self.Margin, 90,
                        t + self.Margin, -90, t + self.Margin, -90, t + self.Margin, 90, t - self.Margin, 90)
        # right side
        self.edge(self.PlateVisibleHeight + t*(0 if self.BoxStyle == "minimalist" else 4) - self.Margin)
        self.edges["f"](t * 4)
        self.corner(90)
        # top
        self.polyline(self.PlateVisibleWidth + t*(4 if self.BoxStyle == "minimalist" else 8) - self.Margin, 90)
        # left side
        self.edges["f"](t * 4)
        self.polyline(self.PlateVisibleHeight + t*(0 if self.BoxStyle == "minimalist" else 4) - self.Margin, 90)
        # move plate
        self.move(self.PlateVisibleWidth + t*(6 if self.BoxStyle == "minimalist" else 10), self.PlateVisibleHeight + t*(4 if self.BoxStyle == "minimalist" else 8), move, label=label)

    def elecCompartmentTop(self, move=None, label=""):
        t = self.thickness
        if self.move(t * 4 + self.PlateVisibleWidth + self.Margin, self.BackgroundDepth + t, move, True):
            return
        # bottom
        self.polyline(t * (4 if self.BoxStyle == "minimalist" else 8) + self.PlateVisibleWidth + self.Margin, 90)
        # right side
        self.edges["f"](self.BackgroundDepth)
        self.corner(90)
        # top
        self.edges["f"](t * (4 if self.BoxStyle == "minimalist" else 8) + self.PlateVisibleWidth + self.Margin)
        self.corner(90)
        # left side
        self.edges["f"](self.BackgroundDepth)
        self.corner(90)
        # move plate
        self.move(t * 4 + self.PlateVisibleWidth + self.Margin, self.BackgroundDepth + t, move, label=label)

    def side(self, ySize, hSize, move=None, label=""):
        t = self.thickness
        be = self.edges["s"] # bottom edge
        if self.move(ySize + t, hSize + t*4, move, True):
            return
        # finger holes for background and elec compartment top
        if self.BoxStyle == "minimalist" :
            self.fingerHolesAt(ySize - self.BackgroundDepth - self.DiffuserPlateThickness/2 - self.Margin/2, self.PlateVisibleHeight + t*4, t*4)
            self.fingerHolesAt(ySize + t - self.BackgroundDepth - self.DiffuserPlateThickness, self.PlateVisibleHeight + t*5.5 + self.Margin, self.BackgroundDepth, angle=0)
        else :
            self.fingerHolesAt(ySize - self.BackgroundDepth - self.DiffuserPlateThickness/2 - self.Margin/2, self.PlateVisibleHeight + t*8, t*4)
            self.fingerHolesAt(ySize + t - self.BackgroundDepth - self.DiffuserPlateThickness, self.PlateVisibleHeight + t*9.5 + self.Margin, self.BackgroundDepth, angle=0)
        # finger hole for background lock
        # bottom
        be(ySize)
        self.corner(90)
        # back side
        self.edge(be.endwidth())
        if self.LockScrewDiameter > 0 :
            self.edges["f"]((hSize - t*3)/2 - self.LockScrewDiameter/2)
            self.screwAttachement()
            self.edges["f"]((hSize - t*3)/2 - self.LockScrewDiameter/2)
        else :
            self.edges["f"](hSize - t*3)
        self.polyline(t*3, 90)
        # top
        self.edges["i"].settings.style = "flush_inset"
        self.edges["i"](t*5)
        self.polyline(self.BackgroundDepth - t*5 + self.DiffuserPlateThickness + self.InterPlateSpacing, 90)
        for i in range(self.WoodPlatesCount):
            self.polyline(t*2 + self.Margin, -90, self.WoodPlateThickness + self.Margin, -90,
                        t*2 + self.Margin, 90, self.InterPlateSpacing - self.Margin, 90)
        # front side
        if self.LockScrewDiameter > 0 :
            self.edges["f"](hSize/2 - self.LockScrewDiameter/2)
            self.screwAttachement()
            self.edges["f"](hSize/2 - self.LockScrewDiameter/2)
        else :
            self.edges["f"](hSize)
        self.edge(be.startwidth())
        self.corner(90)
        # move plate
        self.move(ySize + t, hSize + t*8, move, label=label)

    def rail(self, move=None, label=""):
        t = self.thickness
        if self.move(self.WoodPlatesCount * (self.InterPlateSpacing + self.WoodPlateThickness) + self.DiffuserPlateThickness + t*2, t*3, move, True):
            return
        # bottom
        self.edges["f"](t*2 + self.DiffuserPlateThickness + (self.InterPlateSpacing + self.WoodPlateThickness) * self.WoodPlatesCount)
        self.polyline(self.InterPlateSpacing - t - self.Margin/2, 90)
        # right side
        self.edges["f"](t*2)
        self.corner(90)
        # top
        self.polyline(self.InterPlateSpacing - self.Margin, 90)
        for i in range(self.WoodPlatesCount):
            self.polyline(t + self.Margin, -90, self.WoodPlateThickness + self.Margin, -90,
                        t + self.Margin, 90, self.InterPlateSpacing - self.Margin, 90)
        self.polyline(t + self.Margin, -90, self.DiffuserPlateThickness + self.Margin, -90,
                        t + self.Margin, 90, t - self.Margin/2, 90)
        # left side
        self.polyline(t*2, 90)
        # move plate
        self.move(self.WoodPlatesCount * (self.InterPlateSpacing + self.WoodPlateThickness) + self.DiffuserPlateThickness + t*2, t*3, move, label=label)

    def frontExtraHoles(self):
        t = self.thickness
        # main window, bottom and sides attachements
        if self.BoxStyle == "minimalist" :
            self.rectangularHole(self.PlateVisibleWidth/2 + t*4 + self.Margin/2,self.PlateVisibleHeight/2 + t*6,self.PlateVisibleWidth, self.PlateVisibleHeight, self.WindowCorner)
            self.fingerHolesAt(t*1, self.edges["s"].endwidth() - t*0.5, t * 6 + self.PlateVisibleWidth + self.Margin, angle=0)
            if self.LockScrewDiameter > 0 :
                self.fingerHolesAt(t*1.5, t * 4, self.PlateVisibleHeight/2 + t * 2 + self.Margin/2 - self.LockScrewDiameter/2)
                self.fingerHolesAt(t*1.5, self.PlateVisibleHeight/2 + t * 6 + self.Margin/2 + self.LockScrewDiameter/2, self.PlateVisibleHeight/2 + t * 2 + self.Margin/2 - self.LockScrewDiameter/2)
                self.hole(t*1.5, self.PlateVisibleHeight/2 + t * 6 + self.Margin/2, self.LockScrewDiameter/2)
                self.fingerHolesAt(self.PlateVisibleWidth + t*6.5 + self.Margin, t * 4, self.PlateVisibleHeight/2 + t * 2 + self.Margin/2 - self.LockScrewDiameter/2)
                self.fingerHolesAt(self.PlateVisibleWidth + t*6.5 + self.Margin, self.PlateVisibleHeight/2 + t * 6 + self.Margin/2 + self.LockScrewDiameter/2, self.PlateVisibleHeight/2 + t * 2 + self.Margin/2 - self.LockScrewDiameter/2)
                self.hole(self.PlateVisibleWidth + t*6.5 + self.Margin, self.PlateVisibleHeight/2 + t * 6 + self.Margin/2, self.LockScrewDiameter/2)
            else :
                self.fingerHolesAt(t*1.5, t * 4, self.PlateVisibleHeight + t * 4 + self.Margin)
                self.fingerHolesAt(self.PlateVisibleWidth + t*6.5 + self.Margin, t * 4, self.PlateVisibleHeight + t * 4 + self.Margin)
        else:
            self.rectangularHole(self.PlateVisibleWidth/2 + t*6 + self.Margin/2,self.PlateVisibleHeight/2 + t*8,self.PlateVisibleWidth, self.PlateVisibleHeight, self.WindowCorner)
            self.fingerHolesAt(t*2, self.edges["s"].endwidth() - t*0.5, t * 8 + self.PlateVisibleWidth + self.Margin, angle=0)
            if self.LockScrewDiameter > 0 :
                self.fingerHolesAt(t*1.5, t * 4, self.PlateVisibleHeight/2 + t * 4 + self.Margin/2 - self.LockScrewDiameter/2)
                self.fingerHolesAt(t*1.5, self.PlateVisibleHeight/2 + t * 8 + self.Margin/2 + self.LockScrewDiameter/2, self.PlateVisibleHeight/2 + t * 4 + self.Margin/2 - self.LockScrewDiameter/2)
                self.hole(t*1.5, self.PlateVisibleHeight/2 + t * 8 + self.Margin/2, self.LockScrewDiameter/2)
                self.fingerHolesAt(self.PlateVisibleWidth + t*10.5 + self.Margin, t * 4, self.PlateVisibleHeight/2 + t * 4 + self.Margin/2 - self.LockScrewDiameter/2)
                self.fingerHolesAt(self.PlateVisibleWidth + t*10.5 + self.Margin, self.PlateVisibleHeight/2 + t * 8 + self.Margin/2 + self.LockScrewDiameter/2, self.PlateVisibleHeight/2 + t * 4 + self.Margin/2 - self.LockScrewDiameter/2)
                self.hole(self.PlateVisibleWidth + t*10.5 + self.Margin, self.PlateVisibleHeight/2 + t * 8 + self.Margin/2, self.LockScrewDiameter/2)
            else :
                self.fingerHolesAt(t*1.5, t * 4, self.PlateVisibleHeight + t * 8 + self.Margin)
                self.fingerHolesAt(self.PlateVisibleWidth + t*10.5 + self.Margin, t * 4, self.PlateVisibleHeight + t * 8 + self.Margin)
        # holes for rails attachement #TODO
        if self.BoxStyle == "minimalist" :
            a=1
        else :
            self.fingerHolesAt(t*3.5, self.edges["s"].endwidth(), t*2)
            self.fingerHolesAt(self.PlateVisibleWidth + t*8.5 + self.Margin, self.edges["s"].endwidth(), t*2)
        # extra holes for attachement pegs for extra customizable face
        if self.BoxStyle == "extra customizable face" :
            self.rectangularHole(t*5.5, t*5.5, t, t)
            self.rectangularHole(self.PlateVisibleWidth + t*6.5 + self.Margin, t*5.5, t, t)
            self.rectangularHole(self.PlateVisibleWidth/2 + self.Margin/2 + t*6, self.PlateVisibleHeight + t*10.5 + self.Margin, t, t)

    def backExtraHoles(self):
        t = self.thickness
        # bottom attachement
        if self.BoxStyle == "minimalist" :
            self.fingerHolesAt(t*2, self.edges["s"].endwidth() - t*0.5, t * 4 + self.PlateVisibleWidth + self.Margin, angle=0)
        else :
            self.fingerHolesAt(t*2, self.edges["s"].endwidth() - t*0.5, t * 8 + self.PlateVisibleWidth + self.Margin, angle=0)
        # sides attachements
        if self.BoxStyle == "minimalist" :
            if self.LockScrewDiameter > 0 :
                self.fingerHolesAt(t*1.5, t*4, self.PlateVisibleHeight/2 + t * 0.5 + self.Margin/2 - self.LockScrewDiameter/2)
                self.fingerHolesAt(t*1.5, self.PlateVisibleHeight/2 + t * 4.5 + self.Margin/2 + self.LockScrewDiameter/2, self.PlateVisibleHeight/2 + t * 0.5 + self.Margin/2 - self.LockScrewDiameter/2)
                self.hole(t*1.5, self.PlateVisibleHeight/2 + t * 4.5 + self.Margin/2, self.LockScrewDiameter/2)
                self.fingerHolesAt(self.PlateVisibleWidth + t*6.5 + self.Margin, t*4, self.PlateVisibleHeight/2 + t * 0.5 + self.Margin/2 - self.LockScrewDiameter/2)
                self.fingerHolesAt(self.PlateVisibleWidth + t*6.5 + self.Margin, self.PlateVisibleHeight/2 + t * 4.5 + self.Margin/2 + self.LockScrewDiameter/2, self.PlateVisibleHeight/2 + t * 0.5 + self.Margin/2 - self.LockScrewDiameter/2)
                self.hole(self.PlateVisibleWidth + t*6.5 + self.Margin, self.PlateVisibleHeight/2 + t * 4.5 + self.Margin/2, self.LockScrewDiameter/2)
            else :
                self.fingerHolesAt(t*1.5, t * 3.5, self.PlateVisibleHeight + t * 1 + self.Margin)
                self.fingerHolesAt(self.PlateVisibleWidth + t*6.5 + self.Margin, t * 3.5, self.PlateVisibleHeight + t * 1 + self.Margin)
        else:
            if self.LockScrewDiameter > 0 :
                self.fingerHolesAt(t*1.5, t*3, self.PlateVisibleHeight/2 + t * 4.5 + self.Margin/2 - self.LockScrewDiameter/2)
                self.fingerHolesAt(t*1.5, self.PlateVisibleHeight/2 + t * 6.5 + self.Margin/2 + self.LockScrewDiameter/2, self.PlateVisibleHeight/2 + t * 2.5 + self.Margin/2 - self.LockScrewDiameter/2)
                self.hole(t*1.5, self.PlateVisibleHeight/2 + t * 6.5 + self.Margin/2, self.LockScrewDiameter/2)
                self.fingerHolesAt(self.PlateVisibleWidth + t*10.5 + self.Margin, t*3, self.PlateVisibleHeight/2 + t * 4.5 + self.Margin/2 - self.LockScrewDiameter/2)
                self.fingerHolesAt(self.PlateVisibleWidth + t*10.5 + self.Margin, self.PlateVisibleHeight/2 + t * 6.5 + self.Margin/2 + self.LockScrewDiameter/2, self.PlateVisibleHeight/2 + t * 2.5 + self.Margin/2 - self.LockScrewDiameter/2)
                self.hole(self.PlateVisibleWidth + t*10.5 + self.Margin, self.PlateVisibleHeight/2 + t * 6.5 + self.Margin/2, self.LockScrewDiameter/2)
            else :
                self.fingerHolesAt(t*1.5, + t * 4, self.PlateVisibleHeight + t * 5 + self.Margin)
                self.fingerHolesAt(self.PlateVisibleWidth + t*10.5 + self.Margin, t * 4, self.PlateVisibleHeight + t * 5 + self.Margin)
        # electronic compartment top attachement
        if self.BoxStyle == "minimalist" :
            self.fingerHolesAt(t*2, self.edges["s"].endwidth() + self.PlateVisibleHeight + self.Margin + t*1.5, t * 4 + self.PlateVisibleWidth + self.Margin, angle=0)
        else :
            self.fingerHolesAt(t*2, self.edges["s"].endwidth() + self.PlateVisibleHeight + self.Margin + t*5.5, t * 8 + self.PlateVisibleWidth + self.Margin, angle=0)
        # for each line, make a hole
        for line in self.BackExtraHoles.split("\n") :
            holeParams=line.split(" ")
            # rectangular hole
            if line[0] == "R" :
                self.rectangularHole(float(holeParams[1]) + t*2, float(holeParams[2]) + self.edges["s"].endwidth(), float(holeParams[3]), float(holeParams[4]))
            # round hole
            elif line[0] == "C" :
                self.hole(float(holeParams[1]) + t*2, float(holeParams[2]) + self.edges["s"].endwidth(), float(holeParams[3])/2)

    def frontBackPlate(self, x, h, isFront, move=None, label=""):
        t = self.thickness
        if self.move(x + t*4, h + t*4, move, True):
            return
        # holes callbacks
        if isFront :
            self.frontExtraHoles()
        else :
            self.backExtraHoles()
        # main shape
        self.edge(t*2)
        self.edges["š"](x)
        self.polyline(t*2, 90, h + t * (3 if isFront else 2), [90, t], x + t*2, [90, t], h + t * (3 if isFront else 2), 90)
        # move plate
        self.move(x + t*4,h + t*4, move, label=label)
    
    def render(self):
        t = self.thickness
        # define box inner depth
        y = self.BackgroundDepth + self.DiffuserPlateThickness + (self.WoodPlateThickness + self.InterPlateSpacing) * self.WoodPlatesCount + self.InterPlateSpacing #+ t*2
        if self.BoxStyle == "minimalist" :
            # define box inner width
            x = t * 4 + self.PlateVisibleWidth + self.Margin
            # define box inner height
            h = self.PlateVisibleHeight + t * 4 + self.Margin
        else :
            # define box inner width
            x = t * 8 + self.PlateVisibleWidth + self.Margin
            # define box inner height
            h = self.PlateVisibleHeight + t * 8 + self.Margin

        self.ctx.save()

        # sides
        self.side(y, h, move="mirror", label="left")
        self.side(y, h, move="left up", label="right")

        #rails
        self.rail(move="up", label="rail")
        self.rail(move="up mirror", label="rail")

        # floor
        self.rectangularWall(x, y, "ffff", callback=[lambda:self.railSlots(x, y)], move="up", label="bottom")

        # back
        self.frontBackPlate(x, h, False, move="up", label="back")

        # front and optional customizable front face
        if self.BoxStyle == "minimalist" :
            self.frontBackPlate(x, h, True, move="up", label="front")
        else:
            self.frontBackPlate(x, h, True, move="up", label="front")
        if self.BoxStyle == "extra customizable face" :
            self.rectangularWall(x + t*2, h, "EEEE", callback=[lambda:self.rectangularHole(self.PlateVisibleWidth/2 + t*5 + self.Margin/2,self.PlateVisibleHeight/2 + t*5,self.PlateVisibleWidth, self.PlateVisibleHeight, self.WindowCorner),
                                                                        lambda:self.rectangularHole(t*2.5, t*4.5, t, t),
                                                                        lambda:self.rectangularHole(self.PlateVisibleWidth/2 + t*5 + self.Margin/2, t*0.5, t, t),
                                                                        lambda:self.rectangularHole(self.PlateVisibleHeight + t*5.5 + self.Margin, t*4.5, t, t)
                                                                        ], move="up", label="customizable face")
            self.rectangularWall(t*2, t, move="up")
            self.rectangularWall(t*2, t, move="up")
            self.rectangularWall(t*2, t, move="up")
        
        # electronics compartment top
        self.elecCompartmentTop(move="up", label="elec. comp.")

        # top / lid
        self.drawLid(y - t, x, "i")

        # diffuser plate
        self.diffuserPlate(move="up", label="Diffuser")

        # wood plates with horizontal LEDs
        for i in range(self.WoodPlatesCount):
            self.woodPlate(move="up", label="Insert cut and\nengraved art here")
