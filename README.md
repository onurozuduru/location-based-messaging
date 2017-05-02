# location-based-messaging

Mobile and Social Project Work

## API

* [How To Run](#how-to-run)
* [End Points](#end-points)

### How To Run

To run API, apply the below command under the *api* folder.

```bash
    $ cd project
    $ cd api
    $ python api.py
```

where the *project* is the name of the project folder. 

This command will run the `Flask` application, under `localhost:5000`.

An example output might be like:

```bash
    $ python api.py
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger pin code: 204-872-798
```

### End Points

| Method | End Point | Explanation |
| ------ | --------- | ----------- |
| GET | `/api/messages?q={"lat":<float:latitude>, "long":<float:longitude>}` | returns all messages close to that location |
| GET | `/api/messages/<int:messageid>` | returns message of given `messageid`  |
| GET | `/api/messages?page=<int:pagenumber>` | returns the given page. |
| POST | `/api/messages` | adds new message **(sender must be the current user)**, body form is like: `{"sender":<int:senderid>, "sendername":<string:sendername>, "message": <string:message>, "latitude":<float:latitude>, "longitude":<float:longitude>}` |
| GET | `/api/users/<int:userid>` | returns the user of given `userid` |
| POST | `/api/users` | adds new user **(if username already exits, returns `400`)**, body form is like: `{"username":<string:username>, "password":<string:password>}` |
| POST | `/login` | `{"username":<string:username>, "password":<string:password>}` |
| GET | `/logout` | logs out |
| GET | `/api/messages_found?q={"user_id":<int:user_id>}` | returns messages that found |
| GET | `/api/messages_found/<int:id>` | returns row of given `id` |  

### How to Login

**LOGIN IS DISABLED IN THIS VERSION, END POINT STILL WORKS BUT EVERYTHING CAN BE ACCESSED WITHOUT LOGIN!**

To login the system it is needed to send POST request to `http://localhost:5000/login` URL.
An example request body is shown below.


```python
    {"username":"example1", "password":"example1p"}
```

### Example POST Message

Request header's `Content-Type` for the POST must be `application/json`.

There is an example POST request for creating new message. 

**Sendername and senderid must be matching!**

```json
    {"latitude": 67.0, 
    "longitude": 24.0, 
    "message": "post test", 
    "sender": 1, 
    "sendername": "example0", 
    "timestamp": "2017-05-02 18:55"}
```
