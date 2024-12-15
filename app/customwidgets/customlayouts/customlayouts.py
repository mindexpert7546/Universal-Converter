"""
Custom Layouts Module

This module provides custom layout widgets for the app, including:
- CircularLayout: A custom layout with a circular background and icon color customization.
- Other custom layouts implemented in the kivy file

These layouts are used to enhance the visual organization of the app's UI components.
-------------------------------------------------------------------------------
"""

from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty, ColorProperty

class CircularLayout(MDFloatLayout):
    """
    A custom layout class with a circular background and customizable colors.

    Attributes:
    -----------
    bg_color : str
        The background color of the layout, specified as a hex string.
    icon_color : list or tuple
        The color of the icon within the layout, specified as an RGBA or hex string.
    """
    
    bg_color = StringProperty('#ffffff')
    icon_color = ColorProperty('#ffffff')
    
    def __init__(self, **kwargs):
        super(CircularLayout, self).__init__(**kwargs)