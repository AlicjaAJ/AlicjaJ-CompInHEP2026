#!/usr/bin/python
import re
from pathlib import Path

dir = "brilcalc.log"
if __name__ == "__main__":
    
    text = Path(dir).read_text()
    
    results = re.search(r"#Summary: ", text)
    print(results)
    
    fb = float(results)/1000
    print(f"{fb:.1f} fb^-1")

