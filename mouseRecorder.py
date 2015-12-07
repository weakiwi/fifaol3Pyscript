import pyHook
import pythoncom
import time
import win32api
import threading
import ctypes, win32con, ctypes.wintypes, win32gui
from ctypes import *
import sys
timelist = []#记录每次点击的时间
mouseposition = []#记录每次点击的位置
distance = []#记录每次点击的时间间隔
hm = pyHook.HookManager()
EXIT = False
class Hotkey(threading.Thread):
 
    def run(self):
        global EXIT
        user32 = ctypes.windll.user32
        if not user32.RegisterHotKey(None, 99, win32con.MOD_WIN, win32con.VK_F8):
            raise RuntimeError
        try:
            msg = ctypes.wintypes.MSG()
            print msg
            while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    if msg.wParam == 99:
                        EXIT = True
                        return
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            user32.UnregisterHotKey(None, 1)
def onMouseLeft(event):#每次鼠标左键按下就给相应的列表增加内容
    global timelist,mouseposition
    timelist.append(time.time())
    mouseposition.append(event.Position)
    return True
    
def onWheel(event):
    global timelist,distance,hm
    nl = []
    if event.Wheel == -1:#当鼠标中键向下滚动
        for i in timelist[1:]:
            nl.append(i)
        nl.append(timelist[len(timelist)-1])
        for (i,j) in zip(nl, timelist):
            distance.append(round((i-j),1)) 
        hm.UnhookMouse()
        temp = 0
        print 'stop recording...'
        print 'after 5 sec it will start...'
        for i in [5,4,3,2,1]:
            print i
            time.sleep(1)
        while True:
            for (x,y) in mouseposition:
                mouse_click(x,y)
                time.sleep(distance[temp])
                temp+=1
                if temp == len(distance):
                    temp = 0
                if EXIT:
                    sys.exit()
    return True
def mouse_click(x=None,y=None):
  if not x is None and not y is None:
    mouse_move(x,y)
    time.sleep(0.05)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def mouse_move(x,y):
  windll.user32.SetCursorPos(x, y)
        
def main():
    global hm
    print 'start recording the mouse click...'
    print 'take back the wheel and it will stop'
    hm.MouseLeftDown = onMouseLeft
    hm.MouseWheel = onWheel
    hm.HookMouse()
    pythoncom.PumpMessages()
    
    
if __name__ == '__main__':
    h = Hotkey()
    h.start()
    time.sleep(3)
    main()
