# -*- coding: utf-8 -*-
#vocabulary training for translating English to german
#by Miriam Kümmel
from collections import defaultdict 
import operator

#dictionaries the exercises are based on:
farmDict = {"cat": "Katze", "to work": "arbeiten", "pig": "Schwein", "cow": "Kuh", "barn": "Stall", "farmer": "Bauer", "calf": "Kalb", 
			"egg": "Ei", "chicken": "Huhn", "shovel": "Schaufel", "dog": "Hund", "tractor": "Traktor"}
schoolDict = {"blackboard": "Tafel", "chalk": "Kreide", "chair": "Stuhl", "clock": "Uhr", "teacher": "Lehrer",
				"to learn": "lernen", "break": "Pause", "language": "Sprache", "to calculate": "rechnen",
				"to write": "schreiben"}
bodyDict = {"nose": "Nase", "face": "Gesicht", "muscle": "Muskel", "hair": "Haare", "healthy": "gesund", "strong": "stark",
			"bone": "Knochen", "power": "Kraft", "to dance": "tanzen", "leg": "Bein", "heart": "Herz", "to run": "rennen",
			"to shave": "rasieren"}
holidayDict = {"sand": "Sand", "to fly": "fliegen", "beach": "Strand", "to swim": "schwimmen", "sun": "Sonne", "family": "Familie",
				"book": "Buch", "ocean": "Meer", "sunburn": "Sonnenbrand", "hotel": "Hotel", "to hike": "wandern", "mountain": "Berg",
				"to relax": "entspannen", "to play": "spielen"}

dicts = ["Farm", "School", "Body", "Holidays"]

#dicitionaries for wrong answers
tryAgainFarm = {}
tryAgainSchool = {}
tryAgainBody = {}
tryAgainHoliday = {}

global stars #global variable
stars = 0
schluss = False #will only be true if the user wants to leave the program

#welcome
print "\n\nWelcome, little dwarf! \nYou want to be the best in german vocabularies? Let us carry you off into the forests of vocabularies...once you made it through, you will be a wiser creature. Please choose:"
while not schluss:

	choice = raw_input( #user has several possibilities to start the program
			"""
			
			Wander an unknown forest - press "1"
			Leave the world of vocabularies - press "2"
			Make up for your mistakes - press "3"
			See what level you are - press "4"
			Add a new mystery to the forest - press "5"
	
			""")

#Choice 1: Exercise
	if choice == "1":
		
		#description
		print "\n\nWander around in the forests of vocabularies and collect a star whenever you solve a mystery by typing in the right translation of a word. The more stars you are gathering, the more you will develop! You did a wrong guess? Don't worry, you can make up for your mistakes later on..."
		print "Starting off, you are still a dwarf, but if you learn, study, absorb the wisdom...some day you might be the Lord of the Vocabularies..."
		print "Have an adventurous journey..."
		
		#checks if choice is in dicitionaries
		print "\nThese are the forests:", dicts
		dictsChoice = raw_input ("Which one would you like to wander? ") 
		if dictsChoice in dicts:
			print "\nYou will wander around in this forest of vocabularies:", dictsChoice, "! Please consider capitalization. Good luck!"
		else:
			print "\nThere is no forest called like this. Try again, brave wanderer."
			
		################## Function for the exercise ##################
		def abfrage(welchesDict, welchesTryAgain):
			global stars
	
			for i in welchesDict.keys():#iterates dictionary
				done = False #done only if translation is correct
				while not done:
					print "\nEnglish word:", i
					uebers = raw_input("German translation: ")
					if uebers == welchesDict[i]: #is it correct?
						print "That's correct!"
						stars += 1 #more points
						done = True
					else:
						print "Sorry, not correct!",
						print "Here is a hint:", str(welchesDict[i])[0:1], "..." #hint is first letter of translation
						uebers = raw_input("German translation: ") #nächster Versuch
						if uebers != welchesDict[i]:
							print "Here is another hint:", str(welchesDict[i])[0:3], "..." #another hint
							help = raw_input("Press x to get the complete word, press Enter if you can solve the mystery now.")
							if help == "x": #shows whole word
								print "This is the correct translation:", welchesDict.get(i), ". Type it in again!"
						else:
							print "Now the translation is correct!"
							done = True
						
						#wrong translation will be added to tryAgain so the user can try again in Choice 3
						welchesTryAgain[i] = welchesDict[i] 
						stars -= 1 #less points
						
			print "You've gathered", stars, "star(s)!" #end: all the points gathered will be shown
			if stars <= float((len(welchesDict)*0.5)): 
				print "\nYou can do better!"
			if stars <= float((len(welchesDict)*0.7)):
				print "\nKeep it up!"
			if stars > float((len(welchesDict)*0.9)):
				print "\nGreat!"
		##############################################################		
		
		#Anwendung der Funktion je nach Dictionary
		if dictsChoice == "Farm":
			abfrage(farmDict, tryAgainFarm)
		if dictsChoice == "School":
			abfrage(schoolDict, tryAgainSchool)
		if dictsChoice == "Body":
			abfrage(bodyDict, tryAgainBody)
		if dictsChoice == "Holidays":
			abfrage(holidayDict, tryAgainHoliday)
	
	
#Choice 2: leave the program
	if choice == "2":
		if stars < 10:
			print "You should come back soon. You only gathered", stars, "stars today!"
		else:
			print "Thank you for your brave journey. You've gathered", stars, "stars today!"
		schluss = True 
		
			
#Choice 3: do wrong translations again
	if choice == "3":
		if tryAgainFarm == {} and tryAgainSchool == {} and tryAgainBody == {} and tryAgainHoliday == {}:
			print "You haven't made any mistakes."
		else:
			#right translation gives the user 0.5 points now
			print "You want to make up for your mistakes. Laudable! Remember that every right guess now brings you 0.5 stars."
			
			#in which dictionary?
			newGuess = raw_input("\nIn which forest did you make mistakes? Farm, School, Body or Holidays? ")
			
			#######function for formerly wrong answers##########
			def redo(welchesTryAgain, welchesDict):
				global stars
				
				if welchesTryAgain != {}: #if there have been wrong answers the user can try again
					#iterates wrong answers
					for k in welchesTryAgain.keys():
						done = False
						while not done:
							print "\nGerman word:", k
							uebers = raw_input("Your translation: ")
							if uebers == welchesTryAgain[k]:
								print "Now your translation is correct!"
								welchesTryAgain.remove(k) #remove
								stars += 0.5
								done = True
							else:
								#if the translation is wrong again, show correct answer
								print "Sorry, still not correct! This is the correct translation:", welchesDict.get(k)
								welchesTryAgain[i] = welchesDict.get(k)
								stars -= 1
					print "You've gathered", stars, "star(s) now!" #show points
				
				else: #if there is nothing done wrong, you can't try again
					print "\nNo mistakes have been made here."	
			######################################################################
			
			#depending on user choice: which dictionary will be accessed
			if newGuess == "Farm":
				redo(tryAgainFarm, farmDict)
			if newGuess == "School":
				redo(tryAgainSchool, schoolDict)
			if newGuess == "Body":
				redo(tryAgainBody, bodyDict)
			if newGuess == "Holidays":
				redo(tryAgainHoliday, holidayDict)
			if newGuess not in dicts:
				print "\nThere is no forest named", newGuess, "."
		
	
#Choice 4: show points and level	
	if choice == "4":
		print "You've gathered", stars, "star(s) so far."
		
		#Levels:
		if stars <= 10:
			print "You are still a dwarf! Keep it up!"
		if stars >10 and stars <=15:
			print "You are a goblin already! Keep it up!"
		if stars >15 and stars <=20:
			print "Now you are a fairy! Keep it up!"
		if stars >20 and stars <=25:
			print "Wow! You are an elf! Keep it up!"
		if stars >25 and stars <=30:
			print "You can be proud! You are a sorcerer! Keep it up!"
		if stars >30:
			print "Wow! You've made it! You are the Lord of the Vocabularies!"

			
#Choice 5: add new word pair to dictionary
	if choice == "5":
		#user can only do this if he/she gathered enough points
		if stars < 21:
			print "Sorry, you are not trustworthy enough yet! Learn and gain some wisdom..."
			print "as soon as you have evolved to an elf we will welcome you here again...You still lack", (21-stars), "stars."
		else:
			print "You wish to share your wisdom? There you go..."
			
			print "To which forest do you want to add a mystery?", dicts
			newWords = raw_input("Choose: ")
			
			######### function for adding new word pairs ##########################
			def newWord(whichDict):			
				add = False #only true if user wants to leave
				while add == False:
					neueUeb = raw_input("Put in the english word: ")
					#if the word is there already it is not possible to add it again
					if neueUeb in whichDict.keys():
						print "This mystery is in this forest already."
						break
					englUeb = raw_input("Put in the german translation: ")
					whichDict[neueUeb] = englUeb #adds translation to key
					print "\n","Thank you. Your mystery", neueUeb, "has been added to the forest", newWords,":\n", whichDict, "."
					#does the user want to add more?
					more = raw_input("Do you want to put in more words? Press 'y' or 'n' ")
					if more == "n":
						add = True
			###########################################################################
			
			#use function depending on input
			if newWords == "Farm":
				newWord(farmDict)
			if newWords == "School":
				newWord(schoolDict)
			if newWords == "Body":
				newWord(bodyDict)
			if newWords == "Holidays":
				newWord(holidayDict)

				 
				
				
				
				
	