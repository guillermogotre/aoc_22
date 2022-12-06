import glob
import os
from pathlib import Path

next = max(int(os.path.splitext(x)[0]) for x in glob.glob("*.ipynb")) + 1
for f in [f'{next}.ipynb', f'{next}.input', f'{next}_ex.input']:
    Path(f).touch()