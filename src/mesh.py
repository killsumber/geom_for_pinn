import numpy as np
import matplotlib.pyplot as plt

class Grid_reader:
    """_summary класс для чтения сеток различных форматов
    """
    def __init__(self, format=None):
        self.formats = ['.p2dfmt', 'p3dfmt']
        self.grid_shape = None
        self.points = None
        self.format = format
        if self.format not in self.formats and self.format is not None:
            raise ValueError("ты че за формат указал? еблан?") 

    def read_p2dfmt(self, file_path):
        # try:
        x_coords = []
        y_coords = []
        
        with open(file_path, "r") as f:
            lines = f.readlines()
            self.x_dim_ = int(lines[1].strip().split()[0])
            self.y_dim_ = int(lines[1].strip().split()[1])
            lines = lines[2:]

        index_key = True
        for line in lines:
            line_ = line.strip().split()
            if index_key:
                x_coords.append(line_[0])
                y_coords.append(line_[1])
                x_coords.append(line_[2])
                index_key = False
            else:
                y_coords.append(line_[0])
                x_coords.append(line_[1])
                y_coords.append(line_[2])
                index_key = True
        
        self.coords_mesh = np.array([x_coords, y_coords]).transpose().astype(float)

    def plot_all_mesh(self, format=None, name="", test=True):
        
        x, y = self.coords_mesh[:, 0], self.coords_mesh[:, 1]
        plt.figure(figsize=(10, 8))

        plt.scatter(x, y, label="$Вся сетка$", c='blue', s=10, alpha=0.5,)
        plt.xlabel("$X$")
        plt.ylabel("$Y$")

        if test:
            plt.savefig(f"./plots/test_plots/all_coords_{name}.png", format="png")
        else:
            plt.savefig(f"./plots/not_test/all_coords_{name}.png", format="png")
        plt.show()


    def pinn_mesh(self):
        pass

    def pinn_p(self):
        pass
        
        # except:
        #     pass
        # finally:
        #     pass