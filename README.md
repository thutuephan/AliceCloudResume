# AliceCloudResume

> For code commit history of the first part of the project, please visit [here](https://github.com/thutuephan/TheCloudResumeChallenge)

## Table of Contents
- [Description](#)
- [Website's-Workflows-Diagram](#websites-workflows-diagram)
- [License](#license)

## Website's Workflows Diagram

![AWS-workflows-diagram-part-1](https://github.com/thutuephan/AliceCloudResume/blob/main/src/images/AWS-website-diagram.jpg)


## Description
    - This simple website is a serverless web application built and deployed onlline based on AWS Cloud technologies and services such as SAM (Serverless Application Model), Route 53, CloudFront, CloudFormation, API Gateway, Lambda, DynamoDB, Certificate Managers, etc.
    
    - Every time a user visits the website, the counter will show the updated views on the page. When a fetch API is called, API  will trigger the Lambda function. 

    - The Lambda function then work with the DynamoDB database, thus the data updated and stored in DynamoDB will be retrieved and sent back to the user. 


## License 

This project is licensed under the MIT license.
  MIT
  <br>
  https://mit-license.org


![License Badge](https://img.shields.io/badge/license-MIT-blue.svg)