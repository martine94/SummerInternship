import sys

open3d_path = 'Open3D/build/lib/'
tc_path = 'SummerInternship/'

sys.path.append(open3d_path)
#from py3d import *
from open3d import *

def get_tc_path():
	return tc_path
