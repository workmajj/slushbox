#!/usr/bin/env python

import commands
import functools
import os.path
import re
import string
import sys

import fsevents

BROWSER = "Google Chrome"

REFRESH_SCRIPT = """tell application "%s"
	tell tab id %s of window id %s
		execute javascript "window.location.reload()"
	end tell
end tell
"""

OPEN_SCRIPT = """tell application "%s"
	tell window 1
		make new tab with properties {URL: "file://%s"}
	end tell
end tell
"""

def refresh_page(page, window, tab):
    print "Using %s to reload file: %s" % (BROWSER, page)
    script = REFRESH_SCRIPT % (BROWSER, tab, window)
    return commands.getoutput("osascript -e '%s'" % script)

def event_handler(page, window, tab, event):
    # See fsevents for inotify names.
    if event.mask & fsevents.IN_MODIFY:
        print "File modified: %s" % event.name
    elif event.mask & fsevents.IN_ATTRIB:
        print "File modified: %s" % event.name
    elif event.mask & fsevents.IN_CREATE:
        print "File created: %s" % event.name
    elif event.mask & fsevents.IN_DELETE:
        print "File deleted: %s" % event.name
    elif event.mask % fsevents.IN_MOVED_FROM:
        print "File renamed: %s" % event.name
    elif event.mask & fsevents.IN_MOVED_TO:
        print "File renamed: %s" % event.name
    response = refresh_page(page, window, tab)
    if re.search(r'got an error', response):
        raise Exception("Window or tab no longer open.")

def open_page(page):
    print "Using %s to open file: %s" % (BROWSER, page)
    script = OPEN_SCRIPT % (BROWSER, page)
    return commands.getoutput("osascript -e '%s'" % script)

def main():
    if len(sys.argv) != 2:
        raise Exception("Must pass name of exactly one file to open.")
    page = os.path.abspath(sys.argv[1])
    directory = string.join(page.split('/')[:-1], '/')
    
    output = open_page(page)
    r = re.search(r'tab id (\d+) of window id (\d+)', output)
    if not r:
        raise Exception("Couldn't get window and/or tab IDs.")
    (tab, window) = (r.group(1), r.group(2))
    
    observer = fsevents.Observer()
    callback = functools.partial(event_handler, page, window, tab)
    stream = fsevents.Stream(callback, directory, file_events=True)
    
    observer.schedule(stream)
    observer.start()
    try:
        while True:
            pass
    # Check for KeyboardInterrupt, otherwise ^C won't work.
    except (KeyboardInterrupt, OSError, IOError):
        observer.unschedule(stream)
        observer.stop()
    observer.join()

if __name__ == '__main__':
    main()
