import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

# pip install pyaudio
# pip install pydub
# pip install pandas
# pip install gTTS
   

# This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1 - Generate kripya dheyan dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("p-1.mp3", format="mp3")

    # 2 is from-city

    # 3 - Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("p-3.mp3", format="mp3")

    # 4 is via-city

    # 5 - Generate ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("p-5.mp3", format="mp3")

    # 6 is to-city

    # 7 - Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("p-7.mp3", format="mp3")

    # 8 is train no and name

    # 9 - Generate kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("p-9.mp3", format="mp3")

    # 10 is platform number

    # 11 - Generate par aa rahi hai
    start = 109000
    finish = 112180
    audioProcessed = audio[start:finish]
    audioProcessed.export("p-11.mp3", format="mp3")

    # 1 - may i hv ur attention pls trn no.
    start = 112000
    finish = 116000
    audioProcessed = audio[start:finish]
    audioProcessed.export("p-12.mp3", format="mp3")

    # 3 - from
    start = 122500
    finish = 123200
    audioProcessed = audio[start:finish]
    audioProcessed.export("p-14.mp3", format="mp3")
    
    # 5 - to
    start = 124000
    finish = 125000
    audioProcessed = audio[start:finish]
    audioProcessed.export("p-16.mp3", format="mp3")
    
    # 7 - via
    start = 126000
    finish = 127000
    audioProcessed = audio[start:finish]
    audioProcessed.export("p-18.mp3", format="mp3")
    
    # 9 - is arriving on platform no.
    start = 128700
    finish = 132700
    audioProcessed = audio[start:finish]
    audioProcessed.export("p-20.mp3", format="mp3")
    
def textToSpeechH(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
    
def textToSpeechE(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from-city
        textToSpeechH(item['from'], 'p-2.mp3')

        # 4 - Generate via-city
        textToSpeechH(item['via'], 'p-4.mp3')

        # 6 - Generate to-city
        textToSpeechH(item['to'], 'p-6.mp3')

        # 8 - Generate train no and name
        textToSpeechH(item['train_no'] + " " + item['train_name'], 'p-8.mp3')

        # 10 - Generate platform number
        textToSpeechH(item['platform'], 'p-10.mp3')
        
    
        # 2 - Generate train no and name
        textToSpeechE(item['train_no'] + " " + item['train_name'], 'p-13.mp3')
        
        # 4 - Generate from-city
        textToSpeechE(item['from'], 'p-15.mp3')
        
        # 6 - Generate to-city
        textToSpeechE(item['to'], 'p-17.mp3')

        # 8 - Generate via-city
        textToSpeechE(item['via'], 'p-19.mp3')

        # 10 - Generate platform number
        textToSpeechE(item['platform'], 'p-21.mp3')

        audios= [f"p-{i}.mp3" for i in range(1,22)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")
        
if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
    