#chatbot Ashraj Grewal cs1.0 
def get_bot_response(user_response)
bot_response_happy = ["Great! That's how you belong", "Keep the good times going!", "Good, life is too short to be anything else"]
bot_response_angry = ["Sorry to hear that, take some time to think", "Have a cup of tea!", "Go listen to some calming music"]
bot_response_sad =  ["It is okay to not be okay!", "We need to have downs to appreciate the ups", "*Virtual Hug*"]
bot_response_okay = ["being confused is natural", "use this time to think", "Do something you love to center yourself"]
if user_response == "happy":
    return choice(bot_response_happy)
  elif user_response == "angry":
    return choice(bot_response_sad)
    elif user_response == "sad":
        return choice(bot_response_sad)
    elif user_response == "okay":
        return choice(bot_response_okay)
  else:
    return "We need to feel all emotions to stay human :)"

print("Welcome to the Mood Bot")
print("How do you feel right now? Your mood:")
user_response = ""
while True:
    user_response = input ("How do you feel right now? Your mood:")
    if user_response == 'done':
    break