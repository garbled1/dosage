# SPDX-License-Identifier: MIT
# Copyright (C) 2015-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
import re

from ..scraper import _ParserScraper


class SmackJeeves(_ParserScraper):
    baseUrl = 'https://www.smackjeeves.com/discover/'
    apiBase = 'https://www.smackjeeves.com/api/discover/'
    prevSearch = '//a[i[d:class("i-arrow-double-left-black")]]'
    imageSearch = re.compile("comicData:[^']*'([^']*)'", re.DOTALL)
    help = 'Index format: n'

    def __init__(self, name, id, adult=False, endOfLife=False, last=None):
        super(SmackJeeves, self).__init__('SmackJeeves/' + name)
        self._comicid = id
        self.url = self.baseUrl + 'articleList?titleNo={}'.format(id)
        self.stripUrl = self.baseUrl + 'detail?titleNo={}&articleNo=%s'.format(id)
        self.firstStripUrl = self.stripUrl % 1
        self.adult = adult
        self.endOfLife = endOfLife or last
        self.lastid = (last or 0) - 1
        if name == 'VerloreGeleentheid':
            self.textSearch = True

    def starter(self):
        response = self.session.post(self.apiBase + 'articleList',
            params={'titleNo': self._comicid})
        response.raise_for_status()
        return response.json()['result']['list'][self.lastid]['articleUrl']

    def fetchUrls(self, url, data, urlsearch):
        if urlsearch != self.imageSearch:
            return super(SmackJeeves, self).fetchUrls(url, data, urlsearch)

        # Find image URL in JavaScript
        datatag = data.xpath('//script[contains(text(), "comicData")]')
        if not datatag:
            return ()
        datamatch = self.imageSearch.search(datatag[0].text)
        if not datamatch:
            return ()
        return (datamatch.group(1),)

    def link_modifier(self, fromurl, tourl):
        # All links redirect to /discover/ - so fix it to save a request
        return tourl.replace('com/detail', 'com/discover/detail')

    def namer(self, image_url, page_url):
        articleNo = int(page_url.rsplit('=', 1)[1])
        return '{:04}'.format(articleNo)

    def fetchText(self, url, data, textSearch, optional):
        if 'VerloreGeleentheid' in self.name:
            response = self.session.post('https://www.smackjeeves.com/api/comments/get', params={
                'titleNo': self._comicid,
                'articleNo': url.rsplit('=', 1)[1],
                'page': 1,
                'order': 'new'
            })
            response.raise_for_status()
            comments = response.json()['result']['list']
            for comment in reversed(comments):
                if comment['nickname'] == 'Wolfie_Inu':
                    return comment['commentText']
            return None
        else:
            super(SmackJeeves, self).fetchText(url, data, textSearch, optional)

    @classmethod
    def getmodules(cls):
        return (
            cls('20TimesKirby', 91583),
            cls('2Kingdoms', 112096, endOfLife=True),
            cls('355Days', 114138),
            cls('_A_', 130892, endOfLife=True),
            cls('AB', 110961, adult=True),
            cls('AceOfHearts', 155154),
            cls('AcidMonday', 30447, adult=True),
            cls('Adalsysla', 96496, endOfLife=True),
            cls('ADoodleADay', 141301),
            cls('AdventuresOfLumAndFriends', 122193),
            cls('AdventuresoftheWeird', 4430),
            cls('AetherTheories', 116164),
            cls('AgeOfTheGray', 132378),
            cls('AGirlOnTheServer', 44252),
            cls('AKirbyKomic', 25724),
            cls('ALaMode', 35776),
            cls('AllInLOVE', 6639),
            cls('AllStarHeroes', 127874),
            cls('AlmostTouching', 140881, adult=True),
            cls('AlwaysDamnedWebcomic', 21652, adult=True),
            cls('AlwaysRainingHere', 96902),
            cls('Amaravati', 49250),
            cls('AmorVincitOmnia', 66370, adult=True),
            cls('AmsdenEstate', 105458),
            cls('AngelGuardian', 72720),
            cls('ANGELOU', 21129),
            cls('AnimalAdventures', 125930),
            cls('Animayhem', 53122),
            cls('AnythingAboutNothing', 50399),
            cls('APTComic', 71310),
            cls('AQuestionOfCharacter', 70161),
            cls('Area9', 108861),
            cls('AroundTheBlock', 125385),
            cls('ArtOfAFantasy', 92258, adult=True),
            cls('ASongforElise', 45895, adult=True),
            cls('AtArmsLength', 39242),
            cls('Atlaswebcomic', 140920),
            cls('Autophobia', 82522),
            cls('AyaTakeo', 60325),
            cls('AYuriCollab', 126727, adult=True),
            cls('BabysittingFourDemons', 5992),
            cls('BadassRiz', 130263),
            cls('BallandChain', 99503),
            cls('Bard', 51147),
            cls('BassComicAdventures', 131900),
            cls('BattleSequence', 132075),
            cls('Bearhoney', 111843),
            cls('BearlyAbel', 41761),
            cls('BeautifulLies', 130068),
            cls('BehindTheGlassCurtain', 54480, endOfLife=True),
            cls('BehindTheObsidianMirror', 94375, adult=True),
            cls('BeretCatComics', 136026),
            cls('Bestbrosforever', 132559),
            cls('Betovering', 127694, adult=True),
            cls('BettencourtHotel', 98760, endOfLife=True),
            cls('BeTwin', 97886, endOfLife=True),
            cls('BeyondTheOrdinary', 129233),
            cls('BioRevelation', 121142),
            cls('Bl3', 131849, endOfLife=True),
            cls('BlackAndBlue', 63275, endOfLife=True),
            cls('Blackdemon', 117183),
            cls('BlackDragon', 131654),
            cls('BlackFridayRule', 94517),
            cls('BlackSheepcomic', 91663),
            cls('BleachRedux', 94169),
            cls('BlindandBlue', 110850),
            cls('BloodhuntersBirthOfAVampire', 92969, endOfLife=True),
            cls('BloomAPokemonConquestComic', 122439),
            cls('BlueHair', 119037),
            cls('BoilingPointofBrain', 122291),
            cls('BoogeyDancingMonkeyPot', 128196),
            cls('BreachOfAgency', 82923, endOfLife=True),
            cls('Burn', 93761),
            cls('ByTheBook', 98401, adult=True),
            cls('CafeSuada', 80707),
            cls('Cambion', 112560, adult=True),
            cls('CaptiveSoul', 115786),
            cls('Captured', 135452, adult=True),
            cls('CaravanaTaleofGodsandMen', 129824),
            cls('Cataclysm', 98815, adult=True),
            cls('Catnip', 108592, adult=True),
            cls('Cerintha', 117941),
            cls('ChampionofChampions', 103159),
            cls('ChampionsAndHeroesAgeOfDragons', 98261),
            cls('ChannelDDDNews', 120506),
            cls('ChaosAdventuresII', 64827),
            cls('ChaoticNation', 108410, adult=True),
            cls('Charaktermaske', 118975),
            cls('Chatuplines', 84863),
            cls('CheneysGotaGun', 75737),
            cls('ChickenScratches', 90898),
            cls('ChildrenOfTheNight', 52560),
            cls('ChimiMouryou', 108675),
            cls('ChocolatewithPepper', 132832),
            cls('ClairetheFlare', 121081),
            cls('ClockworkAtrium', 3048),
            cls('CloeRemembrance', 9150, endOfLife=True),
            cls('CockroachTheater', 138343),
            cls('Cogs', 130634),
            cls('ColorBlind', 118617),
            cls('ConventionalWisdom', 89324),
            cls('CosmicDash', 4584),
            cls('Cramberries', 82134),
            cls('CrimsonWings', 113469),
            cls('CrocodileTears', 85055, adult=True),
            cls('CupOfOlea', 130678),
            cls('CurseLineage', 86745),
            cls('DanielleDark', 9257),
            cls('Dasien', 1779, adult=True),
            cls('DavidDoesntGetIt', 115176),
            cls('DBON', 76205),
            cls('DeathNoteIridescent', 87149),
            cls('DEGAF', 120316),
            cls('DEMENTED', 104334, adult=True),
            cls('DemonBattles', 145936),
            cls('DemonCat', 105404),
            cls('DemonEater', 125937, adult=True),
            cls('DenizensAttention', 56481),
            cls('DevilsCake', 26927),
            cls('DevotoMusicinHell', 114862, adult=True),
            cls('Diaz', 129935),
            cls('DigimonSaviors', 43521),
            cls('DigimonTamersMiraiProject', 119257),
            cls('DigitalInsanity', 144866),
            cls('DoItYourself', 103195),
            cls('DoodleBeans', 17473, adult=True),
            cls('DoodlingAround', 117225),
            cls('Dragonet', 119508),
            cls('DragonKid', 96550),
            cls('DreamCatcher', 23687),
            cls('DumpofManyPeople', 138063),
            cls('DungeonHordes', 94210),
            cls('EATATAU', 64889),
            cls('EDepthAngel', 98932),
            cls('EidolonWhispersOfEternity', 136262),
            cls('ElementalSpirits', 18192),
            cls('EnkeltenKentta', 78834, adult=True),
            cls('Enthrall', 113047, adult=True),
            cls('EntreEuxDeux', 97894, endOfLife=True),
            cls('Eorah', 135499, adult=True),
            cls('Equsopia', 127680),
            cls('ERAConvergence', 63750, endOfLife=True),
            cls('ERAIbuki', 129506, endOfLife=True),
            cls('ERRORERROR', 113481),
            cls('EuphemisticEephus', 127121),
            cls('EvilPlan', 19063),
            cls('ExperimentalMegaman', 75706),
            cls('EyesOfADigimon', 97117),
            cls('FailureConfetti', 69275),
            cls('FairyTaleRejects', 99139, adult=True),
            cls('FaithlessDigitals', 137288),
            cls('FalconersDailyStrips', 124329),
            cls('FallenAngelslove', 113208),
            cls('FarOutMantic', 48658),
            cls('FarOutThere', 89199),
            cls('FeralGentry', 119912),
            cls('FinalArcanum', 51191),
            cls('FireredLisasReise', 109151),
            cls('FlyorFail', 104604),
            cls('ForcedSeduction', 61407),
            cls('ForgetTheDistance', 80429, adult=True),
            cls('Fortheloveofabrokenstring', 116411),
            cls('FramebyFrame', 71042, adult=True),
            cls('FrobertTheDemon', 26586),
            cls('FromnowonImagirl', 99018),
            cls('FruitloopAndMrDownbeat', 82798),
            cls('FullSpectrumTherapy', 156285),
            cls('GamerCafe', 138841),
            cls('GamesPeoplePlayUpdatedWeekly', 72207),
            cls('GardenofHearts', 106504),
            cls('GayBacon', 104466),
            cls('GayTimesWithRyanAndJay', 121095),
            cls('GetUpAndGo', 42180, adult=True),
            cls('GigisNuzlockeRuns', 157589),
            cls('Gloomverse', 75498),
            cls('Gnoph', 138286, endOfLife=True),
            cls('GoodGame', 48048, endOfLife=True),
            cls('GoodnightMrsGoose', 73655),
            cls('Grayscale', 100295, adult=True),
            cls('GuardiansoftheGalaxialSpaceways', 70286),
            cls('Habibahssong', 137453),
            cls('HarvestMoonParadiseFound', 105422, endOfLife=True),
            cls('HateThePlayer', 118599),
            cls('HatShop', 71816),
            cls('Helix', 121066),
            cls('HeltonShelton', 124804),
            cls('Hephaestus', 79909),
            cls('HereBeVoodoo', 133691, adult=True),
            cls('HiddenStrengthAWhiteNuzlocke', 116170),
            cls('Hinata', 134703),
            cls('Holocrash', 64113, endOfLife=True),
            cls('HolyBlasphemy', 91250),
            cls('HolyCrap', 13235),
            cls('HopeForABreeze', 40188),
            cls('HouseOfCraziness', 171040),
            cls('HurrocksFardel', 1488),
            cls('IciVontLesMorts', 133719, adult=True),
            cls('Inchoatica', 138342),
            cls('Ingloriousbasterds', 139586),
            cls('InHouseHumor', 108681),
            cls('Inhuman', 108969),
            cls('InsideOuTAYuriTale', 50590),
            cls('InspiredByADream', 48419),
            cls('ItsAn8BitWorldBlankWorld', 88082),
            cls('IWishIggysWish', 107290),
            cls('JackiesStory', 108822),
            cls('Jantar', 134338),
            cls('Jason', 139878),
            cls('JoeysAdventure', 142807),
            cls('JourneyMan', 129303),
            cls('JoyToTheWorld', 129685),
            cls('June', 90624),
            cls('JustAnotherLife', 128013),
            cls('JustCrazy', 84007),
            cls('Justmyluck', 169106),
            cls('KaitoShuno', 100498, adult=True),
            cls('KasaKeira', 78059),
            cls('KazanatoFuneralPlanningService', 24026),
            cls('KCNO', 103010, endOfLife=True),
            cls('KezroChroniclesPhantomOps', 104447),
            cls('Kirbandfriendsshowcase', 85495),
            cls('KirbiesoftheAlternateDimension', 108771),
            cls('KirbyAdventure', 77366),
            cls('KirbyDreamTeam', 112273),
            cls('KirbyFunfestTheOriginals', 90652),
            cls('KirbysDreamAdventure', 69796),
            cls('KirbysDreamlandAdventures', 46154),
            cls('KirbyTheDeeArmy', 115693, endOfLife=True),
            cls('KissmeSnow', 125812),
            cls('KissoftheDevil', 64006),
            cls('Knightface', 97596, adult=True),
            cls('KnightsRequiem', 68098),
            cls('KojiX5', 108937, endOfLife=True),
            cls('Kreetor', 80871),
            cls('Kruptos', 99200, endOfLife=True),
            cls('KuronaFlutterandLylaSpamTime', 124636),
            cls('LastBlockStanding', 125034),
            cls('LavenderLegend', 107018),
            cls('LeCirquedObscure', 103647),
            cls('LedbyaMadMan', 111999),
            cls('LegendOfZeldaAHerosStory', 118155),
            cls('LegendOfZeldaStaffOfPower', 112732),
            cls('LegendOfZeldaTheEdgeAndTheLight', 126345, endOfLife=True),
            cls('LegendOfZeldaTheWindWaker', 49542),
            cls('Lemongrass', 131786),
            cls('LesCendresdelHiver', 131767),
            cls('LethalDose', 115067, adult=True),
            cls('LetLoveRule', 177216),
            cls('LicensedHeroes', 123974),
            cls('LifeAsACutOut', 86222),
            cls('LifeAsItWas', 117747),
            cls('LifeLessOrdinary', 63169, adult=True),
            cls('Lifeonpaper', 126099),
            cls('LightLovers', 135581, adult=True),
            cls('LightwithinShadow', 47016),
            cls('LilLevi', 134946),
            cls('LOGOS', 93415, adult=True),
            cls('LOKI', 93990),
            cls('LondonUnderworld', 45699),
            cls('LostNova', 84173),
            cls('LoveandIcecream', 112872),
            cls('LoveHarbor', 130349),
            cls('LoveMeLoveMyTeddyBear', 50359),
            cls('LoveroftheSunandMoon', 121615),
            cls('LsEmpire', 33751),
            cls('LuffinpuffandEric', 83450),
            cls('LumasParadise', 46770, last=174),
            cls('MagicalMisfits', 138166),
            cls('Magipunk', 131204),
            cls('Manifestedpart1', 140208),
            cls('MarioandLuigiMisadventures', 4806),
            cls('MariosDayJob', 2330),
            cls('MarioVsSonicVsMegaMan', 14122, endOfLife=True),
            cls('MarsMind', 129347),
            cls('MarXistemTWC', 100651),
            cls('Mascara', 59912),
            cls('MatildasSweetCakeCafe', 115251, adult=True),
            cls('MayTheRainCome', 119715, endOfLife=True),
            cls('Mazscara', 12456),
            cls('MegaManTales', 6516),
            cls('MegaPain', 88178),
            cls('MelodyAndMacabre', 28408),
            cls('MetroJack', 61376, adult=True),
            cls('MidnightPrince', 106681, adult=True),
            cls('MineS', 139112),
            cls('Minibot', 18129),
            cls('MinorActsOfHeroism', 78356),
            cls('Missing', 118871),
            cls('Missingversionfrancaise', 126329),
            cls('MobianChaos', 49021),
            cls('Mokepon', 42705),
            cls('Monstar', 141569),
            cls('MoonValley', 157462),
            cls('MorphE', 122406),
            cls('Mortifer', 17271),
            cls('MrFactory', 119931),
            cls('MyFakeHeart', 19105),
            cls('MySisterTheDragon', 9612, endOfLife=True),
            cls('MySparklingPrincesama', 105626),
            cls('MyStereoBot', 133633),
            cls('MysticanDreams', 130154),
            cls('MythsOfUnovaAWhiteNuzlockeRunHardMode', 101385),
            cls('MYth', 36430),
            cls('Nah', 88350),
            cls('Negligence', 66718),
            cls('NeonGlow', 63747),
            cls('NeverTheHero', 132200),
            cls('Nexus', 115357),
            cls('NiceKitty', 75854),
            cls('NighHeavenandHell', 72209, adult=True),
            cls('NightSpace', 142396),
            cls('NIK', 83716),
            cls('NissiesDragonPrincess', 112655),
            cls('NixsFireRedNuzlocke', 127939),
            cls('NobleHeartsHiruandMerroug', 138690, adult=True),
            cls('NoEnd', 138812),
            cls('NormalcyisforWimps', 23862),
            cls('NotyoursamI', 63700, adult=True),
            cls('ObnoxiousHerokun', 146954, adult=True),
            cls('ObsidianHeart', 130610),
            cls('October20th', 122344),
            cls('OddPlaceOddTime', 60037),
            cls('OldElastikid', 97110),
            cls('OneRainyDay', 111352, adult=True),
            cls('Onlyonelovesong', 86555),
            cls('OperationTheater', 97500),
            cls('OriginBook1Codearth', 124751),
            cls('OurTimeInEden', 27011),
            cls('Outbreak', 134869),
            cls('OutofKey', 123152),
            cls('OverSync', 114781),
            cls('Panacea', 79601, adult=True),
            cls('PantsParty', 70630),
            cls('PanzerDragonandEnigmaCompleteEdition', 20039),
            cls('Pause', 135615),
            cls('PencilviewUpdatesMondayscough', 33041),
            cls('PeterPan', 119991),
            cls('Phantomland', 106943),
            cls('PhotoShootNarusasuDoujinshi', 110984, adult=True, last=187),
            cls('PlasticKings', 132377),
            cls('PlayTime', 68440),
            cls('PleaseBeMyBoytoy', 26922),
            cls('PMDExplorersOfHeart', 121563),
            cls('PMDTeamFirefox', 103870),
            cls('PMDVictoryFire', 116780),
            cls('PokemonBeta', 76962, endOfLife=True),
            cls('PokemonCrystalDoubleNuzlockeChallenge', 102420, endOfLife=True),
            cls('PokemonLANDSKY', 120046),
            cls('PokemonNoRakuen', 22822),
            cls('PokemonParallel', 86143),
            cls('PokemonSAKOHJU', 120395),
            cls('Pokeventurous', 98420),
            cls('Ponzi', 85187),
            cls('PrettyMouth', 131442),
            cls('PrincessChroma', 106726),
            cls('ProfessorDolphinpresentsPokemon', 81880),
            cls('ProjectCAPLimit', 137000),
            cls('PTO', 43363, adult=True),
            cls('Puck', 100566),
            cls('PullingYouUnder', 155504, adult=True),
            cls('PulseandBolt', 86022),
            cls('PurpureaNoxa', 103522, adult=True),
            cls('QueerQueen', 130802),
            cls('RainbowMansion', 140231, adult=True),
            cls('RainLGBT', 90588),
            cls('RainxSasori', 108131, adult=True, endOfLife=True),
            cls('RANDOM', 99296),
            cls('RareCandyTreatment', 83853),
            cls('RavenWolf', 97826),
            cls('Regina', 129902),
            cls('ReidyAndFriendsShowcase', 45097),
            cls('RemoteAngel', 46191),
            cls('Replica', 123116, adult=True, endOfLife=True),
            cls('Respectable', 128996, adult=True, endOfLife=True),
            cls('ReturntoEden', 15691),
            cls('ROSIER', 54232),
            cls('RottenApple', 133069),
            cls('RoyalIcing', 81321),
            cls('RubyNation', 107039),
            cls('RuneSpark', 140886),
            cls('RUScrewed', 144524),
            cls('RyuManwebcomicVersion', 135497, endOfLife=True),
            cls('SabishiiGhost', 136824),
            cls('SaintforRent', 123862),
            cls('SakuraDAY', 135342),
            cls('SakuraMishzo', 58018, adult=True),
            cls('SalemUncommons', 70211),
            cls('SallySprocketAndPistonPete', 58930),
            cls('SaltyKiss', 104227),
            cls('SayWhatYouMean', 82290),
            cls('SChIzO', 94872),
            cls('SchoolOfRejectsSoRe', 37768),
            cls('ScionsoftheSeraph', 43320, adult=True),
            cls('ScrappedProject', 73142),
            cls('SecretPowerbk1', 117146),
            cls('SecretPowerbk2', 117458),
            cls('Seki', 123118, adult=True),
            cls('SeriousTimes', 73090),
            cls('SFCBlackjackBay', 123799),
            cls('SFCForestofDreams', 88943),
            cls('ShamelessAdvertisements', 51975),
            cls('Shameless', 130592),
            cls('ShotoutofCanon', 18876),
            cls('ShroudofLight', 121119),
            cls('Signifikat', 12217, adult=True),
            cls('SimpleBear', 120596),
            cls('Sire', 58167),
            cls('Skeptical', 108904),
            cls('Slackmatic', 144286),
            cls('SLightlyAbOVeAvErage', 117203, adult=True),
            cls('SlipstreamSingularity', 66132),
            cls('SmallPressAdventures', 70273),
            cls('SocksMittensandScarfs', 132813),
            cls('SomethingLikeaPhenomenon', 176182, adult=True),
            cls('SonicAuthorAdventII', 5867),
            cls('SonicBoom', 111375),
            cls('SonicClub', 5638),
            cls('SonicDashly', 87024),
            cls('SonicFuture', 30809),
            cls('SonicSchoolRedo', 110100),
            cls('SOSRadio', 107498),
            cls('SouthernCross', 94541),
            cls('SovereignTheMostAmazingComicEver', 129062),
            cls('SparElricsExtras', 125431),
            cls('Spellcross', 125055),
            cls('SpiderWings', 36314),
            cls('SplitScreen', 125293, adult=True, endOfLife=True),
            cls('SPRITEDHeroesofDobalia', 109013),
            cls('Spriterschaos', 11126),
            cls('Sprytts', 70422),
            cls('Stay', 102560, adult=True),
            cls('StellaInChrome', 70107),
            cls('Stereophonic', 129406),
            cls('StolenGeneration', 20901, adult=True, endOfLife=True),
            cls('Storyofadamnedlove', 107702),
            cls('StrangersandFriends', 94050),
            cls('Striped', 79896, adult=True),
            cls('StuntRayWalterswish', 73075),
            cls('SubjecttoChangeCollegeWoes', 48759),
            cls('Sunfall', 133465),
            cls('SunmeetsMoon', 62545),
            cls('SUNRISESTORY', 127611),
            cls('SuperDimensionAfterTheHero', 98885),
            cls('SuperMarioBros3', 18739, endOfLife=True),
            cls('SuperMarjoBros', 136454),
            cls('SupermassiveBlackHoleA', 59625),
            cls('SurvivorFanCharacters', 24928),
            cls('SweetestPoison', 142001),
            cls('SwitchMechanism', 121604, endOfLife=True),
            cls('TaikiTheWebcomic', 87240),
            cls('TailsAdventureThroughTimeandOtherWorlds', 116964),
            cls('TakingPicturesofStrangers', 71337, adult=True),
            cls('TalesFromAaronsWings', 142272, endOfLife=True),
            cls('TEN', 96475),
            cls('ThatWasntThereYesterday', 85420),
            cls('The13thWorld', 108420),
            cls('TheAdventuresOfBanjoZ', 136763, adult=True, endOfLife=True),
            cls('TheAntihero', 64167),
            cls('TheArchipelago', 142266),
            cls('Theatrics', 93578),
            cls('TheBattleInTheSky', 143006),
            cls('TheBookOfNosferatu', 97421),
            cls('TheBrideoftheShark', 61393, adult=True),
            cls('TheBucket', 124197),
            cls('TheCafedAlizee', 80009),
            cls('TheCavernOfSecrets', 126366),
            cls('TheColony', 70272, adult=True),
            cls('TheContract', 121955),
            cls('TheCrawl', 124962),
            cls('TheDarkLegacy', 83199),
            cls('TheDemonicAdventuresOfAngelWitchPita', 105060, adult=True),
            cls('TheDestroyer', 79216, adult=True),
            cls('TheDragonAndTheLemur', 91259, adult=True),
            cls('TheDreaming', 142053, endOfLife=True),
            cls('TheDrifter', 137597, adult=True),
            cls('TheElectricRose', 133024),
            cls('TheForestofWhispers', 123645),
            cls('TheGhostWithTheMost', 125332),
            cls('TheGoldRiderofPern', 30008),
            cls('TheGrayZone', 116458),
            cls('TheHeadhunters', 105336),
            cls('TheHeartofEarth', 113048),
            cls('TheiaMania', 115095),
            cls('TheJosephComics', 19785, endOfLife=True),
            cls('TheKeyHotelEnding', 106307, endOfLife=True),
            cls('TheKwiddexProtocol', 70268),
            cls('TheLastBloodCafe', 136484),
            cls('ThelaughingDeath', 129212),
            cls('TheLegendaryQueen', 17122, adult=True),
            cls('TheLifeofMagFlamequill', 51697),
            cls('TheLoneSwordsman', 18218),
            cls('TheMadMan', 83928),
            cls('TheMegaManandSonicSpriteShowcase', 75689),
            cls('TheNightSurfers', 120705),
            cls('TheNocheComicSeries', 133439, adult=True),
            cls('TheNOMEDSEGA', 127642),
            cls('ThePirateBalthasar', 73113),
            cls('ThePremise', 118125),
            cls('ThePrincessAndTheGiant', 59629, endOfLife=True),
            cls('ThePropertyofHate', 117970),
            cls('TheReborn', 1898),
            cls('TheSearchForHenryJekyll', 139257),
            cls('TheSilverLeague', 110008),
            cls('TheSummerofBlakeSinclair', 95648),
            cls('Theswordsmanandtheamnesiac', 74220, adult=True),
            cls('TheTimeDog', 97194),
            cls('TheTytonNuzlockeChallengeEmeraldEdition', 115517),
            cls('TheWhiteTower', 123161, endOfLife=True),
            cls('TheWinterCampaign', 80021),
            cls('TheYoshiHerd', 5814),
            cls('ThiefCatcherRingTail', 112115),
            cls('ThornsComic', 131578),
            cls('ThornTopia', 54482),
            cls('TLAAOK', 92316, adult=True),
            cls('TosiHuonoYaoiSarjis', 141725, adult=True),
            cls('TotallyCrossover', 73445),
            cls('TPTruePower', 13199),
            cls('TrainerWantsToFight', 134083),
            cls('Transfusions', 77588, adult=True),
            cls('TransUMan', 107514, adult=True, endOfLife=True),
            cls('TroubleNextDoor', 114482, endOfLife=True),
            cls('UglyBoysLove', 102165),
            cls('Uglygame', 61960),
            cls('UnderTheDeadSkies', 114107),
            cls('UnicampaLapis', 111371),
            cls('UpDown', 140374, adult=True),
            cls('UshalaatWorldsEnd', 130596, adult=True),
            cls('Vacan7', 63460, adult=True),
            cls('VACANT', 127276),
            cls('VerloreGeleentheid', 80604, endOfLife=True),
            cls('VoidMisadventures', 129134),
            cls('VoyageoftheBrokenPromise', 137418, adult=True),
            cls('WakeEcho', 70945),
            cls('Wander', 118109),
            cls('WantedDeadorDead', 68540),
            cls('Wayfar', 95839),
            cls('Waysoftheheart', 91122),
            cls('WeAreGolden', 72590, adult=True),
            cls('WelcomeToFreakshow', 72225),
            cls('WelcomeToThePCA', 127811, endOfLife=True),
            cls('WhatAboutLove', 74057, adult=True),
            cls('WHATAboutSHADOWS', 109321, endOfLife=True),
            cls('WhatIsDeepInOnesHeart', 130798),
            cls('WhatWeRememberTheMost', 162746),
            cls('WhenSheWasBad', 12859),
            cls('Whenweweresilent', 156839),
            cls('WhereaboutsOfTime', 133530),
            cls('WhiteHeart', 124545, adult=True),
            cls('WhiteNoise', 63110),
            cls('Wildflowers', 125360),
            cls('WildWingBoysKoathArc', 50240),
            cls('WildWingBoys', 203574),
            cls('WingsOverEthereal', 37417),
            cls('WingsTurnedtoDust', 113033, last=417),
            cls('Wootlabs', 101636),
            cls('XXMoralityXx', 132016),
            cls('YadotCakeShop', 106995, adult=True),
            cls('YamanaokiHighSchool', 82468),
            cls('YoungCannibals', 8027),
            cls('ZaenWell', 111081),
            cls('ZeldaTheNewAdventureofLinkIIMajorasMask', 43724),
        )
