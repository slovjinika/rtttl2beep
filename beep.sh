# midi --> rtttl
beepmyquad.com

# midi --> beep
github.com/Sucharek233/midi2beep

# rtttl --> beep
github.com/slovjinika/rtttl2beep

# Westminster Chime version 2026.10
G=415; F=370; E=330; B=247; L=800; LL=1600; d=200; p=1000; beep -f $E -l $L -D $d -n -f $G -l $L -D $d -n -f $F -l $L -D $d -n -f $B -l $LL -D $p -n -f $E -l $L -D $d -n -f $F -l $L -D $d -n -f $G -l $L -D $d -n -f $E -l $LL -D $p -n -f $G -l $L -D $d -n -f $E -l $L -D $d -n -f $F -l $L -D $d -n -f $B -l $LL -D $p -n -f $B -l $L -D $d -n -f $F -l $L -D $d -n -f $G -l $L -D $d -n -f $E -l $LL; sleep 0.5; H=$(date +"%-I"); echo "Chimes: $H o'clock."; for ((i=1; i<=H; i++)); do beep -f 220 -l 300 -D 50 -n -f 218 -l 1800 -D 600; done

# Westminster Chime version 2026.11
G=415; F=370; E=330; B=247; L=705; LL=2150; d=45; p=100; beep -f $E -l $L -D $d -n -f $G -l $L -D $d -n -f $F -l $L -D $d -n -f $B -l $LL -D $p -n -f $E -l $L -D $d -n -f $F -l $L -D $d -n -f $G -l $L -D $d -n -f $E -l $LL -D $p -n -f $G -l $L -D $d -n -f $E -l $L -D $d -n -f $F -l $L -D $d -n -f $B -l $LL -D $p -n -f $B -l $L -D $d -n -f $F -l $L -D $d -n -f $G -l $L -D $d -n -f $E -l 2250; sleep 0.6; H=$(date +"%-I"); echo "Chimes: $H o'clock."; for ((i=1; i<=H; i++)); do beep -f 220 -l 300 -D 50 -n -f 218 -l 1800 -D 600; done

# gold edition
python3 /home/node17/Soft/rtttl2beep/rtttl2beep.py "StartUp2:d=32,o=4,b=180:16c,16e,16g,16b,8c5,8b,8g,8e,2c5"
# ок
StartUp2:d=32,o=4,b=180:16c,16e,16g,16b,8c5,8b,8g,8e,2c5
StartUp2:d=32,o=7,b=260:16c,16e,16g,16b,8c8,8b,8g,8e,2c8
# повільно, вдумливо
StartUp3:d=16,o=7,b=260:8c,8e,8g,8b,4c8,4b,4g,2c8
# дуже швидко
StartUp1:d=32,o=7,b=260:16c,16e,16g,16b,8c8,8b,8g,2c8

# мелодія на рингтон (допрацювати 2c8)
StartUp2-ringtone:d=32,o=7,b=240:16c,16e,16g,16b,8c8,8b,8g,8e,2c8,16P,16c,16e,16g,16b,8c8,8b,8g,8e,1c8

# classic -> on
beep -f 523 -l 100 -n -f 659 -l 100 -n -f 784 -l 100 -n -f 1046 -l 250
beep -f 523 -l 80 -n -f 659 -l 80 -n -f 784 -l 80 -n -f 1318 -l 250
# classic -> off
beep -f 1046 -l 100 -n -f 784 -l 100 -n -f 659 -l 100 -n -f 523 -l 250

# classic -> reboot
beep -f 880 -l 60 -n -f 659 -l 60 -n -f 440 -l 60 -n -f 220 -l 100 -n -f 880 -l 150 -n -f 1760 -l 250

# error
beep -f 300 -l 100 -n -f 200 -l 150
beep -f 150 -l 400
beep -f 150 -l 250 -n -f 130 -l 250
beep -f 220 -l 150 -n -f 160 -l 300
beep -f 800 -l 30 -n -f 100 -l 200
beep -f 900 -l 50 -n -f 100 -l 300

beep -f 440 -l 60 -n -f 880 -l 120x
beep -f 300 -l 70 -n -f 600 -l 70 -n -f 150 -l 150
beep -f 1500 -l 50 -d 50 -r 3x
beep -f 2000 -l 30 -n -f 1500 -l 30 -n -f 1000 -l 30 -n -f 500 -l 100 
beep -f 1046 -l 100 -n -f 659 -l 100 -d 150 -n -f 1046 -l 100 -n -f 659 -l 100 -d 200 -r 2
beep -f 784 -l 150 -n -f 740 -l 150 -n -f 698 -l 150 -n -f 659 -l 300
beep -f 600 -l 40 -n -f 500 -l 40 -n -f 400 -l 40 -n -f 300 -l 40 -n -f 200 -l 80
beep -f 450 -l 100 -n -f 350 -l 100 -n -f 250 -l 200
beep -f 350 -l 120 -n -f 330 -l 120 -n -f 310 -l 120 -n -f 250 -l 400

# sms
beep -f 1046 -l 30 -n -f 1396 -l 40
beep -f 2000 -l 40 -n -f 1500 -l 60
beep -f 1318 -l 50 -n -f 1568 -l 80

Beep1:d=32,o=6,b=180:32c6,32f6
Beep2:d=32,o=6,b=180:32b6,16g6
Beep3:d=32,o=6,b=180:16e6,16g6

# notification
beep -f 200 -l 50 -n -f 400 -l 50 -n -f 800 -l 50 -n -f 1600 -l 150
beep -f 523 -l 50 -n -f 392 -l 50 -n -f 784 -l 60 -n -f 1568 -l 150
beep -f 1046 -l 80 -n -f 1318 -l 80 -n -f 1568 -l 100 -n -f 2000 -l 250
beep -f 300 -l 60 -n -f 600 -l 60 -n -f 450 -l 60 -n -f 900 -l 60 -n -f 750 -l 60 -n -f 1500 -l 300
beep -f 400 -l 30 -n -f 450 -l 30 -n -f 350 -l 30 -n -f 300 -l 60
beep -f 200 -l 80 -n -f 300 -l 80 -n -f 400 -l 80
beep -f 784 -l 120 -n -f 1046 -l 120 -n -f 784 -l 120 -n -f 1046 -l 200 -d 150 -r 2
beep -f 523 -l 80 -n -f 784 -l 80 -n -f 1046 -l 80 -n -f 784 -l 80 -d 100 -r 3
beep -f 523 -l 90 -n -f 659 -l 90 -n -f 784 -l 90 -n -f 659 -l 90 -d 150 -r 3
beep -f 880 -l 100 -n -f 440 -l 100 -n -f 880 -l 100

# ok
beep -f 988 -l 80 -n -f 1318 -l 250
beep -f 523 -l 80 -n -f 659 -l 80 -n -f 784 -l 80 -n -f 1046 -l 200
beep -f 659 -l 50 -n -f 830 -l 50 -n -f 987 -l 50 -n -f 1318 -l 150
beep -f 800 -l 40 -n -f 1200 -l 40 -n -f 1600 -l 80
beep -f 600 -l 70 -n -f 900 -l 70 -n -f 1200 -l 120
beep -f 1000 -l 40 -n -f 1500 -l 80
beep -f 400 -l 50 -n -f 800 -l 50 -n -f 1600 -l 150

# timer
beep -f 4000 -l 80 -d 80 -r 8
beep -f 1500 -l 50 -d 30 -n -f 1500 -l 50 -d 40 -n -f 1500 -l 300 -d 400 -r 3

# 12:55
beep -f 1760 -l 50 -d 35 -n -f 1760 -l 50 -d 35 -n -f 2349 -l 300 -d 400 -r 3
beep -f 1568 -l 55 -d 30 -n -f 1568 -l 55 -d 30 -n -f 2349 -l 350 -d 500 -r 3
beep -f 2000 -l 40 -d 30 -n -f 2000 -l 40 -d 40 -n -f 2600 -l 250 -d 500 -r 3
beep -f 2200 -l 45 -d 30 -n -f 2200 -l 45 -d 40 -n -f 1760 -l 300 -d 500 -r 3
beep -f 1976 -l 50 -d 35 -n -f 1976 -l 50 -d 35 -n -f 2637 -l 300 -d 450 -r 3
beep -f 1760 -l 50 -d 30 -n -f 2093 -l 50 -d 35 -n -f 2637 -l 350 -d 500 -r 3

# hard -> on
beep -f 150 -l 60 -n -f 150 -l 250 -n -f 300 -l 150 -n -f 600 -l 100 -n -f 1200 -l 250
# hard -> off
beep -f 1200 -l 250 -n -f 600 -l 100 -n -f 300 -l 150 -n -f 150 -l 350

# error
beep -f 80 -l 400 -n -f 110 -l 400 -n -f 70 -l 600
beep -f 880 -l 50 -n -f 440 -l 50 -n -f 1760 -l 50 -n -f 220 -l 100 -n -f 3520 -l 30 -n -f 110 -l 400
beep -f 110 -l 350 -n -f 165 -l 250 -n -f 220 -l 200 -n -f 165 -l 150 -n -f 110 -l 500
beep -f 70 -l 200 -n -f 140 -l 150 -n -f 70 -l 150 -n -f 210 -l 100 -n -f 105 -l 300

# start (part 1)
beep -f 60 -l 500 -n -f 120 -l 300 -n -f 240 -l 200 -n -f 960 -l 150

# start (part 1 + cut)
beep -f 75 -l 350 -n -f 110 -l 250 -n -f 220 -l 100 -n -f 440 -l 80 -n -f 880 -l 60 -n -f 1760 -l 400
beep -f 90 -l 400 -n -f 180 -l 300 -n -f 360 -l 200 -n -f 720 -l 100 -n -f 1440 -l 600
beep -f 60 -l 400 -n -f 120 -l 200 -n -f 240 -l 100 -n -f 960 -l 50 -n -f 480 -l 50 -n -f 1920 -l 400
beep -f 50 -l 400 -n -f 75 -l 300 -n -f 100 -l 250 -n -f 150 -l 200 -n -f 200 -l 400

beep -f 50 -l 400 -n -f 75 -l 300 -n -f 100 -l 250 -n -f 150 -l 200 -n -f 200 -l 400 -n -f 300 -l 350 -n -f 440 -l 150 -n -f 554 -l 150 -n -f 659 -l 200 -n -f 880 -l 600
beep -f 50 -l 400 -n -f 75 -l 300 -n -f 100 -l 250 -n -f 150 -l 200 -n -f 200 -l 400 -n -f 300 -l 350
beep -f 50 -l 400 -n -f 75 -l 300 -n -f 100 -l 250 -n -f 150 -l 200 -n -f 200 -l 400 -n -f 300 -l 350 -n -f 1000 -l 40 -n -f 1500 -l 300

beep -f 60 -l 400 -n -f 120 -l 250 -n -f 240 -l 200 -n -f 480 -l 150 -n -f 580 -l 100 -n -f 659 -l 50 -n -f 830 -l 50 -n -f 987 -l 50 -n -f 1318 -l 200
beep -f 60 -l 400 -n -f 120 -l 250 -n -f 240 -l 200 -n -f 480 -l 150 -n -f 580 -l 100 -n -f 659 -l 50 -n -f 830 -l 50 -n -f 987 -l 50 -n -f 1318 -l 100 -n -f 1318 -l 100 -n -f 987 -l 200

beep -f 70 -l 200 -n -f 140 -l 150 -n -f 70 -l 150 -n -f 210 -l 100 -n -f 280 -l 120 -n -f 350 -l 100 -n -f 140 -l 150 -n -f 70 -l 200 -n -f 140 -l 150 -n -f 70 -l 150 -n -f 210 -l 100 -n -f 420 -l 120 -n -f 560 -l 100 -n -f 210 -l 150 -n -f 90 -l 300 -n -f 180 -l 200 -n -f 90 -l 200 -n -f 270 -l 150 -n -f 360 -l 120 -n -f 450
