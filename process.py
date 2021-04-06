import re
import os
import sys
import nltk
import time
import requests
from PIL import Image
from random import randrange
from nltk.corpus import wordnet as wn
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat


uuid = sys.argv[1]
with open("bing.txt") as f:
    bing_subs = f.read()

with open("speech.txt") as f:
    speech_subs = f.read()

search_url = "https://api.bing.microsoft.com/v7.0/images/search"

headers = {"Ocp-Apim-Subscription-Key" : bing_subs}
speech_config = SpeechConfig(subscription=speech_subs, region="southcentralus")


if (os.path.isfile("results/{}/summary.txt".format(uuid))):
    f2work = "results/{}/summary.txt".format(uuid)
else:
    f2work = "results/{}/text.txt".format(uuid)



with open(f2work) as f:
    text = f.read()


sentences = text.split(".")



sentences= [x for x in sentences if len(x)>5]



for snumb,sentence in enumerate(sentences):
    if(snumb>3):
        break
    os.makedirs("results/{}/{:04d}".format(uuid,snumb))
    words2look4 = []
    sentence = res = re.sub(r'[^\w\s]', '', sentence)
    words = sentence.split(" ")
    for word in words:
        synset = wn.synsets(word)
        if len(synset) > 0 :
            wordtype = synset[0].pos()
            if (wordtype == 'v' or wordtype =='n'):
                words2look4.append(word)
    
    for wi,w2l4 in enumerate(words2look4):
        params  = {"q": w2l4, "imageType": "photo"}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        i2download = [img["contentUrl"] for img in search_results["value"]][randrange(20)]
        print(i2download)
        response = requests.get(i2download)
        ext = i2download[-3:]
        imgfile = open("results/{}/{:04d}/{:04d}.{}".format(uuid,snumb,wi,ext), "wb")
        imgfile.write(response.content)
        imgfile.close() 
        print("Got {}".format(wi))
        time.sleep(2)
    
    audio_config = AudioOutputConfig(filename =  "results/{}/{:04d}/wav.wav".format(uuid,snumb))
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(sentence)

    os.system("python collage_maker.py -o results/{0}/slide-{1:04d}.png -f results/{0}/{1:04d} -w 800 -i 600".format(uuid,snumb))
    
    print('ffmpeg -loop 1 -i results/{0}/slide-{1:04d}.png -i results/{0}/{1:04d}/wav.wav -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest results/{0}/{1:04d}.mp4 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2"'.format(uuid,snumb))
    
    pngs = [x for x in os.listdir("results/{}".format(uuid)) if x[-3:]=="png"]
    
    for png in pngs:
        im = Image.open("results/{}/{}".format(uuid,png))
        im = im.resize((800, 600))
        im.save("results/{}/{}".format(uuid,png))
    print("results/{}/{}".format(uuid,png))

    os.system('ffmpeg -loop 1 -i results/{0}/slide-{1:04d}.png -i results/{0}/{1:04d}/wav.wav -c:v libx264 -tune stillimage -c:a libvo_aacenc -b:a 192k -pix_fmt yuv420p -shortest results/{0}/{1:04d}.mp4 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2"'.format(uuid,snumb))
    

    #ffmpeg -loop 1 -i image.jpg -i audio.wav -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest out.mp4
with open("results/{}/concat-list.txt".format(uuid),"w") as f:
    for i in range(snumb+1):
        f.write("file {1:04d}.mp4\n".format(uuid,i,os.getcwd()))

#os.system("ffmpeg -f concat -i {1}/results/{0}/concat-list.txt -c copy {0}.mp4".format(uuid,os.getcwd()))

os.system("run_ffmpeg.bat {}".format(uuid))
#args = ""
#for i in range(snumb+1):
#    args += "results/{0}/{1:04d}.mp4|".format(uuid,i)
#args = args.rstrip("|")
#print(args)
#os.system('ffmpeg -i "concat:{}" -c copy static/{}.mp4'.format(args,uuid))
