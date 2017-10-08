
import asyncio
from random import randint

from deepspace import DeepSpace
from blueracer import BlueRacer
from crossplatform import CrossplatformFunctions
from kbhit import KBHit


FPS = 0.16666667 # seconds


class GameLoop():

    
    def __init__(self):
        
        self.cross_platform = CrossplatformFunctions()
        self.cross_platform.resize_screen()
        
        self.keyboard = KBHit()
        
        self.space = DeepSpace()
        self.blue_racer = BlueRacer(39, 60, '#', self.space)
        
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.start())


    @asyncio.coroutine
    def start(self):
        while True:
            self.frame()
            yield from asyncio.sleep(FPS)
    
    
    def frame(self):
        #self.blue_racer.move(randint(-1, 1), randint(-1, 1))
        if self.keyboard.kbhit():
            self.blue_racer_move()
        self.print_space()
        
    
    def blue_racer_move(self):
        key = self.keyboard.getch()
        if ord(key) == 51:
            self.blue_racer.move(0, 1)
        elif ord(key) == 49:
            self.blue_racer.move(0, -1)
    
    def print_space(self):
        self.cross_platform.clear_screen()        
        s = ''
        for row in self.space.visible_space:
            r = ''.join(row) + '\n'
            s += r
        print(s)
        print('x: ', self.blue_racer.x, len(self.space.visible_space))
        print('y: ', self.blue_racer.y)

def main():
    game_loop = GameLoop()

if __name__ == '__main__':
    main()
    # print("\x1b[8;42;100t")
