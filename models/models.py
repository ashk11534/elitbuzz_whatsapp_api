from odoo import fields, models, api
import requests

def get_instance_id(access_token):
    data = {
        'access_token': access_token
    }

    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(f'https://api.rangebroadcast.com/api/create_instance', json=data, headers=headers)
        response = response.json()
        return response.get('instance_id')
    except Exception as e:
        return '6715EDA2DBE4A'


def send_message(phone_number, message, instance_id, access_token):
    data = {
        'number': phone_number,
        'message': message,
        'instance_id': instance_id,
        'access_token': access_token,
        'type': 'text'
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(f'https://api.rangebroadcast.com/api/send', json=data, headers=headers)
    print(response.json())

class CRMWhatsappInherit(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def create(self, vals):
        phone_number = vals.get('phone') if vals.get('phone') else '8801955477945'

        try:
            instance_id = get_instance_id('670cf52e29b86')

            message = "Hi, we are from Elitbuzz technologies LTD. A new CRM lead has been created for you."

            send_message(phone_number, message, instance_id, access_token='670cf52e29b86')

        except Exception as e:
            print('Something went wrong')

        return super(CRMWhatsappInherit, self).create(vals)
