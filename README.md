# zoom-link-generator
User Zoom server-to-server oauth to generate a zoom link

Create .env file and put the following: 

```
ACCOUNT_ID=
CLIENT_ID=
CLIENT_SECRET=
ZOOM_USER=<Zoom user account>
HOSTS=<Zoom host email address>
```

Install Python and Run `pip python-dotenv`. 

Create Meeting: 
```
python zoom.py
```
