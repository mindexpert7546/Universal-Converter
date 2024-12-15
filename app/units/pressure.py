"""
Pressure Conversion Module

This module provides functionality to convert pressure values between various units,
such as Atmospheres, Pascals, and Psi.

Classes:
--------
PressureConverter : Provides a static method for converting pressure values between different units.

Variables:
----------
pressure_units : list
    A list of supported pressure units for conversion.
-------------------------------------------------------------------------------
"""

pressure_units = ["Atmospheres", "Bars", "Pascals", "Psi", "Torrs"]

class PressureConverter:
    """
    A class used to convert pressure measurements between different units.

    Methods:
    --------
    convert(value, from_unit, to_unit)
        Converts a pressure value from one unit to another, if the conversion is supported.
    """
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Converts a pressure value from one unit to another.

        Supported units include:
        - Atmospheres
        - Bars
        - Pascals
        - Psi
        - Torrs

        Parameters:
        -----------
        value : float
            The numerical value of the pressure to be converted.
        from_unit : str
            The unit of the input pressure value. Must be one of the supported units.
        to_unit : str
            The unit to convert the pressure value into. Must be one of the supported units.

        Returns:
        --------
        float
            The converted pressure value in the target unit.

        Raises:
        -------
        ValueError
            If the provided units are invalid or if the conversion is unsupported.

        Examples:
        ---------
        >>> PressureConverter.convert(1, 'Atmospheres', 'Pascals')
        101325.0
        >>> PressureConverter.convert(1, 'Psi', 'Bars')
        0.0689476
        """
        
        if from_unit == to_unit:
            return value
        
        elif from_unit == "Atmospheres":
            if to_unit == "Bars":
                return value * 1.01325
            elif to_unit == "Pascals":
                return value * 101325.0
            elif to_unit == "Psi":
                return value * 14.69596432068
            elif to_unit == "Torrs":
                return value * 760.0

        elif from_unit == "Bars":
            if to_unit == "Atmospheres":
                return value / 1.01325
            elif to_unit == "Pascals":
                return value / 0.00001
            elif to_unit == "Psi":
                return value * 14.50378911491
            elif to_unit == "Torrs":
                return value * 750.0616827042

        elif from_unit == "Pascals":
            if to_unit == "Atmospheres":
                return value / 101325.0
            elif to_unit == "Bars":
                return value * 0.00001
            elif to_unit == "Psi":
                return value * 0.0001450378911491
            elif to_unit == "Torrs":
                return value * 0.007500616827042

        elif from_unit == "Psi":
            if to_unit == "Atmospheres":
                return value / 14.69596432068
            elif to_unit == "Bars":
                return value / 14.50378911491
            elif to_unit == "Pascals":
                return value / 0.0001450378911491
            elif to_unit == "Torrs":
                return value / 0.01933679515879

        elif from_unit == "Torrs":
            if to_unit == "Atmospheres":
                return value / 760.0
            elif to_unit == "Bars":
                return value / 750.0616827042
            elif to_unit == "Pascals":
                return value / 0.007500616827042
            elif to_unit == "Psi":
                return value * 0.01933679515879
        
        raise ValueError("Invalid units or conversion not supported")    