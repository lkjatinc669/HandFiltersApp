import cv2 as cv

class HandPosition:
    def __init__(self, mlist) -> None:
        self.mlist = mlist

    def positionData(self):
        wrist = (self.mlist[0][0], self.mlist[0][1])
        thumb_tip = (self.mlist[4][0], self.mlist[4][1])
        index_mcp = (self.mlist[5][0], self.mlist[5][1])
        index_tip = (self.mlist[8][0], self.mlist[8][1])
        midle_mcp = (self.mlist[9][0], self.mlist[9][1])
        midle_tip = (self.mlist[12][0], self.mlist[12][1])
        ring_tip  = (self.mlist[16][0], self.mlist[16][1])
        pinky_tip = (self.mlist[20][0], self.mlist[20][1])

        return [wrist, thumb_tip, index_mcp, index_tip, midle_mcp, midle_tip, ring_tip, pinky_tip]