from ckan.plugins.toolkit import get_action


def qdes_get_category_list(as_select_options=True):
    groups = get_action('group_list')({}, {'all_fields': True})

    if as_select_options:
        return [{'value': group['id'], 'text': group['display_name']} for group in groups]

    return groups
