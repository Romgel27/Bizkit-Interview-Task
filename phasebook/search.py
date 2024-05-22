from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
def search_users(id=None, name=None, age=None, occupation=None):
    results = []

    for user in USERS:
        if id is not None and user['id'] == id:
            return [user]
        
        match = True

        if name is not None and name.lower() not in user['name'].lower():
            match = False
        if age is not None and not (age - 1 <= user['age'] <= age + 1):
            match = False
        if occupation is not None and occupation.lower() not in user['occupation'].lower():
            match = False
        
        if match:
            results.append(user)

    return results
    return USERS
