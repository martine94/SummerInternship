import open3d as o3d
import pandas as pd
import os
import sys
import argparse
parser = argparse.ArgumentParser(description='Choose scan')
parser.add_argument('key', type=str, metavar='N', help='key to scan, example: sg27_station1')
args = parser.parse_args()

path = os.path.join(/home/student/SummerInternship/inputFiles/, args.key, scan.txt)

data = pd.read_csv(path, sep=" ", header=None)
data.columns = ["x", "y", "z", "intensity", "r", "g", "b"]
data = data.drop(columns="intensity")

points = data[["x", "y", "z"]].copy()
colors = data[["r", "g", "b"]].copy()
colors = colors.div(255.0)

print(colors.head())

points = points.values
colors = colors.values

pcd = o3d.PointCloud()
pcd.points = o3d.Vector3dVector(points)
pcd.colors = o3d.Vector3dVector(colors)

path = os.path.join(/home/student/SummerInternship/inputFiles/, args.key, scan.pcd)
o3d.io.write_point_cloud(path, pcd)
