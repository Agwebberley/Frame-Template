import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "frame_template.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import frame_template.users.signals  # noqa: F401
