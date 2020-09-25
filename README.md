# Motion Photo Extraction
## Description
If you take [motion photos](https://support.google.com/googlecamera/answer/9937175) with the 
 [GoogleCamera app](https://play.google.com/store/apps/details?id=com.google.android.GoogleCamera), the motion content
 is persisted into the picture itself. There are several ways to extract the motion content from these photos on your 
 Android device, but once transferred to your computer there is no easy way to accomplish this.
 
With this script, you can easily extract the motion content and save it onto your system.  
This script checks the motion photo for the size of the motion content and extracts the motion content (mp4) with the
 same name.
### Requirements
Tested on macOS/Linux with
* Python 2.7.16
* Python 3.8.5

This possibly works on Windows too, but wasn't validated.
with no third party libraries.
## Extraction
* Download the script to any directory on your system.
* Open the Terminal
    * macOS: 
        * ⌘ (Command) + Space + "Terminal" + ⏎ (Enter)
        * Navigate Finder to /Applications/Utilities/Terminal.app
    * Linux
        * Ctrl + Alt + t
        * Open terminal emulation
* Run the script
    * `python extract.py <file>`
    * `for file in *.jpg; do python extract.py ${file}; done`
