day_of_week = input("Enter a day of week (plural) : ").capitalize()
adj = input("Enter an adjective : ").lower()
least_fav_color = input("Enter your least favourite colour : ").lower()
size = input("Enter a size (e.g. small/ medium/ big/ huge etc - use your imagination!) :").lower()
superpower = input("Enter a superpower (verb) you would love to have : ").lower()
activity = input("Enter your favourite activity : ")
song = input("Enter your favourite happy song : ").title()
fun_place = input("Enter the name of a fun place you would like to be in : ").title()
waterbody = input("Enter name of your favourite lake/ pool/ pond where you would love to splash and have fun : ").title()
number = str(input("Enter a huuuuuuuge number : "))
condiment = input("Enter your favourite condiment (best thing you love to be added to add favourite taste) : ").lower()
fam_mem_pl = input("Enter family relationships whom you find annoying (be honest!) in plural : ").lower()
famous_person = input("Enter your favourite famous personality : ").title()
trick = input("Enter a trick you would love to teach your dog/ cat/ chihuahua etc. : ").lower()
competetion = input("Enter the name of a competetion (be imaginative!) you would love to organise to have fun with your friends : ").title()
nick = input("Enter the nickname (something smart, powerful and punchy) you would call your favourite team : ").upper()

print("\n\n*" *40)
print("\n\n*********** Here Goes The Story!!! ************")


pet_rock_club = f"\n\n I am a member of a very exclusive club, where we meet on\
 {day_of_week} to play with {adj} rocks. Some people have {least_fav_color},\
 {size} rocks and some people have ones that can {superpower}. Regardless of how\
 different they are, they all {activity} together and sing '{song}' in rock language.\
 It's fun for us, their owners. We race them from the {fun_place} to the {waterbody}, take\
 {number} pictures and sometimnes paint them with {condiment}. All \
 our {fam_mem_pl} are jealous. One time, {famous_person} showed up \
 and taught the rocks how to {trick}. Now, we're planning a {competetion}\
 to see whose pet rock wins! GO {nick} GO!!!"

print(pet_rock_club)