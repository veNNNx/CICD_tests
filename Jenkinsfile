pipeline {
    agent any
    
    stages {
        stage('Clone repository') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'git@github.com:veNNNx/CICD_tests.git']]])
            }
        }
        stage('Download repo'){
            steps {
                git 'git@github.com:veNNNx/CICD_tests.git'
            }
        }
        stage('Test') {
            steps {
                // Setup venv
                sh 'python3.11 -m venv venv'
                sh 'source venv/bin/activate'
                
                // Install req
                sh 'pip install -r requirements.txt'
                // Aktywacja środowiska wirtualnego
                sh 'source venv/bin/activate'
                
                // Uruchamianie testów jednostkowych
                sh 'python3.11 -m pytest -v'

            }
        }
        // stage('Create RPM') {
        //     steps {

        //     }
        // }
        
        // stage('Deploy RPM') {
        //     steps {
        //         // przesłanie paczki na vmkę
        //         // uruchomienie flaskowej apki
        //         // Wdrożenie aplikacji
        //         // Dodaj odpowiednie polecenia lub skrypty do wdrożenia aplikacji
        //     }
        // }
        // stage('Test finall VM') {
        //     steps {
        //         // przesłanie paczki na vmkę
        //         // uruchomienie flaskowej apki
        //         // Wdrożenie aplikacji
        //         // Dodaj odpowiednie polecenia lub skrypty do wdrożenia aplikacji
        //     }
        // }
    }
}
