from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class FourDigitPasswordValidator:
    def validate(self, password, user=None):
        if not (password.isdigit() and len(password) == 4):
            raise ValidationError(
                _("Your password must contain exactly 4 digits."),
                code='password_must_be_4_digits',
            )

    def get_help_text(self):
        return _("Your password must contain exactly 4 digits.")
