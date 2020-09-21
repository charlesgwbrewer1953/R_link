import rpy2

from rpy2 import robjects as ro
from ro.robjects import pandas2ri
from ro.robjects.conversion import localconverter

import rpy2.objects as robjects
from rpy2.objects.packages import importr, data

# Import r packages
base = importr("base")
stats = importr("stats")

