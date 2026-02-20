#!/usr/bin/python
import os
import shutil
from multiprocessing import Process

dir = "out_python"
def run(i):
    os.system(f"./ex2 {i} > {dir}/run_{i}.txt")

if __name__ == "__main__":
    try:
        # Compiling with Makefile
        os.system("make")
        # Making new directory to store the results
        if os.path.isdir(dir):
            shutil.rmtree(dir)
        os.makedirs(dir)

        # Running parallel jobs
        n=10
        processes = []
        for j in range(1, n+1):
            p = Process(target=run, args=(j,)).start()
            processes.append(p)
                
        for p in processes:
            p.join()
        print("0")
    except:
        print("1")
        
