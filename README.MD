# Jenkins CICD with ansible automatizated deploy
## Project info
Project is focused on CICD.

Contains:
- Backend (simple Flask code)
- Pytest for Flask API
- ansible playbooks
- jenkinsfile

The result of this pipeline is working flask api as a service on remote VM, with access from local PC

## Jenkins Pipeline
Stages:
- Donwload repo
- Create venv (for pytests)
- Pytests
- Execute ansible playbooks
- Clear workspace

## Ansible playbooks 
#### 'create_tar' 
- tar backend folder

#### 'send_on_remote'
- copy backend.tar on remote machine
- create project folder on remote machine
- untar backend.tar to project folder.

#### 'deploy_api_flask'
- creates venv and install packages into it.
- (re)create api-flask.service
- enable and start api-flask.service

## Required changes before running pipeline
There are some vars you have to change or configure. 
- ansible inventory -credentials for VM
- Jenkinsfile - link to this git project