from util.path_config import *
from util.dataset_params import *
from util.cloud import *
from util.common import *

import os
import csv
import json
import wget

def get_semantic3d():
  dl_files = {"sg27_station1" : "sg27_station1_intensity_rgb",
				"sg27_station2" : "sg27_station2_intensity_rgb",
				"sg27_station4" : "sg27_station4_intensity_rgb",
				"sg27_station5" : "sg27_station5_intensity_rgb",
				"sg27_station9" : "sg27_station9_intensity_rgb",
				"sg28_station4" : "sg28_station4_intensity_rgb"
		   }

	for key in dl_files:
    dir = os.path.join(/home/student/SummerInternship/inputFiles, key)
    for part in list_dir(dir):
      points = []
      colors = []

      with open(os.path.join(args.input_folder, key, "scan.txt"), "r") as f:
        cnt = 0
        for entry in f:
          res = [float(c) for c in entry.split()]
          points.append(np.asarray(res[0:3]))
          colors.append(np.asarray(res[6:7] + res[5:6] + res[4:5]) / 255.0)
          if cnt % 100000 == 0:
            print(cnt)
          cnt += 1

      os.mkdir(os.path.join(args.output_folder, key))
      pcd = PointCloud()
      pcd.points = Vector3dVector(points)
      pcd.colors = Vector3dVector(colors)
      write_point_cloud(os.path.join(args.output_folder, key, "scan.pcd"), pcd)

      cmd = "cp " + os.path.join(args.input_folder, key, "scan.labels") + " " + os.path.join(args.output_folder, key, "scan.labels")
      os.system(cmd)


if args.dataset == "stanford":
	get_stanford()
elif args.dataset == "scannet":
	get_scannet()
elif args.dataset == "semantic3d":
	get_semantic3d()
else:
	print("Wrong dataset type")
