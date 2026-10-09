from django.conf import settings
from django.test import SimpleTestCase


class ConfiguracionAutofieldTests(SimpleTestCase):
    def test_default_auto_field_esta_configurado(self):
        self.assertEqual(
            settings.DEFAULT_AUTO_FIELD,
            'django.db.models.BigAutoField',
        )
