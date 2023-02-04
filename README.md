# mars
The project includes different tools to help with lab automation.
- __backup__ - backup/restore device configuration to/from remote server or locally on device. 
               Filename consist of <device_name>_<file_suffix> . This allows to take backup/restore in different stages of configuration.

- __banner__ - create/read/update/delete banner 

- __software package__ - install/activate/remove software package

- __ipv4 interface__ - create/read/update/delete ipv4 interface

- __isis__ - create/read/update/delete isis configuration

- __bgp__ - create/read/update/delete bgp configuration

- __users__ - create/read/update/delete local users



### To setup your environment:
```bash
git clone https://github.com/ddichev-hub/mars.git
cd mars
apt-get install python3-venv (optional)
python3 -m venv venv  (optional)
source venv/bin/activate  (optional if you prefer to use virtual environment)
pip install wheel
pip install -r requirements.txt
```


### __Executing playbook__

All functionality is orgnized in roles under the folder __roles__
To execute :
```bash
ansible-playbook -i inventory/TEST_LAB.yml playbook_file.yaml 
```

Modify inventory file with IPs, Login credentials for your environment

#### __Backup role__

There are few variables and tags that change the behavior of the playbooks:
 - __crud__ : variable, it can be "_apply_" , "_create_" or "_delete_" .
    - "_apply_" - apply config file from remote server or local. __Device will be reloaded__
    - "_create_" - create config file and upload to remote server or keep it local. Device will not reboot
    - "_delete_" - delete config file from local device memory. Device will not reboot

 - __file_suffix__ : variable, string that will be added at the end of the backup file name. Used during backup and restore

 - __remote__: tag, specifies that backup file will be uploaded/downloaded to/from remote server
 - __local__: tag, specifies that backup file will be stored on the device
 - __delete-local__: tag, it will execute task to delete backup file from device
 - __debug__: tag, enables debug prints

#### __Example to execute backup role__
 Create backup with file_suffix test123 on remote/local and do not delete the local config
```bash
ansible-playbook -i inventory/<inventory_file>.yml backup.yaml -e "crud=create file_suffix=test123" -t [remote|local] --skip-tags delete-local,debug
ansible-playbook -i inventory/<inventory_file>.yml backup.yaml -e "crud=create file_suffix=test123" -t remote --skip-tags debug
```

Delete backup file from device
```bash
ansible-playbook -i inventory/<inventory_file>.yml backup.yaml -e "crud=delete file_suffix=test123" -t local --skip-tags debug
```

Apply config file with file_suffix "test123" 
```bash
ansible-playbook -i inventory/inventory_file backup.yaml -e "crud=apply, file_suffix=test123"  -t [local|remote] --skip-tags debug
ansible-playbook -i inventory/<inventory_file>.yml backup.yaml -e "crud=apply file_suffix=test123" -t remote
```

#### __Banner role__


There are few tags that change the behavior of the playbook:
 - __create__ : tag to create banner
 - __delete__ : tag to delete banner
 - __get__ : tag to get current banner 
 - __debug__: tag to enable debug prints

#### __Example to execute banner role__
```bash
ansible-playbook -i inventory/<inventory_file>.yml banner.yaml -t create --skip-tags debug
ansible-playbook -i inventory/<inventory_file>.yml banner.yaml -t delete --skip-tags debug
ansible-playbook -i inventory/<inventory_file>.yml banner.yaml -t get  --skip-tags debug
```