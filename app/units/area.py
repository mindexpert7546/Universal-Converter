"""
Area Conversion Module

This module provides functionality to convert areas between various units,
such as Square Meters, Acres, and Square Miles.

Classes:
--------
AreaConverter : Provides a static method for converting area values
                between different units.

Variables:
----------
area_units : list
    A list of supported area units for conversion.
-------------------------------------------------------------------------------
"""

area_units = ["Square Metres", "Square Kilometers", "Square Miles", 
              "Square Inches","Square Feet", "Square Yards", "Hectares", "Acres"]

class AreaConverter:
    """
    A class used to convert area measurements between different units.

    Methods:
    --------
    convert(value, from_unit, to_unit)
        Converts an area from one unit to another, if the conversion is supported.
    """
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Converts an area from one unit to another.

        Supported units include:
        - Square Metres
        - Square Kilometers
        - Square Miles
        - Square Inches
        - Square Feet
        - Square Yards
        - Hectares
        - Acres

        Parameters:
        -----------
        value : float
            The numerical value of the area to be converted.
        from_unit : str
            The unit of the input area. Must be one of the supported units.
        to_unit : str
            The unit to convert the area into. Must be one of the supported units.

        Returns:
        --------
        float
            The converted area in the target unit.

        Raises:
        -------
        ValueError
            If the provided units are invalid or if the conversion is unsupported.

        Examples:
        ---------
        >>> AreaConverter.convert(1000, 'Square Metres', 'Hectares')
        0.1
        >>> AreaConverter.convert(1, 'Acres', 'Square Feet')
        43560.0
        """
        
        if from_unit == to_unit:
            return value
        
        elif from_unit == "Square Metres":
            if to_unit == "Square Kilometers":
                return value / 1e+6
            elif to_unit == "Square Miles":
                return value / 2589988.10
            elif to_unit == "Square Yards":
                return value * 1.1959900463
            elif to_unit == "Square Feet":
                return value * 10.76391042
            elif to_unit == "Square Inches":
                return value * 1550.0
            elif to_unit == "Hectares":
                return value / 10000.0
            elif to_unit == "Acres":
                return value / 4046.86
            
        elif from_unit == "Square Kilometers":
            if to_unit == "Square Metres":
                return value * 1e+6
            elif to_unit == "Square Miles":
                return value / 2.58999
            elif to_unit == "Square Yards":
                return value * 1195990.05
            elif to_unit == "Square Feet":
                return value * 10763910.41671
            elif to_unit == "Square Inches":
                return value * 1550003100.00
            elif to_unit == "Hectares":
                return value * 100.0
            elif to_unit == "Acres":
                return value * 247.105
        
        elif from_unit == "Acres":
            if to_unit == "Square Kilometers":
                return value / 247.105
            elif to_unit == "Square Metres":
                return value * 4046.86
            elif to_unit == "Square Miles":
                return value / 640.0
            elif to_unit == "Square Yards":
                return value * 4840.0
            elif to_unit == "Square Feet":
                return value * 43560.0
            elif to_unit == "Square Inches":
                return value * 6272640.0
            elif to_unit == "Hectares":
                return value / 2.4710538146717
            
        elif from_unit == "Hectares":
            if to_unit == "Square Kilometers":
                return value / 100.0
            elif to_unit == "Square Metres":
                return value * 10000.0
            elif to_unit == "Square Miles":
                return value / 258.99881103
            elif to_unit == "Square Yards":
                return value * 11959.900463011
            elif to_unit == "Square Feet":
                return value * 107639.0
            elif to_unit == "Square Inches":
                return value * 15500031.0
            elif to_unit == "Acres":
                return value * 2.4710538146717
            
        elif from_unit == "Square Feet":
            if to_unit == "Square Kilometers":
                return value / 10763910.41671
            elif to_unit == "Square Metres":
                return value / 10.76391042
            elif to_unit == "Square Miles":
                return value / 27878400.0
            elif to_unit == "Square Yards":
                return value / 9.0
            elif to_unit == "Square Inches":
                return value * 144.0
            elif to_unit == "Hectares":
                return value / 107639.0
            elif to_unit == "Acres":
                return value / 43560.0
            
        elif from_unit == "Square Inches":
            if to_unit == "Square Kilometers":
                return value / 1550003100.00
            elif to_unit == "Square Metres":
                return value / 1550.0
            elif to_unit == "Square Miles":
                return value / 4014489600.0
            elif to_unit == "Square Yards":
                return value / 1296.0
            elif to_unit == "Square Feet":
                return value / 144.0
            elif to_unit == "Hectares":
                return value / 15500031.0
            elif to_unit == "Acres":
                return value / 6272640.0
            
        elif from_unit == "Square Miles":
            if to_unit == "Square Kilometers":
                return value * 2.58999
            elif to_unit == "Square Metres":
                return value * 2589988.10
            elif to_unit == "Square Yards":
                return value * 3097600.0
            elif to_unit == "Square Feet":
                return value * 27878400.0
            elif to_unit == "Square Inches":
                return value * 4014489600.0
            elif to_unit == "Hectares":
                return value * 258.99881103
            elif to_unit == "Acres":
                return value * 640.0
            
        elif from_unit == "Square Yards":
            if to_unit == "Square Kilometers":
                return value / 1195990.05
            elif to_unit == "Square Metres":
                return value / 1.1959900463
            elif to_unit == "Square Miles":
                return value / 3097600.0
            elif to_unit == "Square Feet":
                return value * 9.0
            elif to_unit == "Square Inches":
                return value * 1296.0
            elif to_unit == "Hectares":
                return value / 11959.900463011
            elif to_unit == "Acres":
                return value / 4840.0

        raise ValueError("Invalid units or conversion not supported")


