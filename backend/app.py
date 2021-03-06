from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db
import json

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/shows", methods=['GET'])
def get_all_shows():
    shows = db.get('shows')
    minEpisodes = request.args.get('minEpisodes')
    if minEpisodes is None:
        return create_response({"shows": shows})
    minEpisodes = int(minEpisodes)

    filtered_shows = []
    for show in shows:
        if show['episodes_seen'] >= minEpisodes:
            filtered_shows.append(show)
    
    return create_response({"shows": filtered_shows})
    # return create_response({"shows": db.get('shows')})

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")


# TODO: Implement the rest of the API here!
@app.route("/shows/<id>", methods=['GET'])
def get_show(id):
    show = db.getById('shows', int(id))
    if show is None:
        return create_response(status=404, message="No show with this id exists")
    return create_response(show)

@app.route("/shows", methods=['POST'])
def post_show():
    new_show = request.json
    if "name" not in new_show or "episodes_seen" not in new_show:
        return create_response(status=422, message="Not all parameters specified (name and episodes_seen)")

    db.create('shows', new_show)
    return create_response(new_show, 201)

@app.route("/shows/<id>", methods=['PUT'])
def put_show(id):
    int_id = int(id)
    updated_show = request.json
    old_show = db.getById('shows', int_id)
    
    if old_show is None:
        return create_response(status=404, message="No show found with that id")
    print(updated_show)
    db.updateById('shows', int_id, updated_show)
    return create_response(db.getById('shows', int_id), 201)
    

"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
