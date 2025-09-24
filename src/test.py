from mesh import Grid_reader

a = Grid_reader()
a.read_p2dfmt(file_path='./meshs/n0012familyI.2.p2dfmt')
# print(a.coords_mesh)


a.plot_all_mesh(name="тест")