from .base_control import BaseControl


class Button(BaseControl):
    def __init__(self, button_element):
        super().__init__(button_element)

    def is_enabled(self):
        self.element.is_enabled()

    def is_selected(self):
        return self.element.is_selected()
