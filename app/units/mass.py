"""
Mass Conversion Module

This module provides functionality to convert mass values between various units,
such as Grams, Pounds, and Stones.

Classes:
--------
MassConverter : Provides a static method for converting mass values between different units.

Variables:
----------
mass_units : list
    A list of supported mass units for conversion.
-------------------------------------------------------------------------------
"""

mass_units = ["Grams", "Milligrams", "Kilograms", "Tonnes", "Ounces", "Pounds", "Stones", "Carats"]

class MassConverter:
    """
    A class used to convert mass measurements between different units.

    Methods:
    --------
    convert(value, from_unit, to_unit)
        Converts a mass value from one unit to another, if the conversion is supported.
    """
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Converts a mass value from one unit to another.

        Supported units include:
        - Grams
        - Milligrams
        - Kilograms
        - Tonnes
        - Ounces
        - Pounds
        - Stones
        - Carats

        Parameters:
        -----------
        value : float
            The numerical value of the mass to be converted.
        from_unit : str
            The unit of the input mass value. Must be one of the supported units.
        to_unit : str
            The unit to convert the mass value into. Must be one of the supported units.

        Returns:
        --------
        float
            The converted mass value in the target unit.

        Raises:
        -------
        ValueError
            If the provided units are invalid or if the conversion is unsupported.

        Examples:
        ---------
        >>> MassConverter.convert(1000, 'Grams', 'Kilograms')
        1.0
        >>> MassConverter.convert(1, 'Pounds', 'Ounces')
        16.0
        """
        
        if from_unit == to_unit:
            return value
        
        elif from_unit == "Grams":
            if to_unit == "Milligrams":
                return value * 1000.0
            elif to_unit == "Kilograms":
                return value / 1000.0
            elif to_unit == "Tonnes":
                return value * 1e-6
            elif to_unit == "Ounces":
                return value / 28.3495231
            elif to_unit == "Pounds":
                return value / 453.59237
            elif to_unit == "Stones":
                return value / 6350.29318
            elif to_unit == "Carats":
                return value * 5.0
            
        elif from_unit == "Milligrams":
            if to_unit == "Grams":
                return value / 1000.0
            elif to_unit == "Kilograms":
                return value / 1e+6
            elif to_unit == "Tonnes":
                return value / 1e+9
            elif to_unit == "Ounces":
                return value / 28349.5231
            elif to_unit == "Pounds":
                return value / 453592.37
            elif to_unit == "Stones":
                return value / 6350293.18
            elif to_unit == "Carats":
                return value / 200.0
            
        elif from_unit == "Kilograms":
            if to_unit == "Milligrams":
                return value * 1e+6
            elif to_unit == "Grams":
                return value * 1000.0
            elif to_unit == "Tonnes":
                return value * 0.001
            elif to_unit == "Ounces":
                return value * 35.274
            elif to_unit == "Pounds":
                return value * 2.20462
            elif to_unit == "Stones":
                return value / 6.35029
            elif to_unit == "Carats":
                return value * 5000.0
            
        elif from_unit == "Tonnes":
            if to_unit == "Milligrams":
                return value * 1e+9
            elif to_unit == "Grams":
                return value * 1e+6
            elif to_unit == "Kilograms":
                return value * 1000.0
            elif to_unit == "Ounces":
                return value / 0.0000283495231
            elif to_unit == "Pounds":
                return value * 2204.62
            elif to_unit == "Stones":
                return value * 157.473
            elif to_unit == "Carats":
                return value * 5e+6
            
        elif from_unit == "Ounces":
            if to_unit == "Milligrams":
                return value * 28349.5231
            elif to_unit == "Grams":
                return value * 28.3495231
            elif to_unit == "Kilograms":
                return value / 35.274
            elif to_unit == "Tonnes":
                return value * 0.0000283495231
            elif to_unit == "Pounds":
                return value * 0.0625
            elif to_unit == "Stones":
                return value / 224.0
            elif to_unit == "Carats":
                return value / 0.00705479
            
        elif from_unit == "Pounds":
            if to_unit == "Milligrams":
                return value * 453592.37
            elif to_unit == "Grams":
                return value * 453.59237
            elif to_unit == "Kilograms":
                return value / 2.20462
            elif to_unit == "Tonnes":
                return value / 2204.62
            elif to_unit == "Ounces":
                return value * 16.0
            elif to_unit == "Stones":
                return value / 14.0
            elif to_unit == "Carats":
                return value / 0.000440925
            
        elif from_unit == "Stones":
            if to_unit == "Milligrams":
                return value * 6350293.18
            elif to_unit == "Grams":
                return value * 6350.29318
            elif to_unit == "Kilograms":
                return value * 6.35029
            elif to_unit == "Tonnes":
                return value / 157.473
            elif to_unit == "Ounces":
                return value * 224.0
            elif to_unit == "Pounds":
                return value * 14.0
            elif to_unit == "Carats":
                return value / 3.1495e-5
            
        elif from_unit == "Carats":
            if to_unit == "Milligrams":
                return value * 200.0
            elif to_unit == "Grams":
                return value / 5.0
            elif to_unit == "Kilograms":
                return value / 5000.0
            elif to_unit == "Tonnes":
                return value / 5e+6
            elif to_unit == "Ounces":
                return value * 0.00705479
            elif to_unit == "Pounds":
                return value * 0.000440925
            elif to_unit == "Stones":
                return value * 3.1495e-5
            
        raise ValueError("Invalid units or conversion not supported")
            
        
            
