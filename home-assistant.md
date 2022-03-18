---
type: tool
tags: hass home my_IT
---
# Home Assistant

## Done

- [x] remote access
  - [x] FIX android access from within my WiFi!
    - [x] proxy with apache (although not SSL for local connections :-)
- [x] Aqara-cube miss-registered: events missing!? NO
- [x] Bluetooth tracker
- [x] radio-stations in chromecasts: https://community.home-assistant.io/t/lovelace-chromecast-radio-jukebox/83867

## TODO

- [ ] Install Containered
  - [ ] MQTT AddOn
  - [x] cron-job for letsencrypt
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
    and added PTZ card from WebRTC: https://pythonrepo.com/repo/AlexxIT-WebRTC-python-video
  - [ ] Sound Tx/Rx
  - [ ] block chinese servers
- [x] install floor map HACS component
  - [ ] produce map with sweethome3d-furniture-nonfree
  - [ ] link css with entities
- [x] hass-integrate UPS: simply with apcusp "manual" integration
  - [-] replace `acpcupsd` with `nut` server: NO, hass-integration works
  - [-] develop own `acpcupsd` integration (based on https://www.home-assistant.io/integrations/apcupsd/)
  - [x] fixed mismatched entities: maxlinev--->HITRANS, minlinev-->LOTRANS, outputv, LASTXFER, NUMXFERS, BATTV
  - [ ] DEV: new  UPS device, to attach all its entities
- [ ] integrate [Syncthing](https://www.home-assistant.io/integrations/syncthing/)
- Automation rules:
  - [x] battery-low sensors (from blueprints)
  - [ ] Alarm!!
    - [x] zone enter/leave do not trigger with groups- groups miss GPS
  - [x] cube light & radio integrations
  - [x] motion-light override
  - [ ] DIMMING lights with Aqara switch v1:
    - Google search: `+home-assistant aqara push button dimmer`
    - node about
    - [ ] 2017 [Finally - a cheap WIRELESS switch that dims! Xiaomi Switch Gen1 ](https://community.home-assistant.io/t/finally-a-cheap-wireless-switch-that-dims-xiaomi-switch-gen1/27574)
    - Asking for [Increase and Decrease Brightness with ONE button of a switch](https://community.home-assistant.io/t/increase-and-decrease-brightness-with-one-button-of-a-switch/182954)
    - [ ] 2020 Apr [blog about a useful dimming script](https://siytek.com/home-assistant-push-button-dimmer/)
    - [ ] 2019 Jan [Using a Xiaomi Round Button as a dimmer switch with AppDaemon](https://community.home-assistant.io/t/using-a-xiaomi-round-button-as-a-dimmer-switch/93822)
    - [ ] 2017 [Xiaomi hold implementation](https://community.home-assistant.io/t/xiaomi-hold-implementation/14000)
    - [ ] 2021 Jan [single button on/off dim switch blueprint](https://community.home-assistant.io/t/single-button-on-off-dim-switch/265586/7)
    - [ ] 2021 Sep [Dimmer for Aqara buttons (1st gen)](https://community.home-assistant.io/t/dimmer-for-aqara-buttons-1st-gen/341923)
- [ ] DEV: keybase integration
- [ ] install [AppDaemon](https://appdaemon.readthedocs.io/en/latest/index.html)
- [ ] Install VSCode for Hass
  - [-] [VSCode-server on raspi through docker-mod?](https://community.home-assistant.io/t/install-vscode-visual-studio-code-as-a-separate-docker-container/166007/20)
  - [x] VSCode in my laptop+[shared SSHFS](https://community.home-assistant.io/t/solved-a-way-to-share-config-folder-over-nfs-on-hassio/100642/3?u=ankostis)
    NOTE: must chgrp all root-files to edit!
  - [ ] VSCode in my laptop+[shared NFS](https://pimylifeup.com/raspberry-pi-nfs/)
- [Docker-compose files](https://www.wouterbulten.nl/blog/tech/home-automation-setup-docker-compose/#appdaemon) for
  - [ ] AppDaemon
  - [ ] VSCode
  - [ ] Node-RED

## CO2 sensors

NDIR sensors only

- [ZN-P8](https://gr.banggood.com/ZN-P8-Digital-CO2-Gas-Analyzer-400-5000ppm-Air-Quality-Monitor-NDIR-Infrared-Detection-Gas-Detector-with-Temperature-Humidity-Display-p-1925086.html):
  - portable
  - USB-C
  - no connectivity :-(
  - 35.19€ (Banggood)
  - 1200mAh, 44h!!
- [Φορητός ανιχνευτής CO2 5 σε 1 ποιότητας αέρα](https://gr.banggood.com/5-In-1-Portable-CO2-Detector-Air-Quality-Detector-Intelligent-Air-Detector-Temperature-and-Humidity-Sensor-Tester-Carbon-Dioxide-Monitor-TVOC-Formaldehyde-Detection-HCHO-Detector-p-1802125.html)
  - portable
  - [bluetooth!](https://gr.banggood.com/5-In-1-bluetooth-Connected-Carbon-Dioxide-Detector-for-Detecting-TVOC-Formaldehyde-Concentrated-Air-Quality-Temperature-Humidity-CO-p-1880814.html?cur_warehouse=CN&ID=6287845&rmmds=search)
  - 26.39€ (Banggood)
  - 1500mAh, 6h
- [The AirGradient DIY Air Quality Sensor](https://www.airgradient.com/diy/)
  - ~80e
  - ESP (WiFi)
- [High quality ALL-AIR for school](https://www.elitecheu.com/products/temtop-p1000-air-quality-monitor)
  - PM 2.5 & 10
  - 6000mh/6h
  - 7.3inch display
- [DIY Zigbee USB CO2 meter](https://diyruz.github.io/posts/airsense/)