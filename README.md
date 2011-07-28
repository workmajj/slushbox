Slushbox
========

Reloads local web pages when files in their directories change.

Contact
-------

John J. Workman ([@workmajj](https://twitter.com/workmajj))

Description
-----------

When building static web pages, you need to reload them often to see your changes. [Slushbox](http://www.urbandictionary.com/define.php?term=slushbox) opens local pages and then refreshes them automatically when files in their respective directories (or subdirectories) change. So if you edit a CSS file, for example, Slushbox will notice and refresh accordingly.

At this point, Slushbox has a few known (and probably some unknown!) limitations:

* Runs only under Mac OS X, since it uses AppleScript for browser control.

* Currently works only with Google Chrome (not yet tested with Safari, and Firefox has minimal AppleScript support).

* Has no way to integrate with URLs routed by web frameworks.

Thanks to Robert Winslow ([@robert_winslow](http://twitter.com/robert_winslow)) for the initial project idea!

Testing & Usage
---------------

1. Install the MacFSEvents library for Python. If you have ```pip``` on your system, you can do:

        $ pip install macfsevents

2. Next, clone the GitHub repo into a temporary directory:

        $ git clone git://github.com/workmajj/slushbox.git

3. Run Slushbox, telling it to open an example file and to watch its directory (and subdirectories) for changes:

        $ ./slushbox.py ../example/ugly.html

4. At this point, Chrome should open if it's not already running, and the page will load in a new tab.

5. Use a text editor to open the ```style.css``` page, located in the ```example/static``` directory.

6. Modify ```style.css``` and then save your changes. When you save, ```ugly.html``` will reload in Chrome automatically.

7. Try adding or deleting a file in the ```example``` directory and watch Slushbox reload. You can even navigate to other pages in the directory.

8. When you're finished, close the browser tab Slushbox originally opened; the command-line program will quit automatically.

License
-------

Copyright (c) 2011, John J. Workman. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

* Neither the name of the <organization> nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
