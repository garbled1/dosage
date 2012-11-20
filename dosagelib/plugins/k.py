# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, IGNORECASE

from ..scraper import _BasicScraper
from ..util import tagre


class KernelPanic(_BasicScraper):
    latestUrl = 'http://www.ubersoft.net/kpanic/'
    stripUrl = latestUrl + 'd/%s'
    imageSearch = compile(r'src="(.+?/kp/kp.+?)" ')
    prevSearch = compile(r'<li class="previous"><a href="(.+?)">')
    help = 'Index format: yyyymmdd.html'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return imageUrl.split('/')[-1].split('.')[0]



class Key(_BasicScraper):
    latestUrl = 'http://key.shadilyn.com/latestpage.html'
    stripUrl = 'http://key.shadilyn.com/pages/%s.html'
    imageSearch = compile(r'"((?:images/.+?)|(?:pages/images/.+?))"')
    prevSearch = compile(r'</a><a href="(.+?html)".+?prev')
    help = 'Index format: nnn'



class Krakow(_BasicScraper):
    latestUrl = 'http://www.krakowstudios.com/'
    stripUrl = latestUrl + 'archive.php?date=%s'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'


class Kukuburi(_BasicScraper):
    latestUrl = 'http://www.kukuburi.com/current/'
    stripUrl = 'http://thaumic.net/%s'
    imageSearch = compile(r'img src="(http://www.kukuburi.com/../comics/.+?)"')
    prevSearch = compile(r'nav-previous.+?"(http.+?)"')
    help = 'Index format: non'


class KevinAndKell(_BasicScraper):
    latestUrl = 'http://www.kevinandkell.com/'
    stripUrl = latestUrl + '%s/kk%s%s.html'
    imageSearch = compile(r'<img.+?src="(/?(\d+/)?strips/kk\d+.gif)"', IGNORECASE)
    prevSearch = compile(r'<a.+?href="(/?(\.\./)?\d+/kk\d+\.html)"[^>]*><span>Previous Strip', IGNORECASE)
    help = 'Index format: yyyy-mm-dd'

    def setStrip(self, index):
        self.currentUrl = self.stripUrl % tuple(map(int, index.split('-')))


class KillerKomics(_BasicScraper):
    latestUrl = 'http://www.killerkomics.com/web-comics/index_ang.cfm'
    stripUrl = 'http://www.killerkomics.com/web-comics/%s.cfm'
    imageSearch = compile(r'<img src="(http://www.killerkomics.com/FichiersUpload/Comics/.+?)"')
    prevSearch = compile(r'<div id="precedent"><a href="(.+?)"')
    help = 'Index format: strip-name'


class KrazyLarry(_BasicScraper):
    latestUrl = 'http://www.krazylarry.com/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comic[s|/][^"]+)'))
    prevSearch = compile(tagre("a", "href", r'[^"]*(/d/\d+\.s?html)')+r"[^>]+/images/(?:nav_02|previous_day)\.gif")
    help = 'Index format: yyyymmdd'

