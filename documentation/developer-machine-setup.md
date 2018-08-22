# Developer Machine Setup
> Outlines the steps required to get the AR Demo project running on a developer machine. Also includes any troubleshooting items that may have been encountered.

Table of Contents
=================
* [Windows Setup](#windows-setup)
* [Mac Setup](#mac-setup)
* [Troubleshooting](#troubleshooting)

## Overall Setup
> These steps are not specific to any machine, you will have to do this on Mac or Windows and is the same process. 
1. Download the most recent version of [Unity](https://store.unity.com/download?ref=personal).
    - Choose the free "personal" version of Unity. (We don't have a professional plan yet)
2. When going through the Unity installation process, and the prompt comes up for you to choose Component Installation *be sure* to check ["Vuforia Augmented Reality Support"](https://library.vuforia.com/articles/Training/getting-started-with-vuforia-in-unity.html). 

## Windows Setup
> Includes the steps to get the project up and running on a windows machine.
1. Download and install `npm` verson 5.1.0+
2. run `npm install`
3. run `npm run webpack`

## Mac Setup
> The Mac setup is used if you need to build and test for iOS. You can also install and use it for Android if it is your preferred platform to work on.
1. Go to the Mac App Store or [Apple Developer's Website](https://developer.apple.com/xcode/).
    - Download Xcode (it includes to required toolset to run Unity iOS builds)

## Troubleshooting
> Includes common troubleshooting steps that can be taken when issues are encountered.

**Issue**: _Get some error when doing something._

**Solution**: Try doing 'x' to resolved the issue.