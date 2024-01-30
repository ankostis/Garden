# Keyboard

- [Keyboard Market@Reddit](https://www.reddit.com/r/mechmarket/search/?q=title:(%22%5BEU-%22)&restrict_sr=on&sort=new&t=all)

## Preference

1. wDactyl manuform
2. [x] Charybdis Kit
   - Netherlands, 56 keys only
3. Kinesis 360
   - US, no leds, too many thumb keys
4. Moonlander
   - US, no concave
5. Ultimate Hacking Keyboard v2
   - Hungary, no ortholinear, no tenting, no concave, trackball vs thumb cluster @ the right

## Desired Features

- split
- ortholinear
- thumb clusters
- concave
- tenting
- kmk (vs qmk)
- vial (vs via)
- leds

## Layouts

- [All layouts charachteristics](https://www.keyboard-design.com/best-layouts.html)
- [interesting top layout](https://www.keyboard-design.com/letterlayout.html?layout=hieaqmtsrn.en.ansi)
- [Moonlander layouts tutorials](https://configure.zsa.io/moonlander/search?q=programming&page=1&anonymous=false&withTour=true)
- [KeymapDB: an open-source db for ergonomic QMKs](https://keymapdb.com/)

## Dactyl Manuform

- https://www.youtube.com/watch?v=95etDQ0I-Ls
- [Guide for idiots](https://medium.com/swlh/complete-idiot-guide-for-building-a-dactyl-manuform-keyboard-53454845b065)
- [Review and build guide](https://benfrain.com/review-dactyl-manuform-an-ergonomic-custom-built-mechanical-keyboard/#:~:text=I've%20built%204%20Dactyl,ve%20been%20really%20enjoying%20mine.)
- [Guide for tools & material](https://www.youtube.com/watch?v=Y57lNIpAdT4)
- [Etsy 3D printer: wylderbuilds](https://www.etsy.com/shop/Wylderbuilds?ref=shop-header-name&listing_id=1179806888)
- [Etsy 3D printer: Cyboard](https://www.etsy.com/shop/Cyboard?ref=shop-header-name&listing_id=1489087073)
- [Oh, Keycaps 3D print](https://ohkeycaps.com/products/built-to-order-dactyl-manuform-keyboard)
- [VHD with pad & trackjoystick](https://www.vexc-how-design.com/overview) fron UK
- repos:
  - https://github.com/tshort/dactyl-keyboard
  - https://github.com/adereth/dactyl-keyboard
  - https://github.com/jeffgran/ManuForm

## Split keyboards

- [6y of experiernce](https://www.youtube.com/watch?v=CA00USrhOMc)
  with cursor movements sample
- [Moonlander vs Kinesis 360 (11 May '23)](https://www.youtube.com/watch?v=l-qkKIpHu9A)
  - Moonlander tenting (tilt) cumbersome to tune, so dropped
- [Enthusiastic reviewer about split ortholinears mechs: Ergodox vs Moonlander](https://www.youtube.com/watch?v=zEWiAAMLxd4)
- [Ultimate Hacking Keyboard (EU)](https://ultimatehackingkeyboard.com/)

## Colemak

- [Dreymar Colemak "Big Bag papers"](https://dreymar.colemak.org/layers-extend.html)
  - and [linux stuff](https://github.com/DreymaR/BigBagKbdTrixXKB)
- [Colemakd DH vs Workman @ reddit](https://www.reddit.com/r/Colemak/comments/j9pxcb/colemak_dh_vs_workman/)
- [ColemakDH vs ColemakDHm @ reddit](https://www.reddit.com/r/Colemak/comments/lbwqfd/colemakdh_vs_colemakdhm/)
- [Halmak Reddit criticism](https://www.reddit.com/r/KeyboardLayouts/comments/wjhaqa/is_there_anyone_who_use_halmak_keyboard_layout/)

## Home row mods

- [The official QMK tap-hold guide](https://docs.qmk.fm/#/tap_hold)
- [The "precondition" guide about ordering them](https://precondition.github.io/home-row-mods)
- [Miryoku](https://github.com/manna-harbour/miryoku/tree/master/docs/reference)
- [Manna Harbur's Myrioku patches](https://sunaku.github.io/home-row-mods.html#patches)
- [Achordion](https://getreuer.info/posts/keyboards/achordion/index.html#add-achordion-to-your-keymap)

## Keycaps $ switches

- [Custom with hair-iron](https://www.youtube.com/watch?v=jNZkzK4l0F8&t=0s)
- [3D-printed DIY doubleshot keycaps](https://www.youtube.com/watch?v=2RHdFKCa0yk)
- [Quality key caps & swithes](https://www.youtube.com/watch?v=9P,74eCU19d0)
- [Jan Lunge discord about German shops](https://discord.com/channels/811709118284955668/811722737981718568/1115950214004613212):
  - https://keycapsss.com/
  - https://candykeys.com/

## My Charybdis-4x6 keymap

- [json layout](https://discord.com/channels/681309835135811648/747850558630789210/1123239395768684564)
- my layout diagram
- Engram:

  ```txt
  [{ 1| 2= 3~ 4+  5<     6>  7^ 8& 9% 0* ]} /\
     bB yY oO uU  '(     ")  lL dD wW vV zZ #$ @`
     cC iI eE aA  ,;     .:  hH tT sS nN qQ
     gG xX jJ kK  -_     ?!  rR mM fF pP
  ```

- ColemakDH affected by:
  - [Miryoku](https://github.com/manna-harbour/miryoku)
  - [Engram](https://sunaku.github.io/engram-keyboard-layout.html):

  ```txt
  [{ 1| 2= 3~ 4+ 5<      6> 7^ 8& 9% 0* ]}
  qQ wW fF pP bB '(      ") jJ lL uU yY #$
  aA rR sS tT gG ,;      .: mM nN eE iI oO
  zZ xX cC dD vV -_      ?! kK hH #$ /\ @`
  ```

  ```txt
  [{ 1! 2@ 3# 4$ 5<      6> 7& 8* 9% 0^ ]}
  qQ wW fF pP bB '(      ") jJ lL uU yY |?
  aA rR sS tT gG ,;      .: mM nN eE iI oO
  zZ xX cC dD vV -_      `~ kK hH #$ /\ =+

  Esc, Spc, Tab         Back, Del, Enter
  MT(RAlt, Lang)
  ```

- forks:
  - sigvah-3x5 -
  - [edenmagic-3x6](https://discordapp.com/channels/681309835135811648/1193283421619888169/1193382703853215844) - automouse threshold

- [Set RGB-color per layer](https://discordapp.com/channels/681309835135811648/1065902106659274762/1065915197270790174)
