@Library('') _
def parameters = [
        systemName:         "",
        applicationName:    "",
        sonarQubeEnv:       "",
        jiraIssueUpdate:    false ,
        jiraIssuePattern:   "",
        jiraAuth:           "",
        jiraIssueField:     "",
        additionalDockerBuildParameters: "--build-arg applicationName=shared --no-cache --output type=local,dest=./dist",
        lambdaBuild: true
]

dockerPipeline(parameters)