from shutil import copyfile
import os
from tqdm import tqdm

def main():
    leakage_attrs = ["Rel", "Pos + Rel", "Unlabeled"]
    root_addr = "D:\\REU Datasets\\Universal Dependencies 2.8.1\\ud-treebanks-v2.8\\"
    
    for dirname in tqdm(os.listdir(root_addr)):
        directory = root_addr + dirname
        for file in os.listdir(directory):
            file_addr = directory + "\\" + file
            if file.endswith("-dev.conllu"):
                for attr in leakage_attrs:
                    leaky_addr = "D:\\REU Datasets\\Universal Dependencies 2.8.1\\leaky-treebanks\\" + attr + "\\"
                    nonleaky_addr = "D:\\REU Datasets\\Universal Dependencies 2.8.1\\nonleaky-treebanks\\" + attr + "\\"
                    copyfile(file_addr, leaky_addr+dirname+"\\"+file)
                    copyfile(file_addr, nonleaky_addr+dirname+"\\"+file)



    

if __name__ == "__main__":
    main()