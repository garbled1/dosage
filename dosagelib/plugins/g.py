# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile

from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class Galaxion(_BasicScraper):
    latestUrl = 'http://galaxioncomics.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(r'(wordpress/comics/.+?)"')
    prevSearch = compile(r'\| <a href="http://galaxioncomics.com/(\?p=.+?)".+?vious.gif')
    help = 'Index format: non'


class Garanos(_BasicScraper):
    latestUrl = 'http://www.garanos.com/'
    stripUrl = latestUrl + 'pages/page-%s'
    imageSearch = compile(r'<img src=.+?(/pages/.+?)"')
    prevSearch = compile(r'<a href="(http://www.garanos.com/pages/page-.../)">&#9668; Previous<')
    help = 'Index format: n  (unpadded)'


class GUComics(_BasicScraper):
    latestUrl = 'http://www.gucomics.com/comic/'
    stripUrl = latestUrl + '?cdate=%s'
    imageSearch = compile(r'<IMG src="(/comics/\d{4}/gu_.*?)"')
    prevSearch = compile(r'<A href="(/comic/\?cdate=\d+)"><IMG src="/images/cnav_prev')
    help = 'Index format: yyyymmdd'



class GenrezvousPoint(_BasicScraper):
    latestUrl = 'http://genrezvouspoint.com/'
    stripUrl = latestUrl + 'index.php?comicID=%s'
    imageSearch = compile(r'<img src=\'(comics/.+?)\'')
    prevSearch = compile(r' <a[^>]+?href="(.+?)">PREVIOUS</a>')
    help = 'Index format: nnn'



class GirlGenius(_BasicScraper):
    latestUrl = 'http://girlgeniusonline.com/comic.php'
    stripUrl = 'http://www.girlgeniusonline.com/comic.php\?date=%s'
    imageSearch = compile(r"(/ggmain/strips/.+?)'")
    prevSearch = compile(r"</a> <a href=.+?(/comic.php\?date=.+?)'.+?Previous")
    help = 'Index format: yyyymmdd'



class GirlsWithSlingshots(_BasicScraper):
    latestUrl = 'http://www.daniellecorsetto.com/gws.html'
    stripUrl = 'http://www.daniellecorsetto.com/GWS%s.html'
    imageSearch = compile(r'<img src="(images/gws/GWS\d{3}.jpg)"')
    prevSearch = compile(r'(archive.php\?today=\d{3}&comic=\d{3})"[^>]*><img[^>]+src="images/gwsmenu/back_off.jpg"')
    help = 'Index format: nnn'


class Girly(_BasicScraper):
    latestUrl = 'http://girlyyy.com/'
    stripUrl = latestUrl + 'go/%s'
    imageSearch = compile(r'<img src="(http://girlyyy.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"> &nbsp;&lt;&nbsp;prev')

    help = 'Index format: nnn'

class GleefulNihilism(_BasicScraper):
    latestUrl = 'http://gleefulnihilism.com/'
    stripUrl = latestUrl + 'comics/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://gleefulnihilism\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://gleefulnihilism\.com/comics/[^"]+)') + 'Previous')
    help = 'Index format: yyyy/mm/dd/stripname'


class Goats(_BasicScraper):
    latestUrl = 'http://www.goats.com/'
    stripUrl = latestUrl + 'archive/%s.html'
    imageSearch = compile(r'<img.+?src="(/comix/.+?)"')
    prevSearch = compile(r'<a href="(/archive/\d{6}.html)" class="button" title="go back">')
    help = 'Index format: yymmdd'



class GoneWithTheBlastwave(_BasicScraper):
    starter = indirectStarter('http://www.blastwave-comic.com/index.php?p=comic&nro=1',
                              compile(r'href="(index.php\?p=comic&amp;nro=\d+)"><img src="images/page/default/latest'))
    stripUrl = 'http://www.blastwave-comic.com/index.php?p=comic&nro=%s'
    imageSearch = compile(r'<img.+src=".+(/comics/.+?)"')
    prevSearch = compile(r'href="(index.php\?p=comic&amp;nro=\d+)"><img src="images/page/default/previous')
    help = 'Index format: n'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return '%02d' % int(compile(r'nro=(\d+)').search(pageUrl).group(1))



class GunnerkrigCourt(_BasicScraper):
    latestUrl = 'http://www.gunnerkrigg.com/index2.php'
    stripUrl = 'http://www.gunnerkrigg.com/archive_page.php\?comicID=%s'
    imageSearch = compile(r'<img src="(.+?//comics/.+?)"')
    prevSearch = compile(r'<.+?(/archive_page.php\?comicID=.+?)".+?prev')
    help = 'Index format: n'



class Gunshow(_BasicScraper):
    latestUrl = 'http://gunshowcomic.com/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(r'src="(/comics/.+?)"')
    prevSearch = compile(r'(/d/\d+\.html)"><img[^>]+?src="/images/previous_day')
    help = 'Index format: yyyy/mm/dd'



class GleefulNihilism(_BasicScraper):
    latestUrl = 'http://gleefulnihilism.com/'
    stripUrl = latestUrl + 'comics/2009/12/01/just-one-of-the-perks/%s'
    imageSearch = compile(r'<img src="(http://gleefulnihilism.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"[^>]+?>Previous</a>')
    help = 'Index format: yyyy/mm/dd/strip-name'



class GastroPhobia(_BasicScraper):
    latestUrl = 'http://www.gastrophobia.com/'
    stripUrl = latestUrl + 'index.php?date=%s'
    imageSearch = compile(r'<img src="(http://gastrophobia.com/comix/[^"]+)"[^>]*>(?!<br>)')
    prevSearch = compile(r'<a href="(.+?)"><img src="pix/prev.gif" ')
    help = 'Index format: yyyy-mm-dd'



class Geeks(_BasicScraper):
    latestUrl = 'http://sevenfloorsdown.com/geeks/'
    stripUrl = latestUrl + 'archives/%s'
    imageSearch = compile(r'<img src=\'(http://sevenfloorsdown.com/geeks/comics/.+?)\'')
    prevSearch = compile(r'<a href="(.+?)">&laquo; Previous')
    help = 'Index format: nnn'



class GlassHalfEmpty(_BasicScraper):
    latestUrl = 'http://www.defectivity.com/ghe/index.php'
    stripUrl = latestUrl + '?strip_id=%s'
    imageSearch = compile(r'src="(comics/.+?)"')
    prevSearch = compile(r'</a><a href="(.+?)"><img src="\.\./images/onback\.jpg"')
    help = 'Index format: nnn'


class GreystoneInn(_BasicScraper):
    latestUrl = 'http://www.greystoneinn.net/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch=compile(tagre("img", "src", r'(/comic[s|/][^"]+)'))
    prevSearch=compile(tagre("a", "href", r'[^"]*(/d/\d+\.s?html)')+r"[^>]+/images/(?:nav_02|previous_day)\.gif")
    help='Index format: yyyymmdd'

