# ---- Do not change the code below ----
# User identity dictionary
user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}

# delete_database() function, DO NOT CHANGE
def delete_database():
    # perform deletion
    print('Database deleted!')

# ---- Do not change the code above ----


# You code starts here:
# Define a check_permission() decorator:
def check_permission(func):
    def secure_func():
        if user['role'] == 'admin':
            print('Checking Admin')
        else:
            raise PermissionError
    return secure_func

# Use the check_permission() decorator and delete_database() function to create a secure_delete_database() function:
secure_delete_database = check_permission(delete_database)



print(secure_delete_database())


"""
Implement a @access_control decorator that can be used like this:
@access_control(access_level)
def delete_some_file(filename):
    # perform the deletion operation
    print('{} is deleted!'.format(filename))
Your decorator should meet the following requirements:
- It takes in an argument `access_level` and would compare the current user's role with the access level.
- You can get the current user's role, represented by an integer, by calling the `get_current_user_role()` function.
    You don't need to implement this function, we will take care of it for you.
- You may assume smaller access level value would have higher privilege. For example, 0 - admin, 1 - user, 2 - guest.
    So you can check if the user has proper access level like this:
if get_current_user_role() <= access_level:
    # do something
else:
    # forbid
- If the user has the proper access level, we allow the user to call the function (that has this decorator).
- If the user does not have a proper access level, we raise a `PermissionError` with the message:
    'You do not have the proper access level.'
- The decorator should be generic, which means it can be applied to any function that has any amount of
    arguments (or key word arguments).
- Your decorator should keep the original function's `__name__` and `__doc__` strings.
"""


# DO NOT CHANGE
def get_current_user_role() -> int:
    # return the current user's role, represented by an int
    # for example, 0 - admin, 1 - user, 2 - guest
    # You don't need to change this function, we will replace it with a real function that returns the user's role
    return 0


def access_control(access_level: int):
    # You code starts here:
    def user_has_permission(func):
        def secure_func(*args, **kwargs):
            if get_current_user_role() <= access_level:
                return func(*args, **kwargs)
            else:
                raise PermissionError
        return secure_func
    return user_has_permission

