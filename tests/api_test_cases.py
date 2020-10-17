import pytest
import requests
import json
from pytest_schema import schema
headers = {"Content-Type":"application/json","charset":"UTF-8"}

response_schema = {
    "userId": int,
    "id": int,
    "title": str,
    "body": str
}

# Test case to verify if api call returns 100 records
def test_verify_response_has_100_records():
    print("Test case to verify if API returns minimum 100 records")
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    content = json.loads(response.text)
    assert len(content) == 100
    assert schema([response_schema]) == content
    print(" API {} returns 100 records".format(url))

# Test case to verify if api call returns only 1 records for give id
def test_verify_response_has_only_1_record():
    print("Test case to verify if API returns only 1 records")
    id = 1
    url = "https://jsonplaceholder.typicode.com/posts/{}".format(id)
    response = requests.get(url, headers = headers)
    assert response.status_code == 200
    content = json.loads(response.text)
    print(" API {} returns only 1 record".format(url))
    assert content['id'] == 1
    assert schema(response_schema) == content
    print(" API response id is {} as given in url".format(id))


# Test case to verify if api call returns invalid posts error message with 404 error code
def test_verify_invalid_posts_in_response():
    print("Test case to verify invalid response and 404 error code from API")
    url = "https://jsonplaceholder.typicode.com/invalidposts"
    response = requests.get(url, headers=headers)
    assert response.status_code == 404

# Test case to verify if api call to add a record works
def test_verify_add_record_using_api():
    print("Test case to verify if API successfully added record")
    body = {"title":"foo", "body":"bar", "userId":1}
    url = "https://jsonplaceholder.typicode.com/posts"
    # Delete 1 record before adding new record
    r = requests.delete(url+"/100", headers=headers)
    assert r.status_code == 200
    response = requests.post(url, data=str(body), headers=headers)
    assert response.status_code == 201
    content = json.loads(response.text)
    asset_id = content['id']
    post_url = "https://jsonplaceholder.typicode.com/posts/{}".format(asset_id)
    response = requests.get(post_url)
    print(response)
    assert response.status_code == 200
    content = json.loads(response.text)
    assert content['id'] == id
    print(" API response id is {} as given in url".format(id))


# Test case to verify if api call ot update a record works
def test_verify_update_record_using_api():
    print("Test case to verify if API successfully added record")
    body = {"userId":1, "id":1, "title":"abc", "body":"xyz"}
    id = 1
    url = "https://jsonplaceholder.typicode.com/posts/{}".format(id)
    data = json.dumps(body)
    response = requests.put(url, data=data, headers=headers)
    assert response.status_code in [200, 201]
    content = json.loads(response.text)
    print("content")
    print(content)
    # asset_id = content['id']
    post_url = "https://jsonplaceholder.typicode.com/posts/{}".format(id)
    response = requests.get(post_url, headers=headers)
    print(response.text)
    assert response.status_code == 200
    content = json.loads(response.text)
    assert content == body
    print(" Data is not updated properly".format(id))


# Test case to verify if api call to delete a record works
def test_verify_delete_record_using_api():
    print("Test case to verify if API successfully deletes record")
    id = 100
    url = "https://jsonplaceholder.typicode.com/posts/{}".format(id)
    response = requests.delete(url, headers=headers)
    assert response.status_code in [200, 201]
    content = json.loads(response.text)
    print("content")
    print(content)
    post_url = "https://jsonplaceholder.typicode.com/posts/{}".format(id)
    response = requests.get(post_url, headers=headers)
    print(response.text)
    assert response.status_code == 200
    content = json.loads(response.text)
    print("Record is not getting deleted using API")
