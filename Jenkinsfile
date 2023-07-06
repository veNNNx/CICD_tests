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
        stage('Test') {
            steps {
                // Setup venv
                sh 'python3.11 -m venv venv'
                sh '. venv/bin/activate'
                
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
