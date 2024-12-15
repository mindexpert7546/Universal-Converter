"""
Custom Buttons Module

This module provides custom button widgets for the app, including:
- CustomButton: A stylized button with customizable text and background color.
- CardButton: A card-styled button that includes an icon, title, and ripple effect.
- Other custom buttons implemented in the kivy file

These buttons are used throughout the app to enhance the user interface.
-------------------------------------------------------------------------------
"""

from kivy.uix.button import Button, ButtonBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.properties import ColorProperty, StringProperty
from kivymd.uix.floatlayout import MDFloatLayout
    
class CustomButton(RectangularRippleBehavior, Button):
    """
    A custom button class with ripple effect, customizable text, and background color.

    Attributes:
    -----------
    text : str
        The text displayed on the button.
    text_color : list
        The color of the text, defined as an RGBA or hex string.
    bg_color : str
        The background color of the button, defined as a hex string.
    """
    
    text = StringProperty('Button')
    text_color = ColorProperty('white')
    bg_color = StringProperty('#027783')
    
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)

class CardButton(RectangularRippleBehavior, ButtonBehavior, MDFloatLayout):
    """
    A card-styled button widget with an icon, title, and ripple effect.
    
    Attributes:
    -----------
    bg_color : str
        The background color of the button, defined as a hex string.
    unit_icon : str
        The path to the icon image displayed on the button.
    unit_title : str
        The title text displayed on the button.
    
    Methods:
    --------
    __init__(self, **kwargs):
        Initializes the CardButton with any additional properties passed.
    """
    
    bg_color= StringProperty('#ffffff')
    unit_icon = StringProperty('')
    unit_title = StringProperty('Button')
    
    def __init__(self, **kwargs):
        super(CardButton, self).__init__(**kwargs)