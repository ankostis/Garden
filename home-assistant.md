# Home Assistant

## Done

- [x] remote access
  - [x] FIX android access from within my WiFi!
    - [x] proxy with apache (although not SSL for local connections :-)
- [x] Aqara-cube miss-registered: events missing!? NO
- [x] Bluetooth tracker
- [x] radio-stations in chromecasts: https://community.home-assistant.io/t/lovelace-chromecast-radio-jukebox/83867

## TODO

- [ ] Install Supervised
  - [ ] MQTT AddOn
  - [ ] cron-job for letsencrypt: added but UNTESTED
  - [ ] splitBrain DNS (AdGuard) to have a single hass-URL in browsers
- [x] established WebPush html5 notifications
  - [x] test they run (mobile: ok, kudos: ??)
- [x] Zigbee Gateway
  - [x] movement & window sensors
  - [x] presence:
    - [x] nmap: DONE, but may DRAIN BATTERIES!
    - [x] bt
    - [ ] integrate [my router]()https://github.com/ericpignet/home-assistant-tplink_router (needs development)
- [x] integrate Tonia
  - [x] account, 2FA
  - [x] hass-app
    - [ ] fix missed updates
- [x] ONVIF camera,
  - [x] PTZ: https://github.com/Gowresh7/V380_Python
    eventually fixed when upgraded to hass-2021.6.4 (or was never broken!)
    and added PTZ card
  - [ ] Sound Tx/Rx
    - [ ] Rx: WebRTC: https://pythonrepo.com/repo/AlexxIT-WebRTC-python-video
  - [ ] block chinese servers
- [x] install floor map HACS component
  - [ ] produce map with sweethome3d-furniture-nonfree
  - [ ] link css with entities
- [x] hass-integrate UPS: simply with apcusp "manual" integration
  - [-] replace `acpcupsd` with `nut` server: NO, hass-integration works
  - [-] develop own `acpcupsd` integration (based on https://www.home-assistant.io/integrations/apcupsd/)
  - [x] fixed mismatched entities: maxlinev--->HITRANS, minlinev-->LOTRANS, outputv, LASTXFER, NUMXFERS, BATTV
  - [ ] DEV: new  UPS device, to attach all its entities
 - [ ] integrate Syncthing: https://community.home-assistant.io/t/how-to-integrate-your-s-and-even-make-it-talk/209116
- Automation rules:
  - [x] battery-low sensors (from blueprints)
  - [ ] Alarm!!
    - [x] zone enter/leave do not trigger with groups- groups miss GPS
  - [ ] cube light & radio integrations
  - [ ] motion-light override
- [ ] DEV: keybase integration
