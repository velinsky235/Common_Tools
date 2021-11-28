import os
import shutil
from shutil import copyfile


def make_folder_if_not_exists(folder_path):
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)


def delete_file_if_exists(file_path):
	if not os.path.isfile(file_path):
		os.system(f"rm {file_path}")


def error_without_file(fname):
	if not os.path.isfile(fname):
		print(f"{fname} is missing! :0\n")


def check_if_exists(path, _type):
	if _type == "file":
		exists = os.path.isfile(path)
	elif _type == "folder":
		exists = os.path.exists(path)


def get_filenames(fp):
	files = []
	utils.ensure_dir(fp)
	dirs = os.listdir(fp)
	for file_name in dirs:
		if file_name[0] != ".":
			files.append(file_name)
	return files