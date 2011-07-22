Slushbox
========

Reloads local web pages when files in their directories change.

Contact
-------

John J. Workman ([@workmajj](https://twitter.com/workmajj))

Description
-----------

When you edit static web pages, you need to reload them often to see your changes. [Slushbox](http://www.urbandictionary.com/define.php?term=slushbox) opens local pages and then refreshes them automatically when files in their respective directories (or subdirectories) change. So if you edit a CSS file, for example, Slushbox will notice that and refresh accordingly.

At this point, Slushbox is mostly a proof-of-concept project with a few known (and probably some unknown!) limitations:

* Runs only under Mac OS X, since it requires [the MacFSEvents library](http://pypi.python.org/pypi/MacFSEvents/) (though this could probably be generalized to Linux using [```inotify```](http://en.wikipedia.org/wiki/Inotify)).

* Doesn't work with Firefox due to a lack of AppleScript support, and works poorly with Safari.

* Has no way to open dynamic pages, e.g. something you're developing locally using a web framework.

* Handles errors and exceptions very poorly, though it should recognize when windows/tabs have been closed.

* Cannot limit the change-search tree to particular files or subdirectories.

I'm not sure if I'll be developing Slushbox further, but it's at least neat to see the basic idea at work. This differs from most of the other automatic-reload extensions out there in that it's triggered by filesystem changes instead of a simple timer. Thanks to [@robert_winslow](http://twitter.com/robert_winslow) for the initial idea!

Testing & Usage
---------------

1. Install the MacFSEvents library for Python. If you have ```pip``` on your system, you can do:

        $ pip install macfsevents

2. Next, clone the GitHub repo into a temporary directory:

        $ git clone git://github.com/workmajj/slushbox.git

3. Create an HTML file in that temporary directory called ```test.html``` with these contents:

        <p>Lorem ipsum dolor sit amet blah blah blah.</p>

4. Run Slushbox, telling it to open the file and to watch its directory (and subdirectories, if they exist) for changes:

        $ ./slushbox.py test.html

5. At this point, Chrome should open if it's not already running, and the page will load in a new tab.

6. Now modify ```test.html``` in a text editor and then save your changes. When you save, the associated page should reload in Chrome automatically.

License
-------

Copyright (c) 2011, John J. Workman. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

* Neither the name of the <organization> nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
