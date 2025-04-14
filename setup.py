from setuptools import setup

APP = ['tomato_timer.py']

OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'icon.icns',  
    'plist': {
        'CFBundleName': 'Tomato Timer',
        'CFBundleDisplayName': 'Tomato Timer',
        'CFBundleIdentifier': 'com.jeanne.tomato',
        'CFBundleVersion': '0.1.0',
        'LSUIElement': True
    },
    'packages': ['rumps'],
    'frameworks': []
}

setup(
    app=APP,
    data_files=[],
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
