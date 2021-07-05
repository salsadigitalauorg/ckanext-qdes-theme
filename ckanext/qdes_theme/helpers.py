import ckan.model as model
import os
import logging

from ckan.plugins.toolkit import get_action
from pprint import pformat

log = logging.getLogger(__name__)


def get_group_admin_emails(id):
    admins = get_action('member_list')({}, {'id': id, 'object_type': 'user', 'capacity': 'admin'})
    emails = []

    if admins:
        for admin in admins:
            admin_list = list(admin)
            user_dict = get_action('user_show')({}, {'id': admin_list[0]})

            if user_dict.get('email') or None:
                emails.append(user_dict.get('email'))

    return emails


def get_ga_tracking_id():
    return os.getenv('GA_TRACKING_ID')

def return_format_label(resource):    
    data_dict = {}
    data_dict['vocabulary_service_name'] = 'format'
    data_dict['term_label'] = None
    data_dict['term_uri'] = resource
    label = get_action('get_vocabulary_service_term')({}, data_dict)
    return label['label']
