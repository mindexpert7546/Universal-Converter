"""
Time Conversion Module

This module provides functionality to convert time values between various units,
such as Seconds, Minutes, and Hours.

Classes:
--------
TimeConverter : Provides a static method for converting time values between different units.

Variables:
----------
time_units : list
    A list of supported time units for conversion.
-------------------------------------------------------------------------------
"""

time_units = ["Nanoseconds", "Microseconds", "Milliseconds", "Seconds","Minutes", 
              "Hours", "Days", "Weeks","Months", "Years", "Decades", "Centuries"]

class TimeConverter:
    """
    A class used to convert time measurements between different units.

    Methods:
    --------
    convert(value, from_unit, to_unit)
        Converts a time value from one unit to another, if the conversion is supported.
    """
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Converts a time value from one unit to another.

        Supported units include:
        - Nanoseconds
        - Microseconds
        - Milliseconds
        - Seconds
        - Minutes
        - Hours
        - Days
        - Weeks
        - Months
        - Years
        - Decades
        - Centuries

        Parameters:
        -----------
        value : float
            The numerical value of the time to be converted.
        from_unit : str
            The unit of the input time value. Must be one of the supported units.
        to_unit : str
            The unit to convert the time value into. Must be one of the supported units.

        Returns:
        --------
        float
            The converted time value in the target unit.

        Raises:
        -------
        ValueError
            If the provided units are invalid or if the conversion is unsupported.

        Examples:
        ---------
        >>> TimeConverter.convert(1, 'Hours', 'Minutes')
        60.0
        >>> TimeConverter.convert(1, 'Days', 'Hours')
        24.0
        """
        
        if from_unit == to_unit:
            return value
        
        elif from_unit == "Centuries":
            if to_unit == "Nanoseconds":
                return value * 3.154e+18
            elif to_unit == "Microseconds":
                return value * 3.154e+15
            elif to_unit == "Milliseconds":
                return value * 3.154e+12
            elif to_unit == "Seconds":
                return value * 3.154e+9
            elif to_unit == "Minutes":
                return value * 5.256e+7
            elif to_unit == "Hours":
                return value * 876000.0
            elif to_unit == "Days":
                return value * 36500.0
            elif to_unit == "Weeks":
                return value * 5214.29
            elif to_unit == "Months":
                return value * 1200.0
            elif to_unit == "Years":
                return value * 100.0
            elif to_unit == "Decades":
                return value * 10.0

        elif from_unit == "Nanoseconds":
            if to_unit == "Centuries":
                return value / 3.154e+18
            elif to_unit == "Microseconds":
                return value / 1000.0
            elif to_unit == "Milliseconds":
                return value / 1e+6
            elif to_unit == "Seconds":
                return value / 1e+9
            elif to_unit == "Minutes":
                return value / 6e+10
            elif to_unit == "Hours":
                return value / 3.6e+12
            elif to_unit == "Days":
                return value / 8.64e+13
            elif to_unit == "Weeks":
                return value / 6.048e+14
            elif to_unit == "Months":
                return value / 2629746000000000.0
            elif to_unit == "Years":
                return value / 3.154e+16
            elif to_unit == "Decades":
                return value / 3.154e+17

        elif from_unit == "Days":
            if to_unit == "Nanoseconds":
                return value * 8.64e+13
            elif to_unit == "Microseconds":
                return value * 8.64e+10
            elif to_unit == "Milliseconds":
                return value * 8.64e+7
            elif to_unit == "Seconds":
                return value * 86400.0
            elif to_unit == "Minutes":
                return value * 1440.0
            elif to_unit == "Hours":
                return value * 24.0
            elif to_unit == "Weeks":
                return value / 7.0
            elif to_unit == "Months":
                return value / 30.4167
            elif to_unit == "Years":
                return value / 365.0
            elif to_unit == "Decades":
                return value / 3650.0
            elif to_unit == "Centuries":
                return value / 36500.0

        elif from_unit == "Days":
            if to_unit == "Nanoseconds":
                return value * 8.64e+13
            elif to_unit == "Microseconds":
                return value * 8.64e+10
            elif to_unit == "Milliseconds":
                return value * 8.64e+7
            elif to_unit == "Seconds":
                return value * 86400.0
            elif to_unit == "Minutes":
                return value * 1440.0
            elif to_unit == "Hours":
                return value * 24.0
            elif to_unit == "Weeks":
                return value / 7.0
            elif to_unit == "Months":
                return value / 30.4167
            elif to_unit == "Years":
                return value / 365.0
            elif to_unit == "Decades":
                return value / 3650.0
            elif to_unit == "Centuries":
                return value / 36500.0

        elif from_unit == "Decades":
            if to_unit == "Nanoseconds":
                return value * 3.154e+17
            elif to_unit == "Microseconds":
                return value * 3.154e+14
            elif to_unit == "Milliseconds":
                return value * 3.154e+11
            elif to_unit == "Seconds":
                return value * 3.154e+8
            elif to_unit == "Minutes":
                return value * 5.256e+6
            elif to_unit == "Hours":
                return value * 87600.0
            elif to_unit == "Days":
                return value * 3650.0
            elif to_unit == "Weeks":
                return value * 521.429
            elif to_unit == "Months":
                return value * 120.0
            elif to_unit == "Years":
                return value * 10.0
            elif to_unit == "Centuries":
                return value / 10.0

        elif from_unit == "Years":
            if to_unit == "Nanoseconds":
                return value * 3.154e+16
            elif to_unit == "Microseconds":
                return value * 3.154e+13
            elif to_unit == "Milliseconds":
                return value * 31556952000.0
            elif to_unit == "Seconds":
                return value * 3.1536e+7
            elif to_unit == "Minutes":
                return value * 525600.0
            elif to_unit == "Hours":
                return value * 8760.0
            elif to_unit == "Days":
                return value * 365.0
            elif to_unit == "Weeks":
                return value * 52.143
            elif to_unit == "Months":
                return value * 12.0
            elif to_unit == "Decades":
                return value / 10.0
            elif to_unit == "Centuries":
                return value / 100.0

        elif from_unit == "Months":
            if to_unit == "Nanoseconds":
                return value * 2629746000000000.0
            elif to_unit == "Microseconds":
                return value * 2629746000000.0
            elif to_unit == "Milliseconds":
                return value * 2629746000.0
            elif to_unit == "Seconds":
                return value * 2.628e+6
            elif to_unit == "Minutes":
                return value * 43800.0
            elif to_unit == "Hours":
                return value * 730.001
            elif to_unit == "Days":
                return value * 30.4167
            elif to_unit == "Weeks":
                return value * 4.34524
            elif to_unit == "Years":
                return value / 12.0
            elif to_unit == "Decades":
                return value / 120.0
            elif to_unit == "Centuries":
                return value / 1200.0

        elif from_unit == "Weeks":
            if to_unit == "Nanoseconds":
                return value * 6.048e+14
            elif to_unit == "Microseconds":
                return value * 6.048e+11
            elif to_unit == "Milliseconds":
                return value * 6.048e+8
            elif to_unit == "Seconds":
                return value * 604800.0
            elif to_unit == "Minutes":
                return value * 10080.0
            elif to_unit == "Hours":
                return value * 168.0
            elif to_unit == "Days":
                return value * 7.0
            elif to_unit == "Months":
                return value / 4.34524
            elif to_unit == "Years":
                return value / 52.143
            elif to_unit == "Decades":
                return value / 521.429
            elif to_unit == "Centuries":
                return value / 5214.29

        elif from_unit == "Hours":
            if to_unit == "Nanoseconds":
                return value * 3.6e+12
            elif to_unit == "Microseconds":
                return value * 3.6e+9
            elif to_unit == "Milliseconds":
                return value * 3.6e+6
            elif to_unit == "Seconds":
                return value * 3600.0
            elif to_unit == "Minutes":
                return value * 60.0
            elif to_unit == "Days":
                return value / 24.0
            elif to_unit == "Weeks":
                return value / 168.0
            elif to_unit == "Months":
                return value / 730.001
            elif to_unit == "Years":
                return value / 8760.0
            elif to_unit == "Decades":
                return value / 87600.0
            elif to_unit == "Centuries":
                return value / 876000.0

        elif from_unit == "Minutes":
            if to_unit == "Nanoseconds":
                return value * 6e+10
            elif to_unit == "Microseconds":
                return value * 6e+7
            elif to_unit == "Milliseconds":
                return value * 60000.0
            elif to_unit == "Seconds":
                return value * 60.0
            elif to_unit == "Hours":
                return value / 60.0
            elif to_unit == "Days":
                return value / 1440.0
            elif to_unit == "Weeks":
                return value / 10080.0
            elif to_unit == "Months":
                return value / 43800.0
            elif to_unit == "Years":
                return value / 525600.0
            elif to_unit == "Decades":
                return value / 5.256e+6
            elif to_unit == "Centuries":
                return value / 5.256e+7

        elif from_unit == "Seconds":
            if to_unit == "Nanoseconds":
                return value * 1e+9
            elif to_unit == "Microseconds":
                return value * 1e+6
            elif to_unit == "Milliseconds":
                return value * 1000.0
            elif to_unit == "Minutes":
                return value / 60.0
            elif to_unit == "Hours":
                return value / 3600.0
            elif to_unit == "Days":
                return value / 86400.0
            elif to_unit == "Weeks":
                return value / 604800.0
            elif to_unit == "Months":
                return value / 2.628e+6
            elif to_unit == "Years":
                return value / 3.1536e+7
            elif to_unit == "Decades":
                return value / 3.154e+8
            elif to_unit == "Centuries":
                return value / 3.154e+9

        elif from_unit == "Milliseconds":
            if to_unit == "Nanoseconds":
                return value * 1e+6
            elif to_unit == "Microseconds":
                return value * 1000.0
            elif to_unit == "Seconds":
                return value / 1000.0
            elif to_unit == "Minutes":
                return value / 60000.0
            elif to_unit == "Hours":
                return value / 3.6e+6
            elif to_unit == "Days":
                return value / 8.64e+7
            elif to_unit == "Weeks":
                return value / 6.048e+8
            elif to_unit == "Months":
                return value / 2629746000.0
            elif to_unit == "Years":
                return value / 31556952000.0
            elif to_unit == "Decades":
                return value / 3.154e+11
            elif to_unit == "Centuries":
                return value / 3.154e+12

        elif from_unit == "Microseconds":
            if to_unit == "Nanoseconds":
                return value * 1000.0
            elif to_unit == "Milliseconds":
                return value / 1000.0
            elif to_unit == "Seconds":
                return value / 1e+6
            elif to_unit == "Minutes":
                return value / 6e+7
            elif to_unit == "Hours":
                return value / 3.6e+9
            elif to_unit == "Days":
                return value / 8.64e+10
            elif to_unit == "Weeks":
                return value / 6.048e+11
            elif to_unit == "Months":
                return value / 2629746000000.0
            elif to_unit == "Years":
                return value / 3.154e+13
            elif to_unit == "Decades":
                return value / 3.154e+14
            elif to_unit == "Centuries":
                return value / 3.154e+15

        raise ValueError("Invalid units or conversion not supported")