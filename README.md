# PyQt5-Demo

A simple demo of PyQt5, containing simple features including:

- Opening text and image files;

  There are already some files prepared for testing:

  - `misaka.c.txt`: A simple C program styled as one of the Misaka Sisters, originally taken from IOCCC 2013;
  - `misaka-mikoto.png`: A screenshot from *A Certain Magical Index* E15 (*Angel Fall*), showing Kamijou Touma’s sister in Misaka Mikoto’s appearance.

- Downloading simple files from the Internet.

## Launching

To launch this demo, you need to have Python and Pip installed, and run the commands below:

```bash
pip install -r requirements.txt
python pyqt_application.py
```

The `.ui` files can be edited with Qt Designer, and `_form.py` files are the corresponding outputs of `pyuic` which converts `.ui` files into Python modules.

To install Qt Designer, you can install package `PyQt5-tools`, which also includes some other useful tools such as `pyuic` and `pyrcc`:

```bash
pip install PyQt5-tools
```

If you would only like Qt Designer and you’ve installed an official Qt distribution, you may have already had it.

*PS: The user interface is ugly, isn’t it?*

## License

The repo, unless otherwise noted, is licensed under the [GNU General Public License 3.0 (GPL-3.0)](LICENSE), except for some exceptions listed below.

### Exceptions

- `misaka-mikoto.png` is part of the animation series *A Certain Magical Index* produced by J.C. Staff, which is work and property of its copyright holder(s);
- `misaka.c.txt` is originally taken from the work of Don Yang in IOCCC, which is licensed under the CC-BY-SA 3.0 license.

