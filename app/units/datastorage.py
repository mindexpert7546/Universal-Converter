"""
Data Storage Conversion Module

This module provides functionality to convert data storage sizes between various
units, such as Bits, Bytes, Kilobits, and Terabytes.

Classes:
--------
DataStorageConverter : Provides a static method for converting data storage
                       values between different units.

Variables:
----------
data_units : list
    A list of supported data storage units for conversion.
-------------------------------------------------------------------------------
"""

data_units = ["Bits", "Kilobits", "Megabits", "Gigabits", "Terabits", "Kilobytes",
              "Megabytes", "Gigabytes", "Terabytes", "Kibibits", "Mebibits"]

class DataStorageConverter:
    """
    A class used to convert data storage measurements between different units.

    Methods:
    --------
    convert(value, from_unit, to_unit)
        Converts a data storage value from one unit to another, if the conversion
        is supported.
    """
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Converts a data storage value from one unit to another.

        Supported units include:
        - Bits
        - Kilobits
        - Megabits
        - Gigabits
        - Terabits
        - Kilobytes
        - Megabytes
        - Gigabytes
        - Terabytes
        - Kibibits
        - Mebibits

        Parameters:
        -----------
        value : float
            The numerical value of the data storage to be converted.
        from_unit : str
            The unit of the input data storage value. Must be one of the supported units.
        to_unit : str
            The unit to convert the data storage value into. Must be one of the supported units.

        Returns:
        --------
        float
            The converted data storage value in the target unit.

        Raises:
        -------
        ValueError
            If the provided units are invalid or if the conversion is unsupported.

        Examples:
        ---------
        >>> DataStorageConverter.convert(1024, 'Kilobits', 'Megabits')
        1.024
        >>> DataStorageConverter.convert(1, 'Gigabytes', 'Bits')
        8000000000.0
        """
        
        if from_unit == to_unit:
            return value
        
        elif from_unit == "Bits":
            if to_unit == "Kilobits":
                return value / 1000.0
            elif to_unit == "Megabits":
                return value / 1e+6
            elif to_unit == "Gigabits":
                return value / 1e+9
            elif to_unit == "Terabits":
                return value / 1e+12
            elif to_unit == "Kilobytes":
                return value / 8000.0
            elif to_unit == "Megabytes":
                return value / 8e+6
            elif to_unit == "Gigabytes":
                return value / 8e+9
            elif to_unit == "Terabytes":
                return value / 8e+12
            elif to_unit == "Kibibits":
                return value / 1024.0
            elif to_unit == "Mebibits":
                return value / 1048576.0

        elif from_unit == "Kilobits":
            if to_unit == "Bits":
                return value * 1000.0
            elif to_unit == "Megabits":
                return value / 1000.0
            elif to_unit == "Gigabits":
                return value / 1e+6
            elif to_unit == "Terabits":
                return value / 1e+9
            elif to_unit == "Kilobytes":
                return value / 8.0
            elif to_unit == "Megabytes":
                return value / 8000.0
            elif to_unit == "Gigabytes":
                return value / 8e+6
            elif to_unit == "Terabytes":
                return value / 8e+9
            elif to_unit == "Kibibits":
                return value / 1.024
            elif to_unit == "Mebibits":
                return value / 1048.58

        elif from_unit == "Megabits":
            if to_unit == "Bits":
                return value * 1e+6
            elif to_unit == "Kilobits":
                return value * 1000.0
            elif to_unit == "Gigabits":
                return value / 1000.0
            elif to_unit == "Terabits":
                return value / 1e+6
            elif to_unit == "Kilobytes":
                return value * 125.0
            elif to_unit == "Megabytes":
                return value / 8.0
            elif to_unit == "Gigabytes":
                return value / 8000.0
            elif to_unit == "Terabytes":
                return value / 8e+6
            elif to_unit == "Kibibits":
                return value * 976.563
            elif to_unit == "Mebibits":
                return value / 1.04858

        elif from_unit == "Gigabits":
            if to_unit == "Bits":
                return value * 1e+9
            elif to_unit == "Kilobits":
                return value * 1e+6
            elif to_unit == "Megabits":
                return value * 1000.0
            elif to_unit == "Terabits":
                return value / 1000.0
            elif to_unit == "Kilobytes":
                return value * 125000.0
            elif to_unit == "Megabytes":
                return value * 125.0
            elif to_unit == "Gigabytes":
                return value / 8.0
            elif to_unit == "Terabytes":
                return value / 8000.0
            elif to_unit == "Kibibits":
                return value * 976562.5
            elif to_unit == "Mebibits":
                return value * 953.67431640625

        elif from_unit == "Terabits":
            if to_unit == "Bits":
                return value * 1e+12
            elif to_unit == "Kilobits":
                return value * 1e+9
            elif to_unit == "Megabits":
                return value * 1e+6
            elif to_unit == "Gigabits":
                return value * 1000.0
            elif to_unit == "Kilobytes":
                return value * 1.25e+8
            elif to_unit == "Megabytes":
                return value * 125000.0
            elif to_unit == "Gigabytes":
                return value * 125.0
            elif to_unit == "Terabytes":
                return value / 8.0
            elif to_unit == "Kibibits":
                return value * 976562500.0
            elif to_unit == "Mebibits":
                return value * 953674.0

        elif from_unit == "Kilobytes":
            if to_unit == "Bits":
                return value * 8000.0
            elif to_unit == "Kilobits":
                return value * 8.0
            elif to_unit == "Megabits":
                return value / 125.0
            elif to_unit == "Gigabits":
                return value / 125000.0
            elif to_unit == "Terabits":
                return value / 1.25e+8
            elif to_unit == "Megabytes":
                return value / 1000.0
            elif to_unit == "Gigabytes":
                return value / 1e+6
            elif to_unit == "Terabytes":
                return value / 1e+9
            elif to_unit == "Kibibits":
                return value * 7.8125
            elif to_unit == "Mebibits":
                return value * 0.00762939

        elif from_unit == "Megabytes":
            if to_unit == "Bits":
                return value * 8e+6
            elif to_unit == "Kilobits":
                return value * 8000.0
            elif to_unit == "Megabits":
                return value * 8.0
            elif to_unit == "Gigabits":
                return value / 125.0
            elif to_unit == "Terabits":
                return value / 125000.0
            elif to_unit == "Kilobytes":
                return value * 1000.0
            elif to_unit == "Gigabytes":
                return value / 1000.0
            elif to_unit == "Terabytes":
                return value / 1e+6
            elif to_unit == "Kibibits":
                return value * 7812.5
            elif to_unit == "Mebibits":
                return value * 7.62939

        elif from_unit == "Gigabytes":
            if to_unit == "Bits":
                return value * 8e+9
            elif to_unit == "Kilobits":
                return value * 8e+6
            elif to_unit == "Megabits":
                return value * 8000.0
            elif to_unit == "Gigabits":
                return value * 8.0
            elif to_unit == "Terabits":
                return value / 125.0
            elif to_unit == "Kilobytes":
                return value * 1e+6
            elif to_unit == "Megabytes":
                return value * 1000.0
            elif to_unit == "Terabytes":
                return value / 1000.0
            elif to_unit == "Kibibits":
                return value * 7812500.0
            elif to_unit == "Mebibits":
                return value * 7629.39

        elif from_unit == "Terabytes":
            if to_unit == "Bits":
                return value * 8e+12
            elif to_unit == "Kilobits":
                return value * 8e+9
            elif to_unit == "Megabits":
                return value * 8e+6
            elif to_unit == "Gigabits":
                return value * 8000.0
            elif to_unit == "Terabits":
                return value * 8.0
            elif to_unit == "Kilobytes":
                return value * 1e+9
            elif to_unit == "Megabytes":
                return value * 1e+6
            elif to_unit == "Gigabytes":
                return value * 1000.0
            elif to_unit == "Kibibits":
                return value * 7812500000.0
            elif to_unit == "Mebibits":
                return value / 0.000000131072

        elif from_unit == "Kibibits":
            if to_unit == "Bits":
                return value * 1024.0
            elif to_unit == "Kilobits":
                return value * 1.024
            elif to_unit == "Megabits":
                return value / 976.563
            elif to_unit == "Gigabits":
                return value / 976562.5
            elif to_unit == "Terabits":
                return value / 976562500.0
            elif to_unit == "Kilobytes":
                return value / 7.8125
            elif to_unit == "Megabytes":
                return value / 7812.5
            elif to_unit == "Gigabytes":
                return value / 7812500.0
            elif to_unit == "Terabytes":
                return value / 7812500000.0
            elif to_unit == "Mebibits":
                return value / 1024.0

        elif from_unit == "Mebibits":
            if to_unit == "Bits":
                return value * 1048576.0
            elif to_unit == "Kilobits":
                return value * 1048.58
            elif to_unit == "Megabits":
                return value * 1.04858
            elif to_unit == "Gigabits":
                return value / 953.67431640625
            elif to_unit == "Terabits":
                return value / 953674.0
            elif to_unit == "Kilobytes":
                return value / 0.00762939
            elif to_unit == "Megabytes":
                return value / 7.62939
            elif to_unit == "Gigabytes":
                return value / 7629.39
            elif to_unit == "Terabytes":
                return value * 0.000000131072
            elif to_unit == "Kibibits":
                return value * 1024.0
            
        raise ValueError("Invalid units or conversion not supported")