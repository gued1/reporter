from reporter import header
import json
import numpy as np
import matplotlib.pyplot as plt

class Generator:
    
    def __init__(self, json_path, md_file):
        self.json_path = json_path
        self.md_file = md_file
    
    def create_graph(self):
        x = np.array([1, 3, 4, 6])
        y = np.array([2, 3, 5, 1])
        plt.plot(x, y)
        plt.savefig('Documents/Stéphane/Python/formation/reporter/data/fic/graph.png')
    
    def create_markdown(self):
        ##header.header(self.json_path)
        with open(self.json_path, "r") as in_file:
            reloaded = json.load(in_file)
    
        with open(self.md_file, "w") as out_file:
            out_file.write(header.header(reloaded) + f"\n![C'est ma premiere image](graph.png)\n")
            ##with open('Documents/Stéphane/Python/formation/reporter/data/fic/markdown.txt', "w") as out_file:
              ##  out_file.write(plt.savefig)
            ##liste.append((header.header(reloaded) + f"![C'est ma premiere image](graph.png)\n")
        
    
    