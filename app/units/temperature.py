"""
Temperature Conversion Module

This module provides functionality to convert temperature values between various units,
such as Celsius, Fahrenheit, Kelvin, and Rankine.

Classes:
--------
TemperatureConverter : Provides a static method for converting temperature values between different units.

Variables:
----------
temperature_units : list
    A list of supported temperature units for conversion.

-------------------------------------------------------------------------------
"""

temperature_units = ["Celsius", "Fahrenheit", "Kelvin", "Rankine"]

class TemperatureConverter:
    """
    A class used to convert temperature measurements between different units.

    Methods:
    --------
    convert(value, from_unit, to_unit)
        Converts a temperature value from one unit to another, if the conversion is supported.
    """
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Converts a temperature value from one unit to another.

        Supported units include:
        - Celsius
        - Fahrenheit
        - Kelvin
        - Rankine

        Parameters:
        -----------
        value : float
            The numerical value of the temperature to be converted.
        from_unit : str
            The unit of the input temperature value. Must be one of the supported units.
        to_unit : str
            The unit to convert the temperature value into. Must be one of the supported units.

        Returns:
        --------
        float
            The converted temperature value in the target unit.

        Raises:
        -------
        ValueError
            If the provided units are invalid or if the conversion is unsupported.

        Examples:
        ---------
        >>> TemperatureConverter.convert(0, 'Celsius', 'Fahrenheit')
        32.0
        >>> TemperatureConverter.convert(100, 'Celsius', 'Kelvin')
        373.15
        """
        
        if from_unit == to_unit:
            return value
        
        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return value * 1.8 + 32.0
            elif to_unit == "Kelvin":
                return value + 273.15
            elif to_unit == "Rankine":
                return value * 9.0/5.0 + 491.67
            
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return ((value - 32.0) * 5.0) / 9.0
            elif to_unit == "Kelvin":
                return (((value - 32.0) * 5.0) / 9.0) + 273.15
            elif to_unit == "Rankine":
                return value + 459.67
            
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return ((value - 273.15) * 1.8) + 32.0
            elif to_unit == "Rankine":
                return value * 1.8
            
        elif from_unit == "Rankine":
            if to_unit == "Celsius":
                return (value - 491.67) * 5.0/9.0
            elif to_unit == "Fahrenheit":
                return value - 459.67
            elif to_unit == "Kelvin":
                return value / 1.8

        raise ValueError("Invalid units or conversion not supported")