
cd results/%1
ffmpeg -f concat -i concat-list.txt -c copy %1.mp4
cd ..
cd ..
copy results\%1\%1.mp4 static\%1.mp4