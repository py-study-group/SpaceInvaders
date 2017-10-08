
import os
import platform
from time import sleep

LINUX = 0
WINDOWS = 1

EXIT_MSG = '''

    Just remember, if we get caught, 
    you are deaf and I don\'t speak English.

'''


class CrossplatformFunctions:
    
    def __init__(self):
        self.os = self.get_os()


    def clear_screen(self):
        if self.os == LINUX:
            #os.system('clear')
            print("\033c")
        elif self.os == WINDOWS:
            os.system('cls')
        else:
            self.exit_gracefully()
        


    def resize_screen(self):
        if self.os == LINUX:
            print("\x1b[8;46;100t")
        elif self.os == WINDOWS:
            os.system('mode con: cols=100 lines=46')
        else:
            self.exit_gracefully()


    def get_os(self):
        
        if platform.system() == 'Linux':
            return LINUX
        elif platform.system() == 'Windows':
            return WINDOWS
        else:
            self.exit_gracefully()
            
            
    def exit_gracefully(self):
        print(EXIT_MSG)            
        import sys
        sys.exit()    



def main():
    f = CrossplatformFunctions()
    print(f.get_os())
    f.resize_screen()
    sleep(3)
    f.clear_screen()

if __name__ == '__main__':
    main()
