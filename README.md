<p align="center">
    <a>
        <img src="https://raw.githubusercontent.com/gri-gus/loremflickr-streamdeck-plugin/main/assets/images/cover.png" 
        alt="loremflickr-streamdeck-plugin">
    </a>
</p>

<p align="center">
    <a href="https://loremflickr.com/" target="_blank">
        <img src="https://img.shields.io/website?down_color=FF3E87&down_message=offline&label=LoremFlickr website&up_color=004DDD&up_message=online&url=https%3A%2F%2Floremflickr.com%2F" 
         alt="LoremFlickr website">
    </a>
</p>

# loremflickr-streamdeck-plugin

Stream Deck Plugin for installing images from LoremFlickr to button.

**LoremFlickr official website:** https://loremflickr.com/

## Requirements

**Operating systems:**

* MacOS: 10.14 or later
* Windows: 10 or later

**Stream Deck application:** 6.0, 6.1

**Python:** 3.7 or later

## Installation

### Python

> If you have difficulty, then look at articles or videos on the Internet about it.

1. Download Python from the official website and install it: https://www.python.org/downloads/

   > ⚠️ Python version must be 3.7.0 or later.


2. Check that Python is available from the command line:

   <details><summary>MacOS</summary>

   Open the `Terminal` application, enter the command below and press Return(Enter):

   ```shell
   python3 -V
   ```

   If you get a response that looks like `Python 3.10.4`, then you have done everything right.

   If there is no response, then you have installed Python incorrectly.

   </details>

   <details><summary>Windows</summary>

   Open the `Command Prompt` application, enter the command below and press Return(Enter):

   ```shell
   python -V
   ```

   If you get a response that looks like `Python 3.10.4`, then you have done everything right.

   If there is no response, then you have installed Python incorrectly.

   </details>

3. Restart your computer.

### Stream Deck

Download the Stream Deck app from the official website and install it: https://www.elgato.com/en/downloads

### LoremFlickr Stream Deck Plugin

> ⚠️ During the installation of the plugin, you must have internet access.

> Errors may occur during installation. If they are, then a message about it will appear on the screen.

Latest release: https://github.com/gri-gus/loremflickr-streamdeck-plugin/releases

You need to download a file called `com.ggusev.loremflickr.streamDeckPlugin`. Once downloaded, double-click on it. The
Stream Deck application prompts you to install the plugin.

After installation, you will have a `LoremFlickr` category and actions:

<img width="295" height="100" src="https://raw.githubusercontent.com/gri-gus/loremflickr-streamdeck-plugin/main/assets/images/category.png" alt="category">

## Usage

> ⚠️ The button may not start working immediately after installing the plugin, but after about 20 seconds. At this time,
> dependencies are installed. If you do not receive an error message on the screen, but an exclamation mark is displayed
> when you click on the button, then the plugin is not fully installed yet, and you need to wait. This only happens
> after installing the plugin. There is no need to wait for the next use.

Drag the `Set key image` action from `LoremFlickr` category to the desired button.

Click on the button, and you will see the Property Inspector where you can adjust some settings. See the `Manual`
section
in the Property Inspector for more details.

<img width="433" height="230" src="https://raw.githubusercontent.com/gri-gus/loremflickr-streamdeck-plugin/main/assets/images/setkeyimage_pi.png" alt="setkeyimage_pi">

Each time you press the button on the Stream Deck, the picture will be updated.

## Dependencies

[streamdeck-python-sdk](https://github.com/gri-gus/streamdeck-python-sdk)

[streamdeck-javascript-sdk](https://github.com/elgatosf/streamdeck-javascript-sdk)
