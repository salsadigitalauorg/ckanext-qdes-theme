import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.qdes_theme import helpers


class QdesThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'qdes_theme')

    # ITemplateHelpers
    def get_helpers(self):
        return {
            'qdes_get_category_list': helpers.qdes_get_category_list,
        }
