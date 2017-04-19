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
| GET | /api/messages?q={"lat":<float:latitude>, "long":<float:longitude>} | returns all messages close to that location |
| GET | /api/messages/<int:messageid> | returns message of given `messageid`  |
| POST | /api/messages | adds new message **(sender must be the current user)**, body form is like: `{"sender":<int:senderid>, "message": <string:message>, "latitude":<float:latitude>, "longitude":<float:longitude>}` |
| GET | /api/users/<int:userid> | returns the user of given `userid` |
| POST | /api/users | adds new user **(if username already exits, returns `400`)**, body form is like: `{"username":<string:username>, "password":<string:password>}` |
| POST | /login | `{"username":<string:username>, "password":<string:password>}` |
| GET | /logout | logs out |