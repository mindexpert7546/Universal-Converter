"""
Frequency Conversion Module

This module provides functionality to convert frequency values between different units,
such as Hertz, Kilohertz, and Megahertz.

Classes:
--------
FrequencyConverter : Provides a static method for converting frequency values between different units.

Variables:
----------
frequency_units : list
    A list of supported frequency units for conversion.
    
-------------------------------------------------------------------------------
"""

frequency_units = ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"]

class FrequencyConverter:
    """
    A class used to convert frequency measurements between different units.

    Methods:
    --------
    convert(value, from_unit, to_unit)
        Converts a frequency value from one unit to another, if the conversion is supported.
    """
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Converts a frequency value from one unit to another.

        Supported units include:
        - Hertz
        - Kilohertz
        - Megahertz
        - Gigahertz

        Parameters:
        -----------
        value : float
            The numerical value of the frequency to be converted.
        from_unit : str
            The unit of the input frequency value. Must be one of the supported units.
        to_unit : str
            The unit to convert the frequency value into. Must be one of the supported units.

        Returns:
        --------
        float
            The converted frequency value in the target unit.

        Raises:
        -------
        ValueError
            If the provided units are invalid or if the conversion is unsupported.

        Examples:
        ---------
        >>> FrequencyConverter.convert(1000, 'Hertz', 'Kilohertz')
        1.0
        >>> FrequencyConverter.convert(1, 'Gigahertz', 'Megahertz')
        1000.0
        """
        
        if from_unit == to_unit:
            return value
        
        elif from_unit == "Hertz":
            if to_unit == "Kilohertz":
                return value / 1000.0
            elif to_unit == "Megahertz":
                return value / 1e+6
            elif to_unit == "Gigahertz":
                return value / 1e+9

        elif from_unit == "Kilohertz":
            if to_unit == "Hertz":
                return value * 1000.0
            elif to_unit == "Megahertz":
                return value / 1000.0
            elif to_unit == "Gigahertz":
                return value / 1e+6

        elif from_unit == "Megahertz":
            if to_unit == "Hertz":
                return value * 1e+6
            elif to_unit == "Kilohertz":
                return value * 1000.0
            elif to_unit == "Gigahertz":
                return value / 1000.0

        elif from_unit == "Gigahertz":
            if to_unit == "Hertz":
                return value * 1e+9
            elif to_unit == "Kilohertz":
                return value * 1e+6
            elif to_unit == "Megahertz":
                return value * 1000.0

        raise ValueError("Invalid units or conversion not supported")