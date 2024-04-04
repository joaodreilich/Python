# QR Code Generator

## About
A simple QR (Quick Response) Code generator developed in Python for learning and practice purposes.
It will upgrade with new functions and features along along with my progress studying the language (see [Roadmap](#roadmap))

Developed in **Python 3.12**

## Libraries and Modules
This project uses **qrcode** and **Pillow** modules:
```
pip install qrcode
pip install Pillow
```

or use the prompt below to install qrcode with pillow:

```
pip install qrcode[pil]
```

And was compiled using **PyInstaller** module:
```
pip install pyinstaller
```

## Log
04/04/2024: Initial commit

## Roadmap
Some new features that will possibly come:
- Output: PNG or SVG choice
- Output: size choice
- Output: destination folder selected by user
- Generation: add color choice for QR Code
- Generation: add logo in the center of QR Code
- Generation: QR Code type (line, dot, square...)
- Generation: QR Code color option
- Interface: add GUI

## License
This project is currently under [MIT License](https://opensource.org/license/mit)

Copyright 2024 Joao Dreilich

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Supporting Documentation and Disclaimers
- [Python](https://docs.python.org/3/)

- [PyInstaller](https://pyinstaller.org/en/stable/)

- [qrcode](https://github.com/lincolnloop/python-qrcode)

>Copyright (c) 2011, Lincoln Loop
>All rights reserved.
>
>Redistribution and use in source and binary forms, with or without
>modification, are permitted provided that the following conditions are met:
>
>    * Redistributions of source code must retain the above copyright notice,
>      this list of conditions and the following disclaimer.
>    * Redistributions in binary form must reproduce the above copyright notice,
>      this list of conditions and the following disclaimer in the documentation
>      and/or other materials provided with the distribution.
>    * Neither the package name nor the names of its contributors may be
>      used to endorse or promote products derived from this software without
>      specific prior written permission.
>
>THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
>ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
>WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
>DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
>ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
>(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
>LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
>ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
>(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
>SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
>
>-------------------------------------------------------------------------------
>
>Original text and license from the pyqrnative package where this was forked
>from (http://code.google.com/p/pyqrnative):
>
>#Ported from the Javascript library by Sam Curren
>
>QRCode for Javascript
>http://d-project.googlecode.com/svn/trunk/misc/qrcode/js/qrcode.js
>
>Copyright (c) 2009 Kazuhiko Arase
>
>URL: http://www.d-project.com/
>
>Licensed under the MIT license:
>http://www.opensource.org/licenses/mit-license.php
>
>The word "QR Code" is registered trademark of
>DENSO WAVE INCORPORATED
>http://www.denso-wave.com/qrcode/faqpatent-e.html

- [Pillow](https://pillow.readthedocs.io/en/stable/)

>The Python Imaging Library (PIL) is
>
>Copyright © 1997-2011 by Secret Labs AB
>Copyright © 1995-2011 by Fredrik Lundh and contributors
>
>Pillow is the friendly PIL fork. It is
>
>Copyright © 2010-2024 by Jeffrey A. Clark and contributors
>
>Like PIL, Pillow is licensed under the open source HPND License:
>
>By obtaining, using, and/or copying this software and/or its associated
>documentation, you agree that you have read, understood, and will comply
>with the following terms and conditions:
>
>Permission to use, copy, modify and distribute this software and its
>documentation for any purpose and without fee is hereby granted,
>provided that the above copyright notice appears in all copies, and that
>both that copyright notice and this permission notice appear in supporting
>documentation, and that the name of Secret Labs AB or the author not be
>used in advertising or publicity pertaining to distribution of the software
>without specific, written prior permission.
>
>SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
>SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.
>IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR ANY SPECIAL,
>INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
>LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
>OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
>PERFORMANCE OF THIS SOFTWARE.