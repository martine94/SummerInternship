import open3d as o3d
import pandas as pd
import os
import sys
import argparse
parser = argparse.ArgumentParser(description='Choose scan')
parser.add_argument('key', type=str, metavar='N', help='key to scan, example: sg27_station1')
args = parser.parse_args()

path = os.path.join('inputFiles/', args.key, 'scan.txt')

print('Reading scan.txt file')
data = pd.read_csv(path, sep=" ", header=None)
data.columns = ["x", "y", "z", "intensity", "r", "g", "b"]
print('Dropping intensity column')
data = data.drop(columns="intensity")

print('Writing to tmp.xyzrgb')
data.to_csv(r'tmp.xyzrgb', header=False, index=False, sep=" ", mode="a")
print('Read tmp.xyzrgb to pcd')
pcd = o3d.io.read_point_cloud('tmp.xyzrgb')
os.system("rm tmp.xyzrgb")

print('Write to scan.pcd')
path = os.path.join('inputFiles/', args.key, 'scan.pcd')
o3d.io.write_point_cloud(path, pcd)
