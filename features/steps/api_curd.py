from behave import *
import requests


@given('I Set POST posts api endpoint')
def step_impl(context):
    context.api_endpoints['POST_URL'] = str(context.base_url) + '/posts'
    print('url :' + context.api_endpoints['POST_URL'])


@when('I Set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    context.request_headers['Content-Type'] = header_content_type


@when('Set request Body')
def step_impl(context):
    context.request_bodies['POST'] = {"title": "foo", "body": "bar", "userId": "1"}


@when('Send a POST HTTP request')
def step_impl(context):
    response = requests.post(url=context.api_endpoints['POST_URL'], json=context.request_bodies['POST'],
                             headers=context.request_headers)
    context.response_texts['POST'] = response.text
    status_code = response.status_code
    context.response_codes['POST'] = status_code


@then('I receive valid HTTP response code 201')
def step_impl(context):
    print('Post rep code ;' + str(context.response_codes['POST']))
    assert context.response_codes['POST'] is 201


@then('Response BODY "POST" is non-empty')
def step_impl(context):
    print(context.response_texts)
    assert context.response_texts['POST'] is not None


@given(u'I Set GET posts api endpoint "{get_id}"')
def step_impl(context, get_id):
    context.api_endpoints['GET_URL'] = str(context.base_url) + '/posts/' + get_id
    print('url :'+context.api_endpoints['GET_URL'])


@when(u'Send GET HTTP request')
def step_impl(context):
    response = requests.get(url=context.api_endpoints['GET_URL'], headers=context.request_headers)
    context.response_texts['GET'] = response.text
    status_code = response.status_code
    context.response_codes['GET'] = status_code


@then(u'I receive valid HTTP response code 200 for "{request_name}"')
def step_impl(context, request_name):
    assert context.response_codes[request_name] is 200


@then(u'Response BODY "{request_name}" is non-empty')
def step_impl(context, request_name):
    print('request_name: '+request_name)
    print(context.response_texts)
    assert context.response_texts[request_name] is not None


@given(u'I Set PUT posts api endpoint for "{post_id}"')
def step_impl(context, post_id):
    context.api_endpoints['PUT_URL'] = str(context.base_url) + '/posts/'+post_id
    print('url :' + context.api_endpoints['PUT_URL'])


@when(u'I Set Update request Body')
def step_impl(context):
    context.request_bodies['PUT'] = {"title": "foo", "body": "bar", "userId": "1", "id": "1"}


@when(u'Send PUT HTTP request')
def step_impl(context):
    response = requests.put(url=context.api_endpoints['PUT_URL'], json=context.request_bodies['PUT'],
                            headers=context.request_headers)
    context.response_texts['PUT'] = response.text
    print("update response :" + response.text)
    status_code = response.status_code
    context.response_codes['PUT'] = status_code


@given(u'I Set DELETE posts api endpoint for "{del_id}"')
def step_impl(context, del_id):
    context.api_endpoints['DELETE_URL'] = str(context.base_url) + '/posts/' + del_id
    print('url :' + context.api_endpoints['DELETE_URL'])


@when(u'I Send DELETE HTTP request')
def step_impl(context):
    response = requests.delete(url=context.api_endpoints['DELETE_URL'])
    context.response_texts['DELETE'] = response.text
    print("DELETE response :" + response.text)
    status_code = response.status_code
    context.response_codes['DELETE'] = status_code
