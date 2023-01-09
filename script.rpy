# The script of the game goes in this file
# Declare characters used by this game. The color argument colorizes the
# name of the character.
# Blue colour for male characters and for general characters and Pink colour for female characters.
#0040ff- Blue
#ff00ff- Pink
default score= 0
default scorepopquiz= 0

#shs and college pop quiz
define mrpopquiz= Character("Mr.Pop Quiz", color= "#0040ff")

#images for Pop Quiz
image MrPopQuiz= im.Scale("Characters/Mr.PopQuiz.png", 650,820)

#shs
define martin = Character("Martin", color= "#0040ff")
define matthew = Character("Matthew", color= "#0040ff")
define allen = Character ("Allen", color= "#0040ff")
define teachermarites= Character("Teacher Marites", color= "#ff00ff")
define teacherkaren= Character("Teacher Karen", color= "#ff00ff")
define elevenA= Character ("11-A Students", color= "#0040ff")
define player = Character("[playername]", color= "#0040ff")

#college
define adrian= Character("Adrian", color= "#0040ff")
define christian= Character("Christian", color= "#0040ff")
define mark= Character("Mark", color= "#0040ff")
define teacherluna= Character("Teacher Luna", color= "#ff00ff")
define teacherraul= Character("Teacher Raul", color= "#0040ff")

#shs
image Martin = im.Scale("Characters/Martin.png", 650, 820)
image MatthewSweat = im.Scale("Characters/Matthew Sweat.png", 650, 820)
image Matthew= im.Scale("Characters/Matthew.png", 650,820)
image Allen= im.Scale("Characters/Allen.png", 650, 820)
image Wrichmond= im.Scale("Characters/Wrichmond.png", 650,820)
image TeacherMarites= im.Scale("Characters/TeacherMarites.png", 850,900)
image TeacherKaren= im.Scale("Characters/TeacherKaren.png", 850,900)

#college
image Adrian= im.Scale("Characters/Adrian.png", 650,820)
image Christian= im.Scale("Characters/Christian.png", 650,820)
image Mark= im.Scale("Characters/Mark.png", 650,820)
image TeacherLuna= im.Scale("Characters/TeacherLuna.png", 850,900)
image TeacherRaul= im.Scale("Characters/TeacherRaul.png", 650,820)

#QuizSHS
define Question1SHS= Character("Question 1")
define Question2SHS= Character("Question 2")
define Question3SHS= Character("Question 3")
define Question4SHS= Character("Question 4")
define Question5SHS= Character("Question 5")
define Question6SHS= Character("Question 6")
define Question7SHS= Character("Question 7")
define Question8SHS= Character("Question 8")
define Question9SHS= Character("Question 9")
define Question10SHS= Character("Question 10")

#QuizCollege
define Question1College= Character("Question 1")
define Question2College= Character("Question 2")
define Question3College= Character("Question 3")
define Question4College= Character("Question 4")
define Question5College= Character("Question 5")
define Question6College= Character("Question 6")
define Question7College= Character("Question 7")
define Question8College= Character("Question 8")
define Question9College= Character("Question 9")
define Question10College= Character("Question 10")
#
image campus = im.Scale("Places/campus2.jpg",1280,720)
image hallway = im.Scale("Places/hallway.jpg",1280,720)
image cr= im.Scale("Places/cr.jpg", 1280,720)
image cafeteria= im.Scale("Places/cafeteria.jpg", 1280,720)
image ClassroomSHS= im.Scale("Places/classroomshs.png", 1280,720)
image HouseProtag= im.Scale("Places/HouseProtag.png", 1280, 720)
image LivingRoom= im.Scale("Places/LivingRoom.jpg", 1280,720)
image Bedroom= im.Scale ("Places/Bedroom.jpg", 1280,720)
image BlackBG= im.Scale("Backgrounds/black.jpg", 1280,720)
image FoamMattress= im.Scale("FoamMattress.png", 1280,720)
image TheEnd= "The End.jpg"
image chalkboard= im.Scale("Backgrounds/Chalkboard.jpg", 1280,720)
#
image L1SHS= "SHSLessons/L1SHS.png"
image L1SHS2= "SHSLessons/L1SHS2.png"
image L1SHS3= "SHSLessons/L1SHS3.png"
image L1SHS4= "SHSLessons/L1SHS4.png"
image L1SHS5= "SHSLessons/L1SHS5.png"
image L1SHS6= "SHSLessons/L1SHS6.png"
image L1SHS7= "SHSLessons/L1SHS7.png"
image L1SHS8= "SHSLessons/L1SHS8.png"
image L1SHS9= "SHSLessons/L1SHS9.png"
image L1SHS10= "SHSLessons/L1SHS10.png"
image L1SHS11= "SHSLessons/L1SHS11.png"
image L2SHS= "SHSLessons/L2SHS.png"
image L2SHS2= "SHSLessons/L2SHS2.png"
image L2SHS3= "SHSLessons/L2SHS3.png"
image L2SHS4= "SHSLessons/L2SHS4.png"
image L2SHS5= "SHSLessons/L2SHS5.png"
image L2SHS6= "SHSLessons/L2SHS6.png"
image L2SHS7= "SHSLessons/L2SHS7.png"
image L2SHS8= "SHSLessons/L2SHS8.png"
image L2SHS9= "SHSLessons/L2SHS9.png"
image L2SHS10= "SHSLessons/L2SHS10.png"
image L2SHS11= "SHSLessons/L2SHS11.png"
image L2SHS12= "SHSLessons/L2SHS12.png"
image L2SHS13= "SHSLessons/L2SHS13.png"
image L2SHS14= "SHSLessons/L2SHS14.png"
image L2SHS15= "SHSLessons/L2SHS15.png"
image L2SHS16= "SHSLessons/L2SHS16.png"
image L2SHS17= "SHSLessons/L2SHS17.png"
image L2SHS18= "SHSLessons/L2SHS18.png"
image L3SHS= "SHSLessons/L3SHS.png"
image L3SHS2= "SHSLessons/L3SHS2.png"
image L3SHS3= "SHSLessons/L3SHS3.png"
image Mechanics1= "Mechanics1.png"
image Mechanics2= "Mechanics2.png"
#
image L1College= "CollegeLessons/L1College.png"
image L1College2= "CollegeLessons/L1College2.png"
image L1College3= "CollegeLessons/L1College3.png"
image L1College4= "CollegeLessons/L1College4.png"
image L1College5= "CollegeLessons/L1College5.png"
image L1College6= "CollegeLessons/L1College6.png"
image L1College7= "CollegeLessons/L1College7.png"
image L1College8= "CollegeLessons/L1College8.png"
image L1College9= "CollegeLessons/L1College9.png"
image L1College10= "CollegeLessons/L1College10.png"
image L1College11= "CollegeLessons/L1College11.png"
image L2College= "CollegeLessons/L2College.png"
image L2College2= "CollegeLessons/L2College2.png"
image L2College3= "CollegeLessons/L2College3.png"
image L2College4= "CollegeLessons/L2College4.png"
image L3College= "CollegeLessons/L3College.png"
image L3College2= "CollegeLessons/L3College2.png"
image L3College3= "CollegeLessons/L3College3.png"
image L3College4= "CollegeLessons/L3College4.png"


# The game starts here.
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init: ### just setting variables in advance so there are no undefined variable problems
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01),
    false=[Hide('countdown'), Jump(timer_jump)])
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve
        # ^This is the timer bar.

label start:
    #This is for inputting the player name of your choice
    python:
        playername=renpy.input("Please enter the protagonist's name: ", length=32)
        playername=playername.strip()

    #Player name by default if the player entered the game w/o inputting a playern name.
        if not playername:
            playername= "Default"


    #Grade or year level

    menu:
        "Choose your difficulty"

        "Senior High School":
            jump popquizshsprompt
        "College":
            jump popquizcollegeprompt

    return

    label popquizshsprompt:
        menu:
            "Do you want to have a pop quiz first before proceeding to the game?"

            "Yes":
                jump popquizshs
            "Skip pop quiz":
                jump shs

    label popquizshs:

            show chalkboard

            show MrPopQuiz

            mrpopquiz "In this pop quiz, you will answer 5 questions. Whether you answered all of the questions or not,
            the game will proceed so good luck and have fun."

            hide MrPopQuiz

            jump Question1PopQuizSHS

    return

    label Question1PopQuizSHS:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question1popquizshs_slow'      ### set where you want to jump once the timer runs out


        Question1SHS "Who is not a poet?"
        jump q1popquizshs
    return

    label q1popquizshs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. William Shakespeare":
                jump a1popquizshs
            "B. Oscar Wilde":
                jump b1popquizshs
            "C. Rudyard Kipling":
                jump c1popquizshs
            "D. Peter Griffin":
                jump d1popquizshs

    return


    label a1popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Peter Griffin{/b}. You may now proceed to Question no. 2."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question2PopQuizSHS
    return

    label b1popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Peter Griffin{/b}. You may now proceed to Question no. 2."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question2PopQuizSHS
    return

    label c1popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Peter Griffin{/b}. You may now proceed to Question no. 2."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question2PopQuizSHS

    return

    label d1popquizshs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 2."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump Question2PopQuizSHS
    return

    label question1popquizshs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. Peter Griffin{/b}. You may now proceed to Question no. 2."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question2PopQuizSHS
    return


    label Question2PopQuizSHS:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question2popquizshs_slow'                    ### set where you want to jump once the timer runs out


        Question2SHS "Which of the following is a pronoun?"
        jump q2popquizshs
    return

    label q2popquizshs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. He":
                jump a2popquizshs
            "B. Was":
                jump b2popquizshs
            "C. Below":
                jump c2popquizshs
            "D. Under":
                jump d2popquizshs

    return


    label a2popquizshs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 3."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump Question3PopQuizSHS
    return

    label b2popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. He{/b}. You may now proceed to Question no. 3."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question3PopQuizSHS
    return

    label c2popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. He{/b}. You may now proceed to Question no. 3."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question3PopQuizSHS

    return

    label d2popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. He{/b}. You may now proceed to Question no. 3."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question3PopQuizSHS
    return

    label question2popquizshs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. He{/b}. You may now proceed to Question no. 3."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question3PopQuizSHS
    return


    label Question3PopQuizSHS:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question3popquizshs_slow'                    ### set where you want to jump once the timer runs out


        Question3SHS "What is the past tense of leave?"
        jump q3popquizshs
    return

    label q3popquizshs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Leaved":
                jump a3popquizshs
            "B. Lived":
                jump b3popquizshs
            "C. Left":
                jump c3popquizshs
            "D. Leaves":
                jump d3popquizshs

    return

    label a3popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Left{/b}. You may now proceed to Question no. 4."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question4PopQuizSHS
    return

    label b3popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Left{/b}. You may now proceed to Question no. 4."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question4PopQuizSHS
    return

    label c3popquizshs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 4."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump Question4PopQuizSHS

    return

    label d3popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Left{/b}. You may now proceed to Question no. 4"
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question4PopQuizSHS
    return

    label question3popquizshs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Left{/b}. You may now proceed to Question no. 4."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question4PopQuizSHS
    return


    label Question4PopQuizSHS:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question4popquizshs_slow'                    ### set where you want to jump once the timer runs out


        Question4SHS "A noun that serves as the name to a specific place, person, or thing."
        jump q4popquizshs
    return

    label q4popquizshs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Common Noun":
                jump a4popquizshs
            "B. Proper Noun":
                jump b4popquizshs
            "C. Verb":
                jump c4popquizshs
            "D. Pronoun":
                jump d4popquizshs

    return


    label a4popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Proper Noun{/b}. You may now proceed to Question no. 5."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question5PopQuizSHS
    return

    label b4popquizshs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 5."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump Question5PopQuizSHS
    return

    label c4popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Proper Noun{/b}. You may now proceed to Question no. 5."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question5PopQuizSHS

    return

    label d4popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Proper Noun{/b}. You may now proceed to Question no. 5."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question5PopQuizSHS
    return

    label question4popquizshs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Proper Noun{/b}. You may now proceed to Question no. 4."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question5PopQuizSHS
    return


    label Question5PopQuizSHS:
        $ time =10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question5popquizshs_slow'                    ### set where you want to jump once the timer runs out


        Question5SHS "Who wrote the poem and/or Anglican Hymn All Things Bright and Beautiful?"
        jump q5popquizshs
    return

    label q5popquizshs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Emily Dickenson":
                jump a5popquizshs
            "B. Charlie Chaplin":
                jump b5popquizshs
            "C. Dr. Seuss":
                jump c5popquizshs
            "D. Cecil Frances Alexander":
                jump d5popquizshs

    return


    label a5popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Cecil Frances Alexander{/b}.
        And this is the end of the pop quiz, let us now see the results."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump ResultsPopQuizSHS
    return

    label b5popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Cecil Frances Alexander{/b}.
        And this is the end of the pop quiz, let us now see the results."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump ResultsPopQuizSHS
    return

    label c5popquizshs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Cecil Frances Alexander{/b}.
        And this is the end of the pop quiz, let us now see the results."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump ResultsPopQuizSHS

    return

    label d5popquizshs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! And this is the end of the pop quiz, let us
        now see the results."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump ResultsPopQuizSHS
    return

    label question5popquizshs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. Cecil Frances Alexander{/b}.
        And this is the end of the pop quiz, let us now see the results."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump ResultsPopQuizSHS
    return

    label ResultsPopQuizSHS:
        "Congratulations, player. Out of {b}5{/b} questions, you answered {b}[scorepopquiz]{/b} questions. Enjoy playing
        the rest of the game. Good luck and have fun!"

        jump shs

    return

#####For College English Pop Quiz######

    label popquizcollegeprompt:
        menu:
            "Would you like to have a pop quiz first before proceeding to the game?"

            "Yes":
                jump popquizcollege
            "Skip pop quiz":
                jump college

    label popquizcollege:

            show chalkboard

            show MrPopQuiz

            mrpopquiz "In this pop quiz, you will answer 5 questions. Whether you answered all of the questions or not,
            the game will proceed so good luck and have fun."

            hide MrPopQuiz

            jump Question1PopQuizCollege

    return

    label Question1PopQuizCollege:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question1popquizcollege_slow'                    ### set where you want to jump once the timer runs out


        Question1College "Complete this sentence:
            \nI am having dinner with ______ tonight."
        jump q1popquizcollege

    label q1popquizcollege:

        show screen countdown                          ### call and start the timer

        menu:

            "A. he":
                jump a1popquizcollege
            "B. they":
                jump b1popquizcollege
            "C. his":
                jump c1popquizcollege
            "D. him":
                jump d1popquizcollege

    return


    label a1popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. him{/b}. You may now proceed to Question no. 2."
        $ score +=0
        stop sound
        stop music
        jump Question2PopQuizCollege
    return

    label b1popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. him{/b}. You may now proceed to Question no. 2."
        $ score +=0
        stop sound
        stop music
        jump Question2PopQuizCollege
    return

    label c1popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. him{/b}. You may now proceed to Question no. 2."
        $ score +=0
        stop sound
        stop music
        jump Question2PopQuizCollege

    return

    label d1popquizcollege:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 2."
        $ score +=1
        stop sound
        stop music
        jump Question2PopQuizCollege
    return

    label question1popquizcollege_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. him{/b}. You may now proceed to Question no. 2."
        $ score +=0
        stop sound
        stop music
        jump Question2PopQuizCollege
    return


    label Question2PopQuizCollege:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question2popquizcollege_slow'                    ### set where you want to jump once the timer runs out


        Question2SHS "{u}What do you like?{/u}
        \nThis question can be used to ask about hobbies, likes, and dislikes in general."
        jump q2popquizcollege

    label q2popquizcollege:

        show screen countdown                          ### call and start the timer

        menu:

            "A. True":
                jump a2popquizcollege
            "B. False":
                jump b2popquizcollege
            "C. Maybe":
                jump c2popquizcollege
            "D. No Idea":
                jump d2popquizcollege

    return


    label a2popquizcollege:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 3."
        $ score +=1
        stop sound
        stop music
        jump Question3PopQuizCollege
    return

    label b2popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. True{/b}. You may now proceed to Question no. 3."
        $ score +=0
        stop sound
        stop music
        jump Question3PopQuizCollege
    return

    label c2popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. True{/b}. You may now proceed to Question no. 3."
        $ score +=0
        stop sound
        stop music
        jump Question3PopQuizCollege

    return

    label d2popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. True{/b}. You may now proceed to Question no. 3."
        $ score +=0
        stop sound
        stop music
        jump Question3PopQuizCollege
    return

    label question2popquizcollege_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. True{/b}. You may now proceed to Question no. 3."
        $ score +=0
        stop sound
        stop music
        jump Question3PopQuizCollege
    return


    label Question3PopQuizCollege:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question3popquizshs_slow'                    ### set where you want to jump once the timer runs out


        Question3SHS "Elizabeth Bennet is the protagonist of which Jane Austen novel?"
        jump q3popquizcollege

    label q3popquizcollege:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Little Women":
                jump a3popquizcollege
            "B. Lord of the Rings":
                jump b3popquizcollege
            "C. Pride and Prejudice":
                jump c3popquizcollege
            "D. Twilight":
                jump d3popquizcollege

    return


    label a3popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Pride and Prejudice{/b}. You may now proceed to Question no. 4."
        $ score +=0
        stop sound
        stop music
        jump Question4PopQuizCollege
    return

    label b3popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Pride and Prejudice{/b}. You may now proceed to Question no. 4."
        $ score +=0
        stop sound
        stop music
        jump Question4PopQuizCollege
    return

    label c3popquizcollege:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 4."
        $ score +=1
        stop sound
        stop music
        jump Question4PopQuizCollege

    return

    label d3popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Pride and Prejudice{/b}. You may now proceed to Question no. 4."
        $ score +=0
        stop sound
        stop music
        jump Question4PopQuizCollege
    return

    label question3popquizcollege_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Pride and Prejudice{/b}.
        You may now proceed to Question no. 4."
        $ score +=0
        stop sound
        stop music
        jump Question4PopQuizCollege
    return


    label Question4PopQuizCollege:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question4popquizcollege_slow'                    ### set where you want to jump once the timer runs out


        Question4College "What is the name of the Bible's fifth book in Old Testament?"
        jump q4popquizcollege

    label q4popquizcollege:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Genesis":
                jump a4popquizcollege
            "B. Deuteronomy":
                jump b4popquizcollege
            "C. Revelation":
                jump c4popquizcollege
            "D. Psalm":
                jump d4popquizcollege

    return


    label a4popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Deuteronomy{/b}. You may now proceed to Question no. 5."
        $ score +=0
        stop sound
        stop music
        jump Question5PopQuizCollege
    return

    label b4popquizcollege:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 5."
        $ score +=1
        stop sound
        stop music
        jump Question5PopQuizCollege
    return

    label c4popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Deuteronomy{/b}. You may now proceed to Question no. 5."
        $ score +=0
        stop sound
        stop music
        jump Question5PopQuizCollege

    return

    label d4popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Deuteronomy{/b}. You may now proceed to Question no. 5."
        $ score +=0
        stop sound
        stop music
        jump Question5PopQuizCollege
    return

    label question4popquizcollege_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Deuteronomy{/b}. You may now proceed to Question no. 4."
        $ score +=0
        stop sound
        stop music
        jump Question5PopQuizCollege
    return


    label Question5PopQuizCollege:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question5popquizcollege_slow'                    ### set where you want to jump once the timer runs out


        Question5SHS "What is the meaning of the phrase ‘Mein Kampf’ in Hitler’s
        autobiography of the same name?"
        jump q5popquizcollege

    label q5popquizcollege:

        show screen countdown                          ### call and start the timer

        menu:

            "A. My Life":
                jump a5popquizcollege
            "B. My House":
                jump b5popquizcollege
            "C. My Money":
                jump c5popquizcollege
            "D. My Struggle":
                jump d5popquizcollege

    return


    label a5popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. My Struggle{/b}.
        And this is the end of the pop quiz, let us now see the results."
        $ score +=0
        stop sound
        stop music
        jump ResultsPopQuizCollege
    return

    label b5popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. My Struggle{/b}.
        And this is the end of the pop quiz, let us now see the results."
        $ score +=0
        stop sound
        stop music
        jump ResultsPopQuizCollege
    return

    label c5popquizcollege:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. My Struggle{/b}.
        And this is the end of the pop quiz, let us now see the results."
        $ score +=0
        stop sound
        stop music
        jump ResultsPopQuizCollege

    return

    label d5popquizcollege:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! And this is the end of the pop quiz, let us
        now see the results."
        $ score +=1
        stop sound
        stop music
        jump ResultsPopQuizCollege
    return

    label question5popquizcollege_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. My Struggle{/b}.
        And this is the end of the pop quiz, let us now see the results."
        $ score +=0
        stop sound
        stop music
        jump ResultsPopQuizCollege
    return

    label ResultsPopQuizCollege:
        "Congratulations, player. Out of {b}5{/b} questions, you answered {b}[score]{/b} questions. Enjoy playing
        the rest of the game. Good luck and have fun!"

        jump college

    return


    label shs:

        #So this will tackle the scenario of SHS once you chose SHS as your difficulty.

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)
        scene campus

        "There are four friends named Martin, Matthew, Allen, and [playername]. They went to school together today.
        All of them are grade 11 Senior High School students at Belridge Senior High School and they belong to 11-A class."

        stop music

        $renpy.sound.play("audio/Japanese School Bell.mp3", loop=True)

        "(The bell rings)"

        "All students of Belridge Senior High School. Please come to your respective classrooms.
        Your classes will start in 10 minutes."

        stop sound

        play music "audio/The 126ers - End Of Summer Instrumental Extended.mp3"

        show Allen

        allen "Oh, man. We're gonna be late. What are we going to do?"

        hide Allen

        menu:

            "What are they going to do?"

            "Go to the classroom early":
                jump classroom
            "Go to the cafeteria":
                jump cafeteria
            "Go to the comfort room":
                jump CR


        label classroom:

            show Martin

            martin "Alright, guys, let's race our way to the classroom as fast as we can."

            hide Martin

            $renpy.sound.play("audio/Running.mp3", loop=True)

            "The four of them began running all the way to their classroom."

            hide campus

            show hallway

            $renpy.sound.play("audio/Running.mp3", loop=True)

            allen "Look, we're almost there. Let's keep running."

            "They kept running all the way to their classroom."

            stop sound

            "And finally, they made it."

            hide hallway

            stop music

            show black

            play sound "audio/Door Open and Door Close.mp3"

            "(Door opens and closes)"

            stop sound

            hide black

            jump classroomSHS

        return

    label cafeteria:

        player "Since we have 10 minutes before the class starts, would you guys like to accompany me in buying food?"

        show Matthew

        matthew "Hell no!"

        hide Matthew

        show Martin

        martin "You are not a child anymore, man. You can already take care of yourself."

        hide Martin

        show Allen

        allen "It's a no for me."

        hide Allen

        player "Oh, come on! Are you guys really my friends?! Alright, I'll treat you all at the cafeteria,
        but please, let's
        go to the cafeteria together."

        "And they all agreed to go to the cafeteria together."

        hide campus

        show cafeteria

        "After they went to the cafeteria to buy food, they went out and hurriedly went to the classroom."

        hide cafeteria

        show hallway

        $renpy.sound.play("audio/Running.mp3", loop=True)

        allen "Look, we're almost there. Let's keep running."

        "They kept running all the way to their classroom."

        stop sound

        "And finally, they made it."

        hide hallway

        stop music

        show black

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        jump classroomSHS

        jump campusSHS

    return

    label CR:

        "Suddenly, [playername] felt the nature's call."

        player "I need to go to the comfort room. Please wait for me."

        show Allen

        allen "[playername], we're not going to wait for you in the comfort room. We will accompany you instead.
        That's what friends are for, right?"

        hide Allen

        player "Alright then. Let's go."

        "And they went to the comfort room."

        hide campus2

        stop music

        $renpy.sound.play("audio/toilet music.mp3", loop=True)

        show cr

        "[playername] has to stay inside the cubicle toilet a bit longer while
        Matthew, Allen, and Martin will wait for him in the comfort room."

        show Martin

        martin "I think [playername] will take a while in answering the nature's call."

        hide Martin

        show Matthew

        matthew "Well, it seems like [playername] ate a lot of breakfast a while ago before going to school."

        hide Matthew

        show Allen

        allen "Can't blame [playername] about that though if that's the sole reason why. We should wait a little
        bit longer."

        hide Allen

        "After a long time of waiting, [playername] was able to finish answering the call of the nature. [playername] wore his
        pants and his belt on."

        $renpy.sound.play("audio/toilet flush.mp3", loop=True)

        "([playername] flushes the toilet)"

        stop sound

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        "And [playername] went out of the toilet cubicle."

        player "Phew! I feel relieved, guys. Thank you for waiting for me to finish taking a dump."

        show Martin

        martin "No problem, man."

        hide Martin

        "(Martin checked the time on his phone)"

        show Martin

        martin "It's already 7:55. We should hurry to the classroom now!"

        hide Martin

        show Allen

        allen "Sir, yes, sir!"

        hide Allen

        "And they went out of the comfort room to go to their classroom."

        hide cr

        show hallway

        $renpy.sound.play("audio/Running.mp3", loop=True)

        allen "Look, we're almost there. Let's keep running."

        "They kept running all the way to their classroom."

        stop sound

        "And finally, they made it."

        hide hallway

        stop music

        show black

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        jump classroomSHS

    return

    label classroomSHS:

        show classroomshs

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show MatthewSweat

        matthew "Phew! That was tiring."

        hide MatthewSweat

        "Matthew wiped his sweat with his handkerchief and he checked the time on his wristwatch afterwards."

        show Matthew

        matthew "Good thing, we're not yet late. Our class will start at 8:00, but the time is 7:53."

        matthew "So we have seven minutes before the start of our class."

        hide Matthew

        player "Anyway, we should take our seats now."

        show Allen

        allen "Right, we should do that."

        hide Allen

        "[playername], Matthew, Allen, and Martin took their respective seats. At 8:00, their English teacher
    came inside the classroom. She walked towards her table and put down her things.
    Afterwards, she walked in front of the table and started greeting the class."

        show TeacherMarites

        teachermarites "Good morning, 11-A students."

        hide TeacherMarites

        elevenA "Good morning, teacher."

        show TeacherMarites

        teachermarites "I have an announcement to tell so please listen carefully."

        teachermarites "Since we were able to finish our lessons for this week, we won't have an English class
    today. However, we will have a quiz about those lessons tomorrow."

        hide TeacherMarites

        player "Huh??!!!! But, teacher, we only finished discussing those English lessons yesterday."

        show TeacherMarites

        teachermarites "Oh, come on, Mr. [playername]. I've decided to test your knowledge through your tomorrow's quiz
    because I want to see whether all of you learned anything from this class or not."

        teachermarites "Anyway, I will dismiss you early now so you can use your
    free time to study your lessons or to do something else. See you tomorrow, class."

        hide TeacherMarites

        elevenA "See you tomorrow, teacher."

        "Teacher Marites left the classroom immediately. Afterwards, the students left the classroom as well except for
    [playername], Martin, Matthew, and Allen."

        player "Yo! Do you like to study English with me in my house for our quiz tomorrow later after school?"

        show Matthew

        matthew "Sure thing, man. That would be nice."

        hide Matthew

        show Martin

        martin "Besides, studying is not complete without free food, right, [playername]?"

        hide Martin

        show Allen

        allen "Martin, here you go again with your desire to eat food. I think there's a dragon in your stomach, man."

        hide Allen

        show Martin

        martin "Shut it, Allen. I just want to eat while studying. I cannot gain knowledge without food, bro."

        hide Martin

        player "Alright then. It's decided. Don't forget it, okay?"

        "They spent the entire vacant time playing Dark Legends together while waiting for the vacant time to end."

        "At 1:00 p.m., the vacant time was over so their classmates went back to the classroom."

        "A few seconds later, Teacher Karen went inside the classroom and it's time for the entire class to endure
        her boring Math class."

        elevenA "Good afternoon, Teacher Karen."

        show TeacherKaren

        teacherkaren "Good afternoon, students. Our new lesson for today is about algebra."

        hide TeacherKaren

        show Matthew

        matthew "Here we go again."

        hide Matthew

        "They have to endure the boredom until 2:30 p.m. I hope they will be okay throughout the lesson."

        "They went to school so they have to listen to the teacher because that is their responsibility as a student
        no matter how boring the class is."

        stop music

        $renpy.sound.play("audio/Japanese School Bell.mp3", loop=True)

        "At 2:30 p.m., the bell rang again."

        stop sound

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show TeacherKaren

        teacherkaren "Okay, class. You may now dismiss. Goodbye, class."

        hide TeacherKaren

        elevenA "Goodbye, teacher."

        "Teacher Karen and the students of 11-A left the classroom."

        hide classroomshs

        jump campusSHS

    return

    label campusSHS:

        show campus

        player "Finally, school's over."

        show Matthew

        matthew "Yeah, it's already over. We were able to endure the boredom of her class this afternoon."

        hide Matthew

        player "Good thing I can finally go home and play video games for the rest of the day."

        show Martin

        martin "Wait, what? I thought we're going to study for our English quiz tomorrow at your house, remember?"

        hide Martin

        show Matthew

        matthew "Yeah, he's right. Studying for tomorrow's quiz comes first before video games, man."

        hide Matthew

        player "Oh, my bad. We're supposed to study English when we get to my house. But, Martin, I am sure you like
    eating better than studying."

        show Martin

        martin "Give me a break, [playername]. Studying gets better when there's food so deal with it!"

        hide Martin

        player "Relax, Martin, relax. I'm just joking around here, man. Anyway, let's go to my house."

        "And they began walking to [playername]'s home."

        hide campus

        jump shslessons

    return

    label shslessons:

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show HouseProtag

        "After 10 minutes of walking, they were able to make it to [playername]'s house."

        show Martin

        martin "And so we finally made it, everyone. So, [playername], are your parents around?"

        hide Martin

        player "No, they're not here. They went out of town for work, but they will be back after 3 days."

        show Matthew

        matthew "So when did they leave?"

        hide Matthew

        player "They left early in the morning before I went to school."

        show Matthew

        matthew "Oh, I see."

        hide Matthew

        player "Anyway, let's go inside my house."

        "[playername] took the house keys in the backpack and unlocked the door to their house.
        After unlocking the door, they went inside the house."

        hide HouseProtag

        show black

        stop music

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show LivingRoom

        "So this is what the [playername]'s living room looks like."

        "To be honest, this living room looks beautiful in the eyes despite that it is
        simple as the way it is. Well, I can say that I do believe that simplicity is beauty."

        show Allen

        allen "It was quite a tiring day today. Forcing ourselves to study for tomorrow's quiz at this point
        is not effective."

        hide Allen

        show Martin

        martin "Allen's right. It will be better for us to take a rest first before eating and studying."

        hide Martin

        player "Yeah, that is really a good idea, Allen. We better go to my bedroom and start resting."

        "They all went to [playername]'s bedroom to rest and Matthew closed the door."

        hide LivingRoom

        show Bedroom

        player "So as usual, I still use the same bed so only 2 people can sleep in my bed,
        but Martin and I can get the foam mattress in the storage room. Matthew, don't close the door after
        we leave."

        "[playername] opened the door again."

        show Matthew

        matthew "Alright then. We'll just wait here as usual."

        hide Matthew

        "[playername] and Martin left the bedroom to get the foam mattress in the storage room.
        While Allen and Matthew, on the other hand, started having a conversation."

        show Allen

        allen "Matthew, to be honest, I doubt I will be able to pass our English quiz tomorrow.
        That is because I think it is very hard for me to learn our English lessons.
        This is ironic for me as someone who can speak English fluently."

        hide Allen

        show Matthew

        matthew "Allen, I know that it must have been hard for you to learn that subject, but I believe in you.
        I believe that you can do it uh... I mean, you can pass the tomorrow's quiz."

        matthew "Whether you're good at something or not, what matters the most is that you put your effort in doing
        your best."

        matthew "In fact, there is nothing wrong in trying until you succeed."

        matthew "That is because in school, you're not going to study one thing."

        matthew "You will be studying a lot of things and you have to do your best even if the results may turn out well
        or not because what matters the most is that you tried to persevere enough to make an effort in doing your best
        in everything that you do regardless of how important a certain task is."

        matthew "In my case, I wasn't really good at English before, but my teacher told me to keep trying to put a lot of
        effort in learning it"

        matthew "so in the end,
        I was able to improve my skills in English even though there will always be a room for me to make mistakes
        because my English is still not perfect after all."

        hide Matthew

        "Well, that reminds me of one of my junior high school teachers because she used to tell this kind of advice in our
        class before and I still remember and live with this advice of hers until now."

        "To be honest, that advice helped me to persevere in life whether in studies or in other things. Thanks, teacher.
        \n-Wrichmond"

        show Allen

        allen "Wow, that's good to hear, man. It is good to know that I have learned a lot of things from you.
        What I've learned from you today made me realize and understand the importance of putting effort into something."

        allen "Well anyway, thanks for the advice, man."

        hide Allen

        show Matthew

        matthew "No problem, man."

        hide Matthew

        "[playername] and Martin went back to the bedroom with the foam mattress."

        show Bedroom

        show FoamMattress

        window hide

        pause

        hide FoamMattress

        show Allen

        allen "Finally, they're here with the foam mattress."

        hide Allen

        "[playername] and Martin put down the foam mattress."

        player "And since we have the foam mattress here, we can now finally rest for an hour."

        "And so they decided to take a rest for an hour. Matthew and Allen slept on the foam mattress while [playername]
        and Martin slept on [playername]'s bed."

        stop music

        show black

        "After resting for an hour, they woke up and stretched their body."

        hide black

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show Bedroom

        player "(yawns)"

        martin "(yawns)"

        allen "(yawns)"

        matthew "(yawns)"

        show Allen

        allen "Alright, listen up. I have to say something."

        hide Allen

        player "What is it, Allen?"

        show Allen

        allen "Ok so here's the deal: we will eat together at Rowan's Diner after school.
        Regardless of the scores that we get, always remember that what matters the most is that we did our best
        on that day."

        hide Allen

        show Matthew

        matthew "Oh, well, I can't deny that Allen's idea is indeed a great idea. He is smart as Albert Einstein, man so
        I agree with him here."

        hide Matthew

        show Martin

        martin "Same."

        hide Martin

        player "Me too."

        show Matthew

        matthew "That's good to hear, guys. So what are we waiting for? Let's study!!!!!!"

        hide Matthew

        "Okay, player. Before you proceed to the quiz day of [playername], Adrian, Mark, and Christian, I want you
        to help [playername] to get the best score possible for tomorrow's quiz. The [playername]'s fate
        for tomorrow's quiz is in your hands now so you better learn the lessons right away, ok?"

        menu:
            "Yes, man. It's time for me to study!":
                jump study

            "No way highway!":
                jump noway

    return

    label study:

        show Bedroom

        "Okay so you have finally decided to study, player. In that case,
        I will be providing you the images of the lessons that you
        need to learn. Good luck and happy studying!"

        jump studychoicesSHS

    return

    label studychoicesSHS:

        default L1SHSx= False
        default L2SHSy= False
        default L3SHSz= False

        hide black

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show Bedroom

        menu:
            "Which of the following lessons should you study?"

            "Lesson 1: Fundamental Considerations on Text Production and Consumption" if not L1SHSx:
                $ L1SHSx= True
                jump L1SHS

            "Lesson 2: Note Taking and Citation" if not L2SHSy:
                $ L2SHSy= True
                jump L2SHS

            "Lesson 3: The Reaction Paper, Review, and Critique" if not L3SHSz:
                $ L3SHSz= True
                jump L3SHS

            "Call it a day":
                jump ready

    return

    label noway:
        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show Bedroom

        player "Unfortunately, I lost the drive to study today even if I feel like I want to study a while ago."

        "And this is the response of the [playername]'s friends in unison:"

        "Same here!"

        player "That's awesome. That is unexpected for sure. So what should we do today that does not include
        studying?"

        menu:

            "Play computer games":
                jump computergames

            "Watch movies together":
                jump movie

    return

    label computergames:

        show Bedroom

        "[playername] turned on the computer."

        "And so they played computer games for the rest of the day until the friends of [playername] decided to go home
        when evening came."

        hide Bedroom

        show black

        "They ended the day without studying for their tomorrow's quiz."

        "Playing games is a fun thing to do. However, if you have to study for your tomorrow's quiz or exam,
        you better study first before playing games."

        "Games will always be there so always focus on more important things.
        \n-Wrichmond"

        hide black

        jump quizdaySHS

    return

    label movie:

        show Bedroom

        "[playername] turned on the computer and opened the RedFlix app."

        "And so they watched movies together for the rest of the day until the friends of [playername]
        decided to go home when evening came."

        hide Bedroom

        show black

        "They ended the day without studying for their tomorrow's quiz."

        "Watching movies is a fun thing to do. However, if you have to study for your tomorrow's quiz or exam,
        you better study first before playing games."

        "Movies will always be there so always focus on more important things.
        \n-Wrichmond"

        hide black

        jump quizdaySHS

    label L1SHS:

        stop music

        $renpy.music.play("audio/Good Friends- Yasper.mp3", loop=True)

        hide Bedroom

        scene backgroundlesson

        show L1SHS

        window hide

        pause

        hide L1SHS


        show L1SHS2

        window hide

        pause

        hide L1SHS2


        show L1SHS3

        window hide

        pause

        hide L1SHS3


        show L1SHS4

        window hide

        pause

        hide L1SHS4


        show L1SHS5

        window hide

        pause

        hide L1SHS5


        show L1SHS6

        window hide

        pause

        hide L1SHS6


        show L1SHS7

        window hide

        pause

        hide L1SHS7


        show L1SHS8

        window hide

        pause

        hide L1SHS8


        show L1SHS9

        window hide

        pause

        hide L1SHS9


        show L1SHS10

        window hide

        pause

        hide L1SHS10


        show L1SHS11

        window hide

        pause

        hide L1SHS11

        stop music

        show black

        "You may now proceed to the next lesson."

        jump studychoicesSHS

    return

    label L2SHS:

        stop music

        $renpy.music.play("audio/Glimlip - S h e.mp3", loop=True)

        hide Bedroom

        show L2SHS

        window hide

        pause

        hide L2SHS


        show L2SHS2

        window hide

        pause

        hide L2SHS2


        show L2SHS3

        window hide

        pause

        hide L2SHS3


        show L2SHS4

        window hide

        pause

        hide L2SHS4


        show L2SHS5

        window hide

        pause

        hide L2SHS5


        show L2SHS6

        window hide

        pause

        hide L2SHS6


        show L2SHS7

        window hide

        pause

        hide L2SHS7


        show L2SHS8

        window hide

        pause

        hide L2SHS8

        show L2SHS9

        window hide

        pause

        hide L2SHS9


        show L2SHS10

        window hide

        pause

        hide L2SHS10


        show L2SHS11

        window hide

        pause

        hide L2SHS11


        show L2SHS12

        window hide

        pause

        hide L2SHS12


        show L2SHS13

        window hide

        pause

        hide L2SHS13


        show L2SHS14

        window hide

        pause

        hide L2SHS14


        show L2SHS15

        window hide

        pause

        hide L2SHS15


        show L2SHS16

        window hide

        pause

        hide L2SHS16


        show L2SHS17

        window hide

        pause

        hide L2SHS17


        show L2SHS18

        window hide

        pause

        hide L2SHS18

        stop music

        show black

        "You may now proceed to the next lesson."

        jump studychoicesSHS

    return

    label L3SHS:

        stop music

        $renpy.music.play("audio/DLJ - Deep Sleep ft. TABAL.mp3", loop=True)

        hide Bedroom

        show L3SHS

        window hide

        pause

        hide L3SHS


        show L3SHS2

        window hide

        pause

        hide L3SHS2


        show L3SHS3

        window hide

        pause

        hide L3SHS3

        stop music

        show black

        "You may now proceed to the next lesson."

        jump studychoicesSHS

    return

    label ready:
        "And so [playername] and friends finally finished studying for tomorrow's quiz. Player,
        thank you for studying the lessons as well."

        show Martin

        martin "Okay, [playername], it's time for us to go home. We need to go home immediately
        before it gets dark. Goodbye, [playername]. See you tomorrow."

        hide Martin

        player "Goodbye, my friends. See you tomorrow at school. Let us do our best tomorrow."

        show Matthew

        matthew "Alright then, goodbye."

        hide Matthew

        "And so the day has ended that way. We may never know what lies ahead, but we should keep on going and
        we should also do our best."

        stop music

        hide Bedroom

        show black

        "Good luck on your quiz, [playername], Martin, Matthew, and Allen"

        hide black

        jump quizdaySHS

    return

    label quizdaySHS:
        show black

        "The next day"

        hide black

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show classroomshs

        show TeacherMarites

        teachermarites "Good morning, students. Today is your quiz day. Once I gave the quiz sheets to all of you,
        you may now start answering the questions provided. Do your best and good luck."

        hide TeacherMarites

        "Teacher Marites gave the quiz sheets to the students."

        "Okay, player. I will present to you the mechanics of this game so please read and follow the
        mechanics of this game. Thank you."

        hide classroomshs

        show Mechanics1

        window hide

        pause

        hide Mechanics1

        show Mechanics2

        window hide

        pause

        hide Mechanics2

        show classroomshs

        show TeacherMarites

        teachermarites "Okay, you may now start answering."

        hide TeacherMarites

        "Since you are about to take the quiz, you won't hear any background music until the end of the quiz."

        "That is because usually, when you take your in school, you have to take it quietly."

        stop music

        jump Question1SHS

    label Question1SHS:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question1shs_slow'                    ### set where you want to jump once the timer runs out


        Question1SHS "These are words and phrases that you can use in your text in order to guide the reader along."
        jump q1shs
    return

    label q1shs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Academic Writing":
                jump a1shs
            "B. Formal Writing":
                jump b1shs
            "C. Signposts":
                jump c1shs
            "D. Academic Language":
                jump d1shs

    return


    label a1shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Signposts{/b}. You may now proceed to Question no. 2."
        $ score +=0
        stop sound
        stop music
        jump Question2SHS
    return

    label b1shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Signposts{/b}. You may now proceed to Question no. 2."
        $ score +=0
        stop sound
        stop music
        jump Question2SHS
    return

    label c1shs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 2."
        $ score +=1
        stop sound
        stop music
        jump Question2SHS

    return

    label d1shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Signposts{/b}. You may now proceed to Question no. 2."
        $ score +=0
        stop sound
        stop music
        jump Question2SHS
    return

    label question1shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Signposts{/b}. You may now proceed to Question no. 2."
        $ score +=0
        stop sound
        stop music
        jump Question2SHS
    return



    label Question2SHS:
        hide screen countdown
        $ time = 10                                   ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question2shs_slow'                    ### set where you want to jump once the timer runs out

        Question2SHS "It has a unique set of rules: it should be explicit,
        formal and factual as well as objective and analytical in nature."

        jump q2shs
    return

    label q2shs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Formal Writing":
                jump a2shs
            "B. Academic Writing":
                jump b2shs
            "C. Academic Language":
                jump c2shs
            "D. Structure":
                jump d2shs

    return

    label a2shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Academic Language{/b}. You may now proceed to Question no. 3."
        $ score +=0
        stop sound
        stop music
        jump Question3SHS
    return

    label b2shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Academic Language{/b}. You may now proceed to Question no. 3."
        $ score +=0
        stop sound
        stop music
        jump Question3SHS
    return

    label c2shs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 3."
        $ score +=1
        stop sound
        stop music
        jump Question3SHS
    return

    label d2shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Academic Language{/b}.
        You may now proceed to Question no. 3."
        $ score +=0
        stop sound
        stop music
        jump Question3SHS
    return

    label question2shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Academic Language{/b}.
        You may now proceed to Question no. 3."
        $ score +=0
        stop sound
        stop music
        jump Question3SHS
    return




    label Question3SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                            ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question3shs_slow'                    ### set where you want to jump once the timer runs out

        Question3SHS "The verbs are made central as they denote action."
        jump q3shs
    return

    label q3shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. Nominalization":
                jump a3shs
            "B. Passivization":
                jump b3shs
            "C. Explicitness":
                jump c3shs
            "D. Objectivity":
                jump d3shs

    return

    label a3shs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 4."
        $ score +=1
        stop sound
        stop music
        jump Question4SHS
    return

    label b3shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Nominalization{/b}. You may now proceed to Question no. 4."
        $ score +=0
        stop sound
        stop music
        jump Question4SHS
    return

    label c3shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Nominalization{/b}. You may now proceed to Question no. 4."
        $ score +=0
        stop sound
        stop music
        jump Question4SHS
    return

    label d3shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Nominalization{/b}. You may now proceed to Question no. 4."
        $ score +=0
        stop sound
        stop music
        jump Question4SHS
    return

    label question3shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Nominalization{/b}.
        You may now proceed to Question no. 4."
        $ score +=0
        stop sound
        stop music
        jump Question4SHS
        stop music
    return



    label Question4SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                             ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question4shs_slow'                    ### set where you want to jump once the timer runs out

        Question4SHS "Which of the following is true about Academic Writing?"
        jump q4shs
    return

    label q4shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. It requires considerable effort to construct meaningful sentences,
            paragraphs, and arguments that make the text easy to comprehend.":
                jump a4shs
            "B. It reflects your dignified stance in writing as a member of the academic community.":
                jump b4shs
            "C. It is used to avoid redundancy.":
                jump c4shs
            "D. It is based on research and not on the writer’s own opinion about a given topic.":
                jump d4shs

    return

    label a4shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. It is based on research and
        not on the writer’s own opinion about a given topic.{/b}You may now proceed to Question no. 5."
        $ score +=0
        stop sound
        stop music
        jump Question5SHS
    return

    label b4shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. It is based on research and
        not on the writer’s own opinion about a given topic.{/b}You may now proceed to Question no. 5."
        $ score +=0
        stop sound
        stop music
        jump Question5SHS
    return

    label c4shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. It is based on research and
        not on the writer’s own opinion about a given topic.{/b}You may now proceed to Question no. 5."
        $ score +=0
        stop sound
        stop music
        jump Question5SHS
    return

    label d4shs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 5."
        $ score +=1
        stop sound
        stop music
        jump Question5SHS
    return

    label question4shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. It is based on research and
        not on the writer’s own opinion about a given topic.{/b}You may now proceed to Question no. 5."
        $ score +=0
        stop sound
        stop music
        jump Question5SHS
    return



    label Question5SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question5shs_slow'                    ### set where you want to jump once the timer runs out

        Question5SHS "In note-taking, it is one of the simplest and most common ways to take notes.
        Points and keywords are written down in a hierarchical structure."
        jump q5shs
    return

    label q5shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. Charting":
                jump a5shs
            "B. Outlining ":
                jump b5shs
            "C. Mapping":
                jump c5shs
            "D. Plagiarism":
                jump d5shs

    return

    label a5shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Outlining{/b}. You may now proceed to Question no. 6."
        $ score +=0
        stop sound
        stop music
        jump Question6SHS
    return

    label b5shs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 6."
        $ score +=1
        stop sound
        stop music
        jump Question6SHS
    return

    label c5shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Outlining{/b}. You may now proceed to Question no. 6."
        $ score +=0
        stop sound
        stop music
        jump Question6SHS
    return

    label d5shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Outlining{/b}. You may now proceed to Question no. 6."
        $ score +=0
        stop sound
        stop music
        jump Question6SHS
    return

    label question5shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Outlining{/b}. You may now proceed to Question no. 6."
        $ score +=0
        stop sound
        stop music
        jump Question6SHS
    return



    label Question6SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question6shs_slow'                    ### set where you want to jump once the timer runs out

        Question6SHS "What does SQ4R as a method of note-taking stands for?"
        jump q6shs
    return

    label q6shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. Survey, Quality, Realism, Recitation, Reliable, Review":
                jump a6shs
            "B. Service, Quality, Read, Recital, Review, Respectful":
                jump b6shs
            "C. Salmon, Queen, Rider, Rangers, Reload, Rendering":
                jump c6shs
            "D. Survey, Questions, Read, Recite, Relate, Review":
                jump d6shs

    return

    label a6shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Survey, Questions, Read, Recite, Relate, Review{/b}.
        You may now proceed to Question no. 7."
        $ score +=0
        stop sound
        stop music
        jump Question7SHS
    return

    label b6shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Survey, Questions, Read, Recite, Relate, Review{/b}.
        You may now proceed to Question no. 7."
        $ score +=0
        stop sound
        stop music
        jump Question7SHS
    return

    label c6shs:
        hide screen countdown
        play sound "audio/Wrong answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Survey, Questions, Read, Recite, Relate, Review{/b}.
        You may now proceed to Question no. 7."
        $ score +=0
        stop sound
        stop music
        jump Question7SHS
    return

    label d6shs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 7."
        $ score +=1
        stop sound
        stop music
        jump Question7SHS
    return

    label question6shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. Survey, Questions, Read, Recite, Relate, Review{/b}.
        You may now proceed to Question no. 7."
        $ score +=0
        stop sound
        stop music
        jump Question7SHS
    return



    label Question7SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question7shs_slow'                    ### set where you want to jump once the timer runs out

        Question7SHS "Who popularized the Cornell Notes or Cornell Notes System?"
        jump q7shs
    return

    label q7shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. Walter Pauk":
                jump a7shs
            "B. James Sunderland":
                jump b7shs
            "C. Heather Mason":
                jump c7shs
            "D. Harry Mason":
                jump d7shs

    return

    label a7shs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 8."
        $ score +=1
        stop sound
        stop music
        jump Question8SHS
    return

    label b7shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Walter Pauk{/b}. You may now proceed to Question no. 8."
        $ score +=0
        stop sound
        stop music
        jump Question8SHS
    return

    label c7shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Walter Pauk{/b}. You may now proceed to Question no. 8."
        $ score +=0
        stop sound
        jump Question8SHS
    return

    label d7shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Walter Pauk{/b}. You may now proceed to Question no. 8."
        $ score +=0
        stop sound
        stop music
        jump Question8SHS
    return

    label question7shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Walter Pauk{/b}.
        You may now proceed to Question no. 8."
        $ score +=0
        stop sound
        stop music
        jump Question8SHS
    return



    label Question8SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question8shs_slow'                    ### set where you want to jump once the timer runs out

        Question8SHS "When you’re writing a reaction about what
        you have seen or experienced, that would be classified as _____________________"
        jump q8shs
    return

    label q8shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. Tissue Paper":
                jump a8shs
            "B. Review Paper":
                jump b8shs
            "C. Reaction paper":
                jump c8shs
            "D. I have no idea.":
                jump d8shs

    return

    label a8shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Reaction paper{/b}.
        You may now proceed to Question no. 9."
        $ score +=0
        stop sound
        stop music
        jump Question9SHS
    return

    label b8shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Reaction paper{/b}.
        You may now proceed to Question no. 9."
        $ score +=0
        stop sound
        stop music
        jump Question9SHS
    return

    label c8shs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 9."
        $ score +=1
        stop sound
        stop music
        jump Question9SHS
    return

    label d8shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Reaction paper{/b}.
        You may now proceed to Question no. 9."
        $ score +=0
        stop sound
        stop music
        jump Question9SHS
    return

    label question8shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Reaction paper{/b}.
        You may now proceed to Question no. 9."
        $ score +=0
        stop sound
        stop music
        jump Question9SHS
    return



    label Question9SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                             ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question9shs_slow'                    ### set where you want to jump once the timer runs out

        Question9SHS "Expressing your opinion about an event,
        book, restaurant, art, exhibit, performance, movie, or latest trends is called ______."
        jump q9shs
    return

    label q9shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. Scratch Paper":
                jump a9shs
            "B. Bond Paper":
                jump b9shs
            "C. Review Paper":
                jump c9shs
            "D. One whole sheet of paper":
                jump d9shs

    return

    label a9shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Review Paper{/b}.
        You may now proceed to Question no. 10."
        $ score +=0
        stop sound
        stop music
        jump Question10SHS
    return

    label b9shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Review Paper{/b}.
        You may now proceed to Question no. 10."
        $ score +=0
        stop sound
        stop music
        jump Question10SHS
    return

    label c9shs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 10."
        $ score +=1
        stop sound
        stop music
        jump Question10SHS
    return

    label d9shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Review Paper{/b}.
        You may now proceed to Question no. 10."
        $ score +=0
        stop sound
        stop music
        jump Question10SHS
    return

    label question9shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Review Paper{/b}.
        You may now proceed to Question no. 10."
        $ score +=0
        stop sound
        stop music
        jump Question10SHS
    return



    label Question10SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question10shs_slow'                    ### set where you want to jump once the timer runs out

        Question10SHS "How many levels does APA Heading Format (7th ed.) have?."
        jump q10shs
    return

    label q10shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. 2":
                jump a10shs
            "B. 3 ":
                jump b10shs
            "C. 4 ":
                jump c10shs
            "D. 5":
                jump d10shs

    return

    label a10shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. 5{/b}. And this is the end of the quiz, let us
        now see the results."
        $ score +=0
        stop sound
        stop music
        jump ResultsSHS
    return

    label b10shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. 5{/b}. And this is the end of the quiz, let us
        now see the results."
        $ score +=0
        stop sound
        stop music
        jump ResultsSHS
    return

    label c10shs:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. 5{/b}. And this is the end of the quiz, let us
        now see the results."
        $ score +=0
        stop sound
        stop music
        jump ResultsSHS
    return

    label d10shs:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! And this is the end of the quiz, let us
        now see the results."
        $ score +=1
        stop sound
        stop music
        jump ResultsSHS
    return

    label question10shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. 5{/b}. And this is the end of the quiz, let us
        now see the results."
        $ score +=0
        stop sound
        stop music
        jump ResultsSHS
    return


    label ResultsSHS:
        show classroomshs

        "Congratulations, player. Out of {b}10{/b} questions, {b}[playername]{/b} answered {b}[score]{/b} questions. Thanks to you."

        hide classroomshs

        jump EndingSHS

    return


    label EndingSHS:
        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show classroomshs

        show TeacherMarites

        teachermarites "The quiz is over. You may now pass your paper."

        hide Teacher Marites

        "A few minutes later."

        show TeacherMarites

        teachermarites "Congratulations to all of you
        in this class for doing their best for today's quiz. Let's give ourselves a round of applause."

        hide TeacherMarites

        "The students gave theirselves a round of applause."

        show Matthew

        matthew "Yeah! We did it."

        hide Matthew

        playername "That's right. Our time spent in studying for this quiz has finally paid off."

        show Matthew

        matthew "Anyway, we'll talk more about it later."

        hide Matthew

        show Martin

        martin "Alright, then. For now, let us celebrate our own victory."

        hide Martin

        show TeacherMarites

        teachermarites "And so our class ends today. See you tomorrow."

        hide TeacherMarites

        "Teacher Marites left the classroom."

        "After a few hours, their school has finally ended."

        hide classroomshs

        show campus

        show Matthew

        matthew "Before we head to the diner, I forgot to tell you something."

        hide Matthew

        show Allen

        allen "What is it, Matthew?"

        hide Allen

        show Matthew

        matthew "Well, I forgot to tell you that since I made the agreement yesterday, I will be the one to treat
        you all there."

        hide Matthew

        show Martin

        martin "That's a good idea, Matthew! Your timing is perfect because actually..."

        martin "I don't have enough money to eat at the diner so I will accept your treat."

        hide Martin

        show Matthew

        matthew "Don't worry, man. I got this."

        hide Matthew

        show Allen

        allen "Anyway, thank you for giving me a wonderful advice when I was at my lowest yesterday."

        hide Allen

        show Matthew

        matthew "You're welcome, man. That's what friends are for."

        matthew "So what are we waiting for? Let's go!"

        hide Matthew

        "And they went to the diner to have fun eating the best food and drinking the best drink."

        hide campus

        show black

        "Before the game ends, we would like to give our big thanks to sir Gerald for being the best thesis adviser
        that we ever had. He has always been there for us when we need him the most when it comes to advice or guide,
        testing our game, and many more."

        "We wish him all the best. Our respect is big for him."

        "We would also like to give our big thanks in advance to those who will play this game and to those who will
        support us in developing this game because if not because of your support, we won't be able to develop this game
        with our own heart and soul."

        "Until then, goodbye."

        hide black

        show TheEnd

        window hide

        pause

        hide TheEnd

    return


####################

    label college:
        #So this will tackle the scenario of College once you chose College as your difficulty.

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)
        scene campus

        "There are four friends named Martin, Matthew, Allen, and [playername]. They went to school together today.
        All of them are grade 11 Senior High School students at Belridge Senior High School and they belong to 11-A class."

        stop music

        $renpy.sound.play("audio/Japanese School Bell.mp3", loop=True)

        "(The bell rang)"

        "All students of Belridge Senior High School. Please come to your respective classrooms.
        Your classes will start in 10 minutes."

        stop sound

        play music "audio/The 126ers - End Of Summer Instrumental Extended.mp3"

        show Adrian

        adrian "Oh, man. We're gonna be late. What are we going to do?"

        hide Adrian

        menu:

            "What are they going to do?"

            "Go to the classroom early":
                jump classroom2
            "Go to the cafeteria":
                jump cafeteria2
            "Go to the comfort room":
                jump CR2

    label classroom2:
        show Mark

        mark "Alright guys, let's race our way to the classroom as fast as we can."

        hide Mark

        $renpy.sound.play("audio/Running.mp3", loop=True)

        "The four of them began running all the way to their classroom."

        hide campus

        show hallway

        $renpy.sound.play("audio/Running.mp3", loop=True)

        christian "Look, we're almost there. Let's keep running."

        "They kept running all the way to their classroom."

        stop sound

        "And finally, they made it."

        hide hallway

        stop music

        show black

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        jump classroomCollege

        jump campusCollege


    label cafeteria2:
        player "Since we have 10 minutes before the class starts, would you guys like to accompany me in buying food?"

        show Christian

        christian "Hell no!"

        hide Christian

        show Mark

        mark "You are not a child anymore, man. You can already take care of yourself."

        hide Mark

        show Adrian

        adrian "It's a no for me."

        hide Adrian

        player "Oh, come on! Are you guys really my friends?! Alright, I'll treat you all at the cafeteria,
        but please, let's
        go to the cafeteria together."

        "And they all agreed to go to the cafeteria together."

        hide campus

        show cafeteria

        "After they went to the cafeteria to buy food, they went out and hurriedly went to the classroom."

        hide cafeteria

        show hallway

        $renpy.sound.play("audio/Running.mp3", loop=True)

        christian "Look, we're almost there. Let's keep running."

        "They kept running all the way to their classroom."

        stop sound

        "And finally, they made it."

        hide hallway

        stop music

        show black

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        jump classroomCollege

        jump campusCollege

    return

    label CR2:
        "Suddenly, [playername] felt the nature's call."

        player "I need to go to the comfort room. Please wait for me."

        show Adrian

        adrian "[playername], we're not going to wait for you in the comfort room. We will accompany you instead.
        That's what friends are for, right?"

        hide adrian

        player "Alright, then. Let's go."

        "And they went to the comfort room."

        hide campus2

        stop music

        $renpy.sound.play("audio/toilet music.mp3", loop=True)

        show cr

        "[playername] has to stay inside the cubicle toilet a bit longer while
        Matthew, Allen, and Martin will wait for him in the comfort room."

        show Mark

        mark "I think [playername] will take a while in answering the nature's call."

        hide Mark

        show Christian

        christian "Well, it seems like [playername] ate a lot of breakfast a while ago before going to school."

        hide Christian

        show Adrian

        adrian "Can't blame [playername] about that though if that's the sole reason why. We should wait a little
        bit longer."

        hide Adrian

        "After a long time of waiting, [playername] was able to finish answering the call of the nature.
        [playername] wore his pants and his belt on."

        $renpy.sound.play("audio/toilet flush.mp3", loop=True)

        "([playername] flushes the toilet)"

        stop sound

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        "And [playername] went out of the toilet cubicle."

        player "Phew! I feel relieved, guys. Thank you for waiting for me to finish taking a dump."

        show Mark

        mark "No problem, man."

        hide Mark

        "(Mark checked the time on his phone)"

        show Mark

        mark "It's already 7:55. We should hurry to the classroom now!"

        hide Mark

        show Christian

        christian "Sir, yes, sir!"

        hide Christian

        "And they went out of the comfort room to go to their classroom."

        hide cr

        show hallway

        $renpy.sound.play("audio/Running.mp3", loop=True)

        christian "Look, we're almost there. Let's keep running."

        "They kept running all the way to their classroom."

        stop sound

        "And finally, they made it."

        hide hallway

        stop music

        show black

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        jump classroomCollege

    return

    label classroomCollege:
        show classroomshs

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show Adrian

        adrian "Phew! That was tiring."

        hide Adrian

        "Adrian wiped his sweat with his handkerchief and he checked the time on his wristwatch afterwards."

        show Adrian

        adrian "Good thing, we're not yet late. Our class will start at 8:00, but the time is 7:53."

        adrian "So we have seven minutes before the start of our class."

        hide Adrian

        player "Anyway, we should take our seats now."

        show Christian

        christian "Right, we should do that."

        hide Christian

        "[playername], Adrian, Mark, and Christian took their respective seats. At 8:00, their English teacher
    came inside the classroom. She walked towards her table and put down her things.
    Afterwards, she walked in front of the table and started greeting the class."

        show TeacherLuna

        teacherluna "Good morning, 11-A students."

        hide TeacherLuna

        elevenA "Good morning, teacher."

        show TeacherLuna

        teacherluna "I have an announcement to tell so please listen carefully."

        teacherluna "Since we were able to finish our lessons for this week, we won't have an English class
    today. However, we will have a quiz about those lessons tomorrow."

        hide TeacherLuna

        player "Huh??!!!! But, teacher, we only finished discussing those English lessons yesterday."

        show TeacherLuna

        teacherluna "Oh, come on, Mr. [playername]. I've decided to test your knowledge through your tomorrow's quiz
        because I want to see whether all of you learned anything from this class or not."

        teacherluna  "Anyway, I will dismiss you early now so you can use your
        free time to study your lessons or to do something else. See you tomorrow, class."

        hide TeacherLuna

        elevenA "See you tomorrow, teacher."

        "Teacher Luna left the classroom immediately. Afterwards, the students left the classroom as well except for
    [playername], Adrian, Mark, and Christian."

        player "Yo! Do you like to study English with me in my house for our quiz tomorrow later after school?"

        show Mark

        mark "Sure thing, man. That would be nice."

        hide Mark

        show Adrian

        adrian "Besides, studying is not complete without free food, right, [playername]?"

        hide Adrian

        show Christian

        christian "Adrian, here you go again with your desire to eat food. I think there's a dragon in your stomach, man."

        hide Christian

        show Adrian

        adrian "Shut it, Allen. I just want to eat while studying. I cannot gain knowledge without food, bro."

        hide Adrian

        player "Alright, then. It's decided. Don't forget it, okay?"

        "They spent the entire vacant time playing Dark Legends together while waiting for the vacant time to end."

        "At 1:00 p.m., the vacant time was over so their classmates went back to the classroom."

        "A few seconds later, Teacher Raul went inside the classroom and it's time for the entire class to endure
        her boring Math class."

        elevenA "Good afternoon, Teacher Raul."

        show TeacherRaul

        teacherraul "Good afternoon, students. Our new lesson for today is about algebra."

        hide TeacherRaul

        show Mark

        mark "Here we go again."

        hide Mark

        "They have to endure the boredom until 2:30 p.m. I hope they will be okay throughout the lesson."

        "They went to school so they have to listen to the teacher because that is their responsibility as a student
        no matter how boring the class is."

        stop music

        $renpy.sound.play("audio/Japanese School Bell.mp3", loop=True)

        "At 2:30 p.m., the bell rang again."

        stop sound

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show TeacherRaul

        teacherraul "Okay, class. You may now dismiss. Goodbye, class."

        hide TeacherRaul

        elevenA "Goodbye, teacher."

        "Teacher Raul and the students of 11-A left the classroom."

        hide classroomshs

        jump campusCollege


    label campusCollege:
        show campus

        player "Finally, school's over."

        show Mark

        mark "Yeah, it's already over. We were able to endure the boredom of her class this afternoon."

        hide Mark

        player "Good thing I can finally go home and play video games for the rest of the day."

        show Adrian

        adrian "Wait, what? I thought we're going to study for our English quiz tomorrow at your house, remember?"

        hide Adrian

        show Mark

        mark "Yeah, he's right. Studying for tomorrow's quiz comes first before video games, man."

        hide Mark

        player "Oh, my bad. We're supposed to study English when we get to my house. But, Adrian, I am sure you like
    eating better than studying."

        show Adrian

        adrian "Give me a break, [playername]. Studying gets better when there's food so deal with it!"

        hide Adrian

        player "Relax, Martin, relax. I'm just joking around here, man. Anyway, let's go to my house."

        "And they began walking to [playername]'s home."

        hide campus

        jump Collegelessons

    return

    label Collegelessons:
        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show HouseProtag

        "After 10 minutes of walking, they were able to make it to [playername]'s house."

        show Adrian

        adrian "And so we finally made it, everyone. So, [playername], are your parents around?"

        hide Adrian

        player "No, they're not here. They went out of town for work, but they will be back after 3 days."

        show Mark

        mark "So when did they leave?"

        hide Mark

        player "They left early in the morning before I went to school."

        show Mark

        mark "Oh, I see."

        hide Mark

        player "Anyway, let's go inside my house."

        "[playername] took the house keys in the backpack and unlocked the door to their house.
        After unlocking the door, they went inside the house."

        hide HouseProtag

        show black

        stop music

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show LivingRoom

        "So this is what the [playername]'s living room looks like."

        "To be honest, this living room looks beautiful in the eyes despite that it is
        simple as the way it is. Well, I can say that I do believe that simplicity is beauty."

        show Christian

        christian "It was quite a tiring day today. Forcing ourselves to study for tomorrow's quiz at this point
        is not effective."

        hide Christian

        show Adrian

        adrian "Christian's right. It will be better for us to take a rest first before eating and studying."

        hide Adrian

        player "Yeah, that is really a good idea, Christian. We better go to my bedroom and start resting."

        "They all went to [playername]'s bedroom to rest and Mark closed the door."

        hide LivingRoom

        show Bedroom

        player "So as usual, I still use the same bed so only 2 people can sleep in my bed,
        but Adrian and I can get the foam mattress in the storage room. Mark, don't close the door after
        we leave."

        "[playername] opened the door again."

        show Adrian

        adrian "Alright then. We'll just wait here as usual."

        hide Adrian

        "[playername] and Adrian left the bedroom to get the foam mattress in the storage room.
        While Christian and Mark, on the other hand, started having a conversation."

        show Mark

        mark "Christian, to be honest, I doubt I will be able to pass our English quiz tomorrow.
        That is because I think it is very hard for me to learn our English lessons.
        This is ironic for me as someone who can speak English fluently."

        hide Mark

        show Christian

        christian "Mark, I know that it must have been hard for you to learn that subject, but I believe in you.
        I believe that you can do it uh... I mean, you can pass the tomorrow's quiz."

        christian "Whether you're good at something or not, what matters the most is that you put your effort in doing
        your best."

        christian "In fact, there is nothing wrong in trying until you succeed."

        christian "That is because in school, you're not going to study one thing."

        christian "You will be studying a lot of things and you have to do your best even if the results may turn out well
        or not because what matters the most is that you tried to persevere enough to make an effort in doing your best
        in everything that you do regardless of how important a certain task is."

        christian "In my case, I wasn't really good at English before, but my teacher told me to keep trying to put a lot of
        effort in learning it"

        christian "so in the end,
        I was able to improve my skills in English even though there will always be a room for me to make mistakes
        because my English is still not perfect after all."

        hide Christian

        "Well, that reminds me of one of my junior high school teachers because she used to tell this kind of advice in our
        class before and I still remember and live with this advice of hers until now."

        "To be honest, that advice helped me to persevere in life whether in studies or in other things. Thanks, teacher.
        \n-Wrichmond"

        show Mark

        mark "Wow, that's good to hear, man. It is good to know that I have learned a lot of things from you.
        What I've learned from you today made me realize and understand the importance of putting effort into something."

        mark "Well, anyway. Thanks for the advice, man."

        hide Mark

        show Christian

        christian "No problem, man."

        hide Christian

        "And [playername] and Adrian went back to the bedroom with the foam mattress."

        show Bedroom

        show FoamMattress

        window hide

        pause

        hide FoamMattress

        show Christian

        christian "Finally, they're here with the foam mattress."

        hide Christian

        "[playername] and Adrian put down the foam mattress."

        player "And since we have the foam mattress here, we can now finally rest for an hour."

        "And so they decided to take a rest for an hour. Matthew and Allen slept on the foam mattress while [playername]
        and Martin slept on [playername]'s bed."

        stop music

        show black

        "After resting for an hour, they woke up and stretched their body."

        hide black

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show Bedroom

        player "(yawns)"

        adrian "(yawns)"

        mark "(yawns)"

        christian "(yawns)"

        show Christian

        christian "Alright, listen up. I have to say something."

        hide Christian

        player "What is it, Christian?"

        show Christian

        christian "Ok so here's the deal: we will eat together at Rowan's Diner after school.
        Regardless of the scores that we get, always remember that what matters the most is that we did our best
        on that day."

        hide Christian

        show Adrian

        adrian "Oh, well, I can't deny that Christian's idea is indeed a great idea. He is smart as Albert Einstein, man so
        I agree with him here."

        hide Adrian

        show Mark

        mark "Same."

        hide Mark

        player "Me too."

        show Christian

        christian "That's good to hear, guys. So what are we waiting for? Let's study!!!!!!"

        hide Christian

        "Okay, player. Before you proceed to the quiz day of [playername], Adrian, Mark, and Christian, I want you
        to help [playername] to get the best score possible for tomorrow's quiz. The [playername]'s fate
        for tomorrow's quiz is in your hands now so you better learn the lessons right away, ok?"

        menu:
            "Yes, man. It's time for me to study!":
                jump study2

            "No way highway!":
                jump noway2

    return

    label noway2:
        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show Bedroom

        player "Unfortunately, I lost the drive to study today even if I feel like I want to study a while ago."

        "And this is the response of the [playername]'s friends in unison:"

        "Same here!"

        player "That's awesome. That is unexpected for sure. So what should we do today that does not include
        studying?"

        menu:
            "Play computer games":
                jump computergames2

            "Watch movies together":
                jump movie2

    return

    label computergames2:

        show Bedroom

        "[playername] turned on the computer."

        "And so they played computer games for the rest of the day until the friends of [playername] decided to go home
        when evening came."

        hide Bedroom

        show black

        "They ended the day without studying for their tomorrow's quiz."

        "Playing games is a fun thing to do. However, if you have to study for your tomorrow's quiz or exam,
        you better study first before playing games."

        "Games will always be there so always focus on more important things.
        \n-Wrichmond"

        hide black

        jump quizdayCollege

    return

    label movie2:

        show Bedroom

        "[playername] turned on the computer and opened the RedFlix app."

        "And so they watched movies together for the rest of the day until the friends of [playername]
        decided to go home when evening came."

        hide Bedroom

        show black

        "They ended the day without studying for their tomorrow's quiz."

        "Watching movies is a fun thing to do. However, if you have to study for your tomorrow's quiz or exam,
        you better study first before playing games."

        "Movies will always be there so always focus on more important things.
        \n-Wrichmond"

        hide black

        jump quizdayCollege


    label study2:

        show Bedroom

        "Okay so you have finally decided to study, player. In that case,
        I will be providing you the images of the lessons that you
        need to learn. Good luck and happy studying!"

        jump studychoicesCollege

    return

    label studychoicesCollege:
        default L1Collegex= False
        default L2Collegey= False
        default L3Collegez= False

        hide black

        show Bedroom

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        menu:
            "Which of the following lessons should you study?"

            "Lesson 1: Concept Paper" if not L1Collegex:
                $L1Collegex= True
                jump L1College

            "Lesson 2: Position Paper (Part 1)" if not L2Collegey:
                $L2Collegey= True
                jump L2College

            "Lesson 3: Position Paper (Part 2)" if not L3Collegez:
                $L3Collegez= True
                jump L3College

            "Call it a day":
                jump ready2

    return

    label L1College:
        stop music

        $renpy.music.play("audio/Good Friends- Yasper.mp3", loop=True)

        hide Bedroom

        show L1College

        window hide

        pause

        hide L1College


        show L1College2

        window hide

        pause

        hide L1College2


        show L1College3

        window hide

        pause

        hide L1College3


        show L1College4

        window hide

        pause

        hide L1College4


        show L1College5

        window hide

        pause

        hide L1College5


        show L1College6

        window hide

        pause

        hide L1College6


        show L1College7

        window hide

        pause

        hide L1College7


        show L1College8

        window hide

        pause

        hide L1College8


        show L1College9

        window hide

        pause

        hide L1College9


        show L1College10

        window hide

        pause

        hide L1College10


        show L1College11

        window hide

        pause

        hide L1College11

        stop music

        show black

        "You may now proceed to the next lesson."

        jump studychoicesCollege

    return

    label L2College:
        stop music

        $renpy.music.play("audio/Glimlip - S h e.mp3", loop=True)

        hide Bedroom

        show L2College

        window hide

        pause

        hide L2College2


        show L2College2

        window hide

        pause

        hide L2College2


        show L2College3

        window hide

        pause

        hide L2College3


        show L2College4

        window hide

        pause

        hide L2College4

        stop music

        show black

        "You may now proceed to the next lesson."

        jump studychoicesCollege


    return

    label L3College:
        stop music

        $renpy.music.play("audio/DLJ - Deep Sleep ft. TABAL.mp3", loop=True)

        hide Bedroom

        show L3College

        window hide

        pause

        hide L3College


        show L3College2

        window hide

        pause

        hide L3College2


        show L3College3

        window hide

        pause

        hide L3College3


        show L3College4

        window hide

        pause

        hide L3College4

        stop music

        show black

        "You may now proceed to the next lesson."

        jump studychoicesCollege

    return

    label ready2:
        "And so [playername] and friends finally finished studying for tomorrow's quiz. Player,
        thank you for studying the lessons as well."

        show Adrian

        adrian "Okay, [playername], it's time for us to go home. We need to go home immediately
        before it gets dark. Goodbye, [playername]. See you tomorrow."

        hide Adrian

        player "Goodbye, my friends. See you tomorrow at school. Let us do our best tomorrow."

        show Mark

        mark "Alright then, goodbye."

        hide Mark

        "And so the day has ended that way. We may never know what lies ahead, but we should keep on going and
        we should also do our best."

        stop music

        hide Bedroom

        show black

        "Good luck on your quiz, [playername], Adrian, Mark, and Christian"

        hide black

        jump quizdayCollege

    return

    label quizdayCollege:

        show black

        "The next day"

        hide black

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show classroomshs

        show TeacherLuna

        teacherluna "Good morning, students. Today is your quiz day. Once I gave the quiz sheets to all of you,
        you may now start answering the questions provided. Do your best and good luck."

        hide TeacherLuna

        "Teacher Luna gave the quiz sheets to the students."

        "Okay, player. I will present to you the mechanics of this game so please read and follow the
        mechanics of this game. Thank you."

        hide classroomshs

        show Mechanics1

        window hide

        pause

        hide Mechanics1

        show Mechanics2

        window hide

        pause

        hide Mechanics2

        show classroomshs

        show TeacherLuna

        teacherluna "Okay, you may now start answering."

        hide TeacherLuna

        "Since you are about to take the quiz, you won't hear any background music until the end of the quiz."

        "That is because usually, when you take your in school, you have to take it quietly."

        stop music

        jump Question1College

    return

    label Question1College:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question1college_slow'                    ### set where you want to jump once the timer runs out


        Question1College "It is a preliminary document that sets out to explain what
        a proposed study is about, why it is being undertaken, and how it will be carried out."
        jump q1college
    return

    label q1college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Concept Paper":
                jump a1college
            "B. Academic Research":
                jump b1college
            "C. Reaction Paper":
                jump c1college
            "D. Reflection Paper":
                jump d1college

    return

    label a1college:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 2."
        $ score +=1
        stop sound
        stop music
        jump Question2College
    return

    label b1college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Concept Paper{/b}. You may now proceed to Question no. 2."
        $ score +=0
        stop sound
        stop music
        jump Question2College
    return

    label c1college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Concept Paper{/b}. You may now proceed to Question no. 2."
        $ score +=0
        stop sound
        stop music
        jump Question2College
    return

    label d1college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Concept Paper{/b}. You may now proceed to Question no. 2."
        $ score +=0
        stop sound
        stop music
        jump Question2College
    return

    label question1college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Concept Paper{/b}. You may now proceed to Question no. 2."
        $ score +=0
        stop sound
        stop music
        jump Question2College
    return


    label Question2College:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question2college_slow'                    ### set where you want to jump once the timer runs out


        Question2College "What are the 5 elements of a Concept Paper?"
        jump q2college
    return

    label q2college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Project, Project Zero, Timeline, Paper, and Milestones":
                jump a2college
            "B. Project Vision, Project Scope, Project Targets, Timeline, and Milestones":
                jump b2college
            "C. Concept, Plot, Climax, Resolution, Falling Action":
                jump c2college
            "D. Project D, Project Zero, Timeline, Milestones, and Concept Paper":
                jump d2college

    return

    label a2college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Project Vision, Project Scope, Project Targets,
        Timeline, and Milestones.{/b} You may now proceed to Question no. 3."
        $ score +=0
        stop sound
        stop music
        jump Question3College
    return
    return

    label b2college:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 3."
        $ score +=1
        stop sound
        stop music
        jump Question3College
    return

    label c2college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Project Vision, Project Scope, Project Targets,
        Timeline, and Milestones.{/b} You may now proceed to Question no. 3."
        $ score +=0
        stop sound
        stop music
        jump Question3College
    return

    label d2college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is{b}B. Project Vision, Project Scope, Project Targets,
        Timeline, and Milestones.{/b} You may now proceed to Question no. 3."
        $ score +=0
        stop sound
        stop music
        jump Question3College
    return

    label question2college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Project Vision, Project Scope, Project Targets,
        Timeline, and Milestones.{/b} You may now proceed to Question no. 3."
        $ score +=0
        stop sound
        stop music
        jump Question3College
    return


    label Question3College:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question3college_slow'                    ### set where you want to jump once the timer runs out


        Question3College "What are the 3 main elements of Position Paper?"
        jump q3college
    return


    label q3college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Ifrit, Bahamut, Chocobo":
                jump a3college
            "B. International, Bravo, Conclusion":
                jump b3college
            "C. Introduction, Body, Constitution":
                jump c3college
            "D. Introduction, Body, Conclusion":
                jump d3college

    return

    label a3college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Introduction, Body, Conclusion{/b}.
        You may now proceed to Question no. 4."
        $ score+=0
        stop sound
        stop music
        jump Question4College
    return
    return

    label b3college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Introduction, Body, Conclusion{/b}.
        You may now proceed to Question no. 4."
        $ score+=0
        stop sound
        stop music
        jump Question4College
    return

    label c3college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Introduction, Body, Conclusion{/b}.
        You may now proceed to Question no. 4."
        $ score+=0
        stop sound
        stop music
        jump Question4College
    return

    label d3college:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 4."
        $ score+=1
        stop sound
        stop music
        jump Question4College
    return

    label question3college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. Introduction, Body, Conclusion{/b}.
        You may now proceed to Question no. 4."
        $ score+=0
        stop sound
        stop music
        jump Question4College
    return


    label Question4College:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question4college_slow'                    ### set where you want to jump once the timer runs out


        Question4College "It is a special event that represents a point
        in time that marks the expected completion of certain activities and tasks. "
        jump q4college
    return


    label q4college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Milestones":
                jump a4college
            "B. Project Milestone":
                jump b4college
            "C. Timeline":
                jump c4college
            "D. Position Paper":
                jump d4college

    return

    label a4college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Project Milestone{/b}.
        You may now proceed to Question no. 5."
        $ score+=0
        stop sound
        stop music
        jump Question5College
    return
    return

    label b4college:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 5."
        $ score+=1
        stop sound
        stop music
        jump Question5College
    return

    label c4college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Project Milestone{/b}.
        You may now proceed to Question no. 5."
        $ score+=0
        stop sound
        stop music
        jump Question5College
    return

    label d4college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Project Milestone{/b}.
        You may now proceed to Question no. 5."
        $ score+=0
        stop sound
        stop music
        jump Question5College
    return

    label question4college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Project Milestone{/b}.
        You may now proceed to Question no. 5."
        $ score+=0
        stop sound
        stop music
        jump Question5College
    return


    label Question5College:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question5college_slow'                    ### set where you want to jump once the timer runs out


        Question5College "It makes progress visible, expose problems and
        represent the conclusion of a learning cycle."
        jump q5college
    return


    label q5college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Milestones":
                jump a5college
            "B. Project Milestone":
                jump b5college
            "C. Timeline":
                jump c5college
            "D. Position Paper":
                jump d5college

    return

    label a5college:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 6."
        $ score+=1
        stop sound
        stop music
        jump Question6College
    return

    label b5college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Milestones{/b}. You may now proceed to Question no. 6."
        $ score+=0
        stop sound
        stop music
        jump Question6College
    return

    label c5college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Milestones{/b}. You may now proceed to Question no. 6."
        $ score+=0
        stop sound
        stop music
        jump Question6College
    return

    label d5college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Milestones{/b}. You may now proceed to Question no. 6."
        $ score+=0
        stop sound
        stop music
        jump Question6College
    return

    label question5college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Milestones{/b}. You may now proceed to Question no. 6."
        $ score+=0
        stop sound
        stop music
        jump Question6College
    return


    label Question6College:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question6college_slow'                    ### set where you want to jump once the timer runs out


        Question6College "Which of the following is true about Secondary Data?."
        jump q6college
    return


    label q6college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. It is the first-hand information obtained from the ground.":
                jump a6college
            "B. It is based on subjective data factors such as people's opinions.":
                jump b6college
            "C.  It is second-hand information obtained from reading books,
            watching news, videos, the internet, and other already documented material. ":
                jump c6college
            "D. It is based on actual numbers and is, therefore, more objective.":
                jump d6college

    return

    label a6college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. It is second-hand information obtained from reading books,
        watching news, videos, the internet, and other already documented material.{/b}
        You may now proceed to Question no. 7."
        $ score+=0
        stop sound
        stop music
        jump Question7College
    return

    label b6college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. It is second-hand information obtained from reading books,
        watching news, videos, the internet, and other already documented material.{/b}
        You may now proceed to Question no. 7."
        $ score+=0
        stop sound
        stop music
        jump Question7College
    return

    label c6college:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 7."
        $ score+=1
        stop sound
        stop music
        jump Question7College
    return

    label d6college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. It is second-hand information obtained from reading books,
        watching news, videos, the internet, and other already documented material.{/b}
        You may now proceed to Question no. 7."
        $ score+=0
        stop sound
        stop music
        jump Question7College
    return

    label question6college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. It is second-hand information obtained from reading books,
        watching news, videos, the internet, and other already documented material.{/b}
        You may now proceed to Question no. 7."
        $ score+=0
        stop sound
        stop music
        jump Question7College
    return


    label Question7College:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question7college_slow'                    ### set where you want to jump once the timer runs out


        Question7College "What are the two types of data?"
        jump q7college
    return


    label q7college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Save Data and Load Data":
                jump a7college
            "B. Mobile Data and Computer Data":
                jump b7college
            "C. Quantitative Data and Qualitative Data":
                jump c7college
            "D. Database and Data Center":
                jump d7college

    return

    label a7college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Quantitative Data and Qualitative Data{/b}.
        You may now proceed to Question no. 8."
        $ score+=0
        stop sound
        stop music
        jump Question8College
    return

    label b7college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Quantitative Data and Qualitative Data{/b}.
        You may now proceed to Question no. 8."
        $ score+=0
        stop sound
        stop music
        jump Question8College
    return

    label c7college:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 8."
        $ score+=1
        stop sound
        stop music
        jump Question8College
    return

    label d7college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Quantitative Data and Qualitative Data{/b}.
        You may now proceed to Question no. 8."
        $ score+=0
        stop sound
        stop music
        jump Question8College
    return

    label question7college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Quantitative Data and Qualitative Data{/b}.
        You may now proceed to Question no. 8."
        $ score+=0
        stop sound
        stop music
        jump Question8College
    return


    label Question8College:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question8college_slow'                    ### set where you want to jump once the timer runs out


        Question8College "It is first-hand information obtained from the ground,
        for example, by carrying out interviews and site visits. "
        jump q8college
    return


    label q8college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Secondary Data":
                jump a8college
            "B. Primary Data":
                jump b8college
            "C. Save Data":
                jump c8college
            "D. Load Data":
                jump d8college

    return

    label a8college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Primary Data{/b}.
        You may now proceed to Question no. 9."
        $ score+=0
        stop sound
        stop music
        jump Question9College
    return

    label b8college:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 9."
        $ score+=1
        stop sound
        stop music
        jump Question9College
    return

    label c8college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Primary Data{/b}.
        You may now proceed to Question no. 9."
        $ score+=0
        stop sound
        stop music
        jump Question9College
    return

    label d8college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Primary Data{/b}.
        You may now proceed to Question no. 9."
        $ score+=0
        stop sound
        stop music
        jump Question9College
    return

    label question8college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Primary Data{/b}.
        You may now proceed to Question no. 9."
        $ score+=0
        stop sound
        stop music
        jump Question9College
    return


    label Question9College:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question9college_slow'                    ### set where you want to jump once the timer runs out


        Question9College "To take a side on a subject, what should you establish first?"
        jump q9college
    return


    label q9college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Arguability of a topic that interests you":
                jump a9college
            "B. Subject":
                jump b9college
            "C. Conclusion":
                jump c9college
            "D. None of the Above":
                jump d9college

    return

    label a9college:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 10."
        $ score+=1
        stop sound
        stop music
        jump Question10College
    return

    label b9college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Arguability of a topic that interests you.{/b}
        You may now proceed to Question no. 10."
        $ score+=0
        stop sound
        stop music
        jump Question10College
    return

    label c9college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Arguability of a topic that interests you.{/b}
        You may now proceed to Question no. 10."
        $ score+=0
        stop sound
        stop music
        jump Question10College
    return

    label d9college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Arguability of a topic that interests you.{/b}
        You may now proceed to Question no. 10."
        $ score+=0
        stop sound
        stop music
        jump Question10College
    return

    label question9college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Arguability of a topic that interests you.{/b}
        You may now proceed to Question no. 10."
        $ score+=0
        stop sound
        stop music
        jump Question10College
    return


    label Question10College:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question1college_slow'                    ### set where you want to jump once the timer runs out


        Question10College "A good position paper will not only provide ____ but also make proposals for resolutions."
        jump q10college
    return


    label q10college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Facts":
                jump a10college
            "B. Opinions":
                jump b10college
            "C. Subjects":
                jump c10college
            "D. Criticisms":
                jump d10college

    return

    label a10college:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! And this is the end of the quiz, let us now see the results."
        $ score+=1
        stop sound
        stop music
        jump ResultsCollege
    return

    label b10college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Facts{/b}. And this is the end of the quiz, let us
        now see the results."
        $ score+=0
        stop sound
        stop music
        jump ResultsCollege
    return

    label c10college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Facts{/b}. And this is the end of the quiz, let us
        now see the results."
        $ score+=0
        stop sound
        stop music
        jump ResultsCollege
    return

    label d10college:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Facts{/b}. And this is the end of the quiz, let us
        now see the results."
        $ score+=0
        stop sound
        stop music
        jump ResultsCollege
    return

    label question10college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Facts{/b}. And this is the end of the quiz, let us
        now see the results."
        $ score+=0
        stop sound
        stop music
        jump ResultsCollege
    return


    label ResultsCollege:
        show classroomshs

        "Congratulations, player. Out of {b}10{/b} questions, {b}[playername]{/b} answered {b}[score]{/b} questions. Thanks to you."

        hide classroomshs

        jump EndingCollege

    return

    label EndingCollege:
        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show classroomshs

        show TeacherLuna

        teacherluna "The quiz is over. You may now pass your paper."

        hide TeacherLuna

        "The students put their paper on the teacher's table. Afterwards, they returned to their seats and waited for
        the quiz results."

        "A few minutes later."

        show TeacherLuna

        teacherluna "Congratulations to all of you
        in this class for doing their best for today's quiz. Let's give ourselves a round of applause."

        hide TeacherLuna

        "The students gave theirselves a round of applause."

        show Mark

        mark "Yeah! We did it."

        hide Mark

        playername "That's right. Our time spent in studying for this quiz has finally paid off."

        show Mark

        mark "Anyway, we'll talk more about it later."

        hide Mark

        show Adrian

        adrian "Alright, then. For now, let us celebrate our own victory."

        hide Adrian

        show TeacherLuna

        teacherluna "And so our class ends today. See you tomorrow."

        hide TeacherLuna

        "Teacher Luna left the classroom."

        "After a few hours, their school has finally ended."

        hide classroomshs

        show campus

        show Mark

        mark "Before we head to the diner, I forgot to tell you something."

        hide Mark

        show Christian

        christian "What is it, Matthew?"

        hide Christian

        show Mark

        mark "Well, I forgot to tell you that since I made the agreement yesterday, I will be the one to treat
        you all there."

        hide Mark

        show Adrian

        adrian "That's a good idea, Mark! Your timing is perfect because actually..."

        adrian "I don't have enough money to eat at the diner so I will accept your treat."

        hide Adrian

        show Mark

        mark "Don't worry, man. I got this."

        hide Mark

        show Christian

        christian "Anyway, thank you for giving me a wonderful advice when I was at my lowest yesterday."

        hide Christian

        show Mark

        mark "You're welcome, man. That's what friends are for."

        mark "So what are we waiting for? Let's go!"

        hide Mark

        "And they went to the diner to have fun eating the best food and drinking the best drink."

        hide campus

        show black

        "Before the game ends, we would like to give our big thanks to sir Gerald for being the best thesis adviser
        that we ever had. He has always been there for us when we need him the most when it comes to advice or guide,
        testing our game, and many more."

        "We wish him all the best. Our respect is big for him."

        "We would also like to give our big thanks in advance to those who will play this game and to those who will
        support us in developing this game because if not because of your support, we won't be able to develop this game
        with our own heart and soul."

        "Until then, goodbye."

        hide black

        show TheEnd

        window hide

        pause

        hide TheEnd

    return
