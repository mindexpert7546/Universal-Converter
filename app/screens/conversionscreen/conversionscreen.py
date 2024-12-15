"""
ConversionScreen Module

This module defines the ConversionScreen class, which displays the selected
conversion interface, allowing users to convert values between units within a
specific metric category.
-------------------------------------------------------------------------------
"""

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, ListProperty, StringProperty, NumericProperty
from kivy.metrics import dp
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from app.customwidgets.customlayouts.customlayouts import CircularLayout

Window.softinput_mode = 'below_target'

class ConversionScreen(Screen):
    """
    A class to represent the conversion screen for different metrics.

    Attributes:
    -----------
    metric_name : str
        Name of the metric currently displayed.
    converter : object
        The conversion class instance for performing unit conversions.
    metric_units : list
        List of units available for conversion within the selected metric.
    color : str
        Background color associated with the selected metric.
    initial_unit : str
        The default unit displayed in the conversion input.
    initial_value : float
        The default value displayed in the conversion input.

    Methods:
    --------
    on_pre_enter():
        Resets initial values for conversion when the screen is displayed.
    open_first_menu():
        Opens a dropdown menu for the first unit selection.
    open_second_menu():
        Opens a dropdown menu for the second unit selection.
    menu_callback(unit, callback):
        Sets selected unit in the dropdown and initiates conversion.
    format_result(result):
        Formats the conversion result to fit within 12 digits.
    first_conversion():
        Converts value from the first unit to the second unit.
    second_conversion():
        Converts value from the second unit to the first unit.
    """
    
    metric_name = StringProperty('')
    converter = ObjectProperty(None)
    metric_units = ListProperty([])
    color = StringProperty('#ffffff') # Metric special color (set to default color)
    initial_unit = StringProperty('')
    initial_value = NumericProperty(0)
    
    def __init__(self, **kwargs):
        """
        Initializes the ConversionScreen, setting a flag to manage concurrent
        conversion operations.
        """
        super(ConversionScreen, self).__init__(**kwargs)
        self.is_converting = False  # Flag to prevent simultaneous conversion loops
        
    def on_pre_enter(self, *args):
        """
        Called when the screen is displayed. Resets unit values to initial
        values.
        """
        self.ids.first_unit_value.text = f"{self.initial_value}"
        self.ids.second_unit_value.text = f"{self.initial_value}"
        
    def open_first_menu(self):
        """
        Opens the dropdown menu for the first unit selection, displaying
        available units.
        """
        
        self.first_menu = MDDropdownMenu(
            caller = self.ids.first_unit_btn,
            items = [
                {
                    'text': f'{unit}',
                    'on_release': lambda x=f'{unit}': self.menu_callback(x, 'first_menu')
                    }
                for unit in self.metric_units
                ],
            ver_growth = "down",
            max_height = dp(300),
            position = 'bottom'
            
            )
        self.first_menu.open()
        
    def open_second_menu(self):
        """
        Opens the dropdown menu for the second unit selection, displaying
        available units.
        """
        
        self.second_menu = MDDropdownMenu(
            caller = self.ids.second_unit_btn,
            items = [
                {
                    'text': f'{unit}',
                    'on_release': lambda x=f'{unit}': self.menu_callback(x, 'second_menu')
                    }
                for unit in self.metric_units
                ],
            ver_growth = "up",
            max_height = dp(300),
            position = 'top'
            
            )
        self.second_menu.open()
        
    def menu_callback(self, unit, callback):
        """
        Updates the selected unit and performs conversion based on the selected
        unit from the dropdown menu.

        Parameters:
        -----------
        unit : str
            The unit selected from the dropdown menu.
        callback : str
            Indicates whether the selection is for 'first_menu' or 'second_menu'.
        """
        
        if callback == 'first_menu':
            self.ids.first_unit_name.text = unit
            self.first_menu.dismiss()
            self.first_conversion()
        else:
            self.ids.second_unit_name.text = unit
            self.second_menu.dismiss()
            self.second_conversion()
    
    def format_result(self, result):
        """
        Formats the result of a conversion to fit within 12 digits.

        Parameters:
        -----------
        result : float
            The result of a unit conversion.

        Returns:
        --------
        str
            Formatted result with up to 12 characters.
        """
        
        # Format the number in fixed-point notation with up to 12 digits after the decimal
        formatted_result = f"{result:.12f}".rstrip("0").rstrip(".")
        
        # Count digits only (exclude decimal point and negative sign)
        digit_count = len(formatted_result.replace(".", "").replace("-", ""))
        
        # If the result has 12 or fewer digits, return it in fixed-point notation
        if digit_count <= 12:
            return formatted_result
        
        # Otherwise, use scientific notation to fit within 12 characters
        return f"{result:.6e}"[:12]
            
    def first_conversion(self):
        """
        Converts the value from the first unit to the second unit, updating the
        second unit's display with the result.
        """
        
        if self.is_converting:
            return  # Exit if a conversion is already in progress
        
        self.is_converting = True
        
        try:
            # Get the current values and units
            from_value = float(self.ids.first_unit_value.text)
            from_unit = self.ids.first_unit_name.text
            to_unit = self.ids.second_unit_name.text
    
            # Perform the conversion
            result = self.converter.convert(from_value, from_unit, to_unit)

            self.ids.second_unit_value.text = self.format_result(result)
            
        except ValueError:
            self.ids.second_unit_value.text = "Invalid input"
            
        finally:
            self.is_converting = False  # Reset flag after conversion is done

    
    def second_conversion(self):
        """
        Converts the value from the second unit to the first unit, updating the
        first unit's display with the result.
        """
        
        if self.is_converting:
            return  # Exit if a conversion is already in progress
        
        self.is_converting = True
        
        try:
            # Get the current values and units
            from_value = float(self.ids.second_unit_value.text)
            from_unit = self.ids.second_unit_name.text
            to_unit = self.ids.first_unit_name.text

            # Perform the reverse conversion
            result = self.converter.convert(from_value, from_unit, to_unit)

            self.ids.first_unit_value.text = self.format_result(result)
            
        except ValueError:
            self.ids.first_unit_value.text = "Invalid input"
            
        finally:
            self.is_converting = False  # Reset flag after conversion is done