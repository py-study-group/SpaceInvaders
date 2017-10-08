
import sys


class Creature:
    
    
    def __init__(self, x, y, shape, space):
        
        self.x = x
        self.y = y
        self.shape = shape
        self.space = space
        self.move(0, 0)
        
        
    def move(self, x, y):
        
        old_x = self.x
        old_y = self.y
        
        self.space.visible_space[old_x][old_y] = ' '
        
        self.x += x
        self.y += y
        
        if self.x < 0 or self.x >= self.space.y or self.y < 0 or self.y >= self.space.x:
            self.gone_to_hyperspace()
            
        self.space.visible_space[self.x][self.y] = self.shape
        
            
    #override this in subclasses        
    def gone_to_hyperspace(self):
        print('Gone to hyperspace...')
        sys.exit(0)


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
