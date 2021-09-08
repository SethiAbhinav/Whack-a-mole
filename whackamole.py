#url : https://www.memory-improvement-tips.com/whack-a-mole-game.html

# METHOD 3:

import cv2
import pyautogui
import time
import keyboard

# No pause between actions done by pyautogui
pyautogui.PAUSE = 0

#template and dimensions
mole_nose = cv2.imread("mole_nose.png")
mole_nose_gray = cv2.cvtColor(mole_nose, cv2.COLOR_RGB2GRAY)
nose_width, nose_height = mole_nose_gray.shape[::-1] # .shape method gives height then width, that's why i reversed it with ::-1
 
# game window dimensions
top_x, top_y, width, height = 510, 250, 890, 710

time.sleep(4)

replay_button = [1172,716]

def start():
    global f1, f2
    #click on play arrow (white)
    white_arrow = pyautogui.pixel(940,820)
    if white_arrow[0] > 250:
        pyautogui.click(940,820)
        time.sleep(1)

    #click on proceed arrow (brown)
    time.sleep(1)
    brown_arrow = pyautogui.pixel(1200,700)
    if brown_arrow[0] > 60:
        pyautogui.click(1200,700)

    return 0

try:
    start()
except:
    print("start error")
    pyautogui.click(940,820)
    time.sleep(2)
    pyautogui.click(1200,700)

while keyboard.is_pressed('q')==False:
    #screenshot
    pyautogui.screenshot("game_area.png", (top_x, top_y, width, height))
    game_area = cv2.imread("game_area.png")

    while True:

        #show what the computer sees
        '''
        game_area_screen = cv2.resize(
            src = game_area,
            dsize = (450,350) 
        )
        cv2.imshow("Computer sees this", game_area_screen)
        cv2.waitKey(1)     # so that it doesn't close as soon as it opens
        '''

        game_gray = cv2.cvtColor(game_area, cv2.COLOR_RGB2GRAY)

        result = cv2.matchTemplate(
            image = game_gray,
            templ = mole_nose_gray,
            method = cv2.TM_CCOEFF_NORMED
        )

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) #worst match, best match, location of worst, location of best

        #threshold
        if max_val >= 0.6: #more than 60% confidence
            pyautogui.click(
                 x = max_loc[0] + top_x, #screen x
                 y = max_loc[1] + top_y  #screen y
            )

            game_area = cv2.rectangle(
                img = game_area,
                pt1 = max_loc,
                pt2 = (
                    max_loc[0] + nose_width, # = pt2 x 
                    max_loc[1] + nose_height +100# = pt2 y
                ),
                color = (0,0,255),
                thickness = -1 #fill the rectangle
            )
        
        else:
            # replay_button_blue = (pyautogui.pixel(1172,716))[2]

            # if ( replay_button_blue> 20):
            #     pyautogui.click(1172,716)
            break





# METHOD 2:

'''             really bad

import pyautogui
import keyboard
import time

time.sleep(2)

pyautogui.PAUSE=0
while keyboard.is_pressed('q')==False:
    game_area=pyautogui.screenshot('game_area.png',region=(500,300,900,700)) #start_x, start_y, width, height
    game_area.save('game_area.png')
    width, height = game_area.size #900, 700

    for x in range (0, width, 10):
        for y in range (50, height, 10):
            r,g,b = game_area.getpixel((x,y))
            if r in [246,247,248]:    # pink nose has red value 247 or 248
                pyautogui.click(x+500,y+230)
                print(x,y)
                time.sleep(1)
                break
'''


# METHOD 1:

'''         this bot is too slow
import pyautogui
import keyboard
import time

time.sleep(1)
while keyboard.is_pressed('q')==False:
    find_mole_on_screen=pyautogui.locateOnScreen('mole_nose.png',region=(500,230,900,700),grayscale=True,confidence=0.6)
    if find_mole_on_screen!=None:
        # print(find_mole_on_screen)
        x = find_mole_on_screen[0]
        y = find_mole_on_screen[1]
        # x=int(((str(find_mole_on_screen)).split('left=')[1]).split(',')[0])
        # y=int(((str(find_mole_on_screen)).split('top=')[1]).split(',')[0])
        pyautogui.click(x,y)
        continue
    else:
        print("can't see")
        time.sleep(0.1)
'''