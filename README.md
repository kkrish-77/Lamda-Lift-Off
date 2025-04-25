# Lamda-Lift-Off
A serverless User Greeter API built with AWS Lambda, API Gateway, and DynamoDB.
Lambda Lift-Off: User Greeter API
Ek dum mast serverless API banaya maine using AWS Lambda, API Gateway, aur DynamoDB!
Features

POST endpoint to save a user’s name aur greeting return karta hai.
GET endpoint to saare stored names dikhata hai.
Successfully stored 3 entries: Kkrish, Kkrish, aur Singh—badhiya kaam!

Tech Stack

AWS Lambda
API Gateway
DynamoDB
Python (boto3)

Setup

DynamoDB table banaya (UserGreeter) in ap-south-1.
Lambda function set kiya with the code in lambda_function.py.
API Gateway mein GET/POST endpoints banaye in ap-south-1.
Deploy kiya aur test kiya using AWS Console—kaam khatam, boss!

Results

POST endpoint: Saves names to DynamoDB with unique IDs.
GET endpoint: Retrieves all names (check the screenshot below).
Final output: {"names": [{"id": "c3e6c208-...", "name": "Kkrish"}, {"id": "55979b51-...", "name": "Kkrish"}, {"id": "336c1d5e-...", "name": "Singh"}]}


Screenshots
Add your screenshots here to show off your work!
