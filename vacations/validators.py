from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MinimumLengthPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 4:
            raise ValidationError(
                _("Your password must be at least 4 characters long."),
                code='password_too_short',
            )

    def get_help_text(self):
        return _("Your password must be at least 4 characters long.")
