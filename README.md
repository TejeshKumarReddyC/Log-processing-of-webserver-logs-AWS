-->**Introduction**
In this project we're gonna perform log processing of a web server using cloudwatch logs, lambda, s3 and subscription filters.

-->**Installation of a simple http server in EC2**
sudo yum update -y
sudo yum install httpd -y
systemctl start httpd
systemctl enable httpd


-->**AWS CLI installation**
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws configure

-->**Cloudwatch agent installation in EC2**
yum install amazon-cloudwatch-agent -y
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
systemctl enable amazon-cloudwatch-agent
systemctl start amazon-cloudwatch-agent

-->**Create an S3 BUCKET**

-->**Create a subscription filter using the below pattern**
filter pattern 
    403 ( Filters the 403 errors of logs of the web server from the cloudwatch ).
destination
    Lambda function ( It'll be invoked by the cloudwatch and those error messages of web server are stored in S3 for further analysis).

-->**Create a rest API and link it to the Lambda**
  User can access those logs from S3 via API gateway using the API endpoint.
  
    
