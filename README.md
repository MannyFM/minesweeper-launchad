# ROBT206. Microcontrollers. Final Project

This project is implementation of nostalgic Windows game named `minesweeper`. It follows same rules as original game and uses Novation LaunchpadMK2 as input and feedback of game.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
As you understood from previous section, in order to run this project locally, you will need Novation LaunchpadMK2 (other models can be used with little twick in code).

### Prerequisites

What things you need to install the software and how to install them
You will need Python3 and PyGame, launchpad.py libraries.

You can find installing tutorials for [PyGame](https://www.pygame.org/news) and [launchpad.py](https://github.com/FMMT666/launchpad.py) in following links.
* https://www.pygame.org/wiki/GettingStarted
* https://github.com/FMMT666/launchpad.py

### Installing

Clone this repository (or download zip and unarchive it)

```
  git clone https://github.com/MannyFM/minesweeper-launchpad
```

Installing python3 dependencies

```
  pip3 install -r requirements.txt
```

> NOTE: PyGame doesn't install automatically, you need to follow link in previous section in order to get instructions on how to install it on your specific machine

Finally, you can run project with
```
  python3 game.py
```

## Authors


* **Mansur Shakipov**, **Nurzhan Sakenov**: game logic in C (the original logic)
* **Alibek Manabayev**: idea, adapting code for Python (the final iteration)
* **Madiyar Katranov**: tinkering with the hardware, Intel Galileo setup
* **Assem Yeskabyl**: writing the report

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
