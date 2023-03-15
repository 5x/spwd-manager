# SPWD Manager

A complex program for secure and convenient local storage and management of important data, passwords and other contents in encrypted storage files.

## Build Windows Application 

To create runnable execute application use next:
```bash
pyinstaller spwd_manager.spec
```

To reduce file size build with UPX from virtualenv:
```bash
python -m venv .
Scripts\activate.bat
pip install -r requirements.txt
pyinstaller --upx-dir "{{PATH_TO_UPX_DIR}}" spwd_manager.spec
```

[More info about PyInstaller](https://www.pyinstaller.org/)

## Requirements

* Python 3.8 or later
* cryptography
* pyinstaller
* ttkbootstrap

## Support & Contributing
Anyone is welcome to contribute. If you decide to get involved, please take a moment and check out the following:

* [Bug reports](.github/ISSUE_TEMPLATE/bug_report.md)
* [Feature requests](.github/ISSUE_TEMPLATE/feature_request.md)

## License

The code is available under the [MIT license](LICENSE).