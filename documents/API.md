# API REFERENCES
Note: The format using to send data from server to client and backwards is JSON and HTTP protocol is used

## User
---
#### *POST api/v1/accounts/*
Create new user account

Parameters: username, email, password, confirm_password, first_name

---
#### *POST api/v1/auth/login/*
User login

Parameters: username, password

---
#### *POST api/v1/auth/logout/*
User logout

---
#### *GET api/v1/accounts/*
Get all user info from server

---
#### *GET api/v1/auth/accounts/:username/*
Get specific user info from server

---
#### *PUT api/v1/auth/accounts/:username/*
Update user profile

Parameters: user, password, email

---
#### *GET api/v1/account/avatar/:username/*
Get the avatar of a user

JSON format:
```
{
  "avatar": "static/img/default.jpg"
}
```

---
#### *POST api/v1/account/follow/*
Follow a user

JSON format:
```
{
  "id": 1,
  "username": "admin",
  "facebook_id": "123456789"
}
```

---
#### *POST api/v1/account/unfollow/*
Unfollow a user

JSON format:
```
```

---
## Topic
#### *GET api/v1/topics/*
Get all topics available

---
#### *GET api/v1/topic/:topicID/*
Get the topic with id specified

---
#### *GET api/v1/topics/?keyword=test*
Get 10 most related topic with the keyword provided

---
#### *POST api/v1/topic/*
Add new topic to server

---
#### *POST api/v1/topic/?questionID=1*
Add new topic for the question with id specified

JSON format
```
{
  "name": "Music"
}
```

---
#### *DELETE api/v1/topic/?questionID=1*
Delete topic for the question with id specified

JSON format
```
{
  "name": "Music"
}
```

---
## Question

---
#### *GET api/v1/questions/?type=newest&topicID=1&start=1&end=10*
Get list of newest questions from start to end which belongs to the topic with id specified

---
#### *GET api/v1/questions/?type=related&keyword=test*
Get 10 most related questions with the keyword provided

---
#### *GET api/v1/question/?questionID=1*
Get the question with the id provided

---
#### *POST api/v1/question/*
Post new question to server

---
#### *PUT api/v1/question/?questionID=1*
Update a question with id specified

---
## Answer
---
#### *GET api/v1/answers/?questionID=1*
Get all answer of a question with id specified

---
#### *POST api/v1/answer/?questionID=1*
Post an answer for a question with id specified

---
#### *PUT api/v1/answer/?answerID=1*
Update an answer with id specified

---
#### *GET api/v1/answers/?questionID=1&start=1&end=10*
Get all answers for a question with id specified, from start to end in newer order (sorted by created_date)

---
## Comment
---
#### *GET api/v1/comments/?id=1*
Get all comments for a post (question or answer) with id specified

---
#### *POST api/v1/comment/?id=1*
Post new comment for a post (question or answer) with id specified

---
#### *PUT api/v1/comment/?commentID=1*
Update a comment with id specified
