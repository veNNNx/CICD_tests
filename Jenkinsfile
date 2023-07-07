pipeline {
    agent any
    
    stages {
        stage('Download repo'){
            steps {
                git(
                    url: "git@github.com:veNNNx/CICD_tests.git",
                    branch: "main",
                    credentialsId: "1",
                    changelog: true,
                    poll: true
                    )
            }
        }
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
            // Locall creating tar
            steps { 
                sh 'ansible-playbook ansible/create_tar.yaml'
                sh 'ansible-playbook ansible/deploy_remote.yaml -i ansible/inventory.ini -v'
                sh 'ansible-playbook ansible/deploy_api_flask.yaml -i ansible/inventory.ini -v'
            }
        }
    }
    // post {
    //     always {
    //         deleteDir()
    //         cleanWS()
    //     }
    // }
}
