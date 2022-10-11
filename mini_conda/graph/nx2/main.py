from pathlib import Path
import requests
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime, date
from pprint import pprint as pp
from itertools import combinations
import random
from collections import Counter, defaultdict


print(f'NetworkX version: {nx.__version__}')

print(f'Matplotlib version: {mpl.__version__}')