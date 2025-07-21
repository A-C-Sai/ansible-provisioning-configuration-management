# Provisioning & Configuration Manangement with Ansible

## Overview

### Task 1

Create three EC2 instances on AWS:

- 2 Instances with Ubuntu Distribution
- 1 Instance with AWS Linux Distribution

### Task 2

Setup password-less authentication between ansible control node and the newly created EC2 instances.

### Task 3

Automate the shutdown of Ubuntu Instances only.

## Project Setup

### Virtual Environent Creation

1. Navigate to the project directory using terminal

```
cd <PATH_TO_PROJECT_DIRECTORY>
```

2. Create a virtual environment using anaconda

```
conda create -p venv pyhton=3.12 -y
```

3. Open code editor (vscode) from the project directory

```
code .
```

4. Activating the newly created virtual environment

   - View the virtual environments present

     ```
     conda env list
     ```

   - Copy the path to the newly created virtual environment and activate the virtual environment

   ```
   conda activate <PATH_TO_VIRTUAL_ENVIRONMENT>
   ```

   - Re-run `conda env list` to verify the virtual environment is activated (indicated by an asterix (\*) in front of the newly created virtual environment)

### Installing Project Requirements

1. Project requirements are documented in `requirements.txt` file.

2. Install requirements

```
pip3 install -r requirements.txt
```

### AWS Credentials Setup

1. Navigate to `security credentials` and create a new access key and store the access key and secret key.

- If you have the `AWS CLI`, then you can use its interactive `aws configure` command to set up your credentials, default region and output format. You can verify the setup by looking at files in the `~/.aws` directory.

2. In the EC2 Service, under `Network and Security` got to `Key Pairs` and create a new key pair and download the `.pem` file in the current directory. **Change the permissions of this file using `chmod` to `400`.**

### Ansible Vault Setup

1. Create a password for your vault

```
openssl rand -base64 2048 > vault.pass
```

2. Create an encrypted file and store your AWS credentials (Access key and Secret key) in it (Ansible Needs it to communicate with AWS API)

```
ansible-vault create pass.yml --vault-password-file vault.pass
```

    - ec2_access_key: <ACCESS_KEY>
    - ec2_secret_key: <SECRET_KEY>

### General Variables

`vars.yml` contains program wide variables and serves as a central location to change the variables. **Please Modify the necessary variables according to your specifications.**

## Run Project

1. Tasks 1 & 2

```
ansible-playbook task_1_2.yaml --vault-password-file vault.pass
```

2. Task 3

```
ansible-playbook -i inventory.ini task_3.yaml --vault-password-file vault.pass
```

## Challenges

By far the biggest challeng was to automate the process of password-less authentication.

`ssh-keygen` by default isn't script friendly (interactive prompt) so I needed to find the right command options to make it non-interactive.

Automating the process of creating the `inventory.ini` file using `boto3` helped a lot.

The final approach invloves programatically copying public key created using `ssh-keygen` on the control node to all the managed nodes' `~/.ssh/authorized_keys` file.
