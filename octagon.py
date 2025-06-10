import math
import matplotlib.pyplot as plt
import numpy as np

class Octagon:
    ANGLE = 135 
    K = 1 + math.sqrt(2)  

    def __init__(self, side):
        self.side = side
        self.radius_inscribed = (self.side / 2) * Octagon.K 
        self.radius_circumscribed = (self.side / 2) * math.sqrt(4 + 2 * math.sqrt(2))  

    def perimeter(self):
        return 8 * self.side
    
    def square_octagon(self):
        return 2 * Octagon.K * self.side ** 2

    def display_all_info(self):
        print(f"Side length: {self.side:.2f}")
        print(f"Perimeter: {self.perimeter():.2f}")
        print(f"Octagon area: {self.square_octagon():.2f}")
        print(f"Radius of inscribed circle: {self.radius_inscribed:.2f}")
        print(f"Radius of circumscribed circle: {self.radius_circumscribed:.2f}")

    def draw_octagon(self):
        fig, ax = plt.subplots(figsize=(6,6))
        angle_step = math.pi / 4  
        vertices = np.array([
            [self.radius_inscribed / math.cos(math.pi / 8) * math.cos(i * angle_step),
             self.radius_inscribed / math.cos(math.pi / 8) * math.sin(i * angle_step)]
            for i in range(8)
        ])

        x, y = vertices[:, 0], vertices[:, 1]

        ax.fill(x, y, color='lightblue', edgecolor='black', linewidth=2, label="Octagon")

        circle_inscribed = plt.Circle((0, 0), self.radius_inscribed, color='green', fill=False, linewidth=2, label="Inscribed Circle")
        ax.add_patch(circle_inscribed)

        circle_circumscribed = plt.Circle((0, 0), self.radius_circumscribed, color='red', fill=False, linewidth=2, label="Circumscribed Circle")
        ax.add_patch(circle_circumscribed)

        ax.set_xlim(-self.radius_circumscribed * 1.2, self.radius_circumscribed * 1.2)
        ax.set_ylim(-self.radius_circumscribed * 1.2, self.radius_circumscribed * 1.2)
        ax.set_aspect('equal')
        plt.grid()
        plt.title("Octagon Circumscribed Around Inscribed Circle")
        plt.show()


