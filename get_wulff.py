from pymatgen.analysis.wulff import WulffShape
from pymatgen.core import Lattice  # Correct import for Lattice
from pymatgen.core.surface import SlabGenerator, Structure
from mp_api.client import MPRester
import matplotlib.pyplot as plt

API_KEY = "CwDgVg8Lg2X5oRNSNIsj7qBbRyvhjTUf"
mpr = MPRester(API_KEY)

# Example: Get the structure for Silicon (mp-149)
structure = mpr.get_structure_by_material_id("mp-149")

# Example surface energies (in J/m^2) for Si facets
surface_energies = {
    (1, 0, 0): 1.5,
    (1, 1, 0): 1.2,
    (1, 1, 1): 1.0,
    (2, 1, 1): 1.8
}

# Extract Miller indices and corresponding surface energies into separate lists
miller_list = list(surface_energies.keys())
e_surf_list = list(surface_energies.values())

# Create the WulffShape object
lattice = Lattice.cubic(5.431)  # Example lattice for silicon
wulff_shape = WulffShape(lattice, miller_list, e_surf_list)

# Visualize the Wulff shape
fig = wulff_shape.get_plot()

# Customize and show the plot
plt.show()
