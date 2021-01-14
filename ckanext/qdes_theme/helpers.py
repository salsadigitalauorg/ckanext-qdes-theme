import ckan.model as model
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