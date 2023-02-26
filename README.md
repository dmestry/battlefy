# battlefy
take home test for battlefy

##Current Features:
##Github Actions
* pipeline is triggered whenever there is a code push
* CDK and python dependencies are installed 
* cdk synth is run which displays the cloudformation template/stack to be deployed
* stack to be deployed is a lambda function, current lambda function should only displays a hello message.

## TODO
write lambda function to accept accept URL, determine whether it is short or long and return the appropriate URL

#NOTES

Keep in mind:
*Github actions is new to me as I am familiar with bitbucket and Gitlab
* CDK is new to me as I am familiar with Terraform and using Cloudformation
* I had issues setting up the python environment and cdk app, so `cdk synth` didn't work for a while 
* I ran out of time given I had only 4 hours to develop the lambda function