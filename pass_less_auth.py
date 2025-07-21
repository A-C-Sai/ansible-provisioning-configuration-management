import os
import subprocess
import yaml

if not os.path.exists('~/.ssh/id_rsa'):
    subprocess.run("ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ''", shell=True, check=True)

with open('vars.yml', 'r', encoding='utf-8') as fp:
    data = yaml.safe_load(fp)

PEM_FILE=f"./{data['pem_key_file']}.pem"
PUB_KEY="$HOME/.ssh/id_rsa.pub"

def get_instance():
   with open('inventory.ini', 'r') as fp:
      for instance in fp:
         yield instance.strip()



for instance in get_instance():
   subprocess.run(f'cat {PUB_KEY} | ssh -o StrictHostKeyChecking=no -i "{PEM_FILE}" "{instance}" \
                  "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"', shell=True, check=True)


