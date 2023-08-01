from .base_control import BaseControl


class Checkbox(BaseControl):
    def __init__(self, checkbox_element):
        super().__init__(checkbox_element)

    def is_enabled(self):
        self.element.is_enabled()

    def is_selected(self):
        return self.element.is_selected()
