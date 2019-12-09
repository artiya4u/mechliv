import requests
import pkg_resources


class Version:
    def __init__(self):
        pass

    PYPI_URL = "https://pypi.python.org/pypi/mechliv/json"

    @staticmethod
    def latest():
        try:
            res = requests.get(Version.PYPI_URL).json()
            return res['info']['version']
        except Exception as e:
            return '0.0.0'

    @staticmethod
    def current():
        try:
            return pkg_resources.require("mechliv")[0].version
        except Exception as e:
            return '0.0.0'

    @staticmethod
    def new_available():
        latest = Version.latest()
        current = Version.current()
        try:
            if pkg_resources.parse_version(latest) > pkg_resources.parse_version(current):
                print("[+] New version " + latest + " is available")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print("[+] There was an error in trying to fetch updates")
            return False
