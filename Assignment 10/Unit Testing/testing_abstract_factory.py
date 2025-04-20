import unittest
import GUIFactory    # from abstract_factory 
import WindowsButton # from windows_button
import MacOSButton   # from macos_button

class TestGUIFactory(unittest.TestCase):
    def test_create_windows_button(self):
        button = GUIFactory.create_button("windows")
        self.assertIsInstance(button, WindowsButton)

    def test_create_macos_button(self):
        button = GUIFactory.create_button("macos")
        self.assertIsInstance(button, MacOSButton)

    def test_invalid_os_type(self):
        with self.assertRaises(ValueError):
            GUIFactory.create_button("linux")