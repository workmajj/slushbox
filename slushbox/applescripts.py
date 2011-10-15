# Scripts below use tabs instead of spaces.

IS_OPEN_SCRIPT = """tell application "%s"
	tell tab id %s of window id %s
		get URL
	end tell
end tell
"""

RELOAD_SCRIPT = """tell application "%s"
	tell tab id %s of window id %s
		execute javascript "window.location.reload()"
	end tell
end tell
"""

OPEN_SCRIPT = """tell application "%s"
	activate
	tell first window
		make new tab with properties {URL:"%s"}
	end tell
end tell
"""
