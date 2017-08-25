# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
#This program will be used to help review Statistics vocabulary
vocab_blanks = ["__1__","__2__","__3__","__4__","__5__"]

easy_vocab = " ___1___ sampling uses a chance mechanism. This avoids __2__. We __3__ because it is often difficult to conduct a __4__ . Also because\
those who __5__ in samples tend to have stronger opinions"

medium_vocab = " ___1___response sampling means that only those who volunteer to \
participate are included in the sample. __2__ sampling only samples the most convenient group. \
With __3__ random sampling,every different possible sample of the desired size has a chance of being selected.\
With __4__ random sampling, the population is first formed into non-overlapping groups called __5__ and a random sample is selected from each group"

hard_vocab = " With collecting samples there is sometimes __1__ bias. in which the sample __2__ tend to systematically differ from\
the __3__ of interest. For example, there is __4__ bias, where a subset of the sample cannot be contacted or does not respond. There is also \
__5__, where the sampling excludes part of the population."

easy_vocab_answers = ["Random","bias","sample","census","volunteer"]
medium_vocab_answers = ["Voluntary","convenience","simple","stratified","strata"]
hard_vocab_answers = ["selection","participants","population","nonresponse","undercoverage"]

game_input_substitute ={
    'easy': {
     'vocab': easy_vocab,
     'answer': easy_vocab_answers,
    },
    'medium': {
     'vocab':medium_vocab,
     'answer':medium_vocab_answers,
    },
    'hard' : {
     'vocab':hard_vocab,
     'answer':hard_vocab_answers,
    }
 } 
def difficulty_level(hardness):
        hardness = raw_input("Select a difficulty, easy, medium or hard")
        level_choice = hardness
        while  level_choice() == 'easy':
            return easy_vocab
        while level_choice () =="medium" :
            return medium_vocab,medium_vocab_answers,"A little more difficult"
        while level_choice () == "hard":
            return hard_vocab,hard_vocab_answers,"You are a true player"
        else:
                print "You've chosen a non-existent difficulty level. Now why would you do that?"
                return difficulty_level()
def difficulty_vocab_answers ():
    level_pick_answers = difficulty_level
    if level_pick_answers == easy_vocab:
        return (easy_vocab_answers)
    elif level_pick_answers == medium_vocab:
        return (medium_vocab_answers)
    elif level_pick_answers == hard_vocab:
         return (hard_vocab_answers)

def play(hardness):
    hardness = difficulty_level
    quiz = game_input_substitute[level_choice]['vocab']
    answers = game_input_substitute['answer']
    print vocab.split(".")
    player_guess = raw_input('Give an answer for the following' + vocab_blanks)
    if player_guess == answer:
        print "Nicely done"
        quiz = quiz.replace(vocab_blanks, answers)
    else:
        print "Aw, wrong"

play(hardness)

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
