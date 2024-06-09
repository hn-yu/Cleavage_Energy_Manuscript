from pymatgen.analysis.wulff import WulffShape
from pymatgen.core import Lattice, Element 
from pymatgen.core.surface import SlabGenerator, Structure
from pymatgen.io.cif import CifWriter
import matplotlib.pyplot as plt

# from mp_api.client import MPRester
# API_KEY = "CwDgVg8Lg2X5oRNSNIsj7qBbRyvhjTUf"
# mpr = MPRester(API_KEY)
# structure = mpr.get_structure_by_material_id("mp-149")

# 假设你已经通过DFT计算得到了表面能量数据
# 这里是示例数据，实际数据需通过DFT计算获得
surface_energies = {
    (1, 1, 1): 1.0,  # 表面 (111) 的能量，单位：J/m²
    (1, 0, 0): 1.2,  # 表面 (100) 的能量，单位：J/m²
    (1, 1, 0): 1.1,  # 表面 (110) 的能量，单位：J/m²
    (0, 1, 1): 1.3   # 表面 (011) 的能量，单位：J/m²
}

"""
CuO 氧化铜 不是立方晶系。它通常以单斜晶系存在。
具体来说 CuO的晶体结构属于单斜晶系 monoclinic 其空间群是C2/c 编号15。
这个晶体结构不同于Cu2O 氧化亚铜 后者是立方晶系。
"""
# CuO的晶格参数
a = 4.6837
b = 3.4226
c = 5.1288
beta = 99.54

# 创建CuO的单斜晶格结构
cuo_lattice = Lattice.monoclinic(a, b, c, beta)
# Lattice1 = Lattice.cubic(5)


# WulffShape方法出自
# Tran, R.; Xu, Z.; Radhakrishnan, B.; Winston, D.; Persson, K. A.; Ong, S. P.
# (2016). Surface energies of elemental crystals. Scientific Data.


wulff_shape = WulffShape(cuo_lattice, surface_energies.keys(), surface_energies.values())
wulff_coords = wulff_shape.wulff_pt_list

# 创建一个简单的晶体结构
# 这里假设所有顶点都是Cu原子，可以根据实际情况修改
# species = [Element('Cu')] * len(wulff_coords)
species = [Element('Cu'),Element('O')] * (len(wulff_coords) // 2) 

# 创建Structure对象
structure = Structure(
    cuo_lattice,
    species,
    wulff_coords
)


# Visualize the Wulff shape
fig = wulff_shape.get_plot()


# 输出为CIF文件
# cif_writer = CifWriter(structure)
# cif_writer.write_file("Wulff_structure.cif")

# Customize and show the plot
plt.show()
