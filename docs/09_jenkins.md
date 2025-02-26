# Jenkins
Jenkins is an open source CI/CD (Continuous Integration/Continuous Deployment) tool for automating the build, test and deployment of applications. It can automatically compile and run tests after the code is committed and deployed to the production environment.

What does Jenkins do?

 - Jenkins is a CI/CD automation tool for continuous integration (CI) and continuous deployment (CD). It automatically pulls code, compiles, tests, releases, and deploys to the server to improve development efficiency.

## 1. Declarative Pipeline
```groovy
pipeline {
    agent any
    environment {
        JAVA_HOME = "/usr/lib/jvm/java-11-openjdk"
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/example/repo.git'
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }
        stage('Deploy') {
            steps {
                sh './deploy.sh'
            }
        }
    }
}
```
## 2. Jenkins Job Triggering Mechanism (Webhooks, Timed Tasks)
### Webhook Triggering (GitHub, GitLab, Bitbucket)

**Automatically triggering a Jenkins Job** 

1. Configure a Webhook in the Jenkins Job
2. **Configure Webhooks** on GitHub/GitLab/Bitbucket
3. **Push code to remote repository, Jenkins automatically triggers build**

### Timed task triggering
Jenkins **Using CRON syntax** to configure timed builds:

```bash
# Trigger the Job at 3am every day.
0 3 * * * * * 

# Trigger Job every 5 minutes.
*/5 * * * * *
```

📌 **Examples**

``` Groovy
pipeline {
    triggers {
        cron('H 3 * * * *')
    }
}
```

**Role**:

- `H 3 * * * *` → **Automatically run Job at 3:00 every day**
- `*/5 * * * * *` → **Runs every 5 minutes**.

## 3. Jenkins Environment Variable Management
```bash
pipeline {
    environment {
        JAVA_HOME = "/usr/lib/jvm/java-11-openjdk"
        APP_ENV = "production"
    }
    stages {
        stage('Build') {
            steps {
                sh 'echo "Environment: $APP_ENV"'
            }
        }
    }
}
```
**Use `environment {}` to set global variables**.