pipeline {
    agent any
    
    stages {
        stage('Create venv') {
            steps {
                // Setup venv
                sh 'python3.11 -m venv venv'
                sh '. venv/bin/activate'
                // Install req
                sh 'pip install -r backend/requirements.txt'
            }
        }
        stage('Test Flask') {
            steps {
                sh '. backend/venv/bin/activate'
                sh 'python3.11 -m pytest -v'
            }
        }
        stage('Ansible playbooks') {
            steps { // Locall creating tar
                sh 'ansible-playbook ansible/create_tar.yaml'
            }
            steps { // Copy tar and unarchive on remote
                sh 'ansible-playbook ansible/deploy_remote.yaml -i ansible/inventory.ini -v'
            }
            steps { // Create api-flask.service and start it
                sh 'ansible-playbook ansible/deploy_api_flask.yaml -i ansible/inventory.ini -v'
            }
        }
    }
    post {
        always {
            deleteDir()
            cleanWS()
        }
    }
}
