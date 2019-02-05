# clipSave
This program acts as a form of quickly accessible Scratchpad. Using the configured shortcut, any contents on your clipboard will be saved to disk as an html file and opened in your default web browser. This may be useful when filling out forms that clear data if there are errors, or when you've navigated to data that would be difficult to navigate back to.



## Configuration

The save directory defaults to:

```
'c:/nvda-textcopy/' 
```

You can change this on line #17 of clipSave.py (./addon/globalPlugins/clipSave.py)

## Usage

Use:

```
(YOUR_NVDA_KEY) + A
```

## Building

If you are on a UNIX OS (macOS, Linux distro), you can run the build script in the root of the directory and it will output the addon file to ./builds

```
./build.sh
```

If you are on windows, zip the contents of the addon folder and rename them to 'addon.nvda-addon'

