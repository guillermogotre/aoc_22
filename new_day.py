import glob
import os
from pathlib import Path

next = max(int(os.path.splitext(x)[0]) for x in glob.glob("*.ipynb")) + 1
for f in [f'{next:02d}.ipynb', f'inputs/{next:02d}.input', f'inputs/{next:02d}_ex.input']:
    Path(f).touch()