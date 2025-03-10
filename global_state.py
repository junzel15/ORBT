logged_in_user = None


def update_user_data(user):
    global logged_in_user
    logged_in_user = user


def get_logged_in_user():
    return logged_in_user


def logout_user():
    global logged_in_user
    logged_in_user = None
