#check if magician AND expert: "you are a master magician"
#check if magician but not expert: "at least you are getting there"
#if you are not a magician: "you need magic powers"

is_magician = False
is_expert = True

if is_magician and is_expert:
    print('You are a master magician')
elif is_magician:
    print('At least you are getting there')
else:
    print('You need magic powers')