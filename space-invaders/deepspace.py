

X = 100
Y = 40


class DeepSpace:

    
    def __init__(self, x=X, y=Y):
        self.y = y
        self.x = x
        self.visible_space = [[' ' for j in range(X)] for i in range(Y)]


def main():
    s = DeepSpace()
    print(s.visible_space)

if __name__ == '__main__':
    main()
