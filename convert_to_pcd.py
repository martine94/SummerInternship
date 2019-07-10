import open3d as o3d
import pandas as pd

path = "/home/student/SummerInternship/inputFiles/sg27_station1/scan.txt"

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
o3d.io.write_point_cloud("/home/student/SummerInternship/outputFiles/sg27_station1/scan.pcd", pcd)
