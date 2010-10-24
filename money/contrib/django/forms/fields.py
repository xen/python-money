from django.utils.translation import ugettext_lazy as _
from django import forms
from widgets import CurrencySelectWidget
from money import Money, CURRENCY

class MoneyField(forms.MultiValueField):
    def __init__(self, choices=None, decimal_places=2, max_digits=12, *args, **kwargs):
        choices = choices or list(( (u"%s" % (c.code,), u"%s - %s" % (c.code, c.name)) for i, c in sorted(CURRENCY.items()) if c.code != 'XXX'))

        self.widget = CurrencySelectWidget(choices)

        fields = (
            forms.DecimalField(
                decimal_places=decimal_places,
                max_digits=max_digits),
            forms.ChoiceField(choices=choices)
        )
        super(MoneyField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        """
        Take the two values from the request and return a single data value
        """
        if data_list:
            return Money(*data_list)
        return None
