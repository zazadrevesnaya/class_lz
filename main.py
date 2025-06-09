from octagon import Octagon
def main():
    print("For octagon 1:")
    octagon1 = Octagon(5)
    octagon1.display_all_info()
    octagon1.draw_octagon()

    print("\nFor octagon 2:")
    octagon2 = Octagon(8)
    octagon2.display_all_info()
    octagon2.draw_octagon()
    
if __name__ == '__main__':
        main()
