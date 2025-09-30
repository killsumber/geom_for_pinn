from mesh import Grid_reader

a = Grid_reader()
a.read_p2dfmt(file_path= 'src\meshs\\n0012familyI.7.p2dfmt\\n0012familyI.7.p2dfmt')

print(a.coords_mesh_x, a.coords_mesh_y)

# a.plot_all_mesh()

# a.plot_all_mesh(name="тест")

# import py2dm 

# with py2dm.Reader(".\src\meshs\\0012familyI.2.2dm") as m:
#     print(m)

# with open(r"src\meshs\\n0012familyI.7.p2dfmt\\n0012familyI.7.p2dfmt", "r") as f:
#     print(f.readline().strip())

#     print(f.readline().strip())