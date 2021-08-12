# StarNavi task
Task for Junior developer

Type examples:
+ date -> '2021-08-01' - year-month-day

# API Docs
`/api/v1/`

## Auth
### Login `accounts/login/`
#### POST: 
 + username: str
 + paswword: str
 
##### Response: 

Code: 200 -> OK
+ access_token: str
+ refresh_token: str
+ user: nested object with user info

Code: 400 -> wrong credentialds

### Register `accounts/register/`
#### POST: 
+ username: str Required
+ email: str
+ password1: str Required
+ password2: str Required

##### Response:

Code: 201 -> created
+ access_token: str
+ refresh_token: str
+ user: nested object with user info

Code: 400 -> wrong request data

### User Info: `accounts/user/` 
returns info about authorized user
#### GET: 

##### Response:

Code: 200 -> OK
+ pk: int
+ username: str
+ email: str
+ first_name: str
+ last_name: str
+ last_login: datetime
+ last_active: datetime

Code: 401 -> Unauthorized

### Other User Info: `accounts/<int:pk>/` (pk -> user_id)
#### GET: 

##### Response:

Code: 200 -> OK
+ pk: int
+ username: str
+ first_name: str
+ last_name: str
+ last_login: datetime
+ last_active: datetime

Code: 404 -> Not Found

## Posts
### All posts `posts/`
#### GET:
##### Filter Params:
+ author: int
+ created_at_start: date
+ created_at_end: date
+ updated_at_start: date
+ updated_at_end: date
+ ordering: str

##### Response:

Code: 200 -> OK
+ count: int,
+ next: url.
+ previous: url,
+ results: 
  + author: int,
  + image: url | null,
  + text: str,
  + count_likes: int,
  + created_at: datetime,
  + updated_at: datetime

#### POST:
##### Data:
+ author: int,
+ text: str,
+ img: image

##### Response:
+ author: int,
+ text: str,
+ image: url | null,
+ count_likes: int,
+ created_at: datetime,
+ updated_at: datetime


# TODO other endpoints
`posts/<int:pk>/`
`posts/<int:pk>/like/`
`posts/<int:pk>/stats/`




