# coding=utf-8
"""
core.settings.contrib
"""
# needed so cartridge gets correct currency
import locale
from .base import *  # noqa

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
GRAPPELLI_INSTALLED = True

# Extra installed apps - grapelli needs to be added before others
INSTALLED_APPS += (
     'raven.contrib.django.raven_compat',  # enable Raven plugin
     PACKAGE_NAME_GRAPPELLI,
     "celery",
     "config",
     'channels',
     'rest_framework'
)

# mezzanine-mdown options
# RICHTEXT_WIDGET_CLASS = "mdown.forms.WmdWidget"
# RICHTEXT_FILTER = "mdown.filters.codehilite"

MIGRATION_MODULES = {'accounts': 'core.migration'}

GRAPPELLI_ADMIN_TITLE = 'Site administration panel'

PEOPLE_PER_PAGE = 20

EVENT_USE_FEATURED_IMAGE = True
# This one must occur before django provided middleware
# And these after django provided middleware

ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_FORM_CLASS = 'base.forms.SignupForm'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

######################
# Mezzanine agenda settings : https://github.com/jpells/mezzanine-agenda
######################

EVENT_SLUG = u"events"

######################
# CARTRIDGE (ecommerce platform for mezzanine) SETTINGS #
######################

# Cartridge uses locale to determine the number of decimal places for the
# currency. Unfortunately python does not seem to pick up our system
# locale well so we set it here. If you need to change to another locale
# please also see Dockerfile in deployment/docker as it sets up the local
# for en_ZA and you will need to adjust that before your chosen locale works
locale.setlocale(locale.LC_ALL, 'en_ZA.UTF-8')
# The following settings are already defined in cartridge.shop.defaults
# with default values, but are common enough to be put here, commented
# out, for conveniently overriding. Please consult the settings
# documentation for a full list of settings Cartridge implements:
# http://cartridge.jupo.org/configuration.html#default-settings

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

PAGE_MENU_TEMPLATES = (
    (1, "Top navigation bar", "pages/menus/dropdown.html"),
    (2, "Left-hand tree", "pages/menus/tree.html"),
    (3, "Footer", "pages/menus/footer.html"),
)

BROKER_URL = 'amqp://guest:guest@%s:5672//' % 'rabbitmq'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
