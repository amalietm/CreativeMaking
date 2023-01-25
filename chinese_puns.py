
#doesn't register divergences in tweet ex capitalized or different ending to word
#couldn't make twitter bot due to lackk of url

import openai
import random 

# remove key
API_KEY = "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"
openai.api_key = API_KEY

chinese_puns = dict({
    "insult": "paratrooper",
    "censored": "seafood",
    "censorship": "grass mud horse",
    "burned out": "lying flat",
    "social distancing": "sitting",
    "pretending to work": "touch fish",
    "google": "valley dove",
    "covid-19": "green horse",
    "get away": "run",
    "corrupt": "govern-rot",
    "stop trying to make something better": "let it rot",
    "metoo": "rice bunny",
    })

emoji = [
    "\U0001FA82", 
    "\U0001F980", 
    "\U0001F33F" + "\U0001F434", 
    "\U0001F9CE", 
    "\U0001FA91", 
    "\U0001F41F",
    "\U0001F304" + "\U0001F54A", 
    "\U0001F7E2" + "\U0001F40E", 
    "\U0001F3C3", 
    "\U0001F940", 
    "\U0001F922",
    "\U0001F35A" + "\U0001F430",
    ]

# ----- if word is paraphrased - remove

for key in chinese_puns:
  prompt_word = key

  tweet_generated = openai.Completion.create(
    model="text-davinci-003",
    max_tokens = 1000,
    prompt=("write a tweet including the word:" + prompt_word)
  )
  tweet= tweet_generated["choices"][0]["text"]

  for i in tweet:
    if prompt_word.isupper() == True:
      prompt_word.lower()
    tweet_edited = tweet.replace(prompt_word, chinese_puns[prompt_word]) 
    print(prompt_word + tweet_edited)

    if prompt_word == list(chinese_puns.keys())[0]:
      print("#" + emoji[0])
    if prompt_word == list(chinese_puns.keys())[1]:
      print("#" + emoji[1])
    if prompt_word == list(chinese_puns.keys())[2]:
      print("#" + emoji[2])
    if prompt_word == list(chinese_puns.keys())[3]:
      print("#" + emoji[3])
    if prompt_word == list(chinese_puns.keys())[4]:
      print("#" + emoji[4])
    if prompt_word == list(chinese_puns.keys())[5]:
      print("#" + emoji[5])
    if prompt_word == list(chinese_puns.keys())[6]:
      print("#" + emoji[6])
    if prompt_word == list(chinese_puns.keys())[7]:
      print("#" + emoji[7])
    if prompt_word == list(chinese_puns.keys())[8]:
      print("#" + emoji[8])
    if prompt_word == list(chinese_puns.keys())[9]:
      print("#" + emoji[9])
    if prompt_word == list(chinese_puns.keys())[10]:
      print("#" + emoji[10])
    if prompt_word == list(chinese_puns.keys())[11]:
      print("#" + emoji[11])
    break
  





