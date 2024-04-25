---
tags: dev
---
# My PC

- Lenovo T480
- Machine-type: 20L5CT01WW
- Serial: PF1LJ54N
- MB-Serial: L1HF91Z009S
- name: kudos
- date: Mar 20219
- Maintenance tasks for my PC: ~/README.md
- [ ] move `~/README.md --> /etc/`, and link it from my home.
- [ ] etckeeper -> keybase
- [ ] setup `VodafoneTV` & `RadioDroid` in android-box `anbox`
  - [x] installed `anbox` from `snap`
- Bind euro-sign(€) into keyboard

## Keybase woes

- date: Dec 2023
- Keybase is blocking [flatpaks to run](https://github.com/flatpak/flatpak/issues/5496) and [laptop suspend](https://github.com/keybase/client/issues/12458#issuecomment-433745233)
  - applied workarount script in the issue keybase/client#12458, above

## Gnome Shortcuts

- Dec 2023:
  - `F10`: spell fix, no conf needed
  - `Shift+F10`: context-menu, no conf needed
  - `F11`: App-specific fullscreen, no winbar+titlbar, no conf needed
  - `Alt+F11`: Toggle *Maximization* Window, gnome settings needed (Alt+F10 -> Alt+F11),
    superceded by Tiling Assitant (Super+Up) ONLY when "dynamic titling shortcuts"
  - `Super+F11`: Toggle *Fullscreen* Window, no titlbar, not restorable (only toggled),
    gnome settings needed (Super+F10 -> Super+F11)
  - `Shift+Super+Left/Right`: move window to left/right *monitor*
  - `Super+Left/Right`: NOTHING! to get used to tilling shortcuts, was "view split l/r",
    gnome settings needed
  - `Shift+Super+H/V`: Maximize horizontally/vertically, gnome settings needed
  - Enable *Workspaces*:
    - `Super+PgUp/PgUp/Home/End`: switch to left/right/first/last *wrksp*
    - `Shift+Super+PgUp/PgUp/Home/End`: move window to left/rightfirst/last *wrkspc*
  - Enable Tiling Assistant
    - Disable [dynamic titling shortcuts](https://github.com/Leleat/Tiling-Assistant/wiki/Dynamic-Keybindings)
      eg. unpredictable maximize key, unecessary with corner tiling shortcuts
    - `Super+N/E/I/O`: tile left/up/down/right (ColemakDH)
    - `Super+U/Y/,/.`: tile NW/NE/SW/SE (ColemakDH)
      - Unbind Super+O:

        ```bash
        gsettings list-recursively | grep -i "<Super>O"
        gsettings set org.gnome.settings-daemon.plugins.media-keys rotate-video-lock-static []
        ```

    - `Super+N/E/I/O`: *tile* left/up/down/right (ColemakDH)
    - `Super+Up/Down`: Fullscreen(not Maximize!, not restorable, only toggled)/Restore Window
    - Enablje Ecperimantal features (eg. [Layouts](https://github.com/Leleat/Tiling-Assistant/wiki/Layouts))
    - `Super+/`: Select *Layout*
