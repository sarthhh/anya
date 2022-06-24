from __future__ import annotations

import random
import typing as t

__all__: t.Tuple[str, ...] = ("Colors",)


class Colors:
    """
    Custom Color class which returns hex integers.
    """

    @property
    def air_force_blue(self) -> int:
        return 0x5D8AA8

    @property
    def alice_blue(self) -> int:
        return 0xF0F8FF

    @property
    def alizarin_crimson(self) -> int:
        return 0xE32636

    @property
    def almond(self) -> int:
        return 0xEFDECD

    @property
    def amaranth(self) -> int:
        return 0xE52B50

    @property
    def amber(self) -> int:
        return 0xFFBF00

    @property
    def american_rose(self) -> int:
        return 0xFF033E

    @property
    def amethyst(self) -> int:
        return 0x9966CC

    @property
    def android_green(self) -> int:
        return 0xA4C639

    @property
    def anti_flash_white(self) -> int:
        return 0xF2F3F4

    @property
    def antique_brass(self) -> int:
        return 0xCD9575

    @property
    def antique_fuchsia(self) -> int:
        return 0x915C83

    @property
    def antique_white(self) -> int:
        return 0xFAEBD7

    @property
    def ao(self) -> int:
        return 0x008000

    @property
    def apple_green(self) -> int:
        return 0x8DB600

    @property
    def apricot(self) -> int:
        return 0xFBCEB1

    @property
    def aqua(self) -> int:
        return 0x00FFFF

    @property
    def aquamarine(self) -> int:
        return 0x7FFFD4

    @property
    def army_green(self) -> int:
        return 0x4B5320

    @property
    def arylide_yellow(self) -> int:
        return 0xE9D66B

    @property
    def ash_grey(self) -> int:
        return 0xB2BEB5

    @property
    def asparagus(self) -> int:
        return 0x87A96B

    @property
    def atomic_tangerine(self) -> int:
        return 0xFF9966

    @property
    def aureolin(self) -> int:
        return 0xFDEE00

    @property
    def aurometalsaurus(self) -> int:
        return 0x6E7F80

    @property
    def awesome(self) -> int:
        return 0xFF2052

    @property
    def azure(self) -> int:
        return 0x007FFF

    @property
    def azure_mist(self) -> int:
        return 0x0FFFF

    @property
    def baby_blue(self) -> int:
        return 0x89CFF0

    @property
    def baby_blue_eyes(self) -> int:
        return 0xA1CAF1

    @property
    def baby_pink(self) -> int:
        return 0xF4C2C2

    @property
    def ball_blue(self) -> int:
        return 0x21ABCD

    @property
    def banana_mania(self) -> int:
        return 0xFAE7B5

    @property
    def banana_yellow(self) -> int:
        return 0xFFE135

    @property
    def battleship_grey(self) -> int:
        return 0x848482

    @property
    def bazaar(self) -> int:
        return 0x98777B

    @property
    def beau_blue(self) -> int:
        return 0xBCD4E6

    @property
    def beaver(self) -> int:
        return 0x9F8170

    @property
    def beige(self) -> int:
        return 0xF5F5DC

    @property
    def bisque(self) -> int:
        return 0xFFE4C4

    @property
    def biinte(self) -> int:
        return 0x3D2B1

    @property
    def bittersweet(self) -> int:
        return 0xFE6F5E

    @property
    def black(self) -> int:
        return 0x000000

    @property
    def blanched_almond(self) -> int:
        return 0xFFEBCD

    @property
    def bleu_de_france(self) -> int:
        return 0x318CE7

    @property
    def blizzard_blue(self) -> int:
        return 0xACE5EE

    @property
    def blond(self) -> int:
        return 0xFAF0BE

    @property
    def blue(self) -> int:
        return 0x0000FF

    @property
    def blue_bell(self) -> int:
        return 0xA2A2D0

    @property
    def blue_gray(self) -> int:
        return 0x6699CC

    @property
    def blue_green(self) -> int:
        return 0x0D98BA

    @property
    def blue_purple(self) -> int:
        return 0x8A2BE2

    @property
    def blue_violet(self) -> int:
        return 0x8A2BE2

    @property
    def blush(self) -> int:
        return 0xDE5D83

    @property
    def bole(self) -> int:
        return 0x79443B

    @property
    def bondi_blue(self) -> int:
        return 0x0095B6

    @property
    def bone(self) -> int:
        return 0xE3DAC9

    @property
    def boston_university_red(self) -> int:
        return 0xCC0000

    @property
    def bottle_green(self) -> int:
        return 0x006A4E

    @property
    def boysenberry(self) -> int:
        return 0x873260

    @property
    def brandeis_blue(self) -> int:
        return 0x0070FF

    @property
    def brass(self) -> int:
        return 0xB5A642

    @property
    def brick_red(self) -> int:
        return 0xCB4154

    @property
    def bright_cerulean(self) -> int:
        return 0x1DACD6

    @property
    def bright_green(self) -> int:
        return 0x66FF00

    @property
    def bright_lavender(self) -> int:
        return 0xBF94E4

    @property
    def bright_maroon(self) -> int:
        return 0xC32148

    @property
    def bright_pink(self) -> int:
        return 0xFF007F

    @property
    def bright_turquoise(self) -> int:
        return 0x08E8DE

    @property
    def bright_ube(self) -> int:
        return 0xD19FE8

    @property
    def brilliant_lavender(self) -> int:
        return 0xF4BBFF

    @property
    def brilliant_rose(self) -> int:
        return 0xFF55A3

    @property
    def brink_pink(self) -> int:
        return 0xFB607F

    @property
    def british_racing_green(self) -> int:
        return 0x004225

    @property
    def bronze(self) -> int:
        return 0xCD7F32

    @property
    def brown(self) -> int:
        return 0xA52A2A

    @property
    def bubble_gum(self) -> int:
        return 0xFFC1CC

    @property
    def bubbles(self) -> int:
        return 0xE7FEFF

    @property
    def buff(self) -> int:
        return 0xF0DC82

    @property
    def bulgarian_rose(self) -> int:
        return 0x480607

    @property
    def burgundy(self) -> int:
        return 0x800020

    @property
    def burlywood(self) -> int:
        return 0xDEB887

    @property
    def burnt_orange(self) -> int:
        return 0xCC5500

    @property
    def burnt_sienna(self) -> int:
        return 0xE97451

    @property
    def burnt_umber(self) -> int:
        return 0x8A3324

    @property
    def byzantine(self) -> int:
        return 0xBD33A4

    @property
    def byzantium(self) -> int:
        return 0x702963

    @property
    def cg_blue(self) -> int:
        return 0x007AA5

    @property
    def cg_red(self) -> int:
        return 0xE03C31

    @property
    def cadet(self) -> int:
        return 0x536872

    @property
    def cadet_blue(self) -> int:
        return 0x5F9EA0

    @property
    def cadet_grey(self) -> int:
        return 0x91A3B0

    @property
    def cadmium_green(self) -> int:
        return 0x006B3C

    @property
    def cadmium_orange(self) -> int:
        return 0xED872D

    @property
    def cadmium_red(self) -> int:
        return 0xE30022

    @property
    def cadmium_yellow(self) -> int:
        return 0xFFF600

    @property
    def cafe_au_lait(self) -> int:
        return 0xA67B5B

    @property
    def cafe_noir(self) -> int:
        return 0x4B3621

    @property
    def cal_poly_pomona_green(self) -> int:
        return 0x1E4D2B

    @property
    def cambridge_blue(self) -> int:
        return 0xA3C1AD

    @property
    def camel(self) -> int:
        return 0xC19A6B

    @property
    def camouflage_green(self) -> int:
        return 0x78866B

    @property
    def canary(self) -> int:
        return 0xFFFF99

    @property
    def canary_yellow(self) -> int:
        return 0xFFEF00

    @property
    def candy_apple_red(self) -> int:
        return 0xFF0800

    @property
    def candy_pink(self) -> int:
        return 0xE4717A

    @property
    def capri(self) -> int:
        return 0x00BFFF

    @property
    def caput_mortuum(self) -> int:
        return 0x592720

    @property
    def cardinal(self) -> int:
        return 0xC41E3A

    @property
    def caribbean_green(self) -> int:
        return 0x00CC99

    @property
    def carmine(self) -> int:
        return 0xFF0040

    @property
    def carmine_pink(self) -> int:
        return 0xEB4C42

    @property
    def carmine_red(self) -> int:
        return 0xFF0038

    @property
    def carnation_pink(self) -> int:
        return 0xFFA6C9

    @property
    def carnelian(self) -> int:
        return 0xB31B1B

    @property
    def carolina_blue(self) -> int:
        return 0x99BADD

    @property
    def carrot_orange(self) -> int:
        return 0xED9121

    @property
    def celadon(self) -> int:
        return 0xACE1AF

    @property
    def celeste(self) -> int:
        return 0xB2FFF

    @property
    def celestial_blue(self) -> int:
        return 0x4997D0

    @property
    def cerise(self) -> int:
        return 0xDE3163

    @property
    def cerise_pink(self) -> int:
        return 0xEC3B83

    @property
    def cerulean(self) -> int:
        return 0x007BA7

    @property
    def cerulean_blue(self) -> int:
        return 0x2A52BE

    @property
    def chamoisee(self) -> int:
        return 0xA0785A

    @property
    def champagne(self) -> int:
        return 0xFAD6A5

    @property
    def charcoal(self) -> int:
        return 0x36454F

    @property
    def chartreuse(self) -> int:
        return 0x7FFF00

    @property
    def cherry(self) -> int:
        return 0xDE3163

    @property
    def cherry_blossom_pink(self) -> int:
        return 0xFFB7C5

    @property
    def chestnut(self) -> int:
        return 0xCD5C5C

    @property
    def chocolate(self) -> int:
        return 0xD2691E

    @property
    def chrome_yellow(self) -> int:
        return 0xFFA700

    @property
    def cinereous(self) -> int:
        return 0x98817B

    @property
    def cinnabar(self) -> int:
        return 0xE34234

    @property
    def cinnamon(self) -> int:
        return 0xD2691E

    @property
    def citrine(self) -> int:
        return 0xE4D00A

    @property
    def classic_rose(self) -> int:
        return 0xFBCCE7

    @property
    def cobalt(self) -> int:
        return 0x0047AB

    @property
    def cocoa_brown(self) -> int:
        return 0xD2691E

    @property
    def coffee(self) -> int:
        return 0x6F4E37

    @property
    def columbia_blue(self) -> int:
        return 0x9BDDFF

    @property
    def cool_black(self) -> int:
        return 0x002E63

    @property
    def cool_grey(self) -> int:
        return 0x8C92AC

    @property
    def copper(self) -> int:
        return 0xB87333

    @property
    def copper_rose(self) -> int:
        return 0x996666

    @property
    def coquelicot(self) -> int:
        return 0xFF3800

    @property
    def coral(self) -> int:
        return 0xFF7F50

    @property
    def coral_pink(self) -> int:
        return 0xF88379

    @property
    def coral_red(self) -> int:
        return 0xFF4040

    @property
    def cordovan(self) -> int:
        return 0x893F45

    @property
    def corn(self) -> int:
        return 0xFBEC5D

    @property
    def cornell_red(self) -> int:
        return 0xB31B1B

    @property
    def cornflower(self) -> int:
        return 0x9ACEEB

    @property
    def cornflower_blue(self) -> int:
        return 0x6495ED

    @property
    def cornsilk(self) -> int:
        return 0xFFF8DC

    @property
    def cosmic_latte(self) -> int:
        return 0xFFF8E7

    @property
    def cotton_candy(self) -> int:
        return 0xFFBCD9

    @property
    def cream(self) -> int:
        return 0xFFFDD0

    @property
    def crimson(self) -> int:
        return 0xDC143C

    @property
    def crimson_red(self) -> int:
        return 0x990000

    @property
    def crimson_glory(self) -> int:
        return 0xBE0032

    @property
    def cyan(self) -> int:
        return 0x00FFFF

    @property
    def caffodil(self) -> int:
        return 0xFFFF31

    @property
    def dandelion(self) -> int:
        return 0xF0E130

    @property
    def dark_blue(self) -> int:
        return 0x00008B

    @property
    def dark_brown(self) -> int:
        return 0x654321

    @property
    def dark_byzantium(self) -> int:
        return 0x5D3954

    @property
    def dark_candy_apple_red(self) -> int:
        return 0xA40000

    @property
    def dark_cerulean(self) -> int:
        return 0x08457E

    @property
    def dark_chestnut(self) -> int:
        return 0x986960

    @property
    def dark_coral(self) -> int:
        return 0xCD5B45

    @property
    def dark_cyan(self) -> int:
        return 0x008B8B

    @property
    def dark_electric_blue(self) -> int:
        return 0x536878

    @property
    def dark_goldenrod(self) -> int:
        return 0xB8860B

    @property
    def dark_gray(self) -> int:
        return 0xA9A9A9

    @property
    def dark_green(self) -> int:
        return 0x013220

    @property
    def dark_jungle_green(self) -> int:
        return 0x1A2421

    @property
    def dark_khaki(self) -> int:
        return 0xBDB76B

    @property
    def dark_lava(self) -> int:
        return 0x483C32

    @property
    def dark_lavender(self) -> int:
        return 0x734F96

    @property
    def dark_magenta(self) -> int:
        return 0x8B008B

    @property
    def dark_midnight_blue(self) -> int:
        return 0x003366

    @property
    def dark_olive_green(self) -> int:
        return 0x556B2F

    @property
    def dark_orange(self) -> int:
        return 0xFF8C00

    @property
    def dark_orchid(self) -> int:
        return 0x9932CC

    @property
    def dark_pastel_blue(self) -> int:
        return 0x779ECB

    @property
    def dark_pastel_green(self) -> int:
        return 0x03C03C

    @property
    def dark_pastel_purple(self) -> int:
        return 0x966FD6

    @property
    def dark_pastel_red(self) -> int:
        return 0xC23B22

    @property
    def dark_pink(self) -> int:
        return 0xE75480

    @property
    def dark_powder_blue(self) -> int:
        return 0x003399

    @property
    def dark_raspberry(self) -> int:
        return 0x872657

    @property
    def dark_red(self) -> int:
        return 0x8B0000

    @property
    def dark_salmon(self) -> int:
        return 0xE9967A

    @property
    def dark_scarlet(self) -> int:
        return 0x560319

    @property
    def dark_sea_green(self) -> int:
        return 0x8FBC8F

    @property
    def dark_sienna(self) -> int:
        return 0x3C1414

    @property
    def dark_slate_blue(self) -> int:
        return 0x483D8B

    @property
    def dark_slate_gray(self) -> int:
        return 0x2F4F4F

    @property
    def dark_spring_green(self) -> int:
        return 0x177245

    @property
    def dark_tan(self) -> int:
        return 0x918151

    @property
    def dark_tangerine(self) -> int:
        return 0xFFA812

    @property
    def dark_taupe(self) -> int:
        return 0x483C32

    @property
    def dark_terra_cotta(self) -> int:
        return 0xCC4E5C

    @property
    def dark_turquoise(self) -> int:
        return 0x00CED1

    @property
    def dark_violet(self) -> int:
        return 0x9400D3

    @property
    def dartmouth_green(self) -> int:
        return 0x00693E

    @property
    def davy_grey(self) -> int:
        return 0x555555

    @property
    def debian_red(self) -> int:
        return 0xD70A53

    @property
    def deep_carmine(self) -> int:
        return 0xA9203E

    @property
    def deep_carmine_pink(self) -> int:
        return 0xEF3038

    @property
    def deep_carrot_orange(self) -> int:
        return 0xE9692C

    @property
    def deep_cerise(self) -> int:
        return 0xDA3287

    @property
    def deep_champagne(self) -> int:
        return 0xFAD6A5

    @property
    def deep_chestnut(self) -> int:
        return 0xB94E48

    @property
    def deep_coffee(self) -> int:
        return 0x704241

    @property
    def deep_fuchsia(self) -> int:
        return 0xC154C1

    @property
    def deep_jungle_green(self) -> int:
        return 0x004B49

    @property
    def deep_lilac(self) -> int:
        return 0x9955BB

    @property
    def deep_magenta(self) -> int:
        return 0xCC00CC

    @property
    def deep_peach(self) -> int:
        return 0xFFCBA4

    @property
    def deep_pink(self) -> int:
        return 0xFF1493

    @property
    def deep_saffron(self) -> int:
        return 0xFF9933

    @property
    def deep_sky_blue(self) -> int:
        return 0x00BFFF

    @property
    def denim(self) -> int:
        return 0x1560BD

    @property
    def desert(self) -> int:
        return 0xC19A6B

    @property
    def desert_sand(self) -> int:
        return 0xEDC9AF

    @property
    def dim_gray(self) -> int:
        return 0x696969

    @property
    def dodger_blue(self) -> int:
        return 0x1E90FF

    @property
    def dogwood_rose(self) -> int:
        return 0xD71868

    @property
    def dollar_bill(self) -> int:
        return 0x85BB65

    @property
    def drab(self) -> int:
        return 0x967117

    @property
    def duke_blue(self) -> int:
        return 0x00009C

    @property
    def earth_yellow(self) -> int:
        return 0xE1A95F

    @property
    def ecru(self) -> int:
        return 0xC2B280

    @property
    def eggplant(self) -> int:
        return 0x614051

    @property
    def eggshell(self) -> int:
        return 0xF0EAD6

    @property
    def egyptian_blue(self) -> int:
        return 0x1034A6

    @property
    def electric_blue(self) -> int:
        return 0x7DF9FF

    @property
    def electric_crimson(self) -> int:
        return 0xFF003F

    @property
    def electric_cyan(self) -> int:
        return 0x00FFFF

    @property
    def electric_green(self) -> int:
        return 0x00FF00

    @property
    def electric_indigo(self) -> int:
        return 0x6F00FF

    @property
    def electric_lavender(self) -> int:
        return 0xF4BBFF

    @property
    def electric_lime(self) -> int:
        return 0xCCFF00

    @property
    def electric_purple(self) -> int:
        return 0xBF00FF

    @property
    def electric_ultramarine(self) -> int:
        return 0x3F00FF

    @property
    def electric_violet(self) -> int:
        return 0x8F00FF

    @property
    def electric_yellow(self) -> int:
        return 0xFFFF00

    @property
    def emerald(self) -> int:
        return 0x50C878

    @property
    def eton_blue(self) -> int:
        return 0x96C8A2

    @property
    def fallow(self) -> int:
        return 0xC19A6B

    @property
    def falu_red(self) -> int:
        return 0x801818

    @property
    def famous(self) -> int:
        return 0xFF00FF

    @property
    def fandango(self) -> int:
        return 0xB53389

    @property
    def fashion_fuchsia(self) -> int:
        return 0xF400A1

    @property
    def fawn(self) -> int:
        return 0xE5AA70

    @property
    def feldgrau(self) -> int:
        return 0x4D5D53

    @property
    def fern(self) -> int:
        return 0x71BC78

    @property
    def fern_green(self) -> int:
        return 0x4F7942

    @property
    def ferrari_red(self) -> int:
        return 0xFF2800

    @property
    def field_drab(self) -> int:
        return 0x6C541E

    @property
    def fire_engine_red(self) -> int:
        return 0xCE2029

    @property
    def firebrick(self) -> int:
        return 0xB22222

    @property
    def flame(self) -> int:
        return 0xE25822

    @property
    def flamingo_pink(self) -> int:
        return 0xFC8EAC

    @property
    def flavescent(self) -> int:
        return 0xF7E98E

    @property
    def flax(self) -> int:
        return 0xEEDC82

    @property
    def floral_white(self) -> int:
        return 0xFFFAF0

    @property
    def fluorescent_orange(self) -> int:
        return 0xFFBF00

    @property
    def fluorescent_pink(self) -> int:
        return 0xFF1493

    @property
    def fluorescent_yellow(self) -> int:
        return 0xCCFF00

    @property
    def folly(self) -> int:
        return 0xFF004F

    @property
    def forest_green(self) -> int:
        return 0x228B22

    @property
    def french_beige(self) -> int:
        return 0xA67B5B

    @property
    def french_blue(self) -> int:
        return 0x0072BB

    @property
    def french_lilac(self) -> int:
        return 0x86608E

    @property
    def french_rose(self) -> int:
        return 0xF64A8A

    @property
    def fuchsia(self) -> int:
        return 0xFF00FF

    @property
    def fuchsia_pink(self) -> int:
        return 0xFF77FF

    @property
    def fulvous(self) -> int:
        return 0xE48400

    @property
    def fuzzy_wuzzy(self) -> int:
        return 0xCC6666

    @property
    def gainsboro(self) -> int:
        return 0xDCDCDC

    @property
    def gamboge(self) -> int:
        return 0xE49B0F

    @property
    def ghost_white(self) -> int:
        return 0xF8F8FF

    @property
    def ginger(self) -> int:
        return 0xB06500

    @property
    def glaucous(self) -> int:
        return 0x6082B6

    @property
    def glitter(self) -> int:
        return 0xE6E8FA

    @property
    def gold(self) -> int:
        return 0xFFD700

    @property
    def golden_brown(self) -> int:
        return 0x996515

    @property
    def golden_poppy(self) -> int:
        return 0xFCC200

    @property
    def golden_yellow(self) -> int:
        return 0xFFDF00

    @property
    def goldenrod(self) -> int:
        return 0xDAA520

    @property
    def granny_smith_apple(self) -> int:
        return 0xA8E4A0

    @property
    def gray(self) -> int:
        return 0x808080

    @property
    def gray_asparagus(self) -> int:
        return 0x465945

    @property
    def green(self) -> int:
        return 0x00FF00

    @property
    def green_blue(self) -> int:
        return 0x1164B4

    @property
    def green_yellow(self) -> int:
        return 0xADFF2F

    @property
    def grullo(self) -> int:
        return 0xA99A86

    @property
    def guppie_green(self) -> int:
        return 0x00FF7F

    @property
    def halaya_ube(self) -> int:
        return 0x663854

    @property
    def han_blue(self) -> int:
        return 0x446CCF

    @property
    def han_purple(self) -> int:
        return 0x5218FA

    @property
    def hansa_yellow(self) -> int:
        return 0xE9D66B

    @property
    def harlequin(self) -> int:
        return 0x3FFF00

    @property
    def harvard_crimson(self) -> int:
        return 0xC90016

    @property
    def harvest_gold(self) -> int:
        return 0xDA9100

    @property
    def heart_gold(self) -> int:
        return 0x808000

    @property
    def heliotrope(self) -> int:
        return 0xDF73FF

    @property
    def hollywood_cerise(self) -> int:
        return 0xF400A1

    @property
    def honeydew(self) -> int:
        return 0xF0FFF0

    @property
    def hooker_green(self) -> int:
        return 0x49796B

    @property
    def hot_magenta(self) -> int:
        return 0xFF1DCE

    @property
    def hot_pink(self) -> int:
        return 0xFF69B4

    @property
    def hunter_green(self) -> int:
        return 0x355E3B

    @property
    def icterine(self) -> int:
        return 0xFCF75E

    @property
    def inchworm(self) -> int:
        return 0xB2EC5D

    @property
    def india_green(self) -> int:
        return 0x138808

    @property
    def indian_red(self) -> int:
        return 0xCD5C5C

    @property
    def indian_yellow(self) -> int:
        return 0xE3A857

    @property
    def indigo(self) -> int:
        return 0x4B0082

    @property
    def international_klein_blue(self) -> int:
        return 0x002FA7

    @property
    def international_orange(self) -> int:
        return 0xFF4F00

    @property
    def iris(self) -> int:
        return 0x5A4FCF

    @property
    def isabelline(self) -> int:
        return 0xF4F0EC

    @property
    def islamic_green(self) -> int:
        return 0x009000

    @property
    def ivory(self) -> int:
        return 0xFFFFF0

    @property
    def jade(self) -> int:
        return 0x00A86B

    @property
    def jasmine(self) -> int:
        return 0xF8DE7E

    @property
    def jasper(self) -> int:
        return 0xD73B3E

    @property
    def jazzberry_jam(self) -> int:
        return 0xA50B5E

    @property
    def jonquil(self) -> int:
        return 0xFADA5E

    @property
    def june_bud(self) -> int:
        return 0xBDDA57

    @property
    def jungle_green(self) -> int:
        return 0x29AB87

    @property
    def ku_crimson(self) -> int:
        return 0xE8000D

    @property
    def kelly_green(self) -> int:
        return 0x4CBB17

    @property
    def khaki(self) -> int:
        return 0xC3B091

    @property
    def la_salle_green(self) -> int:
        return 0x087830

    @property
    def languid_lavender(self) -> int:
        return 0xD6CADD

    @property
    def lapis_lazuli(self) -> int:
        return 0x26619C

    @property
    def laser_lemon(self) -> int:
        return 0xFEFE22

    @property
    def laurel_green(self) -> int:
        return 0xA9BA9D

    @property
    def lava(self) -> int:
        return 0xCF1020

    @property
    def lavender(self) -> int:
        return 0xE6E6FA

    @property
    def lavender_blue(self) -> int:
        return 0xCCCCFF

    @property
    def lavender_blush(self) -> int:
        return 0xFFF0F5

    @property
    def lavender_gray(self) -> int:
        return 0xC4C3D0

    @property
    def lavender_indigo(self) -> int:
        return 0x9457EB

    @property
    def lavender_magenta(self) -> int:
        return 0xEE82EE

    @property
    def lavender_mist(self) -> int:
        return 0xE6E6FA

    @property
    def lavender_pink(self) -> int:
        return 0xFBAED2

    @property
    def lavender_purple(self) -> int:
        return 0x967BB6

    @property
    def lavender_rose(self) -> int:
        return 0xFBA0E3

    @property
    def lawn_green(self) -> int:
        return 0x7CFC00

    @property
    def lemon(self) -> int:
        return 0xFFF700

    @property
    def lemon_yellow(self) -> int:
        return 0xFFF44F

    @property
    def lemon_chiffon(self) -> int:
        return 0xFFFACD

    @property
    def lemon_lime(self) -> int:
        return 0xBFFF00

    @property
    def light_crimson(self) -> int:
        return 0xF56991

    @property
    def light_thulian_pink(self) -> int:
        return 0xE68FAC

    @property
    def light_apricot(self) -> int:
        return 0xFDD5B1

    @property
    def light_blue(self) -> int:
        return 0xADD8E6

    @property
    def light_brown(self) -> int:
        return 0xB5651D

    @property
    def light_carmine_pink(self) -> int:
        return 0xE66771

    @property
    def light_coral(self) -> int:
        return 0xF08080

    @property
    def light_cornflower_blue(self) -> int:
        return 0x93CCEA

    @property
    def light_cyan(self) -> int:
        return 0xE0FFFF

    @property
    def light_fuchsia_pink(self) -> int:
        return 0xF984EF

    @property
    def light_goldenrod_yellow(self) -> int:
        return 0xFAFAD2

    @property
    def light_gray(self) -> int:
        return 0xD3D3D3

    @property
    def light_green(self) -> int:
        return 0x90EE90

    @property
    def light_khaki(self) -> int:
        return 0xF0E68C

    @property
    def light_pastel_purple(self) -> int:
        return 0xB19CD9

    @property
    def light_pink(self) -> int:
        return 0xFFB6C1

    @property
    def light_salmon(self) -> int:
        return 0xFFA07A

    @property
    def light_salmon_pink(self) -> int:
        return 0xFF9999

    @property
    def light_sea_green(self) -> int:
        return 0x20B2AA

    @property
    def light_sky_blue(self) -> int:
        return 0x87CEFA

    @property
    def light_slate_gray(self) -> int:
        return 0x778899

    @property
    def light_taupe(self) -> int:
        return 0xB38B6D

    @property
    def light_yellow(self) -> int:
        return 0xFFFFED

    @property
    def lilac(self) -> int:
        return 0xC8A2C8

    @property
    def lime(self) -> int:
        return 0xBFFF00

    @property
    def lime_green(self) -> int:
        return 0x32CD32

    @property
    def lincoln_green(self) -> int:
        return 0x195905

    @property
    def linen(self) -> int:
        return 0xFAF0E6

    @property
    def lion(self) -> int:
        return 0xC19A6B

    @property
    def liver(self) -> int:
        return 0x534B4F

    @property
    def lust(self) -> int:
        return 0xE62020

    @property
    def msu_green(self) -> int:
        return 0x18453B

    @property
    def macaroni_and_cheese(self) -> int:
        return 0xFFBD88

    @property
    def magenta(self) -> int:
        return 0xFF00FF

    @property
    def magic_mint(self) -> int:
        return 0xAAF0D1

    @property
    def magnolia(self) -> int:
        return 0xF8F4FF

    @property
    def mahogany(self) -> int:
        return 0xC04000

    @property
    def maize(self) -> int:
        return 0xFBEC5D

    @property
    def majorelle_blue(self) -> int:
        return 0x6050DC

    @property
    def malachite(self) -> int:
        return 0x0BDA51

    @property
    def manatee(self) -> int:
        return 0x979AAA

    @property
    def mango_tango(self) -> int:
        return 0xFF8243

    @property
    def mantis(self) -> int:
        return 0x74C365

    @property
    def maroon(self) -> int:
        return 0x800000

    @property
    def mauve(self) -> int:
        return 0xE0B0FF

    @property
    def mauve_taupe(self) -> int:
        return 0x915F6D

    @property
    def mauvelous(self) -> int:
        return 0xEF98AA

    @property
    def maya_blue(self) -> int:
        return 0x73C2FB

    @property
    def meat_brown(self) -> int:
        return 0xE5B73B

    @property
    def medium_persian_blue(self) -> int:
        return 0x0067A5

    @property
    def medium_aquamarine(self) -> int:
        return 0x66DDAA

    @property
    def medium_blue(self) -> int:
        return 0x0000CD

    @property
    def medium_candy_apple_red(self) -> int:
        return 0xE2062C

    @property
    def medium_carmine(self) -> int:
        return 0xAF4035

    @property
    def medium_champagne(self) -> int:
        return 0xF3E5AB

    @property
    def medium_electric_blue(self) -> int:
        return 0x035096

    @property
    def medium_jungle_green(self) -> int:
        return 0x1C352D

    @property
    def medium_lavender_magenta(self) -> int:
        return 0xDDA0DD

    @property
    def medium_orchid(self) -> int:
        return 0xBA55D3

    @property
    def medium_purple(self) -> int:
        return 0x9370DB

    @property
    def medium_red_violet(self) -> int:
        return 0xBB3385

    @property
    def medium_sea_green(self) -> int:
        return 0x3CB371

    @property
    def medium_slate_blue(self) -> int:
        return 0x7B68EE

    @property
    def medium_spring_bud(self) -> int:
        return 0xC9DC87

    @property
    def medium_spring_green(self) -> int:
        return 0x00FA9A

    @property
    def medium_taupe(self) -> int:
        return 0x674C47

    @property
    def medium_teal_blue(self) -> int:
        return 0x0054B4

    @property
    def medium_turquoise(self) -> int:
        return 0x48D1CC

    @property
    def medium_violet_red(self) -> int:
        return 0xC71585

    @property
    def melon(self) -> int:
        return 0xFDBCB4

    @property
    def midnight_blue(self) -> int:
        return 0x191970

    @property
    def midnight_green(self) -> int:
        return 0x004953

    @property
    def mikado_yellow(self) -> int:
        return 0xFFC40C

    @property
    def mint(self) -> int:
        return 0x3EB489

    @property
    def mint_cream(self) -> int:
        return 0xF5FFFA

    @property
    def mint_green(self) -> int:
        return 0x98FF98

    @property
    def misty_rose(self) -> int:
        return 0xFFE4E1

    @property
    def moccasin(self) -> int:
        return 0xFAEBD7

    @property
    def mode_beige(self) -> int:
        return 0x967117

    @property
    def moonstone_blue(self) -> int:
        return 0x73A9C2

    @property
    def mordant_red_19(self) -> int:
        return 0xAE0C00

    @property
    def moss_green(self) -> int:
        return 0xADDFAD

    @property
    def mountain_meadow(self) -> int:
        return 0x30BA8F

    @property
    def mountbatten_pink(self) -> int:
        return 0x997A8D

    @property
    def mulberry(self) -> int:
        return 0xC54B8C

    @property
    def munsell(self) -> int:
        return 0xF2F3F4

    @property
    def mustard(self) -> int:
        return 0xFFDB58

    @property
    def myrtle(self) -> int:
        return 0x21421E

    @property
    def nadeshiko_pink(self) -> int:
        return 0xF6ADC6

    @property
    def napier_green(self) -> int:
        return 0x2A8000

    @property
    def naples_yellow(self) -> int:
        return 0xFADA5E

    @property
    def navajo_white(self) -> int:
        return 0xFFDEAD

    @property
    def navy_blue(self) -> int:
        return 0x000080

    @property
    def neon_carrot(self) -> int:
        return 0xFFA343

    @property
    def neon_fuchsia(self) -> int:
        return 0xFE59C2

    @property
    def neon_green(self) -> int:
        return 0x39FF14

    @property
    def non_photo_blue(self) -> int:
        return 0xA4DDED

    @property
    def north_texas_green(self) -> int:
        return 0x059033

    @property
    def ocean_boat_blue(self) -> int:
        return 0x0077BE

    @property
    def ochre(self) -> int:
        return 0xCC7722

    @property
    def office_green(self) -> int:
        return 0x008000

    @property
    def old_gold(self) -> int:
        return 0xCFB53B

    @property
    def old_lace(self) -> int:
        return 0xFDF5E6

    @property
    def old_lavender(self) -> int:
        return 0x796878

    @property
    def old_mauve(self) -> int:
        return 0x673147

    @property
    def old_rose(self) -> int:
        return 0xC08081

    @property
    def olive(self) -> int:
        return 0x808000

    @property
    def olive_drab(self) -> int:
        return 0x6B8E23

    @property
    def olive_green(self) -> int:
        return 0xBAB86C

    @property
    def olivine(self) -> int:
        return 0x9AB973

    @property
    def onyx(self) -> int:
        return 0x0F0F0F

    @property
    def opera_mauve(self) -> int:
        return 0xB784A7

    @property
    def orange(self) -> int:
        return 0xFFA500

    @property
    def orange_yellow(self) -> int:
        return 0xF8D568

    @property
    def orange_peel(self) -> int:
        return 0xFF9F00

    @property
    def orange_red(self) -> int:
        return 0xFF4500

    @property
    def orchid(self) -> int:
        return 0xDA70D6

    @property
    def otter_brown(self) -> int:
        return 0x654321

    @property
    def outer_space(self) -> int:
        return 0x414A4C

    @property
    def outrageous_orange(self) -> int:
        return 0xFF6E4A

    @property
    def oxford_blue(self) -> int:
        return 0x002147

    @property
    def pacific_blue(self) -> int:
        return 0x1CA9C9

    @property
    def pakistan_green(self) -> int:
        return 0x006600

    @property
    def palatinate_blue(self) -> int:
        return 0x273BE2

    @property
    def palatinate_purple(self) -> int:
        return 0x682860

    @property
    def pale_aqua(self) -> int:
        return 0xBCD4E6

    @property
    def pale_blue(self) -> int:
        return 0xAFEEEE

    @property
    def pale_brown(self) -> int:
        return 0x987654

    @property
    def pale_carmine(self) -> int:
        return 0xAF4035

    @property
    def pale_cerulean(self) -> int:
        return 0x9BC4E2

    @property
    def pale_chestnut(self) -> int:
        return 0xDDADAF

    @property
    def pale_copper(self) -> int:
        return 0xDA8A67

    @property
    def pale_cornflower_blue(self) -> int:
        return 0xABCDEF

    @property
    def pale_gold(self) -> int:
        return 0xE6BE8A

    @property
    def pale_goldenrod(self) -> int:
        return 0xEEE8AA

    @property
    def pale_green(self) -> int:
        return 0x98FB98

    @property
    def pale_lavender(self) -> int:
        return 0xDCD0FF

    @property
    def pale_magenta(self) -> int:
        return 0xF984E5

    @property
    def pale_pink(self) -> int:
        return 0xFADADD

    @property
    def pale_plum(self) -> int:
        return 0xDDA0DD

    @property
    def pale_red_violet(self) -> int:
        return 0xDB7093

    @property
    def pale_robin_egg_blue(self) -> int:
        return 0x96DED1

    @property
    def pale_silver(self) -> int:
        return 0xC9C0BB

    @property
    def pale_spring_bud(self) -> int:
        return 0xECEBBD

    @property
    def pale_taupe(self) -> int:
        return 0xBC987E

    @property
    def pale_violet_red(self) -> int:
        return 0xDB7093

    @property
    def pansy_purple(self) -> int:
        return 0x78184A

    @property
    def papaya_whip(self) -> int:
        return 0xFFEFD5

    @property
    def paris_green(self) -> int:
        return 0x50C878

    @property
    def pastel_blue(self) -> int:
        return 0xAEC6CF

    @property
    def pastel_brown(self) -> int:
        return 0x836953

    @property
    def pastel_gray(self) -> int:
        return 0xCFCFC4

    @property
    def pastel_green(self) -> int:
        return 0x77DD77

    @property
    def pastel_magenta(self) -> int:
        return 0xF49AC2

    @property
    def pastel_orange(self) -> int:
        return 0xFFB347

    @property
    def pastel_pink(self) -> int:
        return 0xFFD1DC

    @property
    def pastel_purple(self) -> int:
        return 0xB39EB5

    @property
    def pastel_red(self) -> int:
        return 0xFF6961

    @property
    def pastel_violet(self) -> int:
        return 0xCB99C9

    @property
    def pastel_yellow(self) -> int:
        return 0xFDFD96

    @property
    def patriarch(self) -> int:
        return 0x800080

    @property
    def payne_grey(self) -> int:
        return 0x536878

    @property
    def peach(self) -> int:
        return 0xFFE5B4

    @property
    def peach_puff(self) -> int:
        return 0xFFDAB9

    @property
    def peach_yellow(self) -> int:
        return 0xFADFAD

    @property
    def pear(self) -> int:
        return 0xD1E231

    @property
    def pearl(self) -> int:
        return 0xEAE0C8

    @property
    def pearl_aqua(self) -> int:
        return 0x88D8C0

    @property
    def peridot(self) -> int:
        return 0xE6E200

    @property
    def periwinkle(self) -> int:
        return 0xCCCCFF

    @property
    def persian_blue(self) -> int:
        return 0x1C39BB

    @property
    def persian_indigo(self) -> int:
        return 0x32127A

    @property
    def persian_orange(self) -> int:
        return 0xD99058

    @property
    def persian_pink(self) -> int:
        return 0xF77FBE

    @property
    def persian_plum(self) -> int:
        return 0x701C1C

    @property
    def persian_red(self) -> int:
        return 0xCC3333

    @property
    def persian_rose(self) -> int:
        return 0xFE28A2

    @property
    def phlox(self) -> int:
        return 0xDF00FF

    @property
    def phthalo_blue(self) -> int:
        return 0x000F89

    @property
    def phthalo_green(self) -> int:
        return 0x123524

    @property
    def piggy_pink(self) -> int:
        return 0xFDDDE6

    @property
    def pine_green(self) -> int:
        return 0x01796F

    @property
    def pink(self) -> int:
        return 0xFFC0CB

    @property
    def pink_flamingo(self) -> int:
        return 0xFC74FD

    @property
    def pink_sherbet(self) -> int:
        return 0xF78FA7

    @property
    def pink_pearl(self) -> int:
        return 0xE7ACCF

    @property
    def pistachio(self) -> int:
        return 0x93C572

    @property
    def platinum(self) -> int:
        return 0xE5E4E2

    @property
    def plum(self) -> int:
        return 0xDDA0DD

    @property
    def portland_orange(self) -> int:
        return 0xFF5A36

    @property
    def powder_blue(self) -> int:
        return 0xB0E0E6

    @property
    def princeton_orange(self) -> int:
        return 0xFF8F00

    @property
    def prussian_blue(self) -> int:
        return 0x003153

    @property
    def psychedelic_purple(self) -> int:
        return 0xDF00FF

    @property
    def puce(self) -> int:
        return 0xCC8899

    @property
    def pumpkin(self) -> int:
        return 0xFF7518

    @property
    def purple(self) -> int:
        return 0x800080

    @property
    def purple_heart(self) -> int:
        return 0x69359C

    @property
    def purple_mountains_majesty(self) -> int:
        return 0x9D81BA

    @property
    def purple_mountain_majesty(self) -> int:
        return 0x9678B6

    @property
    def purple_pizzazz(self) -> int:
        return 0xFE4EDA

    @property
    def purple_taupe(self) -> int:
        return 0x50404D

    @property
    def rackley(self) -> int:
        return 0x5D8AA8

    @property
    def radical_red(self) -> int:
        return 0xFF355E

    @property
    def raspberry(self) -> int:
        return 0xE30B5D

    @property
    def raspberry_glace(self) -> int:
        return 0x915F6D

    @property
    def raspberry_pink(self) -> int:
        return 0xE25098

    @property
    def raspberry_rose(self) -> int:
        return 0xB3446C

    @property
    def raw_sienna(self) -> int:
        return 0xD68A59

    @property
    def razzle_dazzle_rose(self) -> int:
        return 0xFF33CC

    @property
    def razzmatazz(self) -> int:
        return 0xE3256B

    @property
    def red(self) -> int:
        return 0xFF0000

    @property
    def red_orange(self) -> int:
        return 0xFF5349

    @property
    def red_brown(self) -> int:
        return 0xA52A2A

    @property
    def red_violet(self) -> int:
        return 0xC71585

    @property
    def rich_black(self) -> int:
        return 0x004040

    @property
    def rich_carmine(self) -> int:
        return 0xD70040

    @property
    def rich_electric_blue(self) -> int:
        return 0x0892D0

    @property
    def rich_lilac(self) -> int:
        return 0xB666D2

    @property
    def rich_maroon(self) -> int:
        return 0xB03060

    @property
    def rifle_green(self) -> int:
        return 0x414833

    @property
    def robins_egg_blue(self) -> int:
        return 0x1FCECB

    @property
    def rose(self) -> int:
        return 0xFF007F

    @property
    def rose_bonbon(self) -> int:
        return 0xF9429E

    @property
    def rose_ebony(self) -> int:
        return 0x674846

    @property
    def rose_gold(self) -> int:
        return 0xB76E79

    @property
    def rose_madder(self) -> int:
        return 0xE32636

    @property
    def rose_pink(self) -> int:
        return 0xFF66CC

    @property
    def rose_quartz(self) -> int:
        return 0xAA98A9

    @property
    def rose_taupe(self) -> int:
        return 0x905D5D

    @property
    def rose_vale(self) -> int:
        return 0xAB4E52

    @property
    def rosewood(self) -> int:
        return 0x65000B

    @property
    def rosso_corsa(self) -> int:
        return 0xD40000

    @property
    def rosy_brown(self) -> int:
        return 0xBC8F8F

    @property
    def royal_azure(self) -> int:
        return 0x0038A8

    @property
    def royal_blue(self) -> int:
        return 0x4169E1

    @property
    def royal_fuchsia(self) -> int:
        return 0xCA2C92

    @property
    def royal_purple(self) -> int:
        return 0x7851A9

    @property
    def ruby(self) -> int:
        return 0xE0115F

    @property
    def ruddy(self) -> int:
        return 0xFF0028

    @property
    def ruddy_brown(self) -> int:
        return 0xBB6528

    @property
    def ruddy_pink(self) -> int:
        return 0xE18E96

    @property
    def rufous(self) -> int:
        return 0xA81C07

    @property
    def russet(self) -> int:
        return 0x80461B

    @property
    def rust(self) -> int:
        return 0xB7410E

    @property
    def sacramento_state_green(self) -> int:
        return 0x00563F

    @property
    def saddle_brown(self) -> int:
        return 0x8B4513

    @property
    def safety_orange(self) -> int:
        return 0xFF6700

    @property
    def saffron(self) -> int:
        return 0xF4C430

    @property
    def saint_patrick_blue(self) -> int:
        return 0x23297A

    @property
    def salmon(self) -> int:
        return 0xFF8C69

    @property
    def salmon_pink(self) -> int:
        return 0xFF91A4

    @property
    def sand(self) -> int:
        return 0xC2B280

    @property
    def sand_dune(self) -> int:
        return 0x967117

    @property
    def sandstorm(self) -> int:
        return 0xECD540

    @property
    def sandy_brown(self) -> int:
        return 0xF4A460

    @property
    def sandy_taupe(self) -> int:
        return 0x967117

    @property
    def sap_green(self) -> int:
        return 0x507D2A

    @property
    def sapphire(self) -> int:
        return 0x0F52BA

    @property
    def satin_sheen_gold(self) -> int:
        return 0xCBA135

    @property
    def scarlet(self) -> int:
        return 0xFF2400

    @property
    def school_bus_yellow(self) -> int:
        return 0xFFD800

    @property
    def screamin_green(self) -> int:
        return 0x76FF7A

    @property
    def sea_blue(self) -> int:
        return 0x006994

    @property
    def sea_green(self) -> int:
        return 0x2E8B57

    @property
    def seal_brown(self) -> int:
        return 0x321414

    @property
    def seashell(self) -> int:
        return 0xFFF5EE

    @property
    def selective_yellow(self) -> int:
        return 0xFFBA00

    @property
    def sepia(self) -> int:
        return 0x704214

    @property
    def shadow(self) -> int:
        return 0x8A795D

    @property
    def shamrock(self) -> int:
        return 0x45CEA2

    @property
    def shamrock_green(self) -> int:
        return 0x009E60

    @property
    def shocking_pink(self) -> int:
        return 0xFC0FC0

    @property
    def sienna(self) -> int:
        return 0x882D17

    @property
    def silver(self) -> int:
        return 0xC0C0C0

    @property
    def sinopia(self) -> int:
        return 0xCB410B

    @property
    def skobeloff(self) -> int:
        return 0x007474

    @property
    def sky_blue(self) -> int:
        return 0x87CEEB

    @property
    def sky_magenta(self) -> int:
        return 0xCF71AF

    @property
    def slate_blue(self) -> int:
        return 0x6A5ACD

    @property
    def slate_gray(self) -> int:
        return 0x708090

    @property
    def smalt(self) -> int:
        return 0x003399

    @property
    def smokey_topaz(self) -> int:
        return 0x933D41

    @property
    def smoky_black(self) -> int:
        return 0x100C08

    @property
    def snow(self) -> int:
        return 0xFFFAFA

    @property
    def spiro_disco_ball(self) -> int:
        return 0x0FC0FC

    @property
    def spring_bud(self) -> int:
        return 0xA7FC00

    @property
    def spring_green(self) -> int:
        return 0x00FF7F

    @property
    def steel_blue(self) -> int:
        return 0x4682B4

    @property
    def stil_de_grain_yellow(self) -> int:
        return 0xFADA5E

    @property
    def stizza(self) -> int:
        return 0x990000

    @property
    def stormcloud(self) -> int:
        return 0x008080

    @property
    def intaw(self) -> int:
        return 0xE4D96F

    @property
    def sunglow(self) -> int:
        return 0xFFCC33

    @property
    def sunset(self) -> int:
        return 0xFAD6A5

    @property
    def sunset_orange(self) -> int:
        return 0xFD5E53

    @property
    def tan(self) -> int:
        return 0xD2B48C

    @property
    def tangerine_yellow(self) -> int:
        return 0xFFCC00

    @property
    def taupe(self) -> int:
        return 0x483C32

    @property
    def taupe_gray(self) -> int:
        return 0x8B8589

    @property
    def tawny(self) -> int:
        return 0xCD5700

    @property
    def tea_green(self) -> int:
        return 0xD0F0C0

    @property
    def tea_rose(self) -> int:
        return 0xF4C2C2

    @property
    def teal(self) -> int:
        return 0x008080

    @property
    def teal_blue(self) -> int:
        return 0x367588

    @property
    def teal_green(self) -> int:
        return 0x006D5B

    @property
    def terra_cotta(self) -> int:
        return 0xE2725B

    @property
    def thistle(self) -> int:
        return 0xD8BFD8

    @property
    def thulian_pink(self) -> int:
        return 0xDE6FA1

    @property
    def tickle_me_pink(self) -> int:
        return 0xFC89AC

    @property
    def tiffany_blue(self) -> int:
        return 0x0ABAB5

    @property
    def tiger_eye(self) -> int:
        return 0xE08D3C

    @property
    def timberwolf(self) -> int:
        return 0xDBD7D2

    @property
    def titanium_yellow(self) -> int:
        return 0xEEE600

    @property
    def tomato(self) -> int:
        return 0xFF6347

    @property
    def toolbox(self) -> int:
        return 0x746CC0

    @property
    def topaz(self) -> int:
        return 0xFFC87C

    @property
    def tractor_red(self) -> int:
        return 0xFD0E35

    @property
    def trolley_grey(self) -> int:
        return 0x808080

    @property
    def tropical_rain_forest(self) -> int:
        return 0x00755E

    @property
    def true_blue(self) -> int:
        return 0x0073CF

    @property
    def tufts_blue(self) -> int:
        return 0x417DC1

    @property
    def tumbleweed(self) -> int:
        return 0xDEAA88

    @property
    def turkish_rose(self) -> int:
        return 0xB57281

    @property
    def turquoise(self) -> int:
        return 0x30D5C8

    @property
    def turquoise_blue(self) -> int:
        return 0x00FFEF

    @property
    def turquoise_green(self) -> int:
        return 0xA0D6B4

    @property
    def tuscan_red(self) -> int:
        return 0x66424D

    @property
    def twilight_lavender(self) -> int:
        return 0x8A496B

    @property
    def tyrian_purple(self) -> int:
        return 0x66023C

    @property
    def ua_blue(self) -> int:
        return 0x0033AA

    @property
    def ua_red(self) -> int:
        return 0xD9004C

    @property
    def ucla_blue(self) -> int:
        return 0x536895

    @property
    def ucla_gold(self) -> int:
        return 0xFFB300

    @property
    def ufo_green(self) -> int:
        return 0x3CD070

    @property
    def up_forest_green(self) -> int:
        return 0x014421

    @property
    def up_maroon(self) -> int:
        return 0x7B1113

    @property
    def usc_cardinal(self) -> int:
        return 0x990000

    @property
    def usc_gold(self) -> int:
        return 0xFFCC00

    @property
    def ube(self) -> int:
        return 0x8878C3

    @property
    def ultra_pink(self) -> int:
        return 0xFF6FFF

    @property
    def ultramarine(self) -> int:
        return 0x120A8F

    @property
    def ultramarine_blue(self) -> int:
        return 0x4166F5

    @property
    def umber(self) -> int:
        return 0x635147

    @property
    def united_nations_blue(self) -> int:
        return 0x5B92E5

    @property
    def university_of_california_gold(self) -> int:
        return 0xB78727

    @property
    def unmellow_yellow(self) -> int:
        return 0xFFFF66

    @property
    def upsdell_red(self) -> int:
        return 0xAE2029

    @property
    def urobilin(self) -> int:
        return 0xE1AD21

    @property
    def defutah_crimson(self) -> int:
        return 0xD3003F

    @property
    def utah_crimson(self) -> int:
        return 0xD3003F

    @property
    def vanilla(self) -> int:
        return 0xF3E5AB

    @property
    def vegas_gold(self) -> int:
        return 0xC5B358

    @property
    def venetian_red(self) -> int:
        return 0xC80815

    @property
    def verdigris(self) -> int:
        return 0x43B3AE

    @property
    def vermilion(self) -> int:
        return 0xE34234

    @property
    def violet(self) -> int:
        return 0xEE82EE

    @property
    def violet_blue(self) -> int:
        return 0x324AB2

    @property
    def violet_red(self) -> int:
        return 0xF75394

    @property
    def viridian(self) -> int:
        return 0x40826D

    @property
    def vivid_auburn(self) -> int:
        return 0x922724

    @property
    def vivid_burgundy(self) -> int:
        return 0x9F1D35

    @property
    def vivid_cerise(self) -> int:
        return 0xDA1D81

    @property
    def vivid_tangerine(self) -> int:
        return 0xFFA089

    @property
    def vivid_violet(self) -> int:
        return 0x9F00FF

    @property
    def warm_black(self) -> int:
        return 0x004242

    @property
    def waterspout(self) -> int:
        return 0x00FFFF

    @property
    def wenge(self) -> int:
        return 0x645452

    @property
    def wheat(self) -> int:
        return 0xF5DEB3

    @property
    def white(self) -> int:
        return 0xFFFFFF

    @property
    def white_smoke(self) -> int:
        return 0xF5F5F5

    @property
    def wild_intawberry(self) -> int:
        return 0xFF43A4

    @property
    def wild_watermelon(self) -> int:
        return 0xFC6C85

    @property
    def wild_blue_yonder(self) -> int:
        return 0xA2ADD0

    @property
    def wine(self) -> int:
        return 0x722F37

    @property
    def wisteria(self) -> int:
        return 0xC9A0DC

    @property
    def xanadu(self) -> int:
        return 0x738678

    @property
    def yale_blue(self) -> int:
        return 0x0F4D92

    @property
    def yellow(self) -> int:
        return 0xFFFF00

    @property
    def yellow_green(self) -> int:
        return 0x9ACD32

    @property
    def zaffre(self) -> int:
        return 0x0014A8

    @property
    def zinnwalditebrown(self) -> int:
        return 0x2C1608

    def random_with(self, like: str) -> None | list[int]:
        return [getattr(self, a) for a in self.__dict__ if like in a] or None

    def random(self) -> int:
        return getattr(
            self,
            random.choice([attr for attr in self.__dict__ if not attr.startswith("_")]),
        )
