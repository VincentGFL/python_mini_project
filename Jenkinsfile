pipeline{
        agent any
        stages{
            stage('Build'){
                steps{
                    sh "./scripts/build.sh"
                }
            }
	    stage('Deploy'){
                steps{
                    sh "./scripts/deploy.sh"
                }
            }
        }
}
