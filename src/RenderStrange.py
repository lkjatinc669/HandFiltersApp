import cv2 as cv

class RenderStrange:
    def __init__(self) -> None:
        pass

    def render(targetImg, frame, x, y, size=None):
        if size is not None:
            targetImg = cv.resize(targetImg, size)

        newFrame = frame.copy()
        b, g, r, a = cv.split(targetImg)
        overlay_color = cv.merge((b, g, r))
        mask = cv.medianBlur(a, 1)
        h, w, _ = overlay_color.shape
        roi = newFrame[y:y + h, x:x + w]

        img1_bg = cv.bitwise_and(roi.copy(), roi.copy(), mask=cv.bitwise_not(mask))
        img2_fg = cv.bitwise_and(overlay_color, overlay_color, mask=mask)
        newFrame[y:y + h, x:x + w] = cv.add(img1_bg, img2_fg)

        return newFrame