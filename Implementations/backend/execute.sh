#!/usr/bin/env bash
cd ../
cd SiamMask
export SiamMask=$PWD
cd Video
#cd $1
#for video in `ls`
#do
	#echo $video
	export VIDEO=$PWD
	video=`ls`
	ffmpeg -i $video -vf fps=24 %05d.jpg
        a=`identify -format "%w %h" 00001.jpg`
        b=($a)
        W=${b[0]}
        H=${b[1]}
#done
cd $SiamMask
export PYTHONPATH=$PWD:$PYTHONPATH
echo $PYTHONPATH
mkdir Result
mkdir processed
cd $SiamMask/experiments/siammask_sharp
export PYTHONPATH=$PWD:$PYTHONPATH
echo $PYTHONPATH
source activate siammask
echo $1 $2 $3 $4
#A2=NumberInt($2)
#A1=NumberInt($1)
#A3=NumberInt($3)
#A4=numberInt($4)
#echo $A1 $A2 $A3 $A4
#h=`expr $H \* 320 / $W`
#gap=`expr 270 - $h`
#y=`expr $A2 - $gap / 2`
#x=`expr $A1 \* $W / 320`
#y=`expr $y \* $H / $h`
#w=`expr $A3 \* $W / 320`
#h=`expr $A4 \* $H / $h`
h=`expr $H \* 360 / $W`
gap=`expr 270 - $h`
y=`expr $2 - $gap / 2`
x=`expr $1 \* $W / 360`
y=`expr $y \* $H / $h`
w=`expr $3 \* $W / 360`
h=`expr $4 \* $H / $h`
python ../../tools/demo.py --resume SiamMask_DAVIS.pth --config config_davis.json --base_path $VIDEO --selection_box $x,$y,$w,$h
cd ../../
mv Result $VIDEO
mv processed $VIDEO
cd Video/processed
ffmpeg -f image2 -i %d.jpg processed.mp4
