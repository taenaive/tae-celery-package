import os 
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
print(os.getcwd())
print(sys.path)

from tae_server import add