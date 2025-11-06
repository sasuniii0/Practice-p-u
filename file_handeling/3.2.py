import shutil
import os

shutil.copy("tasks.txt", "renamed_folder/tasks_backup.txt")
shutil.move("renamed_folder/tasks_backup.txt", "tasks_backup.txt")
os.remove("tasks_backup.txt")