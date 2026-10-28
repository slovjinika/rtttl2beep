# slovjinika beep (pc speaker)

# Westminster Chime
G=415; F=370; E=330; B=247; L=800; LL=1600; d=200; p=1000; beep -f $E -l $L -D $d -n -f $G -l $L -D $d -n -f $F -l $L -D $d -n -f $B -l $LL -D $p -n -f $E -l $L -D $d -n -f $F -l $L -D $d -n -f $G -l $L -D $d -n -f $E -l $LL -D $p -n -f $G -l $L -D $d -n -f $E -l $L -D $d -n -f $F -l $L -D $d -n -f $B -l $LL -D $p -n -f $B -l $L -D $d -n -f $F -l $L -D $d -n -f $G -l $L -D $d -n -f $E -l $LL; sleep 0.5; H=$(date +"%-I"); echo "Chimes: $H o'clock."; for ((i=1; i<=H; i++)); do beep -f 220 -l 300 -D 50 -n -f 218 -l 1800 -D 600; done

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
beep -f 440 -l 60 -n -f 880 -l 120

beep -f 150 -l 250 -n -f 130 -l 250
beep -f 220 -l 150 -n -f 160 -l 300
beep -f 800 -l 30 -n -f 100 -l 200
beep -f 900 -l 20 -n -f 100 -l 150
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

# notification
beep -f 200 -l 50 -n -f 400 -l 50 -n -f 800 -l 50 -n -f 1600 -l 150
beep -f 523 -l 50 -n -f 392 -l 50 -n -f 784 -l 60 -n -f 1568 -l 150
beep -f 1046 -l 80 -n -f 1318 -l 80 -n -f 1568 -l 100 -n -f 2000 -l 450

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
