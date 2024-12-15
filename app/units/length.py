"""
Length Conversion Module

This module provides functionality to convert length values between various units,
such as Meters, Inches, and Miles.

Classes:
--------
LengthConverter : Provides a static method for converting length values between different units.

Variables:
----------
length_units : list
    A list of supported length units for conversion.
-------------------------------------------------------------------------------
"""

length_units = ["Millimeters", "Centimeters", "Meters", "Kilometers", "Inches", "Feet", "Yards", "Miles", "Nautical Miles"]

class LengthConverter:
    """
    A class used to convert length measurements between different units.

    Methods:
    --------
    convert(value, from_unit, to_unit)
        Converts a length value from one unit to another, if the conversion is supported.
    """
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Converts a length value from one unit to another.

        Supported units include:
        - Millimeters
        - Centimeters
        - Meters
        - Kilometers
        - Inches
        - Feet
        - Yards
        - Miles
        - Nautical Miles

        Parameters:
        -----------
        value : float
            The numerical value of the length to be converted.
        from_unit : str
            The unit of the input length value. Must be one of the supported units.
        to_unit : str
            The unit to convert the length value into. Must be one of the supported units.

        Returns:
        --------
        float
            The converted length value in the target unit.

        Raises:
        -------
        ValueError
            If the provided units are invalid or if the conversion is unsupported.

        Examples:
        ---------
        >>> LengthConverter.convert(1000, 'Meters', 'Kilometers')
        1.0
        >>> LengthConverter.convert(1, 'Miles', 'Feet')
        5280.0
        """
        
        if from_unit == to_unit:
            return value
        elif from_unit == "Centimeters":
            if to_unit == "Millimeters":
                return value * 10.0
            elif to_unit == "Meters":
                return value / 100.0
            elif to_unit == "Kilometers":
                return value / 100000.0
            elif to_unit == "Inches":
                return value / 2.54
            elif to_unit == "Feet":
                return value / 30.48
            elif to_unit == "Yards":
                return value / 91.44
            elif to_unit == "Miles":
                return value / 160934.4
            elif to_unit == "Nautical Miles":
                return value / 185200.0
        elif from_unit == "Feet":
            if to_unit == "Millimeters":
                return value * 304.8
            elif to_unit == "Centimeters":
                return value * 30.48
            elif to_unit == "Meters":
                return value * 0.3048
            elif to_unit == "Kilometers":
                return value * 0.0003048
            elif to_unit == "Inches":
                return value * 12.0
            elif to_unit == "Yards":
                return value / 3.0
            elif to_unit == "Miles":
                return value / 5280.0
            elif to_unit == "Nautical Miles":
                return value / 6076.12
        elif from_unit == "Inches":
            if to_unit == "Millimeters":
                return value * 25.4
            elif to_unit == "Centimeters":
                return value * 2.54
            elif to_unit == "Meters":
                return value / 39.37007874
            elif to_unit == "Kilometers":
                return value / 39370.07874
            elif to_unit == "Feet":
                return value / 12.0
            elif to_unit == "Yards":
                return value / 36.0
            elif to_unit == "Miles":
                return value / 63360.0
            elif to_unit == "Nautical Miles":
                return value / 72913.4
        elif from_unit == "Meters":
            if to_unit == "Millimeters":
                return value * 1000.0
            elif to_unit == "Centimeters":
                return value * 100.0
            elif to_unit == "Kilometers":
                return value / 1000.0
            elif to_unit == "Inches":
                return value * 39.37007874
            elif to_unit == "Feet":
                return value / 0.3048
            elif to_unit == "Yards":
                return value / 0.9144
            elif to_unit == "Miles":
                return value / 1609.344
            elif to_unit == "Nautical Miles":
                return value / 1852.0
        elif from_unit == "Kilometers":
            if to_unit == "Millimeters":
                return value * 1000000.0
            elif to_unit == "Centimeters":
                return value * 100000.0
            elif to_unit == "Meters":
                return value * 1000.0
            elif to_unit == "Inches":
                return value * 39370.07874
            elif to_unit == "Feet":
                return value / 0.0003048
            elif to_unit == "Yards":
                return value / 0.0009144
            elif to_unit == "Miles":
                return value / 1.609344
            elif to_unit == "Nautical Miles":
                return value / 1.85200
        elif from_unit == "Miles":
            if to_unit == "Millimeters":
                return value * 1609344.0
            elif to_unit == "Centimeters":
                return value * 160934.4
            elif to_unit == "Meters":
                return value * 1609.344
            elif to_unit == "Kilometers":
                return value * 1.609344
            elif to_unit == "Inches":
                return value * 63360.0
            elif to_unit == "Feet":
                return value * 5280.0
            elif to_unit == "Yards":
                return value * 1760.0
            elif to_unit == "Nautical Miles":
                return value / 1.15078
        elif from_unit == "Millimeters":
            if to_unit == "Centimeters":
                return value / 10.0
            elif to_unit == "Meters":
                return value / 1000.0
            elif to_unit == "Kilometers":
                return value / 1000000.0
            elif to_unit == "Inches":
                return value / 25.4
            elif to_unit == "Feet":
                return value / 304.8
            elif to_unit == "Yards":
                return value / 914.4
            elif to_unit == "Miles":
                return value / 1609344.0
            elif to_unit == "Nautical Miles":
                return value / 1852000.0
        elif from_unit == "Nautical Miles":
            if to_unit == "Millimeters":
                return value * 1852000.0
            elif to_unit == "Centimeters":
                return value * 185200.0
            elif to_unit == "Meters":
                return value * 1852.0
            elif to_unit == "Kilometers":
                return value * 1.85200
            elif to_unit == "Inches":
                return value * 72913.4
            elif to_unit == "Feet":
                return value * 6076.12
            elif to_unit == "Yards":
                return value * 2025.37
            elif to_unit == "Miles":
                return value * 1.15078
        elif from_unit == "Yards":
            if to_unit == "Millimeters":
                return value * 914.4
            elif to_unit == "Centimeters":
                return value * 91.44
            elif to_unit == "Meters":
                return value * 0.9144
            elif to_unit == "Kilometers":
                return value * 0.0009144
            elif to_unit == "Inches":
                return value * 36.0
            elif to_unit == "Feet":
                return value * 3.0
            elif to_unit == "Miles":
                return value / 1760.0
            elif to_unit == "Nautical Miles":
                return value / 2025.37
        
        raise ValueError("Invalid units or conversion not supported")
