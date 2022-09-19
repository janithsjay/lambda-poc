@Library('') _
def parameters = [
        additionalDockerBuildParameters: "--build-arg applicationName=shared --no-cache --output type=local,dest=./dist",
        lambdaBuild: true
]

dockerPipeline(parameters)