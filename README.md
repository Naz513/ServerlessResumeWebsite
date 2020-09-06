# Serverless Resume Website
Serverless Resume Website Using Cloudformation

## Live Project and Blog :books:
Live Project: [Serverless Resume Website Live](https://resume.mohdsaquib.com)

Blog Post: [Serverless Resume Blog Post](https://mohdsaquib.com/content/projects/resumeproject.html)

## Project Description :movie_camera:
Developed a website to display my resume on a serverless architecture infrastructure using the power of AWS Cloudformation. The Infrastrcuture code can be used to deploy any static website. Entire infrastructure is deployed on AWS and deploys within 10 mins. 

## Project Architecture :wrench:

The following image displays the entire architecture developed in cloudforamtion.

![Architecture](https://mohdsaquib.com/assets/resumeProjectImages/architecture.png)

## Services :truck:
The following AWS Services will be created:
1. S3 Bucket
1. S3 Logs Bucket
1. ACM Certificate
1. API
1. APIDeployment
1. APIStage
1. APIUsagePlan
1. BucketPolicy
1. CloudFront
1. CloudFrontOAI
1. CodeCommitRepo
1. CodePipeline
1. CodePipeline Role
1. DynamoDb Table
1. Lambda Function
1. Lambda Function Permission
1. Lambda Execution Role
1. Route 53 Config


## How to Use? :clipboard:

This template can be used by anyone to provision their serverless static wesbite with only a few clicks and information.

### Prerequisites :book:
1. User must own a domain in AWS or have trasnfered their custom domain to AWS
1. User must not use a Root Account
1. User must hae the rights to provision and deploy all the resources
1. User needs to be knowdlegeable about basic YAML, Javascript, Python, HTML, CSS
1. Must have access to root user's email for AWS certification Authorization.

### Steps! :rocket:
1. Log in to AWS Console
1. Go to Cloudformation
1. Click on **Create Stack**
1. Select **With new resources**
1. Select **Upload a template file**
1. Click on **Next**
1. Enter a **Stack Name**
1. Fill out the following Parameters
    1. S3 Configuration
    1. Back-End Configuration
    1. API Configuration
    1. Other Configuration 
    1. Tags
1. Click on **Next**
1. Enter any tags if necessary 
1. Click on **Next**
1. Check **I acknowledge that AWS CloudFormation might create IAM resources.** to allow Cloudformation to create all the necessary IAM resources
1. Click on **Create Stack**
1. After 6-7 mins, the root account will get a confirmation to **verify the ACM Certificate**
1. Within **10 mins**, the infrastucture will be loaded in.
1. Click on **Outputs**
1. Copy the CodeRepoURL to push your static website code

#### NOTE! 📝 
**PLEASE GO THROUGH THE CODE. THERE ARE SOME PLACES WHERE YOU NEED TO INSERT THE API MANUALY AND UPDATE CERTAIN PARTS OF THE INFRASTRUCTURE.**

### Cost :moneybag:
The project can cost ~$1.50 per month and may vary depending on several factors. Best to refer back to AWS documents for pricings.

#### Got Questions? :question:
Feel free to email me at *nsaquib96@gmail.com*
