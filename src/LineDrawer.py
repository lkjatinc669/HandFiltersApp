import cv2 as cv

class LineDrawer:
    def __init__(self) -> None:
        self.lineColor = (0, 140, 255)

    def drawLine(self, frame, p1, p2, size=5):
        cv.line(frame, p1, p2, self.lineColor, size)
        cv.line(frame, p1, p2, (255, 255, 255), round(size / 2))
        return frame
