"""
Angle Conversion Module

This module provides functionality to convert angles between various units,
such as Degrees, Radians, and Gradians.

Classes:
--------
AngleConverter : Provides static methods for converting angle values
                 between different units.

Variables:
----------
angle_units : list
    A list of supported angle units for conversion.
-------------------------------------------------------------------------------
"""

from math import pi

angle_units = ["Degrees", "Radians", "Milliradians", "Gradians", "Seconds of Arc", "Minutes of Arc"]

class AngleConverter:
    """
    A class used to convert angle measurements between different units.

    Methods:
    --------
    convert(value, from_unit, to_unit)
        Converts an angle from one unit to another, if the conversion is supported.
    """
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Converts an angle from one unit to another.

        Supported units include:
        - Degrees
        - Radians
        - Milliradians
        - Gradians
        - Seconds of Arc
        - Minutes of Arc

        Parameters:
        -----------
        value : float
            The numerical value of the angle to be converted.
        from_unit : str
            The unit of the input angle. Must be one of the supported units.
        to_unit : str
            The unit to convert the angle into. Must be one of the supported units.

        Returns:
        --------
        float
            The converted angle in the target unit.

        Raises:
        -------
        ValueError
            If the provided units are invalid or if the conversion is unsupported.

        Examples:
        ---------
        >>> AngleConverter.convert(180, 'Degrees', 'Radians')
        3.141592653589793
        >>> AngleConverter.convert(1, 'Radians', 'Degrees')
        57.29577951308232
        """
        
        if from_unit == to_unit:
            return value
        
        elif from_unit == "Degrees":
            if to_unit == "Radians":
                return value * (pi / 180.0)
            elif to_unit == "Gradians":
                return value * (200.0 / 180.0)
            elif to_unit == "Milliradians":
                return value * ((1000.0 * pi) / 180.0)
            elif to_unit == "Minutes of Arc":
                return value * 60.0
            elif to_unit == "Seconds of Arc":
                return value * 3600.0
            
        elif from_unit == "Radians":
            if to_unit == "Degrees":
                return value * (180.0 / pi)
            elif to_unit == "Gradians":
                return value * (200.0 / pi)
            elif to_unit == "Milliradians":
                return value * (1000.0)
            elif to_unit == "Minutes of Arc":
                return value * ((60.0 * 180.0) / pi)
            elif to_unit == "Seconds of Arc":
                return value * ((3600.0 * 180.0) / pi)
            
        elif from_unit == "Gradians":
            if to_unit == "Degrees":
                return value * (180.0 / 200.0)
            elif to_unit == "Radians":
                return value * (pi / 200.0)
            elif to_unit == "Milliradians":
                return value * ((1000.0 * pi) / 200.0)
            elif to_unit == "Minutes of Arc":
                return value * (60.0 / 54.0)
            elif to_unit == "Seconds of Arc":
                return value * (3600.0 / 3240.0)
            
        elif from_unit == "Milliradians":
            if to_unit == "Degrees":
                return value * ((180.0 * 1000.0 * pi))
            elif to_unit == "Radians":
                return value * (1000.0)
            elif to_unit == "Gradians":
                return value * ((200.0 * 1000.0 * pi))
            elif to_unit == "Minutes of Arc":
                return value * ((60.0 * 180.0 * 1000.0 * pi))
            elif to_unit == "Seconds of Arc":
                return value * ((3600.0 * 180.0 * 1000.0 * pi))
            
        elif from_unit == "Minutes of Arc":
            if to_unit == "Degrees":
                return value / 60.0
            elif to_unit == "Radians":
                return value * (pi / (60.0 * 180.0))
            elif to_unit == "Gradians":
                return value * 54.0
            elif to_unit == "Milliradians":
                return value * ((1000.0 * pi) / (60.0 * 180.0))
            elif to_unit == "Seconds of Arc":
                return value * 60.0
            
        elif from_unit == "Seconds of Arc":
            if to_unit == "Degrees":
                return value / 3600.0
            elif to_unit == "Radians":
                return value * (pi / (180.0 * 3600.0))
            elif to_unit == "Gradians":
                return value / 3240.0
            elif to_unit == "Milliradians":
                return value * ((1000.0 * pi) / (180.0 * 3600.0))
            elif to_unit == "Minutes of Arc":
                return value / 60.0

        raise ValueError("Invalid units or conversion not supported")


