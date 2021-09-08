# Whack-a-mole
**Automating the whack-a-mole game.
A project I had completed on 27th of June, 2021**

# Requirements:
```
OpenCV          --> Screenshotting and Shapes
pyautogui       --> Locating objects on screen and Clicking
time            --> Delay
keyboard        --> Exit program 
```

# Project Details:
I had always wanted to learn how bots were made for slightly more complex games, and thus I challenged myself to try to automate this game.


**Idea:**
- For this project, I wanted to take screenshots of the current game state and locate the position of the moles. Once located, I would instruct the computer to click at that location.

**Process:**
- I used OpenCV (a widely used computer vision library) to take the screenshots.
- Locating the moles was a lot more challenging, as all the moles were different and thus I had to improvise. I realised that I could use the nose to locate them (as they all had similar noses).

**Problems faced:**
- The bot was repeatedly clicking on the same pixel, and thus I had to "hide" the nose of the just clicked mole (I chose to draw a rectangle over the pixel I just clicked).
- The bot was too slow as it was trying to search for the moles in the entire screen, and thus I had to reduce the area which I was screenshotting.
- The bot was much better now, but still not upto the mark, and thus I decided to add a confidence factor while locating the nose on the screen(I set it to 60%).

**After project thoughts:**
- The bot could be improved by using a faster screenshotting library, i.e mss (did not know about this at the time of doing the project).
- The bot could search every 10th pixel instead of checking every pixel (will speed it up by a considerable amount).

**Note:**
I have left all my approaches in the code for anyone interested in going through my thought process.
