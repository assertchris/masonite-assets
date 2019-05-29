import os
import sys

current_path = os.path.abspath(os.path.dirname(__file__))

if current_path not in sys.path:
    sys.path.insert(0, current_path)
