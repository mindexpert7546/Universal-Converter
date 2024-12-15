"""
Main Application Module

This module initializes and runs the Universal Convert application. It loads the initial screen.

Classes:
--------
MainApp : MDApp
    The main application class that sets up the app's title and loads the
    starting screen.
-------------------------------------------------------------------------------
"""

from kivy.config import Config
Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '665')

from kivymd.app import MDApp
from app.screens.menuscreen.menuscreen import MenuScreen
from app.screens.conversionscreen.conversionscreen import ConversionScreen

class MainApp(MDApp):
    """
    The main application class for Universal Convert, an app that allows users to
    convert units across various metrics.

    Methods:
    --------
    build():
        Sets up the main app title and returns the initial app structure.
    on_start():
        Sets the initial screen to 'menu_screen' when the app starts.
    """
    
    def build(self):
        """
        Builds the application, setting up the main title.

        Returns:
        --------
        None
        """
        
        self.title = "Universal Convert"
        
    def on_start(self):
        """
        Callback triggered when the application starts. Sets the initial screen
        to 'menu_screen'.
        """
        
        self.root.current = 'menu_screen'
    
if __name__ == "__main__":
    MainApp().run()