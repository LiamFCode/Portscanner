# Port Scanner
A lightweight Nmap wrapper designed to simplify command construction, provide quickly executable script presets, and overall streamline the reconnaissance process.

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
