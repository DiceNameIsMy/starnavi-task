# StarNavi task
Task for Junior developer

# API Docs
`/api/v1/`

## Auth
### Login
#### POST: `accounts/login/`
 + username: str
 + paswword: str
 
#### Response: 

Code: 200 -> OK
+ access_token: str
+ refresh_token: str
+ user: nested object with user info

Code: 400 -> wrong credentialds

### Register
#### POST: `accounts/register`
+ username: str Required
+ email: str
+ password1: str Required
+ password2: str Required

#### Response:

Code: 201 -> created
+ access_token: str
+ refresh_token: str
+ user: nested object with user info

Code: 400 -> wrong request data

### User Info: returns info about authorized user
#### GET: `accounts/user` 

#### Response:

Code: 200 -> OK
+ pk: int
+ username: str
+ email: str
+ first_name: str
+ last_name: str
+ last_login: datetime
+ last_active: datetime

Code: 401 -> Unauthorized

### Other User Info:
#### GET: `accounts/<int:pk>/` (pk -> user_id)

#### Response:

Code: 200 -> OK
+ pk: int
+ username: str
+ first_name: str
+ last_name: str
+ last_login: datetime
+ last_active: datetime

Code: 404 -> Not Found



