#IMPORT#
import time
import math
import random
#DEFINE#
global location
global health
global turns
global str_rand_num
global current_num_path
global sleep_counter
global dragon_name
global area_name
global name_list
global inventory
global item_location_list
global itemlocation
global item_location
global item_location_dict
item_location_list = ["headpiece","weapon","shield","amulet"]
inventory = []
name_list= []
#INITIAL LISTS#
inside_choices = ['1','3','5','7','9']
used_choices = []
outside_choices = ['2','4','6','8','10']
total_options = len(inside_choices) + len(outside_choices)
enemy_names = ["Aribter","Kha'zix","Arthus", "Jiralhanee","Fleegman","Calindar","Ticonderoga","Ganondorf","Bowser","Haiecam"]
title_names = ["Lord","Sir","Guardian","Magus","Eternal","First of his name,","Duke","General","Heretic","Harold","Big Haus"]
numeral_names = ["I","II","III","IV","V","VI","VII","VIII","IX","X","first born","harbringer of death","revered","Apex predator"]
area_names = ["Morrowind","Runeterra","Tamriel","Hyrule","Azeroth","Stevenson","Lordran","Eredium","Dovakhim","Argonath","Riverglens"]
area_titles = ["Middle Earth", "Seven Kingdoms","Graet Kingdom", "Coasts of Dover","Tree of life","Great plains","Northern Kingdom"]
dragon_names = ["Patacki","Bahamut","Phalax","Fatalis","Anegulus","Alexstraza","Raquaza","Charizard","Ridley","Akatosh","Aludin","Deathwing"]
#FUNCTIONS#
def TravellingTime(time_seconds):
    time_factor = 0.5
    for x in range(0,time_seconds):
        print("...")
        time.sleep(1*time_factor)

def CheckType():
    global location
    if (location == "dungeons" or location == "caves"):
        location_type = "inside"
        return location_type
    if (location == "mountains" or location == "plains"):
        location_type = "outside"
        return location_type

def AskQuestion():
    global location
    global name_list
    global current_num_path
    location_type = CheckType()
    rand_num = '1'
    if location_type == "inside":
        rand_num = random.choice(inside_choices)
        inside_choices.remove(rand_num)
    elif location_type == "outside":
        rand_num = random.choice(outside_choices)
        outside_choices.remove(rand_num)
    str_rand_num = str(rand_num)
    current_num_path = str_rand_num
    return scenarios[str_rand_num]

def AskOption():
    global location
    global health
    global name_list
    global turns
    global current_num_path
    global sleep_counter
    print(questions[current_num_path])
    response = input("what do you do? ")
    valid_responses = [option1[current_num_path],option2[current_num_path]]
    while response not in valid_responses:
        print("Sorry, " + response + " is not in " + str(valid_responses) + "try again?")
        TravellingTime(1)
        response = input("Do what? ")
    if response == option1[current_num_path]:
        #SETTING VARIABLES FOR NEXT SCENARIO
        print(endmessage1[current_num_path])
        location = endlocation1[current_num_path]
        health = health - int(health1[current_num_path])
    if response == option2[current_num_path]:
        print(endmessage2[current_num_path])
        location = endlocation2[current_num_path]
        health = health - int(health2[current_num_path])
    CheckHealth()
    turns = turns + 1
    if sleep_counter >= 1:
        sleep_counter = sleep_counter - 1
    else:
        sleep_counter = 0
    return(location)

def NextTurn():
    if len(outside_choices) == 0 or len(inside_choices) == 0:
        StartEnding()
    else:
        next_move = input("What is your next move adventurer?  ")
        valid_responses = ["continue","check health","check location","check time","end","sleep","check inventory","equip item","check equipment"]
        while next_move not in valid_responses:
            print("Sorry, " + next_move + " is not in " + str(valid_responses) + "try again?")
            TravellingTime(1)
            next_move = input("What is your next move? ")
        DoAction(next_move)
        return()

def DoAction(next_move):
    if next_move == "continue":
        print(str(AskQuestion()))
        AskOption()
        TravellingTime(5)
        return()
    if next_move == "check health":
        print("Your current health is: " + str(health))
        return()
    if next_move == "check location":
        print("Your current location is: " + location)
        return()
    if next_move == "check time":
        if turns == 1:
            print("You have been travelling for: " + str(turns) + " hour (" + str(turns) + " scenario)!")
        elif turns >= 2:
            print("You have been travelling for: " + str(turns) + " hours (" + str(turns) + " scenarios)!")
        return()
    if next_move == "end":
        print("Exiting...")
        quit()
    if next_move == "sleep":
        Sleep()
        return()
    if next_move == "check inventory":
        print("The items in your inventory are: " + str(inventory))
        return()
    if next_move == "equip item":
        item_to_equip = input("What item would you like to equip: ")
        while item_to_equip not in inventory:
            print("Sorry, " + item_to_equip + " is not in " + str(inventory) + "try again?")
            TravellingTime(1)
            item_to_equip = input("What would you like to equip? ")
        EquipItem(item_to_equip)
        return()
    if next_move == "check equipment":
        print("Your equipment is: " + str(item_location_dict))
        return()

def EquipItem(item_to_equip):
    print("A")
    global inventory
    global item_location_list
    global itemlocation
    global item_location
    global item_location_dict
    item_area = item_location[item_to_equip]
    if item_location_dict[item_area] != "none":
        equip_response = input("Are you sure you want to equip " + item_to_equip + " instead of " + item_location_dict[item_area] + ", reply with ['yes,'no']")
        equip_responses = ["yes","no"]
        while equip_response not in equip_responses:
            print("Please respond with ['yes','no']? ")
            equip_response = input("Are you sure you want to equip " + item_to_equip + " instead of " + item_location_dict[item_area] + ", reply with ['yes,'no']")
        if equip_response == "yes":
            item_location_dict[item_area] = item_to_equip
            print("You equpped: " + item_to_equip + " as your " + item_area)
        elif equip_response == "no":
            return()
    else:
        item_location_dict[item_area] = item_to_equip
        print("You equpped: " + item_to_equip + " as your " + item_area)
        return()



def Simulate():
    while len(inside_choices) != 0 or len(outside_choices) != 0:
        NextTurn()
        TravellingTime(1)
    StartEnding()

def StartEnding():
    global location
    global health
    global name_list
    if CheckType()== "inside":
        print("You finally step outside into the light and hear the roar of a dragon!!!")
    elif CheckType() == "outside":
        print("After climbing the last foothill you see the outline of a dragon in the distance!!!")
    print("It must be... " + dragon_name + "!!!")
    end_list = ['-1','-2','-3']
    location = "dragon's lair"
    for x in end_list:
        print("Your current health is: " + str(health))
        TravellingTime(3)
        print(scenarios[x])
        TravellingTime(1)
        print(questions[x])
        end_response = input("What do you do? ")
        valid_end_responses = [option1[x],option2[x]]
        while end_response not in valid_end_responses:
            print("Sorry " + end_response + " is not in " + str(valid_end_responses))
            end_response = input("Try again? ")
        if end_response == option1[x]:
            print(endmessage1[x])
            health = health - int(health1[x])
        if end_response == option2[x]:
            print(endmessage2[x])
            health = health - int(health2[x])
        CheckHealth()
    Win()

def CheckEnding():
    if CheckType() == "inside":
        if len(inside_choices) == 0:
            return True
    elif CheckType() == "outside":
        if len(outside_choices) == 0:
            return True
    return False

def CheckHealth():
    global health
    if health <= 0:
        Die()

def Die():
    TravellingTime(3)
    print("Your health has reached 0!")
    print("Sorry, " + user_name + " you have died in the " + location + " after " + str(turns) + " hours of travel!")
    quit()

def Win():
    print("You have Won!")
    print("Congratulations " + user_name + " you were victorious in your adventure and killed " + dragon_name + " in the " + location + " after " + str(turns) + " hours of travel!")
    quit()

def CreateName(num_characters):
    global name_list
    for x in range(0,num_characters):
        name_list.append(random.choice(title_names) + " " + random.choice(enemy_names) + " the " + random.choice(numeral_names))
    return()

def Sleep():
    global sleep_counter
    global health
    if sleep_counter == 0:
        print("You light a fire and manage to sleep for the night...")
        TravellingTime(8)
        print("You feel rejuvinated for the morning and are ready to move onwards!")
        health = health + 15
        sleep_counter = sleep_counter + 3
        return()
    else:
        print("You have already slept enough, keep moving forwards!")
        return()

def PickUp(item):
    global inventory
    inventory.append(item)
    print("Congratulations " +user_name + ", you picked up: " + item)
    return()
#SCENARIOS#
    #INSIDE IS ODD
    #OUTSIDE IS EVEN
CreateName(5)
scenarios = {
'1':"The ceiling is collapsing!",
'2':"Mounted hunters are coming from over the hill",
'3':"You see a mummy coming down a corridor in front of you!",
'4':"A swarm of locusts is on the horizon!",
'5':"An undead warrior charges you with a warhammer!",
'6':"You ran into an Orc whose chestplate read: " + name_list[0],
'7':"You see an ancient Elven Rune on the wall that reads: Wubba Lubba Dub Dub....!",
'8':"You see a rainbow in the mist and a stocky creature crounching behind a small pot of gold that reads: This belongs to " + name_list[1],
'9':"An old warlock emerges from the shadows... the undead chant " + name_list[2] + " repeatedly!",
'10':"You find a creepy looking ring that reads: This belongs to " + name_list[3] + " R.I.P.",
'-1':"The dragon is sweeping down towards you!",
'-2':"The dragon retreats slightly and then prepares to breathe fire on you!",
'-3':"The dragon knocks the sword and shield out of your hand and faces you head on...but he is weak!"
}

questions = {
'1':"You can either [run back] the way you came or try to [find shelter] from the falling debris!",
'2':"You can choose to [fight the hunters] or run and [hide in a ditch]!",
'3':"You can [tackle the mummy] or try to [unravel the bandages]!",
'4':"You can try to [outrun the swarm] or [scare them] away with fire!",
'5':"You can try to [steal his warhammer] or [consume his soul]!",
'6':"You can [duel him] or [befriend him]!",
'7':"You can [touch the rune] or you can [break the rune] on the wall!",
'8':"You can [shoot an arrow] at " + name_list[1] + " or [pull out your tomahawk] and apprach him!",
'9':"You can [break his staff] or [seek his advice]!",
'10':"You can either [put the ring on] or [throw it in the creek]",
'-1':"You can [swing your sword] at it's wings or [roll to the side]!",
'-2':"You can either [block with your shield] or [charge the dragon] and surprise it!",
'-3':"You can either [jump on it's back] and stab it with your dagger or [slide below it]!"
}
option1 ={
'1':"run back",
'2':"fight the hunters",
'3':"tackle the mummy",
'4':"outrun the swarm",
'5':"steal his warhammer",
'6':"duel him",
'7':"touch the rune",
'8':"shoot an arrow",
'9':"break his staff",
'10':"put the ring on",
'-1':"swing your sword",
'-2':"block with your shield",
'-3':"jump on it's back"
}
option2 ={
'1':"find shelter",
'2':"hide in a ditch",
'3':"unravel the bandages",
'4':"scare them",
'5':"consume his soul",
'6':"befriend him",
'7':"break the rune",
'8':"pull out your tomahawk",
'9':"seek his advice",
'10':"throw it in the creek",
'-1':"roll to the side",
'-2':"charge the dragon",
'-3':"slide below it"
}
endlocation1 = {
'1':"mountains",
'2':"plains",
'3':"caves",
'4':"mountains",
'5':"caves",
'6':"caves",
'7':"mountains",
'8':"plains",
'9':"dungeons",
'10':"plains"
}
endlocation2 = {
'1':"caves",
'2':"caves",
'3':"plains",
'4':"plains",
'5':"caves",
'6':"caves",
'7':"mountains",
'8':"dungeons",
'9':"plains",
'10':"plains"
}
endmessage1 = {
'1':"You ran back the way you came through the caves and ended up outside in the mountains!",
'2':"You fought the monsters head on and sustained a few injuries but managed to get away!",
'3':"You dive head first in the mummy, stunning it! This gives you time to run onwards to where it came from!",
'4':"Outrunning the swarm won't work, there are too many!",
'5':"You tried to steal his warhammer but he slapped you instead!",
'6':"You tried to duel " + name_list[0] + " but after getting wounded you managed to run away into a cave",
'7':"You touched the rune and feel a surge of energy and decide to return outside to explore more!",
'8':"You shot an arrow and poked "  + name_list[1] + "'s eye out, the leprachuan runs toward the grassy knols and you steal his gold an then follow his path",
'9':"You broke " + name_list[2] + "'s favconorite staff and a curse falls upon you and you decide to run away!",
'10':"The ring was not cursed and actually looks nice, good find!",
'-1':"Your sword bounced of it's scales and you were knocked to the side!",
'-2':"Blocking with your shield worked and the flames slowly subside after scorching the ground around you!",
'-3':"You climb onto it's scales and find the sweet spot between it's neck and stab it, slaying the dragon!"
}
endmessage2 = {
'1':"You found a small passage leading to a deeper part of the cave!",
'2':"After crawling in the ditch for some time you found a small entrance to a cave!",
'3':"You run up and tug on the bandage spinning around the mummy, confusing it and giving you time to find an exit!",
'4':"You and your companions light a fire to scare away the locusts but it just makes them more angry...run!",
'5':"You consumed his soul and you feel revitalized!",
'6':"After befriending " + name_list[0] + " you stab him in the back in his cave and steal his elixers and eat his cabbage to feel better!",
'7':"The broken rune glows and an Elven ghost warrior screams at you causing you to run outside in panic!",
'8':"Amateur move using a tomahawk against a leprachuan\nYou move forward but fall into his trap door and look around at the dungeon around you!",
'9':"You ask the wise warlock what to do and he helps you find a way above ground",
'10':"You see a sign that reads: No Littering, \nguards see you and chase you away",
'-1':"You managed to get away in time and are ready to keep fighting the dragon!",
'-2':"As you charge the dragon it snaps its head toward you and swallows you whole!",
'-3':"As you try to slide below the dragon it stomps on your face and kills you!"
}
health1 = {
'1':"0",
'2':"20",
'3':"10",
'4':"30",
'5':"15",
'6':"40",
'7':"-10",
'8':"0",
'9':"30",
'10':"0",
'-1':"20",
'-2':"0",
'-3':"0"
}
health2 = {
'1':"0",
'2':"5",
'3':"0",
'4':"20",
'5':"-30",
'6':"25",
'7':"10",
'8':"15",
'9':"0",
'10':"5",
'-1':"0",
'-2':"200",
'-3':"200"
}
items ={
'warhammer':['100','0'],
'not cursed ring':['0','0'],
'basic shield':['5','40'],
'basic sword':['15','5'],
'shield of gold':['90','15']
}
item_location={
'warhammer':"weapon",
'not cursed ring':"amulet",
'basic shield':"shield",
'basic sword':"weapon",
'shield of gold':"shield"
}
item_location_dict={
'headpiece':"none",
'weapon':"none",
'amulet':"none",
'shield':"none"
}
#START OF STORY#
if __name__ == "__main__":
    dragon_name = ""
    dragon_name = random.choice(dragon_names) + " the " + random.choice(numeral_names)
    area_name = ""
    area_name = random.choice(area_names) + " of " + random.choice(area_titles)
    sleep_counter = 0
    TravellingTime(3)
    print("Welcome to " + area_name + ", this is a dangerous area controlled by warlocks, \nundead monsters, orcs, and most of all dragons.")
    print("A Great dragon named: " + dragon_name + " rules this land and it is your quest to defeat him!")
    TravellingTime(1)
    health = 100
    turns = 0
    command_responses = ["continue","check health","check location","check time","end","sleep","check inventory","equip item","check equipment"]
    user_name = input("So.....what is your name traveller? ")
    print("Nice to meet you " + user_name)
    PickUp("basic sword")
    PickUp("basic shield")
    location_type = ""
    TravellingTime(2)
    print("So " + user_name + ", where would you like to start your adventure?")
    location_answers = ["mountains","caves","plains","dungeons"]
    print("Answer with " + str(location_answers))
    location = input("Travel to: ")
    location = location.lower()
    while location  not in location_answers:
        print("Sorry, " + location + " is not in " + str(location_answers) + "try again?")
        TravellingTime(1)
        location = input("Travel to: ")
    TravellingTime(3)
    print("You are now in...the " + location)
    start_quote = ""
    if CheckType()== "inside":
        start_quote = "Now that you are inside and wa..."
    elif CheckType() == "outside":
        start_quote = "Now that you are outside and have some fresh a..."
    print(start_quote + "Ahhhhh!!!!!")
    TravellingTime(2)
    print(AskQuestion())
    AskOption()
    TravellingTime(2)
    print("Your current health is: " + str(health))
    TravellingTime(1)
    print("Dang! It can be dangerous out there so watch out!\nIf you need to check your health or see where you are you can use the following \ncommands " + str(command_responses))
    print("I think you can handle the rest from here...")
    TravellingTime(3)
    #MAIN#
    Simulate()
