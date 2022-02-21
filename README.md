# [Crypto Monster](http://cryptoomonster.com/)

## Introduction

A website to encode and decode classical ciphers. Now we support 
1. Caesar Cipher
2. Linear Cipher
3. Vigenere Cipher


<img src="media/st1.png" width="80%" height="80%" />

Our algorithm supports decoding without key. Note that the longer the ciphers, the better it works. 


<img src="media/st2.png" width="80%" height="80%" />


For Vigenere Cipher, you can choos to decode just with the length of the key or even nothing.


<img src="media/st3.png" width="80%" height="80%" />
<img src="media/st4.png" width="80%" height="80%" />

## Backend 
### Deployment
The backend is hosted on AWS Lambda and AWS API Gateway. We employ Zappa for deployment automation.

```bash
pip install -r requirements.txt
cd backend
pipenv shell
# Update your API
zappa update dev
```
## Frontend
The frontend is hosted on AWS S3. You can also run it in the local enrironment. 
### Run in local. 
```bash
cd frontend
npm install -D tailwindcss
npm install -D flowbite
npm install -D boxicons
npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch
```
### Deployment
Todo
