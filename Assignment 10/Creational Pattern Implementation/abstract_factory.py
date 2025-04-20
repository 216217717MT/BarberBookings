import WindowsButton   #from windows_button 
import MacOSButton     #from macos_button 
import Button          #from button 

class GUIFactory:
    @staticmethod
    def create_button(os_type: str) -> Button:
        if os_type.lower() == "windows":
            return WindowsButton()
        elif os_type.lower() == "macos":
            return MacOSButton()
        else:
            raise ValueError(f"Unknown OS type: {os_type}")
