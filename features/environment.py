from yaml import load


def before_all(context):
    context.settings = load(open('features/conf.yaml').read())
    context.base_url = context.settings['base_url']
    context.staging_url = context.settings['staging_base_url']
    context.api_endpoints = {}
    context.request_headers = {}
    context.response_codes = {}
    context.request_bodies = {}
    context.response_texts = {}
    context.verify_ssl = True
