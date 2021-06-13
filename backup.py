import json
import ansible_runner
from ansible_runner.utils import isinventory

extra_vars = {'crud': 'create', 'file_suffix': 'test123'}

s3_inventory = {
   "all": {
      "vars": {
         "project_name": "TEST_LAB",
         "ansible_python_interpreter": "venv/bin/python3",
         "servers": [
            {
               "ip": "192.0.2.100",
               "root_dir": "home/test/lab-automation/{{project_name}}",
               "xftp": "sftp",
               "user": "test",
               "password": "test123"
            }
         ]
      },
      "children": {
         "devices": {
            "children": {
               "devices_10x": {
                  "vars": {
                     "ansible_user": "user",
                     "ansible_password": "user123"
                  },
                  "hosts": {
                     "D5164_19": {
                        "ansible_ssh_host": "192.0.2.19",
                        "ansible_user": "user",
                        "ansible_password": "userABC",
                     },
                     "D5164_20": {
                        "ansible_ssh_host": "192.0.2.20",
                      }
                  }
               }
            }
         }
      }
   }
}

#r = ansible_runner.run(private_data_dir='./', playbook='backup_10x.yaml', inventory='inventory/S3_LAB.yml', envvars= env_vars, extravars=extra_vars, verbosity=0, cmdline='-t remote')
r = ansible_runner.run(private_data_dir='./', playbook='backup_10x.yaml', inventory=s3_inventory, extravars=extra_vars, verbosity=3, cmdline='-t remote')
#print("{}: {}".format(r.status, r.rc))
# successful: 0
#for each_host_event in r.events:
#    print(each_host_event['event'])
#print("Final status:")
#print(json.dumps(r.stats, indent=2))