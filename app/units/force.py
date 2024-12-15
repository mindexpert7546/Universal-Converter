"""
Force Conversion Module

This module provides functionality to convert force values between various units,
such as Newtons, Dynes, and Poundals.

Classes:
--------
ForceConverter : Provides a static method for converting force values between different units.

Variables:
----------
force_units : list
    A list of supported force units for conversion.
-------------------------------------------------------------------------------
"""

force_units = ["Newtons", "Dynes", "Poundals", "Kilogramforce"]

class ForceConverter:
    """
   A class used to convert force measurements between different units.

   Methods:
   --------
   convert(value, from_unit, to_unit)
       Converts a force value from one unit to another, if the conversion is supported.
   """
   
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Converts a force value from one unit to another.

        Supported units include:
        - Newtons
        - Dynes
        - Poundals
        - Kilogramforce

        Parameters:
        -----------
        value : float
            The numerical value of the force to be converted.
        from_unit : str
            The unit of the input force value. Must be one of the supported units.
        to_unit : str
            The unit to convert the force value into. Must be one of the supported units.

        Returns:
        --------
        float
            The converted force value in the target unit.

        Raises:
        -------
        ValueError
            If the provided units are invalid or if the conversion is unsupported.

        Examples:
        ---------
        >>> ForceConverter.convert(1, 'Newtons', 'Dynes')
        100000.0
        >>> ForceConverter.convert(1, 'Kilogramforce', 'Newtons')
        9.80665
        """
        
        if from_unit == to_unit:
            return value
        
        elif from_unit == "Newtons":
            if to_unit=="Dynes":
                return value * 100000.0
            elif to_unit=="Poundals":
                return value * 7.23301
            elif to_unit=="Kilogramforce":
                return value / 9.80665
            
        elif from_unit == "Dynes":
            if to_unit=="Newtons":
                return value / 100000.0
            elif to_unit=="Poundals":
                return value / 13825.4954376
            elif to_unit=="Kilogramforce":
                return value / 980665.0
            
        elif from_unit == "Poundals":
            if to_unit=="Newtons":
                return value / 7.23301
            elif to_unit=="Dynes":
                return value * 13825.4954376
            elif to_unit=="Kilogramforce":
                return value / 70.93163528397
            
        elif from_unit == "Kilogramforce":
            if to_unit=="Newtons":
                return value * 9.80665
            elif to_unit=="Dynes":
                return value * 980665.0
            elif to_unit=="Poundals":
                return value * 70.93163528397
            
        raise ValueError("Invalid units or conversion not supported")
        

