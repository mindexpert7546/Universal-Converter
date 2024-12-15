"""
MenuScreen Module

This module defines the MenuScreen class, which represents the main menu screen
in the app. MenuScreen allows users to select from different
metric categories, each of which opens a ConversionScreen with the appropriate
conversion settings.
-------------------------------------------------------------------------------
"""

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.factory import Factory
from app.customwidgets.custombuttons.custombuttons import CustomButton, CardButton

class MenuScreen(Screen):
    """
    A class to represent the main menu screen where users select the metric
    category for conversion.

    Methods:
    --------
    navigate_to_conversion_screen(metric_name, converter, units, color, init_unit, init_value):
        Sets up and navigates to the ConversionScreen for the selected metric.
    angle_conversion():
        Prepares ConversionScreen for angle conversions.
    area_conversion():
        Prepares ConversionScreen for area conversions.
    datastorage_conversion():
        Prepares ConversionScreen for data storage conversions.
    force_conversion():
        Prepares ConversionScreen for force conversions.
    frequency_conversion():
        Prepares ConversionScreen for frequency conversions.
    length_conversion():
        Prepares ConversionScreen for length conversions.
    mass_conversion():
        Prepares ConversionScreen for mass conversions.
    pressure_conversion():
        Prepares ConversionScreen for pressure conversions.
    speed_conversion():
        Prepares ConversionScreen for speed conversions.
    temperature_conversion():
        Prepares ConversionScreen for temperature conversions.
    time_conversion():
        Prepares ConversionScreen for time conversions.
    volume_conversion():
        Prepares ConversionScreen for volume conversions.
    open_popup():
        Opens a popup for app exit confirmation.
    exit_app():
        Exits the application.
    """
    
    def __init__(self, **kwargs):
        """
        Initializes the MenuScreen, sets up event binding for app exit.
        """
        super(MenuScreen, self).__init__(**kwargs)
        Window.bind(on_request_close=self.exit_app)
        
    def navigate_to_conversion_screen(self, metric_name, converter, units, color, init_unit, init_value):
        """
        Configures and navigates to the ConversionScreen with the settings
        specific to the selected metric.

        Parameters:
        -----------
        metric_name : str
            The name of the metric category.
        converter : object
            The conversion class instance for the metric.
        units : list
            List of units available for the selected metric.
        color : str
            Color theme for the ConversionScreen specific to the metric.
        init_unit : str
            The initial unit to display.
        init_value : float
            The initial value to display in the conversion.
        """
        
        # Access the ConversionScreen instance
        conversion_screen = self.manager.get_screen('conversion_screen')
        
        # Check if the screen already displays the current metric
        if conversion_screen.metric_name == metric_name:
            # If the screen name matches, just navigate to the screen without reinitializing
            self.manager.current = 'conversion_screen'
            self.manager.transition.direction = 'left'
            return
        
        # If metric is different, set properties and update the screen_name
        conversion_screen.color = color
        conversion_screen.converter = converter
        conversion_screen.initial_value = init_value
        conversion_screen.initial_unit = init_unit
        conversion_screen.metric_units = units
        conversion_screen.metric_name = metric_name
        
        # Navigate to the ConversionScreen
        self.manager.current = 'conversion_screen'
        self.manager.transition.direction = 'left'
        
    def angle_conversion(self):
        """Sets ConversionScreen for angle conversions."""
        from app.units.angle import AngleConverter, angle_units
        self.navigate_to_conversion_screen("angle", AngleConverter(), angle_units, '#6f0000', "Degrees", 90)
        
    def area_conversion(self):
        """Sets ConversionScreen for area conversions."""
        from app.units.area import AreaConverter, area_units
        self.navigate_to_conversion_screen("area", AreaConverter(), area_units, '#111111', "Square Metres", 1)
        
    def datastorage_conversion(self):
        """Sets ConversionScreen for datastorage conversions."""
        from app.units.datastorage import DataStorageConverter, data_units
        self.navigate_to_conversion_screen("datastorage", DataStorageConverter(), data_units, '#3f4c6b', "Kilobits", 1)
        
    def force_conversion(self):
        """Sets ConversionScreen for force conversions."""
        from app.units.force import ForceConverter, force_units
        self.navigate_to_conversion_screen("force", ForceConverter(), force_units, '#2a9064', "Newtons", 1)
        
    def frequency_conversion(self):
        """Sets ConversionScreen for frequency conversions."""
        from app.units.frequency import FrequencyConverter, frequency_units
        self.navigate_to_conversion_screen("frequency", FrequencyConverter(), frequency_units, '#0f3443', "Hertz", 1)
        
    def length_conversion(self):
        """Sets ConversionScreen for length conversions."""
        from app.units.length import LengthConverter, length_units
        self.navigate_to_conversion_screen("length", LengthConverter(), length_units, '#61a830', "Meters", 1)
    
    def mass_conversion(self):
        """Sets ConversionScreen for mass conversions."""
        from app.units.mass import MassConverter, mass_units
        self.navigate_to_conversion_screen("mass", MassConverter(), mass_units, '#aa388d', "Grams", 1)
        
    def pressure_conversion(self):
        """Sets ConversionScreen for pressure conversions."""
        from app.units.pressure import PressureConverter, pressure_units
        self.navigate_to_conversion_screen("pressure", PressureConverter(), pressure_units, '#f7a800', "Atmospheres", 1)
        
    def speed_conversion(self):
        """Sets ConversionScreen for speed conversions."""
        from app.units.speed import SpeedConverter, speed_units
        self.navigate_to_conversion_screen("speed", SpeedConverter(), speed_units, '#3f2683', "Metres per Second", 1)
        
    def temperature_conversion(self):
        """Sets ConversionScreen for temperature conversions."""
        from app.units.temperature import TemperatureConverter, temperature_units
        self.navigate_to_conversion_screen("temperature", TemperatureConverter(), temperature_units, '#ec662c', "Celsius", 25)
        
    def time_conversion(self):
        """Sets ConversionScreen for time conversions."""
        from app.units.time import TimeConverter, time_units
        self.navigate_to_conversion_screen("time", TimeConverter(), time_units, '#cf112d', "Minutes", 1)
        
    def volume_conversion(self):
        """Sets ConversionScreen for volume conversions."""
        from app.units.volume import VolumeConverter, volume_units
        self.navigate_to_conversion_screen("volume", VolumeConverter(), volume_units, '#0060a8', "Litres", 1)
            
    def open_popup(self):
        """Opens an exit confirmation popup."""
        model_inst = Factory.ExitPopup()
        yes_btn = model_inst.ids.yes_btn
        yes_btn.bind(on_release= self.exit_app)
        model_inst.open()
        
    def exit_app(self, *args):
        """Exits the application."""
        App.get_running_app().stop()
        Window.close()