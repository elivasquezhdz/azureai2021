# azureai2021
Azure AI Hackathon submission

# Inspiration
The fun art of creating videos slideshows, most of the time requires the tedious task of looking for images and narrating the text when necessary.

We've been inspired by the <a href="https://www.youtube.com/watch?v=Jr9sptoLvJU">carykh Automatically making YouTube videos with Google Images </a>

# What it does
This is a web app on which you paste the text , you can summarize if you want to. The app will search for Bing images, and join them. It will create text for narration with the Text to Speech API on Azure Cognitive Services.

How we built it
Develop a python web page to captureCancel changes the text to work with. Process the text with nltk and pysummarize. Look for images with the Bing API Create slides with the [collage maker repo](https://github.com/delimitry/collagemaker)_ Join the audio and slides with ffmpeg

Generate the audio with the _Text to Speech Azure API _

#Challenges we ran into
I was planning on submitting with friends help, but he could not help me, so I had to do all the work myself :(

#Accomplishments that we're proud of
Finishing on time!

#What we learned
More tools on Azure Cognitive Services

#What's next for Video Generator
Much improvement on the NLP side is needed. We can also improve the slides generation

#Usage
_pip install -r requirements_
_python manage.py_
_visit http://localhost_
or try the [live demo ](http://70.37.89.237/)

