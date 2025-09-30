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

        x_blocks = []
        y_blocks = []
        
        with open(file_path, "r") as f:
            nbl = int(f.readline().strip())

            dims = []
            line = f.readline().split()

            for n in range(nbl):
                idim = int(line[2*n])
                jdim = int(line[2*n + 1])
                dims.append((idim, jdim))

            for n in range(nbl):
                idim, jdim = dims[n]
            
            # Чтение строки с данными для блока
                clear_list = []
                lines = f.readlines()
                for line in lines:
                    for l in line.split():
                        clear_list.append(l.strip())
                print(clear_list)
            
            # Общее количество элементов для x и y
                total_elements = idim * jdim * 2
            
            # Проверка достаточности данны
                
                data = list(map(float, clear_list))
                x_data = data[:idim*jdim]
                y_data = data[idim*jdim:2*idim*jdim]
                
                # Преобразование в 2D массивы с правильной формой
                x_block = x_data
                y_block = y_data
                
                x_blocks.append(x_data)
                y_blocks.append(y_data)

        # index_key = True
        # for line in lines:
        #     line_ = line.strip().split()
        #     if index_key:
        #         x_coords.append(line_[0])
        #         y_coords.append(line_[1])
        #         x_coords.append(line_[2])
        #         index_key = False
        #     else:
        #         y_coords.append(line_[0])
        #         x_coords.append(line_[1])
        #         y_coords.append(line_[2])
        #         index_key = True
        
        self.coords_mesh_x, self.coords_mesh_y = np.array(x_blocks).transpose(), np.array(y_blocks).transpose()


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