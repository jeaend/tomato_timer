from setuptools import setup

APP = ['tomato_timer.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'tomato_icon.icns',  # ← fixed line
    'plist': {
        'CFBundleName': 'Tomato Timer',
        'CFBundleDisplayName': 'Tomato Timer',
        'CFBundleIdentifier': 'com.jeanne.tomato',
        'CFBundleVersion': '0.1.0',
        'LSUIElement': True,  # hides dock icon
    },
}

setup(
    app=APP,
    name='Tomato Timer',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
