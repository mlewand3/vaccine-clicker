import pyautogui
from time import sleep


# endless main loop
while True:
    pyautogui.click('szukaj.png')
    
    # inner loop for one result processing
    while True:
        choose_btn = pyautogui.locateCenterOnScreen('wybierz.png')
        
        # if there is an option to reserve
        if choose_btn:
            print('Option found')
            x, y = choose_btn
            # click as soon as possible
            pyautogui.click(x, y)
            # wait a little to monit to show
            sleep(0.2)
            
            # confirm choice
            pyautogui.click('tak.png')
            print('Confirming')
            
            # failover (e.g. option is invalid already because someone was faster)
            sleep(2)
            # go back to main loop
            pyautogui.click('wroc.png')
            break
        
        # if there is "Nie mozna znalezc terminu" -> we need to refresh page`
        if pyautogui.locateOnScreen('nie.png'):`
            print('refresh...')
            pyautogui.move(50, 50)
            break
        # else: we keep waiting in the inner loop to show either "nie" or "wybierz"
        else:
            print('keep searching on this page')
            continue
