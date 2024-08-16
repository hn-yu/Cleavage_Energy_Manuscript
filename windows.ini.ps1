#mamba create -n cgcnn_env python=3.10
# use conda activate instead of mamba activate
conda activate cgcnn_env

# install packages
mamba install matplotlib numpy pandas scikit-learn tqdm skorch 
mamba install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia
mamba install ase pymatgen=2023.9.10 spglib pymongo
mamba install ipykernel jupyter