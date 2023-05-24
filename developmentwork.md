# Development Work
## Pseudocode
### 
Give a brief description to the user where they are at and a short introduction.

Welcome them to their first room and give them a brief summary about the room.

    If the user got randomized enemy attacking event, they will have to do the event and then choose what their action will be. They have to fight with what they have in their inventories
      If successful
		    Gain more inventories
	  If unsuccessful
		  If they user already have no inventories
			  It will be become negative and the user don’t get to keep their next inventory even if they want it
		  Else they lose inventories 
    Else keep going with the game and give the user the options to choose their action

Give the user options on what they can do.

    If the user choose to walk around
	   they will get to explore the space a little bit
    Else if the user choose to search
    	they will get to search the place and what they will find will be randomized
    	If the user found some objects, they get to decide if they want to keep it or not
	   	 If the user decides to keep it
		      It will be added to their inventory and they will be able to access it
	     Else if they user decides to not keep it
		    	It will not be added to their inventory
         Else
	     		Repeat the question and give a “wrong message”
      Else if the user found nothing
		    They will keep going
    Else if the user wants to check their inventories 
	  Show them the inventories 
    Else if the user choose to quit the game
    	They game will break and it will give fail and see you next time message 
    Else if the user choose to move on to solve the puzzle
    	Give the user the puzzle
      Repeat this until the user answers correctly 	
        If the user asks for hint
		  	Give them hint
    		Else the user solve it themselves
	    If the user answers the puzzle correctly
		  	Break and move to the next room and repeat the steps 
      	Else asks if the user wants hint
		  	If yes
		  		Give them hint and asks for the answer 
    			If no
		  		Let them solve it themselves and ask for the answer
    Else
    	Give the user the “wrong message” and asks for their actions again

## Code Tasks
- character class
- puzzles
- room class and child class
- empty inventories
- events class
- objects used against enemies class
- objects used to survive class
- randomizing events function
- randomizing enemies function
- pathway function
- main menu
- keep the changelog updated
- action function

## Timeline
_Brainstorm_ - until May 14th
### 
- finish proposal
- finish development work
- needs to figure out what puzzles I am doing
- figure out the outline of the game (characters, rooms, pathway, objects...)
##
_Characters/Objects/Inventories/Actions_ - until May 21nd
###
- create classes
##
_Pathway and Puzzles_ - until May 27th
###
- turn the puzzles into codes
- create classes for the room descriptions
- randomize events
##
_Finish up_ - until June 2nd
###
- perfect loops and classes
- beta testing
- alpha testing
##
_Hand in_ - until June 6th
###
- play the games a few times as a programmer and see if there's anything that can be improved
- hand in