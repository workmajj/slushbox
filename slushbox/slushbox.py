#!/usr/bin/env python

import commands
import functools
import os.path
import re
import string
import sys
import time

import fsevents

from applescripts import OPEN_SCRIPT, RELOAD_SCRIPT, IS_OPEN_SCRIPT

BROWSER = "Google Chrome"
DEBUG = False

def osascript(script):
    return commands.getoutput("osascript -e '%s'" % (script))

def page_is_open(directory, window, tab):
    output = osascript(IS_OPEN_SCRIPT % (BROWSER, tab, window))
    if re.search(r'file://%s' % (directory), output):
        return True
    else:
        return False

def reload_page(page, window, tab, event):
    # See fsevents for inotify names.
    if DEBUG:
        if event.mask & fsevents.IN_MODIFY:
            print "File modified: %s" % (event.name)
        elif event.mask & fsevents.IN_ATTRIB:
            print "File modified: %s" % (event.name)
        elif event.mask & fsevents.IN_CREATE:
            print "File created: %s" % (event.name)
        elif event.mask & fsevents.IN_DELETE:
            print "File deleted: %s" % (event.name)
        elif event.mask & fsevents.IN_MOVED_FROM:
            print "File renamed: %s" % (event.name)
        elif event.mask & fsevents.IN_MOVED_TO:
            print "File renamed: %s" % (event.name)
    
    if DEBUG:
        print "Using %s to reload file: %s" % (BROWSER, page)
    output = osascript(RELOAD_SCRIPT % (BROWSER, tab, window))
    if re.search(r'got an error', output):
        raise Exception("Window and/or tab no longer open.")

def open_page(page):
    if DEBUG:
        print "Using %s to open file: %s" % (BROWSER, page)
    output = osascript(OPEN_SCRIPT % (BROWSER, page))
    r = re.search(r'tab id (\d+) of window id (\d+)', output)
    if not r:
        raise Exception("Couldn't get window and/or tab IDs.")
    return (r.group(2), r.group(1))

def main():
    if len(sys.argv) != 2:
        raise Exception("Must pass name of exactly one file to open.")
    page = os.path.abspath(sys.argv[1])
    directory = os.path.dirname(page)
    
    (window, tab) = open_page(page)
    callback = functools.partial(reload_page, page, window, tab)
    stream = fsevents.Stream(callback, directory, file_events=True)
    
    observer = fsevents.Observer()
    observer.schedule(stream)
    
    observer.start()
    try:
        while True:
            # Hack: Running the AppleScript in page_is_open() too quickly will
            # fail to return the correct result; one-second delay makes it work.
            time.sleep(1)
            # End program if page is closed in browser.
            if not page_is_open(directory, window, tab):
                observer.stop()
                break
            # End program if thread raises exception.
            if not observer.isAlive():
                break
    # Otherwise end program by checking for ^C with KeyboardInterrupt.
    except (KeyboardInterrupt, OSError, IOError):
        observer.stop()
    
    observer.unschedule(stream)
    observer.join()

if __name__ == '__main__':
    main()
