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

class Kamishibai_simple(_TopEdge):
    """Kamishibai butai (japanese image theatre)"""

    ui_group = "Misc"
    description = "This is a simple kamishibai butai (japanese image theatre)"

    def __init__(self) -> None:
        Boxes.__init__(self)
        self.addSettingsArgs(edges.FingerJointSettings, surroundingspaces=1.5)
        self.argparser.add_argument(
            "--SheetWidth",  action="store", type=float, default=380.0,
            help="width of the sheets in mm")
        self.argparser.add_argument(
            "--SheetHeight",  action="store", type=float, default=280.0,
            help="height of the sheets in mm")
        self.argparser.add_argument(
            "--SheetsStackDepth",  action="store", type=float, default=20.0,
            help="Depth of the sheets stack in mm")
        self.argparser.add_argument(
            "--FrameThickness",  action="store", type=int, default=4,
            help="Frame thickness in multiples of thickness")
        self.argparser.add_argument(
            "--FrameCornerRadius",  action="store", type=float, default=5.0,
            help="Radius of the frame corners in mm")
        self.argparser.add_argument(
            "--Margin",  action="store", type=float, default=2.0,
            help="Margin for sheets and moving parts in mm")
            
    def render(self):
       hi = self.SheetHeight + self.Margin
       wi = self.SheetWidth + self.Margin
       di = self.SheetsStackDepth + self.Margin
       
       # front
       self.rectangularWall(wi, hi, "FFFe", callback=[lambda:self.rectangularHole(self.thickness*self.FrameThickness, self.thickness*self.FrameThickness, wi - self.thickness*self.FrameThickness*2, hi - self.thickness*self.FrameThickness*2, self.FrameCornerRadius, False, False)], move="up", label="front")
       # back
       self.rectangularWall(wi, hi, "FeFF", callback=[lambda:self.rectangularHole(self.thickness*self.FrameThickness, self.thickness*self.FrameThickness, wi - self.thickness*self.FrameThickness*2, hi - self.thickness*self.FrameThickness*2, self.FrameCornerRadius, False, False)], move="up", label="back")
       
       # top
       self.rectangularWall(wi, di, "fFfe", move="up", label="top")
       # bottom
       self.rectangularWall(wi, di, "fefF", move="up", label="bottom")
       
       # closed side
       self.rectangularWall(hi, di, "ffff", move="up", label="side")
       
