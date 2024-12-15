"""
Volume Conversion Module

This module provides functionality to convert volume values between various units,
such as Litres, Gallons, and Cubic Inches.

Classes:
--------
VolumeConverter : Provides a static method for converting volume values between different units.

Variables:
----------
volume_units : list
    A list of supported volume units for conversion.
-------------------------------------------------------------------------------
"""

volume_units = ["Millilitres", "Litres", "Kilolitres", "Teaspoons", 
                "Tablespoons","Quarts", "Pints", "Gallons", "Fluid Ounces",
                "Cubic Metres", "Cubic Feet", "Cubic Inches", "Oil Barrels"]

class VolumeConverter:
    """
    A class used to convert volume measurements between different units.

    Methods:
    --------
    convert(value, from_unit, to_unit)
        Converts a volume value from one unit to another, if the conversion is supported.
    """
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """
        Converts a volume value from one unit to another.

        Supported units include:
        - Millilitres
        - Litres
        - Kilolitres
        - Teaspoons
        - Tablespoons
        - Quarts
        - Pints
        - Gallons
        - Fluid Ounces
        - Cubic Metres
        - Cubic Feet
        - Cubic Inches
        - Oil Barrels

        Parameters:
        -----------
        value : float
            The numerical value of the volume to be converted.
        from_unit : str
            The unit of the input volume value. Must be one of the supported units.
        to_unit : str
            The unit to convert the volume value into. Must be one of the supported units.

        Returns:
        --------
        float
            The converted volume value in the target unit.

        Raises:
        -------
        ValueError
            If the provided units are invalid or if the conversion is unsupported.

        Examples:
        ---------
        >>> VolumeConverter.convert(1, 'Litres', 'Millilitres')
        1000.0
        >>> VolumeConverter.convert(1, 'Gallons', 'Cubic Feet')
        0.133681
        """
        
        if from_unit == to_unit:
            return value
        
        elif from_unit == "Millilitres":
            if to_unit == "Litres":
                return value / 1000.0
            elif to_unit == "Kilolitres":
                return value / 1000000.0
            elif to_unit == "Teaspoons":
                return value / 5.9193904674479161344
            elif to_unit == "Tablespoons":
                return value / 17.758171402343747584
            elif to_unit == "Quarts":
                return value / 1136.52296975
            elif to_unit == "Pints":
                return value / 568.26148487499988992
            elif to_unit == "Gallons":
                return value / 4546.091879
            elif to_unit == "Fluid Ounces":
                return value / 28.413074243749994496
            elif to_unit == "Cubic Metres":
                return value / 1000000.0
            elif to_unit == "Cubic Feet":
                return value / 28316.8
            elif to_unit == "Cubic Inches":
                return value / 16.3871
            elif to_unit == "Oil Barrels":
                return value / 158987.0

        elif from_unit == "Litres":
            if to_unit == "Millilitres":
                return value * 1000.0
            elif to_unit == "Kilolitres":
                return value / 1000.0
            elif to_unit == "Teaspoons":
                return value / 0.005919390467447916134
            elif to_unit == "Tablespoons":
                return value / 0.017758171402343747584
            elif to_unit == "Quarts":
                return value / 1.13652296975
            elif to_unit == "Pints":
                return value / 0.56826148487499988992
            elif to_unit == "Gallons":
                return value / 4.546091879
            elif to_unit == "Fluid Ounces":
                return value / 0.028413074243749994496
            elif to_unit == "Cubic Metres":
                return value / 1000.0
            elif to_unit == "Cubic Feet":
                return value / 28.3168
            elif to_unit == "Cubic Inches":
                return value * 61.0237
            elif to_unit == "Oil Barrels":
                return value / 158.987

        elif from_unit == "Kilolitres":
            if to_unit == "Millilitres":
                return value * 1000000.0
            elif to_unit == "Litres":
                return value * 1000.0
            elif to_unit == "Teaspoons":
                return value / 0.000005919390467447916
            elif to_unit == "Tablespoons":
                return value / 0.000017758171402343747
            elif to_unit == "Quarts":
                return value / 0.00113652296975
            elif to_unit == "Pints":
                return value / 0.000568261484874999889
            elif to_unit == "Gallons":
                return value / 0.0045460918799
            elif to_unit == "Fluid Ounces":
                return value / 0.0000284130742437499946
            elif to_unit == "Cubic Metres":
                return value * 1.0
            elif to_unit == "Cubic Feet":
                return value * 35.3147
            elif to_unit == "Cubic Inches":
                return value * 61023.7
            elif to_unit == "Oil Barrels":
                return value * 6.28981

        elif from_unit == "Teaspoons":
            if to_unit == "Millilitres":
                return value * 5.9193904674479161344
            elif to_unit == "Litres":
                return value * 0.005919390467447916134
            elif to_unit == "Kilolitres":
                return value * 0.000005919390467447916
            elif to_unit == "Tablespoons":
                return value / 3.0
            elif to_unit == "Quarts":
                return value / 192.0
            elif to_unit == "Pints":
                return value / 96.0
            elif to_unit == "Gallons":
                return value / 768.0
            elif to_unit == "Fluid Ounces":
                return value / 4.8
            elif to_unit == "Cubic Metres":
                return value / 168936.0
            elif to_unit == "Cubic Feet":
                return value / 4783.74
            elif to_unit == "Cubic Inches":
                return value / 2.76837
            elif to_unit == "Oil Barrels":
                return value / 26858.7

        elif from_unit == "Tablespoons":
            if to_unit == "Millilitres":
                return value * 17.758171402343747584
            elif to_unit == "Litres":
                return value * 0.017758171402343747584
            elif to_unit == "Kilolitres":
                return value * 0.000017758171402343747
            elif to_unit == "Teaspoons":
                return value * 3.0
            elif to_unit == "Quarts":
                return value / 64.0
            elif to_unit == "Pints":
                return value / 32.0
            elif to_unit == "Gallons":
                return value / 256.0
            elif to_unit == "Fluid Ounces":
                return value / 1.6
            elif to_unit == "Cubic Metres":
                return value / 56312.1
            elif to_unit == "Cubic Feet":
                return value / 1594.58
            elif to_unit == "Cubic Inches":
                return value * 1.08367
            elif to_unit == "Oil Barrels":
                return value / 8952.91

        elif from_unit == "Quarts":
            if to_unit == "Millilitres":
                return value * 1136.52296975
            elif to_unit == "Litres":
                return value * 1.13652296975
            elif to_unit == "Kilolitres":
                return value * 0.00113652296975
            elif to_unit == "Teaspoons":
                return value * 192.0
            elif to_unit == "Tablespoons":
                return value * 64.0
            elif to_unit == "Pints":
                return value * 2.0
            elif to_unit == "Gallons":
                return value / 4.0
            elif to_unit == "Fluid Ounces":
                return value * 40.0
            elif to_unit == "Cubic Metres":
                return value / 879.877
            elif to_unit == "Cubic Feet":
                return value / 24.9153
            elif to_unit == "Cubic Inches":
                return value * 69.3549
            elif to_unit == "Oil Barrels":
                return value / 139.889

        elif from_unit == "Pints":
            if to_unit == "Millilitres":
                return value * 568.26148487499988992
            elif to_unit == "Litres":
                return value * 0.56826148487499988992
            elif to_unit == "Kilolitres":
                return value * 0.000568261484874999889
            elif to_unit == "Teaspoons":
                return value * 96.0
            elif to_unit == "Tablespoons":
                return value * 32.0
            elif to_unit == "Quarts":
                return value  / 2.0
            elif to_unit == "Gallons":
                return value / 8.0
            elif to_unit == "Fluid Ounces":
                return value * 20.0
            elif to_unit == "Cubic Metres":
                return value / 1759.75
            elif to_unit == "Cubic Feet":
                return value / 49.8307
            elif to_unit == "Cubic Inches":
                return value * 34.6774
            elif to_unit == "Oil Barrels":
                return value / 279.779

        elif from_unit == "Gallons":
            if to_unit == "Millilitres":
                return value * 4546.091879
            elif to_unit == "Litres":
                return value * 4.546091879
            elif to_unit == "Kilolitres":
                return value * 0.0045460918799
            elif to_unit == "Teaspoons":
                return value * 768.0
            elif to_unit == "Tablespoons":
                return value * 256.0
            elif to_unit == "Quarts":
                return value * 4.0
            elif to_unit == "Pints":
                return value * 8.0
            elif to_unit == "Fluid Ounces":
                return value * 160.0
            elif to_unit == "Cubic Metres":
                return value / 219.969
            elif to_unit == "Cubic Feet":
                return value / 6.22884
            elif to_unit == "Cubic Inches":
                return value * 277.419
            elif to_unit == "Oil Barrels":
                return value / 34.9723

        elif from_unit == "Fluid Ounces":
            if to_unit == "Millilitres":
                return value * 28.413074243749994496
            elif to_unit == "Litres":
                return value * 0.028413074243749994496
            elif to_unit == "Kilolitres":
                return value * 0.000028413074243749994
            elif to_unit == "Teaspoons":
                return value * 4.8
            elif to_unit == "Tablespoons":
                return value * 1.6
            elif to_unit == "Quarts":
                return value / 40.0
            elif to_unit == "Pints":
                return value / 20.0
            elif to_unit == "Gallons":
                return value / 160.0
            elif to_unit == "Cubic Metres":
                return value / 35195.1
            elif to_unit == "Cubic Feet":
                return value / 996.614
            elif to_unit == "Cubic Inches":
                return value * 1.73387
            elif to_unit == "Oil Barrels":
                return value / 5595.57

        elif from_unit == "Cubic Metres":
            if to_unit == "Millilitres":
                return value * 1000000.0
            elif to_unit == "Litres":
                return value * 1000.0
            elif to_unit == "Kilolitres":
                return value * 1.0
            elif to_unit == "Teaspoons":
                return value * 168936.0
            elif to_unit == "Tablespoons":
                return value * 56312.1
            elif to_unit == "Quarts":
                return value * 879.877
            elif to_unit == "Pints":
                return value * 1759.75
            elif to_unit == "Gallons":
                return value * 219.969
            elif to_unit == "Fluid Ounces":
                return value * 35195.1
            elif to_unit == "Cubic Feet":
                return value * 35.3147
            elif to_unit == "Cubic Inches":
                return value * 61023.7
            elif to_unit == "Oil Barrels":
                return value * 6.28981

        elif from_unit == "Cubic Feet":
            if to_unit == "Millilitres":
                return value * 28316.8
            elif to_unit == "Litres":
                return value * 28.3168
            elif to_unit == "Kilolitres":
                return value / 35.3147
            elif to_unit == "Teaspoons":
                return value * 4783.74
            elif to_unit == "Tablespoons":
                return value * 1594.58
            elif to_unit == "Quarts":
                return value * 24.9153
            elif to_unit == "Pints":
                return value * 49.8307
            elif to_unit == "Gallons":
                return value * 6.22884
            elif to_unit == "Fluid Ounces":
                return value * 996.614
            elif to_unit == "Cubic Metres":
                return value / 35.3147
            elif to_unit == "Cubic Inches":
                return value * 1728.0
            elif to_unit == "Oil Barrels":
                return value / 5.61458

        elif from_unit == "Cubic Inches":
            if to_unit == "Millilitres":
                return value * 16.3871
            elif to_unit == "Litres":
                return value / 61.0237
            elif to_unit == "Kilolitres":
                return value / 61023.7
            elif to_unit == "Teaspoons":
                return value * 2.76837
            elif to_unit == "Tablespoons":
                return value / 1.08367
            elif to_unit == "Quarts":
                return value / 69.3549
            elif to_unit == "Pints":
                return value / 34.6774
            elif to_unit == "Gallons":
                return value / 277.419
            elif to_unit == "Fluid Ounces":
                return value / 1.73387
            elif to_unit == "Cubic Metres":
                return value / 61023.7
            elif to_unit == "Cubic Feet":
                return value / 1728.0
            elif to_unit == "Oil Barrels":
                return value / 9702.0

        elif from_unit == "Oil Barrels":
            if to_unit == "Millilitres":
                return value * 158987.0
            elif to_unit == "Litres":
                return value * 158.987
            elif to_unit == "Kilolitres":
                return value / 6.28981
            elif to_unit == "Teaspoons":
                return value * 26858.7
            elif to_unit == "Tablespoons":
                return value * 8952.91
            elif to_unit == "Quarts":
                return value * 139.889
            elif to_unit == "Pints":
                return value * 279.779
            elif to_unit == "Gallons":
                return value * 34.9723
            elif to_unit == "Fluid Ounces":
                return value * 5595.57
            elif to_unit == "Cubic Metres":
                return value / 6.28981
            elif to_unit == "Cubic Feet":
                return value * 5.61458
            elif to_unit == "Cubic Inches":
                return value * 9702.0

        raise ValueError("Invalid units or conversion not supported")