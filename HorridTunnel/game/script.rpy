define e = Character("[charname]", color = "#fdee00")
define s = Character("Someone", color = "#b2beb5")
define sh = Character("Shadowy Figure", color = "#b2beb5")
define h = Character("Haunted Voices", color = "#b2beb5")
define c = Character("Ghoul", color = "#b2beb5")

label start:
    stop music fadeout 1.0
    play music "audio/scary music.mp3"
    scene bg black
    with fade

    show text "{cps=7}Welcome to the Horrid Tunnel!{/cps} "
    with dissolve
    pause 5
    hide text
    with dissolve

    jump main

label main:

    scene bg tunnel

    show text "{cps=10}As a thrill-seeker, you have bravely decided to visit the infamous Horrid Tunnel alone.{/cps}"
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{cps=10}However, during your admirable adventure, you find yourself lost.\nYou can choose to walk in multiple directions to find a way out.{/cps}"
    with dissolve
    pause 5
    hide text
    with dissolve

    $ charname = renpy.input("{cps=10}Let's start with your name:{/cps}", exclude="1234567890!@#$%^&*()-_=+:;'|\<,>.?/`~")

    scene bg someone

    show text "{cps=10}Someone whispers to your ear as if that someone is standing near you.{/cps}"
    with dissolve
    pause 3
    hide text
    with dissolve

    s "{cps=7}Hope you can get out here alive...{/cps} "
    s "{cps=4}{b}[charname]{/b}...{/cps}"

    e "{cps=7}Whoa! Who was that? Where are you?{/cps}"

    "You decided to move for 5 minutes straight on your way out perhaps."
    
    jump fourway

label fourway:
    stop music fadeout 1.0
    play music "audio/celtic music.mp3"
    scene bg fourway

    "Now, you are at a crossroads, and you can choose to go down to 3 directions."
    "It is too late go back now. Where would you like to go?"
    menu:
        "Left":
            jump shadowz
        "Right":
            jump skeletons
        "Forward":
            jump haunted

label shadowz:
    stop music fadeout 1.0
    play music "audio/shadow music.mp3"
    scene bg shadowz

    "You see a shadowy figure appear in the distance."
    "It looks like that it is approaching you any minute."
    
    "Where will you go now?"
    menu:
        "Right":
            jump cameras
        "Backwards":
            jump fourway

label skeletons:
    stop music fadeout 1.0
    play music "audio/skeletons music.mp3"
    scene bg skeletons

    "You see a wall of skeletons as you walk into the room."
    "Someone is watching you."

    "Decide quickly on where to go."
    menu:
        "Forward":
            jump creature
        "Right":
            jump knife
        "Backward":
            jump fourway

label haunted:
    stop music fadeout 1.0
    play music "audio/haunted music.mp3"
    scene bg haunted

    "You hear crying voices that comes out from that hole in the wall."
    "You think you have awoken some ancient spirits."

    "Where to go?"
    menu:
        "Right":
            "A massive count of zombies rising from the tombs as you enter the room."
            "You are shred into pieces."
            jump yesno
        "Left":
            jump escape
        "Backward":
            jump fourway

label creature:
    stop music fadeout 1.0
    play music "audio/creature music.mp3"
    scene bg creature

    "A strange ghoul-like creature has appeared.\nYou can either run or fight it."

    menu:
        "Run":
            jump skeletons
        "Fight":
            scene bg 
            "The ghoul-like creature has killed you and reap your flesh."
            jump yesno

label cameras:
    stop music fadeout 1.0
    play music "audio/camera music.mp3"
    scene bg cameras

    "You see a camera has been dropped on the ground."
    e "Someone has been here recently..."

    "Where would you like to go?"
    menu:
        "Forward":
            jump escape
        "Backward":
            jump shadowz

label knife:
    stop music fadeout 1.0
    play music "audio/knife music.mp3"
    scene bg knife

    "You find a knife glowing which is held by one of corpse in the wall."
    "You keep it and think you might need it somehow..."
    pause 5

    stop music fadeout 1.0
    play music "audio/creature music.mp3"
    scene bg creature

    "The strange ghoul-like creature approaches.\nYou slashed the ghoul using the knife."
    c "{cps=7}Ahgg... ... ...{/cps}"
    e "What's that light ahead. Finally, I can see the way out."

    jump escape

label escape:
    stop music fadeout 1.0
    play music "audio/escape music.mp3"
    scene bg escape

    e "{cps=7}At last! I finally I escaped this cursed tunnel.\nI will never go back.{/cps}"
    pause 5
    return

label yesno:
    scene bg black

    "Do you want to enter the Horrid Tunnel again?"
    menu:
        "Yes":
            jump start
        "No":
            "{cps=7}Thank you for playing the game!\n-Farrell Baruel(StackTrek Batch 9){/cps}"
            pause 5
            return
