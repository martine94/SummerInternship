import sys

open3d_path = '/home/martin/Open3D/build/lib/'
tc_path = '/home/martin/tangent_conv/'

sys.path.append(open3d_path)
from py3d import *

def get_tc_path():
	return tc_path
