# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
import urllib2
import os
import locale
import rfc822
import time

from .output import out
from .util import urlopen, saneDataSize, normaliseURL
from .events import getHandler

class FetchComicError(IOError):
    """Exception for comic fetching errors."""
    pass

class ComicStrip(object):
    """A list of comic image URLs."""

    def __init__(self, name, parentUrl, imageUrls, namer):
        """Store the image URL list."""
        self.name = name
        self.parentUrl = parentUrl
        self.imageUrls = imageUrls
        self.namer = namer

    def getImages(self):
        """Get a list of image downloaders."""
        for imageUrl in self.imageUrls:
            yield self.getDownloader(normaliseURL(imageUrl))

    def getDownloader(self, url):
        """Get an image downloader."""
        filename = self.namer(url, self.parentUrl)
        if filename is None:
            filename = url.rsplit('/', 1)[1]
        return ComicImage(self.name, url, self.parentUrl, filename)


class ComicImage(object):
    """A comic image downloader."""

    def __init__(self, name, url, referrer, filename):
        """Set URL and filename."""
        self.name = name
        self.referrer = referrer
        self.url = url
        self.filename, self.ext = os.path.splitext(filename)
        self.filename = self.filename.replace(os.sep, '_')
        self.ext = self.ext.replace(os.sep, '_')

    def connect(self):
        """Connect to host and get meta information."""
        try:
            self.urlobj = urlopen(self.url, referrer=self.referrer)
        except urllib2.HTTPError, he:
            raise FetchComicError, ('Unable to retrieve URL.', self.url, he.code)

        if self.urlobj.info().getmaintype() != 'image' and \
           self.urlobj.info().gettype() not in ('application/octet-stream', 'application/x-shockwave-flash'):
            raise FetchComicError, ('No suitable image found to retrieve.', self.url)

        # Always use mime type for file extension if it is sane.
        if self.urlobj.info().getmaintype() == 'image':
            self.ext = '.' + self.urlobj.info().getsubtype().replace('jpeg', 'jpg')
        self.contentLength = int(self.urlobj.info().get('content-length', 0))
        self.lastModified = self.urlobj.info().get('last-modified')
        out.write('... filename = %r, ext = %r, contentLength = %d' % (self.filename, self.ext, self.contentLength), 2)

    def touch(self, filename):
        """Set last modified date on filename."""
        if self.lastModified:
            tt = rfc822.parsedate(self.lastModified)
            if tt:
                mtime = time.mktime(tt)
                os.utime(filename, (mtime, mtime))

    def save(self, basepath):
        """Save comic URL to filename on disk."""
        self.connect()
        filename = "%s%s" % (self.filename, self.ext)
        comicSize = self.contentLength
        comicDir = os.path.join(basepath, self.name.replace('/', os.sep))
        if not os.path.isdir(comicDir):
            os.makedirs(comicDir)

        fn = os.path.join(comicDir, filename)
        if os.path.isfile(fn) and os.path.getsize(fn) >= comicSize:
            self.urlobj.close()
            self.touch(fn)
            out.write('Skipping existing file "%s".' % (fn,), 1)
            return fn, False

        try:
            out.write('Writing comic to file %s...' % (fn,), 3)
            with open(fn, 'wb') as comicOut:
                startTime = time.time()
                comicOut.write(self.urlobj.read())
                endTime = time.time()
            self.touch(fn)
        except:
            if os.path.isfile(fn):
                os.remove(fn)
            raise
        else:
            size = os.path.getsize(fn)
            bytes = locale.format('%d', size, True)
            if endTime != startTime:
                speed = saneDataSize(size / (endTime - startTime))
            else:
                speed = '???'
            attrs = dict(fn=fn, bytes=bytes, speed=speed)
            out.write('Saved "%(fn)s" (%(bytes)s bytes, %(speed)s/sec).' % attrs, 1)
            getHandler().comicDownloaded(self.name, fn)
        finally:
            self.urlobj.close()

        return fn, True
