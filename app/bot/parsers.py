from flask_restful import reqparse

organizations_create_org_parser = reqparse.RequestParser(bundle_errors=True)
organizations_create_org_parser.add_argument('username', required=True, location='json')
organizations_create_org_parser.add_argument('api_key', required=True, location='json')
organizations_create_org_parser.add_argument('translation_origin', required=True, location='json')


organizations_update_org_parser = reqparse.RequestParser(bundle_errors=True)
organizations_update_org_parser.add_argument('external_id', location='json')
organizations_update_org_parser.add_argument('username', location='json')
organizations_update_org_parser.add_argument('api_key', location='json')
organizations_update_org_parser.add_argument('translation_origin', location='json')


organizations_add_org_language_parser = reqparse.RequestParser(bundle_errors=True)
organizations_add_org_language_parser.add_argument('name', required=True, location='json')
organizations_add_org_language_parser.add_argument('shortname', required=True, location='json')

