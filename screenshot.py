import numpy as np
import win32gui
import win32ui
import win32con

#captures frame
class Screenshot():
    w,h = 0,0
    hwnd = None

    def __init__(self, windowname):
        self.hwnd = win32gui.FindWindow(None, windowname)
        self.w = win32gui.GetWindowRect(self.hwnd)[2] - win32gui.GetWindowRect(self.hwnd)[0]
        self.h = win32gui.GetWindowRect(self.hwnd)[3] - win32gui.GetWindowRect(self.hwnd)[1]

    def get_frame(self):
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (0, 0), win32con.SRCCOPY)

        frame = np.fromstring(dataBitMap.GetBitmapBits(True), dtype='uint8')
        frame.shape = (self.h, self.w, 4)
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        frame = frame[..., :3]
        frame = np.ascontiguousarray(frame)

        return frame

    def crop(self, image):
        return image[400:460, 130:600]

