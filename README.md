# Port Scanner
A lightweight Nmap wrapper designed to simplify command construction, provide quickly executable script presets, and overall streamline the reconnaissance process.

When in the reconnaissance stage sometimes you're sitting at a desk with all the time in the world and a collection of tools, but sometimes you simply don't have that time luxury and you need to be able to use those tools much faster. Nmap is a phenomenal tool, and is incredibly powerful, but in a pinch needing to remember exact arguments and flags to write out the right script can be tedious. This project is a wrapper for Nmap that allows you to write those script out beforehand and run them at a moments notice with a user-friendly interface.

## Implementation

### Setup:
Clone repo: <br>
```git clone github.com/LiamFCode/Portscanner.git``` <br>
<br>
Edit the config.yaml file to build scripts, using Nmap syntax for the arguments. <br>
```name``` corresponds to what is displayed in the terminal when selecting between scripts. <br>
```outputFileName``` is the file name for the document of results from the scan. This can be in csv, txt, or json format, as set by ```outputFileType```. <br>

### Usage:
To use the port scanner, simply run ```python scanner.py```, then select whether you wish to configure scripts via terminal interface, or run a preexisting script. From there you can simply follow the prompts and listed options to execute functions.

## License
MIT License

Copyright (c) 2026 LiamFCode

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
