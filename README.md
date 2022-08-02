# AliceCloudResume

> For code commit history of the first part of the project, please visit [here](https://github.com/thutuephan/TheCloudResumeChallenge)

## Table of Contents

- [Website](https://alicezenmind.com/)
- [Website's-Workflows-Diagram](#websites-workflows-diagram)
- [Description](#)
- [Future Development](#future-development)
- [Resources](#resources)
- [License](#license)

## Website's Workflows Diagram

![AWS-workflows-diagram-part-1](https://github.com/thutuephan/AliceCloudResume/blob/main/src/images/AWS-website-diagram.jpg)


## Description

> This simple website is a serverless web application built and deployed onlline based on AWS Cloud technologies and services such as SAM (Serverless Application Model), Route 53, CloudFront, CloudFormation, API Gateway, Lambda, DynamoDB, Certificate Managers, etc.
    
> Every time a user visits the website, the counter will show the updated views on the page. When a fetch API is called, API  will trigger the Lambda function. 

> The Lambda function then work with the DynamoDB database, thus the data updated and stored in DynamoDB will be retrieved and sent back to the user. 


### I. Front-end

1. Prepare the HTML resume styled with CSS, deployed as an Amazon S3 static website.

2. HTTPS

The S3 website URL should use HTTPS for security. Amazon CloudFront helps with this.

3. DNS 

- Purchase a domain name via Amazon Route 53
- Point the custom DNS domain name to the CloudFront distribution so the resume can be accessed at the domain name and also at the alternative DN.

4. Database

Use Amazon's DynamoDB for this

5. API

Create an API that accepts requests from the web app and communicates with the database. AWS's API Gateway and Lambda services are good for this.

6. Python

Write a bit of code in the Lambda function, use Python's boto3 library for AWS.

7. Test

Use Cypress for testing

8. Infrastructure as Code

Define the API Gateway and the Lambda function in an AWS Serverless Application Model (SAM) template and deploy them using AWS SAM CLI. This is called `infrastructure as code` or IaC.

9. Source Control: Github

10. CI/CD for Back-end and Front-end

Set up Github Actions such that when I push an update / make a change to the code from my laptop, the website is automatically updated.






## Future Development

1. Database

- Store the visitor counter in a relational database instead of DynamoDB, maybe using AWS's RDS Postgres or MySQL service.

2. Using React.js framework for the front-end.

3. API - Playing the Hits

- The visitor counter was built is a `hit` counter, it'll update everytime we refresh the page, even though I'm just one unique visitor.

- The goal is to see if I can create a new API method to only count unique visitors.

## Resources

- [CORS](https://medium.com/@patrick.krisko/cors-in-api-gateway-3d615cc0d141)

- [Diagram](https://app.diagrams.net/)

- [Amazon services](https://aws.amazon.com/)

- [Github Actions](https://www.youtube.com/watch?v=i2aRzr4ymEk&t=193s)



## License 

This project is licensed under the MIT license.
  MIT
  <br>
  https://mit-license.org


![License Badge](https://img.shields.io/badge/license-MIT-blue.svg)