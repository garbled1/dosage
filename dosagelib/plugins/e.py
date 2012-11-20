# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, IGNORECASE

from ..helpers import indirectStarter
from ..scraper import _BasicScraper
from ..util import tagre


class EerieCuties(_BasicScraper):
    latestUrl = 'http://www.eeriecuties.com/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'(/d/.+?.html).+?/previous_day.gif')
    help = 'Index format: yyyymmdd'


class EdgeTheDevilhunter(_BasicScraper):
    name = 'KeenSpot/EdgeTheDevilhunter'
    latestUrl = 'http://www.edgethedevilhunter.com/'
    stripUrl = latestUrl + 'comics/%s'
    imageSearch = compile(r'(http://www.edgethedevilhunter.com/comics/.+?)" alt')
    prevSearch = compile(r'(http://www.edgethedevilhunter.com/comics/.+?)"><span class="prev')
    help = 'Index format: mmddyyyy or name'



class Eriadan(_BasicScraper):
    stripUrl = 'http://www.shockdom.com/eriadan/?p=%s'
    imageSearch = compile(r'title="[^"]+?" src="http://www\.shockdom\.com/eriadan/(wp-content/uploads/.+?)"')
    prevSearch = compile(r"<link rel='prev' title='.+?' href='http://www\.shockdom\.com/eriadan/(\?p=.+?)'")
    starter = indirectStarter('http://www.shockdom.com/eriadan/', compile(r'<ul class="latest2">[^<]+?<li class="list-title"><a href="(http://www\.shockdom.com/eriadan/\?p=.+?)"'))
    help = 'Index format: nnn (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return '%d' % (int(compile(r'p=(\d+)').search(pageUrl).group(1)))



class ElGoonishShive(_BasicScraper):
    name = 'KeenSpot/ElGoonishShive'
    latestUrl = 'http://www.egscomics.com/'
    stripUrl = latestUrl + '?date=%s'
    imageSearch = compile(r"'(comics/.+?)'")
    prevSearch = compile(r"<a href='(/\?date=.+?)'.+?arrow_prev.gif")
    help = 'Index format: yyyy-mm-dd'



class ElGoonishShiveNP(_BasicScraper):
    name = 'KeenSpot/ElGoonishShiveNP'
    latestUrl = 'http://www.egscomics.com/egsnp/'
    stripUrl = latestUrl + '?date=%s'
    imageSearch = compile(r'<div class=\'comic2\'><img src=\'(comics/\d{4}/\d{2}.+?)\'')
    prevSearch = compile(r'<a href=\'(.+?)\'[^>]+?onmouseover=\'\$\("navimg(6|2)"\)')
    help = 'Index format: yyyy-mm-dd'



class ElsieHooper(_BasicScraper):
    latestUrl = 'http://www.elsiehooper.com/todaysserial.htm'
    stripUrl = 'http://www.elsiehooper.com/comics/comic%s.htm'
    imageSearch = compile(r'<img src="(/comics_/.+?)">')
    prevSearch = compile(r'<A href="(.+?)"><IMG (height=27 src="/images/previous.gif"|src="/images/previous.gif")', IGNORECASE)
    help = 'Index format: nnn'



class EmergencyExit(_BasicScraper):
    latestUrl = 'http://www.eecomics.net/'
    stripUrl = None
    imageSearch = compile(r'"(comics/.+?)"')
    prevSearch = compile(r'START.+?"(.+?)"')
    # XXX ?
    help = 'God help us now!'



class ErrantStory(_BasicScraper):
    latestUrl = 'http://www.errantstory.com/'
    stripUrl = latestUrl + 'archive.php?date=%s'
    imageSearch = compile(r'<img[^>]+?src="([^"]*?comics/.+?)"')
    prevSearch = compile(r'><a href="(.+?)">&lt;Previous</a>')
    help = 'Index format: yyyy-mm-dd'



class EternalVenture(_BasicScraper):
    latestUrl = 'http://www.pulledpunches.com/venture/'
    stripUrl = 'http://www.beaglespace.com/pulledpunches/venture/?p=%s'
    imageSearch = compile(r'<img src="(http://www.beaglespace.com/pulledpunches/venture/comics/.+?)"')
    prevSearch = compile(r'id="prev"><a href="(http://www.beaglespace.com/pulledpunches/venture/.+?)" ')
    help = 'Index format: nn'



class Evercrest(_BasicScraper):
    latestUrl = 'http://www.evercrest.com/archives/20030308'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(r'<img.+?src="([^"]*/(images/oldstrips|archives/i)/[^"]*)"')
    prevSearch = compile(r'<a.+?href="(http://www.evercrest.com/archives/\d+)">&lt; Previous')
    help = 'Index format: yyyymmdd'


class EverybodyLovesEricRaymond(_BasicScraper):
    latestUrl = 'http://geekz.co.uk/lovesraymond/'
    stripUrl = latestUrl + 'archive/%s'
    imageSearch = compile(r'<img src="((?:http://geekz.co.uk)?/lovesraymond/wp-content(?:/images)/ep\d+\w?\.jpg)"', IGNORECASE)
    prevSearch = compile(r'&laquo; <a href="(http://geekz.co.uk/lovesraymond/archive/[^/"]*)">')
    help = 'Index format: name-of-old-comic'


class EvilDiva(_BasicScraper):
    latestUrl = 'http://www.evildivacomics.com/'
    stripUrl = latestUrl + '%s.html'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'http.+?com/(.+?)".+?"prev')
    help = 'Index format: cpn (unpadded)'

class EvilInc(_BasicScraper):
    latestUrl = 'http://www.evil-comic.com/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch=compile(tagre("img", "src", r'(/comic[s|/][^"]+)'))
    prevSearch=compile(tagre("a", "href", r'[^"]*(/d/\d+\.s?html)')+r"[^>]+/images/(?:nav_02|previous_day)\.gif")
    help='Index format: yyyymmdd'


class Exiern(_BasicScraper):
    latestUrl = 'http://www.exiern.com/'
    stripUrl = latestUrl + 'comic/%s'
    imageSearch = compile(r'<img src="(http://www.exiern.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://www.exiern.com/.+?)" class="navi navi-prev"')
    help = 'Index format: ChapterName-StripName'



class ExiernDarkReflections(_BasicScraper):
    latestUrl = 'http://darkreflections.exiern.com/'
    stripUrl = latestUrl + 'index.php?strip_id=%s'
    imageSearch = compile(r'"(istrip.+?)"')
    prevSearch = compile(r'First.+?(/index.+?)".+?prev')
    help = 'Index format: n'



class ExtraLife(_BasicScraper):
    latestUrl = 'http://www.myextralife.com/'
    stripUrl = latestUrl + 'comic/%s/'
    imageSearch = compile(r'<img src="(http://www.myextralife.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://www.myextralife.com/comic/.+?)"')
    help = 'Index format: mmddyyyy'



class EyeOfRamalach(_BasicScraper):
    latestUrl = 'http://theeye.katbox.net/'
    stripUrl = latestUrl + 'index.php?strip_id=%s'
    imageSearch = compile(r'="(.+?strips/.+?)"')
    prevSearch = compile(r'(index.php\?strip_id=.+?)".+?navigation_back')
    help = 'Index format: n (unpadded)'


class EarthsongSaga(_BasicScraper):
    latestUrl = 'http://www.earthsongsaga.com/'
    stripUrl = None
    imageSearch = compile(r'<img src="((?:\.\./)?images/vol\d+/ch\d+/\d+\.\w+)"')
    prevSearch = compile(r'<a href="([^"]+\.html)"[^>]*><img src="(?:(?:\.\.)?/)?images/testing/prev')
    starter = indirectStarter('http://www.earthsongsaga.com/',
                              compile(r'a href="(.+?)".+?current-page.jpg'))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        imgmatch = compile(r'images/vol(\d+)/ch(\d+)/(\d+)\.\w+$', IGNORECASE).search(imageUrl)
        return 'vol%02d_ch%02d_%02d' % (int(imgmatch.group(1)), int(imgmatch.group(2)), int(imgmatch.group(3)))



class ExploitationNow(_BasicScraper):
    latestUrl = 'http://exploitationnow.com/'
    stripUrl = latestUrl + 'comic.php?date=%s'
    imageSearch = compile(r'src="(comics/.+?)"')
    prevSearch = compile(r' <a href="(.+?)" title="\[Back\]">')
    help = 'Index format: yyyy-mm-dd'



class Ellerbisms(_BasicScraper):
    latestUrl = 'http://www.ellerbisms.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(r'<img src="(http://www.ellerbisms.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://www.ellerbisms.com/.+?)"><span class="prev">')
    help = 'Index format: nnn'
