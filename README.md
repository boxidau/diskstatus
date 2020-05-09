# diskstatus

If a drive failed it was hard to work out which one had actually failed

This program allows you to write a csv file to `~/.local/disk_inventory`
containing an inventory of the disks in your system

The program can then be run to determine if a disk is longer present in the system

Output looks like this:

```
position    name    status    size    brand     serial           wwn
----------  ------  --------  ------  --------  ---------------  ------------------
         1  sde     OK           500  Seagate   9VM7HT01         0x5000c5001a2270d4
         2  sdf     OK          2000  Samsung   S1UYJ1KSC03073   0x50024e9002ac06bb
         3  sdg     OK          2000  WD        WD-WCAZA1013014  0x50014ee2afaba77f
         4  sdc     OK            64  Kingston  06J9A0042328
         5  sda     OK          4000  Seagate   Z301DLBV         0x5000c50066334bd1
         6  sdd     OK          4000  Seagate   Z301D792         0x5000c50066249085
         7  sdb     OK          4000  Seagate   Z304TKNN         0x5000c50086decec3
         8          MISSING     4000  Seagate   Z303FP2J
         9  sdj     OK          4000  Seagate   Z306LARX         0x5000c500910a92a3
        10  sdi     OK          4000  Seagate   Z304TK6N         0x5000c50086dee757
```

Now I know the disk in physical position 8 is missing from the system for some reason
