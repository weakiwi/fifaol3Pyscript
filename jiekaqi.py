#coding=utf-8
import win32api
import win32con
import win32gui
from ctypes import *
import time
import random
from PIL import ImageGrab
from PIL import Image
import operator
import math
VK_CODE = { #定义主要按键的键值
  'backspace':0x08,
  'tab':0x09,
  'clear':0x0C,
  'enter':0x0D,
  'shift':0x10,
  'ctrl':0x11,
  'alt':0x12,
  'pause':0x13,
  'caps_lock':0x14,
  'esc':0x1B,
  'spacebar':0x20,
  'page_up':0x21,
  'page_down':0x22,
  'end':0x23,
  'home':0x24,
  'left_arrow':0x25,
  'up_arrow':0x26,
  'right_arrow':0x27,
  'down_arrow':0x28,
  'select':0x29,
  'print':0x2A,
  'execute':0x2B,
  'print_screen':0x2C,
  'ins':0x2D,
  'del':0x2E,
  'help':0x2F,
  '0':0x30,
  '1':0x31,
  '2':0x32,
  '3':0x33,
  '4':0x34,
  '5':0x35,
  '6':0x36,
  '7':0x37,
  '8':0x38,
  '9':0x39,
  'a':0x41,
  'b':0x42,
  'c':0x43,
  'd':0x44,
  'e':0x45,
  'f':0x46,
  'g':0x47,
  'h':0x48,
  'i':0x49,
  'j':0x4A,
  'k':0x4B,
  'l':0x4C,
  'm':0x4D,
  'n':0x4E,
  'o':0x4F,
  'p':0x50,
  'q':0x51,
  'r':0x52,
  's':0x53,
  't':0x54,
  'u':0x55,
  'v':0x56,
  'w':0x57,
  'x':0x58,
  'y':0x59,
  'z':0x5A,
  'numpad_0':0x60,
  'numpad_1':0x61,
  'numpad_2':0x62,
  'numpad_3':0x63,
  'numpad_4':0x64,
  'numpad_5':0x65,
  'numpad_6':0x66,
  'numpad_7':0x67,
  'numpad_8':0x68,
  'numpad_9':0x69,
  'multiply_key':0x6A,
  'add_key':0x6B,
  'separator_key':0x6C,
  'subtract_key':0x6D,
  'decimal_key':0x6E,
  'divide_key':0x6F,
  'F1':0x70,
  'F2':0x71,
  'F3':0x72,
  'F4':0x73,
  'F5':0x74,
  'F6':0x75,
  'F7':0x76,
  'F8':0x77,
  'F9':0x78,
  'F10':0x79,
  'F11':0x7A,
  'F12':0x7B,
  'F13':0x7C,
  'F14':0x7D,
  'F15':0x7E,
  'F16':0x7F,
  'F17':0x80,
  'F18':0x81,
  'F19':0x82,
  'F20':0x83,
  'F21':0x84,
  'F22':0x85,
  'F23':0x86,
  'F24':0x87,
  'num_lock':0x90,
  'scroll_lock':0x91,
  'left_shift':0xA0,
  'right_shift ':0xA1,
  'left_control':0xA2,
  'right_control':0xA3,
  'left_menu':0xA4,
  'right_menu':0xA5,
  'browser_back':0xA6,
  'browser_forward':0xA7,
  'browser_refresh':0xA8,
  'browser_stop':0xA9,
  'browser_search':0xAA,
  'browser_favorites':0xAB,
  'browser_start_and_home':0xAC,
  'volume_mute':0xAD,
  'volume_Down':0xAE,
  'volume_up':0xAF,
  'next_track':0xB0,
  'previous_track':0xB1,
  'stop_media':0xB2,
  'play/pause_media':0xB3,
  'start_mail':0xB4,
  'select_media':0xB5,
  'start_application_1':0xB6,
  'start_application_2':0xB7,
  'attn_key':0xF6,
  'crsel_key':0xF7,
  'exsel_key':0xF8,
  'play_key':0xFA,
  'zoom_key':0xFB,
  'clear_key':0xFE,
  '+':0xBB,
  ',':0xBC,
  '-':0xBD,
  '.':0xBE,
  '/':0xBF,
  '`':0xC0,
  ';':0xBA,
  '[':0xDB,
  '\\':0xDC,
  ']':0xDD,
  "'":0xDE,
  '`':0xC0}
class POINT(Structure):
  _fields_ = [("x", c_ulong),("y", c_ulong)]
def press(*args):#定义短按操作
    '''
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0,0,0)
        time.sleep(.05)
        win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)

def pressAndHold(*args):
    '''
    press and hold. Do NOT release.
    accepts as many arguments as you want.
    e.g. pressAndHold('left_arrow', 'a','b').
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0,0,0)
        time.sleep(.05)
           
def pressHoldRelease(*args):
    '''
    press and hold passed in strings. Once held, release
    accepts as many arguments as you want.
    e.g. pressAndHold('left_arrow', 'a','b').

    this is useful for issuing shortcut command or shift commands.
    e.g. pressHoldRelease('ctrl', 'alt', 'del'), pressHoldRelease('shift','a')
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0,0,0)
        time.sleep(.05)
            
    for i in args:
            win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)
            time.sleep(.1)
            
        

def release(*args):
    '''
    release depressed keys
    accepts as many arguments as you want.
    e.g. release('left_arrow', 'a','b').
    '''
    for i in args:
           win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)
def get_mouse_point():
  po = POINT()
  windll.user32.GetCursorPos(byref(po))
  return int(po.x), int(po.y)
def mouse_click(x=None,y=None):
  if not x is None and not y is None:
    mouse_move(x,y)
    time.sleep(0.05)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def mouse_dclick(x=None,y=None):
  if not x is None and not y is None:
    mouse_move(x,y)
    time.sleep(0.05)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def mouse_move(x,y):
  windll.user32.SetCursorPos(x, y)
def key_input(str=''):
  for c in str:
    win32api.keybd_event(VK_CODE[c],0,0,0)
    win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.01)
def TopmostMe():
    hwnd = win32gui.GetForegroundWindow()
    (left, top, right, bottom) = win32gui.GetWindowRect(hwnd)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, left, top, right-left, bottom-top, 0)

def crazyEsc(cishu, jiange):
    for i in range(cishu):
        time.sleep(jiange)
        key_input('esc') 
def When2Esct(im1, im2):#判断是否在回放  
    h1 = im1.histogram()
    h2 = im2.histogram()   
    rms = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return rms
def pressEsc():
    win32api.keybd_event(27,0,0,0)
    time.sleep(0.1)
    win32api.keybd_event(27,0,win32con.KEYEVENTF_KEYUP,0)
def moveAndclick(x, y):
    mouse_move(x, y)
    mouse_click(x, y)    
if __name__ == '__main__':
    game_hwnd = win32gui.FindWindow('FIFANG','FIFA ONLINE3 - Developed by SPEARHEAD')
    win32gui.ShowWindow(game_hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(game_hwnd) 
#    x_zhou = random.randrange(1396,1531)#vs经理人
#    y_zhou = random.randrange(818,911)
#    x_zhou1 = random.randrange(1234,1243)#选择电脑
#   y_zhou1 = random.randrange(851,864)
#    y_zhou2 = random.randrange(1021, 1037)
#   TopmostMe()#窗口置顶
    game_rect = win32gui.GetWindowRect(game_hwnd)
#   肖雷(248,208)
#   里贝里（263,493）
#   戈丁（262,271)
#   买(579,226)
#   购买（717, 572）
#   购买2（443,498）
#   该球员已出售（373, 318)
#   贝恩斯 359
    for i in range(5):
        print i
        time.sleep(1)
    user_x,user_y = get_mouse_point()
    time.sleep(0.1)
    moveAndclick(user_x, user_y)
    time.sleep(1)
#    im1 = Image.open('1.jpg')
#    rgb_im = im2.convert('RGB')
#    r,g,b = rgb_im.getpixel((1,1))
#    print r,g,b
    while(1):
            moveAndclick(game_rect[0]+user_x, game_rect[1]+user_y)
            time.sleep(0.5)
            moveAndclick(game_rect[0]+579, game_rect[1]+226)
            time.sleep(0.5)
            moveAndclick(game_rect[0]+717, game_rect[1]+572)
            time.sleep(0.5)
            pressHoldRelease('enter')
#            moveAndclick(game_rect[0]+443, game_rect[1]+498)
            time.sleep(1)
            pressHoldRelease('enter')  
            time.sleep(0.5)
            moveAndclick(user_x, user_y)
            time.sleep(3)
        
