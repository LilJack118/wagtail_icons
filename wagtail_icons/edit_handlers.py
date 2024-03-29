from .widgets import AdminIconChooser
try:
    from wagtail.admin.panels import FieldPanel
except ImportError:
    from wagtail.admin.edit_handlers import FieldPanel

class IconsChooserPanel(FieldPanel):
    def __init__(self, field_name, group=None, *args, **kwargs):
        super().__init__(field_name, *args, **kwargs)
        self.group = group

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs.update(
            group=self.group,
        )
        return kwargs

    def widget_overrides(self):
        return {
            self.field_name: AdminIconChooser(group=self.group),
        }

    def get_form_options(self):
        options = super().get_form_options()
        options['widgets'] = {
            self.field_name: AdminIconChooser(group=self.group),
        }
        return options
