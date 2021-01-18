import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.qdes_theme.helpers as helpers

from ckan.lib.plugins import DefaultTranslation


class QdesThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITranslation)
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
            'get_group_admin_emails': helpers.get_group_admin_emails
        }
