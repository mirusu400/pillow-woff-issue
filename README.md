# pillow-woff-issue
Issue about woff files

## Description
This simple method has OSError when trying to open some woff and woff2 files.
```python
fnt = ImageFont.truetype(f'./fonts/Youth.woff2')
```
```
Traceback (most recent call last):
  File "/Users/mirusu400/kwoss/pillow-woff-issue/test.py", line 14, in <module>
    raise e
  File "/Users/mirusu400/kwoss/pillow-woff-issue/test.py", line 10, in <module>
    fnt = ImageFont.truetype(f'./fonts/{file}')
  File "/usr/local/lib/python3.9/site-packages/PIL/ImageFont.py", line 959, in truetype
    return freetype(font)
  File "/usr/local/lib/python3.9/site-packages/PIL/ImageFont.py", line 956, in freetype
    return FreeTypeFont(font, size, index, encoding, layout_engine)
  File "/usr/local/lib/python3.9/site-packages/PIL/ImageFont.py", line 247, in __init__
    self.font = core.getfont(
OSError: unknown file format
```

## My Environment
```
ProductName:	macOS
ProductVersion:	12.4
BuildVersion:	21F79
Python 3.9.13 (main, May 24 2022, 21:28:31)
[Clang 13.1.6 (clang-1316.0.21.2)] on darwin
Pillow==9.2.0
```

## Test Methods
```bash
python3 test.py
```

## Result
```bash
python3 test.py
Trying to convert GangwonEduSaeeum_OTFMediumA.woff ...  ...Success
Trying to convert Youth.woff2 ...       ...Failed unknown file format
Trying to convert .DS_Store ... ...Failed unknown file format
Trying to convert ChosunCentennial.woff2 ...    ...Failed unknown file format
Trying to convert Cafe24Ssurround.woff ...      ...Success
Trying to convert CookieRun-Regular.woff ...    ...Success
Trying to convert Minhye.woff ...       ...Success
Trying to convert TTTogetherA.woff ...  ...Success
Trying to convert GangwonEduPowerExtraBoldA.woff ...    ...Success
Trying to convert ChosunGs.woff ...     ...Success
Trying to convert Cafe24Oneprettynight.woff ... ...Success
```
