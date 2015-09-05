# pacman

This is an unfinished pacman written in python using the pygame framework.

![Screenshot](https://raw.githubusercontent.com/JnyJny/pacman/e0a8ff74958e2b1b5c90c637f73c74a35eccdb2a/screenshots/Screen%20Shot%202015-09-05%20at%205%20Sep%2010.43.22%20AM.png)

It's interesting for a couple of reasons, despite being unfinished:

 1. State machine driven
 2. Maze generation driven by text configuration file
 3. Much of the design was driven by the excellent Pacman deconstruction, [Pacman Dossier](http://home.comcast.net/~jpittman2/pacman/pacmandossier.html)

In it's current state, the Puckman can be manuvered through the maze and eat dots (regular and power). The ghosts
are placed in the maze, but they are largely unfinished: no sprite animations, no movement, no direct interaction
with Puckman.  There is stubbed out support for the various scenes found in the arcade version of Pacman ( attract,
intermissions, end game ), but nothing beyond that.

## Font
The implementation depends on the excellent free/libre TrueType font "Press Start 2 Play" which
you can download from: http://www.zone38.net/font/pressstart2p.zip
