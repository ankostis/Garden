---
tags: dev
---
# Mikrotik 750GL

- model: [RB750GL](ttps://mikrotik.com/product/RB750GL)
- [Atheros8327 switch chip](https://wiki.mikrotik.com/wiki/Manual:Interface/Bridge#Bridge_Hardware_Offloading) supports [most features](https://wiki.mikrotik.com/wiki/Manual:Switch_Chip_Features)
- Interface MACs:
  - ether1-gateway: 00:0C:42:CE:CC:62
  - ether2-master-local: 00:0C:42:CE:CC:63
  - ether3-slave-local: 00:0C:42:CE:CC:64
  - ether4-slave-local: 00:0C:42:CE:CC:65
  - ether5-slave-local: 00:0C:42:CE:CC:66

## initial setup

- `/system identity set name=ankhometik`
- SNTP for logs to have correct date
- DHCP Server runs on ETH ports 2-5
  - NEED default route --> ZTE router in IP | Routes
  - IP | Pool: 192.168.88.33-192.168.88.254
- DHCP Client runs on WAN port 1
  - Web admin accessible on ETH ports 2-5 ONLY!
- +1 graping for all IFs.
- +1 DNS server ie 1.1.1.1
- Import ssh keys as "strict"
- Create self-signed cestificate
  - assign to www-ssl,
  - disable `wfww` service
- [HASS integration](https://www.home-assistant.io/integrations/mikrotik)
[- DoH setup](https://www.shellhacks.com/mikrotik-dns-over-https-doh-server-cloudflare/)

## Tips

- [Code fragments](https://forum.mikrotik.com/viewtopic.php?t=177551#p980163)
- [Firewall battles](https://forum.mikrotik.com/viewtopic.php?t=83387)

## DHCP Leases

```txt
/ip dhcp-server lease print brief
Flags: X - disabled, R - radius, D - dynamic, B - blocked
 #   ADDRESS                    MAC-ADDRESS       HOST-NAME        SERVER
  0   ;;; raspanki
      192.168.88.8               B8:27:EB:2E:51:96 raspanki         default
  1   ;;; RackSwitch
      192.168.88.129             E4:F0:04:98:FB:7C RackSwitch       default
  2   ;;; printerM2070
      192.168.88.13              00:15:99:EE:2E:C0 M2070            default
  3   ;;; freedombox
      192.168.88.4               02:D7:02:C1:D1:3F                  default
  4   ;;; climaAC
      192.168.88.18              AC:93:C4:AE:CC:DC net_ac_CCDC      default
  5   ;;; climaDehumid
      192.168.88.19              84:7C:9B:67:FB:E0                  default
  6   ;;; V380Cam
      192.168.88.20              7C:E0:00:CC:CB:F3                  default
  7   ;;; ImouCam
      192.168.88.21              BC:32:5F:DB:76:73                  default
  8   ;;; kitapiAadm
      192.168.88.165             AC:1F:6B:A9:6A:7F kitapiAadm       default
  9   ;;; kitapiBadm
      192.168.88.166             AC:1F:6B:A9:6A:9B kitapiBadm       default
 10   ;;; kitapiCadm
      192.168.88.167             AC:1F:6B:A9:6A:68                  default
 11   ;;; kitapiDadm
      192.168.88.168             AC:1F:6B:A9:6A:67                  default
 12   ;;; V380bulb
      192.168.88.22              C4:3C:B0:43:BF:AF                  default
 13   ;;; broadlinkIR
      192.168.88.25              A0:43:B0:BA:1C:04 BroadLink-Rem... default
 14   ;;; kitapiA
      192.168.88.133             AC:1F:6B:B0:DF:C2 kitapiA          default
 15   ;;; RE200
      192.168.88.5               BA:BB:AC:BB:BB:AC RE200            default
 16   ;;; chromeAudio
      192.168.88.14              54:60:09:D5:B1:64 Chromecast-Audio default
 17   ;;; kudosETH
      192.168.88.10              E8:6A:64:AF:FD:E2 kudos            default
 18   ;;; KudosWIFI
      192.168.88.11              D4:3B:04:7C:25:E5 kudos            default
 19   ;;; tonia11s
      192.168.88.27              9E:3E:2B:E1:97:3E Redmi-Note-11S   default
 20   ;;; ank11s
      192.168.88.28              48:87:59:2E:3F:98 Redmi-Note-11S   default
 21   ;;; toniaPC
      192.168.88.29              94:B8:6D:4C:14:C7 DESKTOP-GE1HJHD  default
```

## BRIDGE ZTE

- [Guide from adslgr](https://www.adslgr.com/forum/threads/1079809-ZTE-ZXHN-H267A-bridge-mode-%CE%BC%CE%B5-ASUS-DSL-AC87VG?p=6490627#post6490627)
- ZTE/Internet/WAN: Create bridge VLAN=8935 "InternetBridge"
- ZTE/Internet/WAN/Port bindings: "InternetBridge" <--> LAN4
- eth-cable MikroTik-ETH1-GW <--> ZTE-LAN4
- ZTE/WAN (later): disable existing VLAN of "HSIv"
- MikroTik/IFs/VLAN: create VLAN=835,"vodafone-data-vlan",IF-ether1-gateway
- MikroTik/PPP/IFs: create PPPoE-Client `vodafone-internet-pppoe`
  - on IFs=`ether1-gateway` (and NOT on `vodafone-data-vlan`)
  - user: guest@adsl.gr, pswd: guest
  - add-default-route: yes
  - MaxMTU/MRU(?): 1492
  - Use peer DNS: NO (or will reset mine!)
- MikroTik/IP/DHCP-Client: set IF=`vodafone-internet-pppoe`
  - add-default-route: yes
  - Use peer DNS: NO (or will reset mine!)
- MikroTik/IP/Firewall/NAT: set OutIF=`vodafone-internet-pppoe`
- MikroTik/IP/Routes: *check* if old default route to ZTE still there!

### Port Forwarding & Hairpin Loopback

- ENABLE UPnP on Mikrotik, so that `raspanki:/etc/init.d/ddns.py` script works:
  - Add UPnP on BOTH IFs:
    - `vodafone-internet-pppoe`, type=`external`
    - `ether2-master-local`, type=`internal`
- create `lanet` local LAN network [*/ip firewall address-list*](https://wiki.mikrotik.com/wiki/Manual:IP/Firewall/Address_list): 192.168.88.0/24
- Create Hairpin NAT rule: `src-address-list` = `dst-address-list` = `lanet`
- MOVE IT above(earlier) the outbound *src-nat* rule,
  at least according to [this video](https://www.youtube.com/watch?v=_kw_bQyX-3U)
  but according to my understanding, *src-nat* [happens in POSTROUTING](https://help.mikrotik.com/docs/display/ROS/NAT#NAT-TypesofNAT:) which comes AFTER PREROUTING where *dst-nat* port-foarwardings happen, so not needed.
- DONT disable default `drop` firewall  route.
- create `wanip` Firewall/Address_list to store PPoE IP.
- Add dst-nat rules for each port-forwarding with `dst-address-list="wanip"`
- Schedule this script every 1min, name=`updwanat`:

## OLD updwan

```lua
# Update a firewall address-list with the current WAN IP from the PPPoE interface.
# Adapted from https://forum.mikrotik.com/viewtopic.php?p=911253&hilit=event+event+pppoe#p911253
{
  :local wanif      "wan-pppoe"
  :local wanAdList    "wanip"

  :local status [/interface get $wanif running]
  :if ($status) do={
    :local addrListId [/ip firewall address-list find list=$wanAdList ]
    :local old [/ip firewall address-list get $addrListId address ]

    :local new [/ip address get [find where dynamic=yes and interface=$wanif] address]
    :set new [:pick $new 0 [:find $new "/"] ]

    :log debug "UpdWANAT: old($old) == new($new)? $($new = $old)"
    :if ($new != $old) do={
      /ip firewall address-list set $addrListId address=$new
      :log info "UpdWANAT: old($old) -> new($new)"
    }
  }
}
```

## Update Wan & DynDNS on PPP callback

```lua
# Update Dynamic-DNS  with the current WAN IP from the address-list.
# A NameCheap dynamic-DNS client in MikroTik syntax
# - based on https://wiki.mikrotik.com/wiki/Dynamic_DNS_Update_Script_for_EveryDNS
# - and adapted by https://pastebin.com/qkaPy86x
# - according to https://www.namecheap.com/support/knowledgebase/article.aspx/29/11/how-do-i-use-a-browser-to-dynamically-update-the-hosts-ip
#
# Args from `/ppp profile on-up` property
# (see https://help.mikrotik.com/docs/display/ROS/PPP+AAA#PPPAAA-UserProfiles):
#
#  - $wanIfId: the id of the WAN IF
#  - $newIp: the remote IP assigned to the WAN IF
#  - $host: dynamic DNS host name (alone)
#  - $domain: dynamic DNS domain
#
# Attention: The WAN IF name is also used as the WAN address-list name,
# ie. this address-list must have been created!
:log debug "UpdWAN: WAN IP($wanIfId) -> $newIp -> $host.$domain, $[:tostr [/system script environment print as-value]]"

:local ifName [/interface get $wanIfId name]

# Bail out if WAN is (unexpectedly) down.
:local status [/interface get $wanIfId running]
:if (!$status) do={
  :error "UpdWAN: WAN-IF('$ifName') is not running!"
}

:local addrListId [/ip firewall address-list find list=$ifName ]
:local oldIp [/ip firewall address-list get $addrListId address ]

:local hostname   "$host.$domain"
:local dnsIp  [:resolve $hostname]

:log debug "UpdWAN: wan_if: $ifName, new_ip: $newIp, old_ip: $oldIp, dns_ip: $dnsIp"

:if ($newIp != $oldIp) do={
  /ip firewall address-list set $addrListId address=$newIp
  :log info "UpdWAN: WAN address-list: $oldIp -> $newIp"
} else={
  :log info "UpdWAN: WAN address-list already '$newIp', no action."
}

:if ($newIp != $dnsIp) do={
  :local okRegex "ErrCount>0"
  :local url (\
    "https://dynamicdns.park-your-domain.com/update\?domain=$domain&" .\
    "password=190892ae5e99440e902deb5d9e84a051&" .\
    "host=$host"\
  )

  # HTTP-GET to the dynamic DNS.
  :local response ([/tool fetch url=$url mode=http output=user as-value]->"data")
  :delay 1

  # Check if error messages received from file.
  :if (! ($response ~ $okRegex)) do={
    :error "UpdWAN: dynamic DNS FAILED $dnsIp -> $newIp, response: $response"
  }

  :log info "UpdWAN: dynamic DNS:($oldIp, $dnsIp) -> $newIp"
  :log debug "UpdWAN: dynamic DNS HTTP-response: $response"
} else={
  :log info "UpdWAN: dynamic DNS already '$newIp', no action."
}
```

### Update Wan & DynDNS Listener

```lua
/system script run [find name=updwanat];
:local WanChanged [:parse [/system script get [find name=updwan] source]]; $WanChanged interface=$wanIfId newIp=$"local-address"
```

## [DNS batch-sync from DHCP](https://wiki.mikrotik.com/wiki/Setting_static_DNS_record_for_each_DHCP_lease)

```lua
# DNS record for DHCP lease, `hostname`` derrived in this order (1st wins):
# - lease-comment
# - `MACtoNames` array indeced by lease-mac
# - lease-host-name

:local topdomain "ank.home";
:local MACtoNames {
  "SO:ME:MA:CA:DD:RR"="hostname"
}

:local hostname;
:local leaseIP;
:local leaseMAC

/ip dhcp-server lease;

:foreach i in=[find] do={
  :set leaseMAC [get $i mac-address]
  :set leaseIP [get $i address];

  :set hostname [get $i comment]
  :if ([:len $hostname] = 0) do={
    :set hostname ($MACtoNames->$leaseMAC);
    :if ([:len $hostname] = 0) do={
      :set hostname [get $i host-name];
    }
  }

  :if ([:len $hostname] = 0) do={
    :log warning "SyncDNS: no hostname for ($leaseMAC, $[:tostr $leaseIP])!"
  } else={
    :local fqdn "$hostname.$topdomain";
    :local active [get $i active-address]

    /ip dns static

    :if $active do={
      :do {
        :log info "SyncDNS: $fqdn --> $leaseIP";
        :if [find name=$fqdn] do={
          set [find name=$fqdn] address=$leaseIP comment="SyncDns"
        } else={
          add name=$fqdn address=$leaseIP comment="SyncDns"
        }
      } on-error={
        :log info "SyncDNS: FAIL adding: $fqdn --> ($leaseMAC, $leaseIP)";
      }
    } else={
        :log info "SyncDNS: DELETE $fqdn --> ($leaseMAC, $leaseIP)"
        /ip dns static remove [find name=$fqdn]
    }
  }
}
```

## DNS from DHCP callback

```lua
# Called after a DHCP-lease changes status and it update host's DNS AAA record.
# Variables that can be used in the script:
# - leaseMAC      - DHCP mac address
# - leaseIP       - DHCP IP address
# - leaseHostname - (optional) DHCP detedted hostname
# - topDomain     - Appended to hostname to derrive FQDN
# - MACtoNames    - (array) overrides/defaults for the hostnames derrived from DHCP.
{
  :log debug "UpdDhcpDns: leaseMAC: $leaseMAC, leaseIP: $leaseIP, leaseHostname: $leaseHostname, topDomain: $topDomain, MACtoNames: $[:tostr $MACtoNames]"

  :local hostname

  # Derive hostname from DHCP-comment, overrides, DHCP-hostname, or fail.
  :set hostname [/ip dhcp-server lease get [find mac-address=$leaseMAC] comment]
  :if ([:len $hostname] = 0) do={
    :set hostname ($MACtoNames->$leaseMAC);
    :if ([:len $hostname] = 0) do={
      :set hostname $leaseHostname;
    }
  }
  :if ([:len $hostname] = 0) do={
    :error "UpdDhcpDns: unknown hostname for ($leaseIP, $leaseMAC)";
  }

  /ip dns static
  :set hostname "$hostname.$topDomain"

  :local prevId [find name=$hostname];
  :if ($prevId) do={
    :local prevIP [get $prevId address];
    :log debug "UpdDhcpDns: $hostname ($leaseIP, $leaseMAC) was $prevIP"

    :if ($prevIP = $leaseIP) do={
        :log info "UpdDhcpDns: no change: $hostname --> ($leaseIP, $leaseMAC)"
        :return 0
    }
  }

  :do {
    :log info "UpdDhcpDns: $hostname --> ($leaseIP, $leaseMAC) (was $prevIP)"
    :if $prevId do={
        set $prevId address=$leaseIP comment="UpdDchpDns"
    } else={
        add name=$hostname address=$leaseIP comment="UpdDchpDns"
    }
  } on-error={
    :error "UpdDhcpDns: failed!\n $[:tostr [/system script environment print as-value]]"
  }
}
```

### DNS from DHCP Listener

```lua
# Called aftes a DHCP-lease changes status and it update host's DNS AAA record.
# - leaseBound        - set to "1" if bound, otherwise set to "0"
# - leaseServerName   - DHCP server name
# - (*)leaseActMAC    - active mac address
# - (*)leaseActIP     - active IP address
# - (*)lease-hostname - client hostname (if not in `MACtoNames` overrides)
# - lease-options     - an array of received options
{
  #:log debug ("Calling UpdDhcpDns(bound: $leaseBound, leaseMAC=$leaseActMAC leaseIP=$leaseActIP leaseHostname=" . $"lease-hostname" . "(")
  :local MACtoNames {"mac"="ip"}

  # Do nothing(!) if lease unbound.
  :if ($leaseBound=1) do={
    :local cb [:parse [/system script get upddhcpdns source]]
    $cb leaseMAC=$leaseActMAC leaseIP=$leaseActIP leaseHostname=$"lease-hostname" topDomain="ank.home" MACtoNames=$MACtoNames
  }
}
```
