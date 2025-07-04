import os
import shutil
from datetime import datetime
source = "/var/jenkins_home"
destination= "/etc"
curr_time= datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
backup_name = f"{source}-backup-{curr_time}"
backup_path= os.path.join(destination, backup_name)
shutil.make_archive(backup_path, 'zip', source)
print(f"Backup completed successfully!")

