# Virtual Tour - Shared Albums for Shared Spaces
## Abstract
Virtual Tour is an album hosting and viewing service allowing users to mark points-of-interest within images. It utilizes Amazon Web Services for all aspects of functionality and is modeled with the three-tier architecture. Elastic Beanstalk hosts our front-end website. Lambda performs our business-logic functions and provides an API. DynamoDB and S3 store album information and image files. Lastly, development was done with GitHub.

## Usage
Click albums to view their images and learn about the location. Add images to albums or create new ones by typing in the album name, choosing an image file `.jpg, .png, or .gif`, and clicking the submit button.

## Services Used
- Elastic Beanstalk
- S3
- DynamoDB
- Lambda
- Provided Web API
- GitHub

![Cloud Architecture](https://www.dropbox.com/s/8u5sywxgvrx7qn5/AWS%20Diagram.png?raw=1)

## Monitoring and SLA
Elastic Beanstalk and Lambda share an IAM role to prevent unauthorized access to account resources. Service usage is monitored on the Elastic Beanstalk console. An account authentication system can be used to limit polling on the website and API. An S3 bucket policy is used to prevent users from uploading non-image files.

```Latex
Elastic Beanstalk 99.98% * Lambda 99.99% * S3 (Estimate) 99.9% * DynamoDB 99.99%
= Total Availability of 99.86%
```
