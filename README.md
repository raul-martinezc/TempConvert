# TempConverter

A minimal desktop app for converting between Celsius and Fahrenheit in real time.

## How it works

Type a value in either field and the other updates instantly — no button press needed. The two fields stay in sync as you type.

## Running locally

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install PySide6
   ```

3. Run the app:
   ```bash
   python temp.py
   ```

## Building a macOS .app

```bash
pip install pyinstaller
pyinstaller --windowed --name "TempConverter" -y temp.py
```

The `.app` will be in the `dist/` folder.

## Building a Windows .exe

Run the following on a Windows machine:

```bash
pip install pyinstaller
pyinstaller --windowed --onefile --name "TempConverter" temp.py
```

The `.exe` will be in the `dist/` folder.

## Building for Linux

Run the following on a Linux machine:

```bash
pip install pyinstaller
pyinstaller --windowed --onefile --name "TempConverter" temp.py
```

This produces a standalone binary in `dist/`. To package it as a native installer:

**Debian/Ubuntu (.deb):**

```bash
sudo apt install python3-stdeb fakeroot
python setup.py --command-packages=stdeb.command bdist_deb
```

Or use `dpkg-deb` manually by creating a package directory structure:

```text
TempConverter_1.0/
  DEBIAN/control
  usr/local/bin/TempConverter
```

Then build with:

```bash
dpkg-deb --build TempConverter_1.0
```

**Fedora/RHEL (.rpm):**

```bash
sudo dnf install rpm-build
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
```

Place the binary in `~/rpmbuild/SOURCES/`, write a `.spec` file, then build with:

```bash
rpmbuild -bb TempConverter.spec
```

The resulting `.rpm` will be in `~/rpmbuild/RPMS/`.

## Requirements

- Python 3.9+
- PySide6
