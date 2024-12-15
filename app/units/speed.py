"""
Speed Conversion Module

This module provides functionality to convert speed values between various units,
such as Kilometres per Hour, Miles per Hour, and Knots.

Classes:
--------
SpeedConverter : Provides a static method for converting speed values between different units.

Variables:
----------
speed_units : list
    A list of supported speed units for conversion.
    
-------------------------------------------------------------------------------
"""


speed_units = ["Feet per Second", "Metres per Second", "Kilometres per Hour", "Miles per Hour", "Knots"]

class SpeedConverter:
    """
    A class used to convert speed measurements between different units.

    Methods:
    --------
    convert(value, from_unit, to_unit)
        Converts a speed value from one unit to another, if the conversion is supported.
    """
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Converts a speed value from one unit to another.

        Supported units include:
        - Feet per Second
        - Metres per Second
        - Kilometres per Hour
        - Miles per Hour
        - Knots

        Parameters:
        -----------
        value : float
            The numerical value of the speed to be converted.
        from_unit : str
            The unit of the input speed value. Must be one of the supported units.
        to_unit : str
            The unit to convert the speed value into. Must be one of the supported units.

        Returns:
        --------
        float
            The converted speed value in the target unit.

        Raises:
        -------
        ValueError
            If the provided units are invalid or if the conversion is unsupported.

        Examples:
        ---------
        >>> SpeedConverter.convert(1, 'Kilometres per Hour', 'Miles per Hour')
        0.621371
        >>> SpeedConverter.convert(10, 'Metres per Second', 'Knots')
        19.4384
        """
        
        if from_unit == to_unit:
            return value
        
        elif from_unit == "Feet per Second":
            if to_unit == "Miles per Hour":
                return value / 1.46667
            elif to_unit == "Kilometres per Hour":
                return value * 1.09728
            elif to_unit == "Metres per Second":
                return value / 3.28084
            elif to_unit == "Knots":
                return value / 1.68781
            
        elif from_unit == "Kilometres per Hour":
            if to_unit == "Miles per Hour":
                return value / 1.60934
            elif to_unit == "Feet per Second":
                return value / 1.09728
            elif to_unit == "Metres per Second":
                return value / 3.6
            elif to_unit == "Knots":
                return value / 1.852
            
        elif from_unit == "Knots":
            if to_unit == "Miles per Hour":
                return value * 1.15078
            elif to_unit == "Kilometres per Hour":
                return value * 1.852
            elif to_unit == "Feet per Second":
                return value * 1.68781
            elif to_unit == "Metres per Second":
                return value / 1.94384
            
        elif from_unit == "Metres per Second":
            if to_unit == "Miles per Hour":
                return value * 2.23694
            elif to_unit == "Kilometres per Hour":
                return value * 3.6
            elif to_unit == "Feet per Second":
                return value * 3.28084
            elif to_unit == "Knots":
                return value * 1.94384
            
        elif from_unit == "Miles per Hour":
            if to_unit == "Kilometres per Hour":
                return value * 1.60934
            elif to_unit == "Feet per Second":
                return value * 1.46667
            elif to_unit == "Metres per Second":
                return value / 2.23694
            elif to_unit == "Knots":
                return value / 1.15078

        raise ValueError("Invalid units or conversion not supported")
