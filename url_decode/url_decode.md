# Decoding urls

Internet URL (universal resource locator) are encoded in such way that it appear with
escaped characters like `%3A` for `:`, `%2F` for`/` and so on. Those characters are not
decoded by default by the browser.

Python includes a library to decode those characters in a way that we can use them in the web
browser.

```python
#!/usr/bin/env python3
import urllib
url = 'http%3A%2F%2Fwww.cis.syr.edu%2F~wedu%2FTeaching%2Fcis643%2FLectureNotes_New%2FMAC.pdf'
print(urllib.parse.unquote(url))
#'http://www.cis.syr.edu/~wedu/Teaching/cis643/LectureNotes_New/MAC.pdf' Result

```
