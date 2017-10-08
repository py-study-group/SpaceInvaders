
from creature import Creature


class BlueRacer(Creature):

        def __init__(self, x, y, shape, space):
            super().__init__(x, y, shape, space)


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
