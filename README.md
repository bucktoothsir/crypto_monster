# [Crypto Monster](http://cryptoomonster.com/)

## Introduction

A website to encode and decode classical ciphers. Now we support 
1. Caesar Cipher
2. Linear Cipher
3. Vigenere Cipher


<img src="media/st1.png" width="80%" height="80%" />

Our algorithm supports decoding without key. Note that the longer the ciphers, the better it works. 


<img src="media/st2.png" width="80%" height="80%" />


For Vigenere Cipher, you can choose to decode just with the length of the key or even nothing.


<img src="media/st3.png" width="80%" height="80%" />
<img src="media/st4.png" width="80%" height="80%" />

## Backend 
### Automatation Deployment
The backend is on AWS Lambda and AWS API Gateway. We employ Zappa for automation deploymentation.

```bash
pip install -r requirements.txt
cd backend
pipenv shell
# Update your dev API in localhost 
zappa update dev
```
Production API will be deployed automately by Github Actions.

## Frontend
The frontend is developed by React and hosted on AWS S3. You can also run it in the local enrironment. 
### Run in local. 
```bash
cd frontend
npm install -D
#test in localhost 
npm run start
# build
npm run build
```
### Deployment
```bash
aws s3 cp build/* s3://crypto-monster/
```
Automation deploymentation will be triggered when files in frontend directory are changed.
