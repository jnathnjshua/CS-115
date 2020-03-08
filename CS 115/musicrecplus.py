'''"I pledge my honor that I have abided by the Stevens Honor System." - Jonathan Joshua'''
import sys
pref_file = "musicrecplus.txt" 
user_to_artists = {}

def main():
    '''This will be the function that runs it all. Takes a name that you give it in the form of a username and if it’s not in user_map, then it gives back the menu.'''
    user_map = load_users(pref_file)
    username = input('Enter your name (put a $ symbol after your name if you wish your preferences to remain private):')
    if username not in user_map:
        prefs = enter_pref(username, user_map)
        save_and_quit(username, prefs, user_map, pref_file)
    return menu(username, user_map)

def menu(username, user_map):
    '''This function deals with the menu of the reccomender.''' 
    while True:
        print('Enter a letter to choose the option: ')
        print('e - Enter preferences')
        print('r - Get recommendations')
        print('p - Show most popular artists')
        print('h - How popular is the most popular')
        print('m - Which user has the most likes')
        print('q - Save and quit')
        choice = input()
        if choice == 'e':
            prefs = enter_pref(username, user_map)
            save_and_quit(username, prefs, user_map, pref_file)
        elif choice == 'r':
            recs = get_recs(username, user_map[username], user_map)
            print_recs(recs, username)
            prefs = user_map[username]
            save_and_quit(username, prefs, user_map, pref_file)
        elif choice == 'p':
            most_popular_artists(user_map)
        elif choice == 'h':
            how_popular(user_map)
        elif choice == 'm':
            most_likes(user_map)
        elif choice == 'q':
            try:
                save_and_quit(username, prefs, user_map, pref_file)
                break
            except:
                break
    
def load_users(filename):
    '''Grabs a filename and brings up a database user and the artists they like.'''
    try:
        input_file = open(filename, 'r')
    except:
        input_file = open(filename, 'w')
        input_file.close()
        return user_to_artists
    for line in input_file:
        line = line.strip()
        if len(line) == 0:
            continue
        user, artists = line.split(':')
        artists = artists.split(',')
        for i in range(len(artists)):
            artists[i] = artists[i].strip()
        user_to_artists[user] = artists
    input_file.close()
    return user_to_artists

def enter_pref(username, user_map):
    '''Allows user to enter artists that they like which will be stored in a txt file.'''
    new_pref = ''
    if username in user_map:
        prefs = user_map[username]
        new_pref = input("Enter an artist that you like (Enter to finish):")
        prefs = []
    else:
        prefs = []
        new_pref = input("Enter an artist that you like (Enter to finish):")
    while new_pref != "":
        prefs.append(new_pref.strip())
        new_pref = input("Enter an artist that you like (Enter to finish):")
    prefs.sort()
    return prefs

def save_and_quit(username, prefs, user_map, filename):
    '''Takes everything user gave, saves and quits.'''
    user_map[username] = prefs
    file = open(pref_file, 'w')
    for user in user_map:
        save = str(user) + ':' + ','.join(user_to_artists[user]) + '\n'
        file.write(save)
    file.close()

def get_recs(curr_user, prefs, user_map):
    '''Goes and looks for a recommendation that another user interests also align with.'''
    best_user = find_best_user(curr_user, prefs, user_map)
    if best_user != None:
        complete_list = list(prefs)
        for user in best_user:
            complete_list += user_map[user]
        final_list = delete_duplicates(complete_list)
        recs = drop(prefs, final_list)
    else:
        recs = []
    return recs

def print_recs(recs, username):
    '''Takes what user has given and print a recommendation, if one is found.'''
    if len(recs) == 0:
        print("No recommendations available at this time.")
    else:
        for artist in recs:
            print(artist)

def delete_duplicates(lst):
    '''Grabs a list and returns it without any repeats.'''
    artist_dict = {}
    for artist in lst:
        if artist in artist_dict:
            artist_dict[artist] += 1
        else:
            artist_dict[artist] = 1
    return list(artist_dict.keys())

def find_best_user(curr_user, prefs, user_map):
    '''Grabs users info and finds another user who shares commonalities.'''
    users = user_map.keys()
    possible_users = []
    for user in users:
        if "$" not in user:
            possible_users.append(user)
    best_user = None
    best_score = 0
    for user in possible_users:
        score = num_matches(prefs, user_map[user])
        if score > best_score and curr_user != user and prefs != user_map[user]:
            best_score = score
            best_user = [user]
        elif score == best_score and curr_user != user and prefs != user_map[user] and best_user != None:
            best_score = score
            best_user.append(user)
    return best_user

def num_matches(L1, L2):
    '''Grabs two sorted lists and returns how many matching elements their are.'''
    L1.sort()
    L2.sort()
    matches = i = j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            matches += 1
            i += 1
            j += 1
        elif L1[i] < L2[j]:
            i += 1
        else:
            j += 1
    return matches

def drop(list1, list2):
    '''Grabs two lists and give back a list with no matching elements.'''
    list1.sort()
    list2.sort()
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result

def most_likes(user_map):
    '''Takes in a user_map. Returns the user with the most likes.'''
    users = list(user_map)
    maximum = 0
    best_user = []
    for x in range(len(users)):
        if len(user_map[users[x]]) > maximum and users[x][-1] != "$":
            maximum = len(user_map[users[x]])
            best_user = [users[x]]
        if len(user_map[users[x]]) == maximum and users[x][-1] != "$":
            maximum= len(user_map[users[x]])
            best_user.append(users[x])
    if len(best_user) == 1:
        print(best_user[0])
    elif len(best_user) == 0:
        print("Sorry no artist found.")
    elif len(best_user) > 1:
        for users in best_user[1:]:
            print(users)

def most_popular_artists(user_map):
    '''Gives you the most popular artist, if there is one.'''
    user_list = user_map.keys()
    most_popular = []
    likes = {}
    maximum = 0
    possible_users = []
    for user in user_list:
        if '$' not in user:
            possible_users.append(user)
    for user in possible_users:
        for artist in user_map[user]:
            if artist in likes:
                likes[artist] += 1
            else:
                likes[artist] = 1
    for artist in likes:
        if likes[artist] > maximum:
            maximum = likes[artist]
    for artist in likes:
        if likes[artist] == maximum:
            most_popular.append(artist)
    if len(most_popular) == 1:
        print(most_popular[0])
    elif len(most_popular) == 0:
        print("Sorry no artists found.")
    else:
        for pop in most_popular:
            print(pop)
        
def how_popular(user_map):
    '''Takes in a user_map. Gives an occurence of how popular the artist is.'''
    user_list = user_map.keys()
    most_popular = []
    likes = {}
    maximum = 0
    possible_users = []
    for user in user_list:
        if '$' not in user:
            possible_users.append(user)
    for user in possible_users:
        for artist in user_map[user]:
            if artist in likes:
                likes[artist] += 1
            else:
                likes[artist] = 1
    for artist in likes:
        if likes[artist] > maximum:
            maximum = likes[artist]
    for artist in likes:
        if likes[artist] == maximum:
            most_popular.append(artist)
    if len(most_popular) == 1:
        print(maximum)
    elif len(most_popular) == 0:
        print("Sorry, no artist found.")
    else:
        print(maximum)
    
main()
