from src.GameFunc.settings.SettingDataObject import SettingDataObject


class SettingManager:
    @staticmethod
    def ApplySetting_display(instance, setting_data: SettingDataObject = None):
        instance.display.set_mode((500, 500))
        instance.display.set_caption("Avoid Moster | ver1.0")

