# AliceCloudResume

> For code commit history of the first part of the project, please visit [here](https://github.com/thutuephan/TheCloudResumeChallenge)

## Table of Contents

- [Website](https://alicezenmind.com/)
- [Website's-Workflows-Diagram](#websites-workflows-diagram)
- [Description](#)
- [License](#license)

## Website's Workflows Diagram

![AWS-workflows-diagram-part-1](https://github.com/thutuephan/AliceCloudResume/blob/main/src/images/AWS-website-diagram.jpg)


## Description

> This simple website is a serverless web application built and deployed onlline based on AWS Cloud technologies and services such as SAM (Serverless Application Model), Route 53, CloudFront, CloudFormation, API Gateway, Lambda, DynamoDB, Certificate Managers, etc.
    
> Every time a user visits the website, the counter will show the updated views on the page. When a fetch API is called, API  will trigger the Lambda function. 

> The Lambda function then work with the DynamoDB database, thus the data updated and stored in DynamoDB will be retrieved and sent back to the user. 


### I. 

## Future Development

1. Database

- Store the visitor scounter in a relational databse instead of DynamoDB, maybe using AWS's RDS Postgres or MySPL service.

2. Using React.js framework for the front-end.

3. API - Playing the Hits

- The visitor counter was built is a `hit` counter, it'll update everytime we refresh the page, even though I'm just one unique visitor.

- The goal is to see if I can create a new API method to only count unique visitors.

## License 

This project is licensed under the MIT license.
  MIT
  <br>
  https://mit-license.org


![License Badge](https://img.shields.io/badge/license-MIT-blue.svg)