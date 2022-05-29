# STM32 pills

## 27 May 2022

- My x2 black-pill-I come from [WeActTogether](https://github.com/WeActTC/MiniSTM32F4x1)
  as seen from USB-IDs in the logs when connectin them.
- [Blue vs Black pills](https://hackaday.com/2021/01/20/blue-pill-vs-black-pill-transitioning-from-stm32f103-to-stm32f411/)
  with many resources
- [Black-magic fw --> blue-pill](https://satoshinm.github.io/blog/171223_jtagswdpillblink_jtagswd_debugging_via_black_magic_probe_on_an_stm32_blue_pill_and_blinking_a_led_using_stm32cubemx_libopencm3_and_bare_metal_c.html)
 FIT FOR STM32F103xxx ONLY (NOT FOR STM32F4(0 & 1)1, aka black-pill I & II)
- [blue-pill --> Black-magic probe](https://paramaggarwal.medium.com/converting-an-stm32f103-board-to-a-black-magic-probe-c013cf2cc38c)
  DOES NOT WORK
- Flashed BlackMagic following [this guide](https://acassis.wordpress.com/2020/06/07/flashing-the-blackpill-on-linux-using-dfu-util/)
  DOES NOT WORK

  ```logs
  $ dfu-util -d 0483:df11 -a 0 -s 0x08000000:leave -D ~/tmp/t/blackmagic_dfu-swlink.bin
  dfu-util 0.11

  Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
  Copyright 2010-2021 Tormod Volden and Stefan Schmidt
  This program is Free Software and has ABSOLUTELY NO WARRANTY
  Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

  dfu-util: Warning: Invalid DFU suffix signature
  dfu-util: A valid DFU suffix will be required in a future dfu-util release
  Opening DFU capable USB device...
  Device ID 0483:df11
  Device DFU version 011a
  Claiming USB DFU Interface...
  Setting Alternate Interface #0 ...
  Determining device status...
  DFU state(10) = dfuERROR, status(10) = Device's firmware is corrupt. It cannot return to run-time (non-DFU) operations
  Clearing status
  Determining device status...
  DFU state(2) = dfuIDLE, status(0) = No error condition is present
  DFU mode device DFU version 011a
  Device returned transfer size 2048
  DfuSe interface name: "Internal Flash  "
  Downloading element to address = 0x08000000, size = 7280
  Erase   	[=========================] 100%         7280 bytes
  Erase    done.
  Download	[=========================] 100%         7280 bytes
  Download done.
  File downloaded successfully
  Submitting leave request...
  Transitioning to dfuMANIFEST state
  ```

## 28 May 2022

- effort: 0.2
- [x] Locate [BlakMagic --> BlackPill guide](https://github.com/koendv/blackmagic-blackpill/blob/main/README_DEVELOPER.md)!!!
  - [ ] apply BlakMagic --> BlackPill guide
