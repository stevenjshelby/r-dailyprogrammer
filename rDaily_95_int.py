#Python Filler Text Generator
#r/dailyprogrammer
#95 intermediate

import random

#Letter frequencies obtained from
#"http://en.algoritmy.net/article/40379/Letter-frequency-English"
FREQ = {"a":.08167,"b":.01492,"c":.02782,"d":.04253,"e":.12702,
        "f":.02228,"g":.02015,"h":.06094,"i":.06966,"j":.00153,
        "k":.00772,"l":.04025,"m":.02406,"n":.06749,"o":.07507,
        "p":.01929,"q":.00095,"r":.05987,"s":.06327,"t":.09056,
        "u":.02758,"v":.00978,"w":.02360,"x":.00150,"y":.01974,"Z":.00074}

#The key-value pair we will actually use to pick letters
FREQ_ADJ = {"a":.08167}
prev = -1
for k in FREQ.keys():
    if prev < 0:
        prev = FREQ[k]
        continue
    
    val = prev + FREQ[k]
    
    FREQ_ADJ[k] = round(val,5)
    prev = val
    
        
#Each word is made up of 1-12 chars
def word():
    word = ""
    
    l = random.randrange(1,12)
    for i in range(l):
        lc = random.random()
        
        prev = "a"
        for k in FREQ_ADJ:
            if FREQ_ADJ[k] > lc:
                word += prev
                break
            prev = k
    
    return word

#Each sentence is made up of 3-8 words
#Sentences have first word capitalized and a period at the end
def sentence():
    sentence = word().title()
    
    l = random.randrange(3,8)
    for i in range(l):
        sentence += " " + word()
        
    sentence += "."
    
    return sentence

#The argument to function is the approx number of words.
#After each sentence there is a 15% chance of a linebreak and
#an additional 50% chance of this line break being a paragraph break.
def generateFiller(approx):
    filler = ""
    
    while len(filler.split(" ")) < approx:
        filler += sentence() + " "
        
        lb = True if random.random() < .15 else False
        pb = True if random.random() < .50 else False
        
        if lb:
            filler += "\n"
        if pb:
            filler += "\n"
        
    return filler
        
        
if __name__ == '__main__':
    print generateFiller(1000)
        