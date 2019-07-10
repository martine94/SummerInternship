
path = /home/student/SummerInternship/inputFiles/sg27_station1_intensity_rgb

with open(path, "r") as f:
	
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
