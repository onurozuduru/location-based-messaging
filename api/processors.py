from flask_login import current_user
from flask_restless import ProcessingException


def user_auth_func(instance_id=None, **kw):
    if not instance_id:
        raise ProcessingException(description='Not Authorized', code=401)
    if not instance_id == current_user.get_id():
        raise ProcessingException(description='Not Authorized', code=401)
    if not current_user.is_authenticated:
        raise ProcessingException(description='Not Authorized', code=401)


def auth_func(**kw):
    if not current_user.is_authenticated:
        raise ProcessingException(description='Not Authorized', code=401)


def message_post(data=None, **kw):
    if data and 'sender' in data:
        if not data['sender'] == current_user.get_id():
            raise ProcessingException(
                description='Not Authorized - Sender is not the current user',
                code=401)


def message_location_filter(search_params=None, **kw):
    # This checks if the preprocessor function is being called before a
    # request that does not have search parameters.
    if search_params is None:
        return
    if "lat" not in search_params and "long" not in search_params:
        return
    radius = 2
    latitude = search_params["lat"]
    longitude = search_params["long"]
    # filter results by inside the circle
    filt = {"and": [{"name": "latitude", "op": "lt", "val": latitude + radius},
             {"name": "latitude", "op": "gt", "val": latitude - radius},
             {"name": "longitude", "op": "lt", "val": longitude + radius},
             {"name": "longitude", "op": "gt", "val": longitude - radius}]}
    # Check if there are any filters there already.
    if 'filters' not in search_params:
        search_params['filters'] = []
    # Append filter to the list of filters.
    search_params['filters'].append(filt)
