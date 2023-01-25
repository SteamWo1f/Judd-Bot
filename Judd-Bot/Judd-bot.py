#-Imports-
from email import message
import string
import discord
import os
import random
from discord.ext import commands, tasks
from itertools import cycle
import io
import aiohttp
 
intents = discord.Intents(messages=True, guilds=True)

#-Client Bullshit-
client = discord.Client(intents=intents)


#-Judd Files-


myfiles = ["dryer.png","The Big Think.jpg","Thumb s up Judd.gif","The nice sleep.gif","Splatfeast Judd old.gif","RAINBOW.gif","Nya Judd.gif","Mini Judd FACE.gif","judd.gif","Judd old dance.gif","Flags.gif","BIG JUDD.gif", "trio.gif"]
 

myjudd = ['Zzz..','Meow..','Mreoww..' 'Mew!']

myjuddpet = ["Headpat_judd.gif"]

myjuddmeow = ["Mreoow.. (thank you for the head pat)"]

#I am sorry...
myqoutes = ["A Splat Bombs timer is only active while it's on the ground! So will explode quicker when rolled than when thrown through the air!",

"Did you ever notice that light on top of your Ink Tank? It tells you when you've got enough ink to use your Sub Weapon!",

"Press ZL to squid up and swim up inked-up walls. Press B to climb even faster!",

"The Splat Bomb is the most basic kind of sub-weapon. The explosion timer starts when it hits the ground. You can make it explode faster by rolling it.",

"Suction Bombs are bombs that attach to the ground or to walls. They take slightly longer to detonate than Splat Bombs, but their blast radius is a bit larger.",

"Burst Bombs are bombs that detonate on impact. They don't use much ink and aren't very powerful, so throw two in a row at unsuspecting opponents!",

"In the heat of battle, it's impurrtant to know when you're dealing damage to opponents! So listen fur the satisfying pop sound when you're roughing someone up.",

"Super Jumping is a super useful way to get around, but it can also be risky, opponents can see your landing spot when you Super Jump! So check the map for any potential ambushers before you take flight!",

"If you attach lots of the same type of abilities, you'll get diminishing returns. So if you really want to maximize your potential, try your best to carefully balance your abilities.",

"You know you can't swim, right? And that your ink dissolves in water?! So be extra careful, and watch your step around any watery areas, ya hear!",

"When hanging around outside of battle, press X to open up the main menu. There's an Options tab that lets you adjust things to suit your style.",

"hiding in your own ink makes you hard to see. But if you swim around, your foes may notice the ink ripples you make! So keep an eye out for ripples in enemy ink. And spray away if you cat-ch your foes in the act!",

"Are you checking the Turf Map with X? Don't just stand there after you get splatted... Check the Turf Map and plan your next move! Head for an area with fewer bad guys, or Super Jump to a teammate to help 'em out!",

"Kid form leaves you exposed, so when you're not attacking, stay hidden in your ink! This will make it harder for the opponents to spot you, and you'll also refill your ink tank a lot faster!",

"The stages available for battle are different each day. Try to choose a weapon that works well on all the day's stages!",

"Use right trigger to shoot", "Use left trigger to go into the ink",

"Don't squid party in ranked",

"Hiding then attacking is a good technique to get some splats",

"Remember to always stand at the forward edge of ledges so you can reach as much as possible",

"When playing charger, you want to be as far back as you possibly can be to keep yourself safe",

"Running large amounts of run speed can help counteract the slow running speed of dynamo roller",

"Running a full bomb defense loadout can help survive more splash damage hits from specials like tentamissiles",

"Your style is as fresh as an old litter box... play some Turf War battles in the battle pot. Oh, and once you've leveled up a bit, don't furrrget to visit Ammo Knights in the square!",

"Make sure you visit Ammo Knights after you level up. They might have new stuff in stock. Leveling up earns you Sheldon Licenses, which will let you buy even MORE weapons!",

"Have you met Murch in the square yet? That guy is pawsitively obsessed with gear!",

"Purrress to reset the camera to its default pawsition. If you look straight ahead as you move, it'll be easier to ink turf and splat opponents. Why not practice it now? Brrreak a target while keeping it in sight!",

"You can purrress Up or Down to send signals to your teammates!, Press Down to send a \"Booyah!\" Use this when you're fired up about something. Press Up to send a \"This way!\" Use this to call teammates to your pawsition!.. Get splatted, and Up on changes to \"Ouch...\" so you can let your teammates know. Sending signals may not guarantee victory, but it'll impurrrove your teamwork! Take a minute and send out a few signals to see how you like them.",

"Your style is as fresh as an old litter box... play some Turf War battles in the battle pot, Oh, and once you've leveled up a bit, don't furrrget to visit Ammo Knights in the square!",

"Make sure you visit Ammo Knights after you level up. They might have new stuff in stock. Leveling up earns you Sheldon Licenses, which will let you buy even MORE weapons!",

"Have you met Murch in the square yet? That guy is pawsitively obsessed with gear!",

"Purrress to reset the camera to its default pawsition. If you look straight ahead as you move, it'll be easier to ink turf and splat opponents. Why not practice it now? Brrreak a target while keeping it in sight!",

"You can purrress Up or Down to send signals to your teammates! , Press Down to send a \"Booyah! \" Use this when you're fired up about something. Press Up to send a \"This way! \" Use this to call teammates to your pawsition! .. Get splatted, and Up on changes to \"Ouch...\" so you can let your teammates know. Sending signals may not guarantee victory, but it'll impurrrove your teamwork!  Take a minute and send out a few signals to see how you like them.",

"Swimming around fast in ink will make little ripples that your opponents can see. Tilt gently to swim slowly and sneak up on opponents without splashing! There is a way to swim fast and not splash though: wear gear with the Ninja Squid ability!  You can never be too sneaky!",

"Keep an eye on the icons at the top of the screen to see which team is ahead. Be careful if your team's numbers are low, but be bold if your opponents are on the ropes!",

"In the heat of battle, it's impurrrtant to know when you're dealing damage to opponents! So listen furrr the satisfying \"pop\" sound when you're roughing someone up. You can hear how this works when trying out weapons too, so give it a go!",

"Have you been to any of the shops yet? Some new gear could really help you out in battle! There are three kinds of gear headgear, clothing, and shoes. Make sure to try out all three!",

"Press to use your sub weapon! They're great for helping your team push, or for inking spots normal weapons can't reach... Sub weapons use more ink than main weapons, though, so watch your ink tank... Go to the Equip menu, select a weapon, and hit twice to learn more about sub weapons. Why don't you take a few sub weapons for a spin at the test range?",

"The Fresh Meter in the match menu measures your purrrformance! When you win, the meter goes up. But if you lose a Turf War battle, it drops. The meter also changes the color of the flag by each weapon in the Equip menu. Use the Fresh Meter to see your personal records for each weapon, then try to top them!",

"Ever run out of ink at a critical moment? Press to dive into your ink and refill!  Pro tip: swimming in your team's ink is the fastest way to refill your ink tank! Why not put that fast ink refilling to work with some target practice?",

"When you're not busy in a battle, press to open up the main menu... There's an Options tab in there that'll let you adjust things to suit your style. For instance, if the camera moves too fast or ink colors are hard to tell apart, you can change it. Speaking of the camera, you can even have diffurrrent settings for TV and handheld modes!",

"Press during battle to open the Turf Map it's supurrr useful! One glance, and you'll see where each team has inked. Then you can plan your next move! Don't believe me? Try opening the Turf Map now!",

"To Super Jump to a teammate, open the Turf Map, select them with, and press Super Jumping is super good at getting you back to the front lines after being splatted. You can also tilt your controller to select which teammate you want to Super Jump to. And!  If there's a Squid Beakon on the map, you can Super Jump to that too. See for yourself!",

" .. Super Jumping is a REALLY useful way to get around, but it can also be a bit risky... That's because opponents can see where Super Jumps are gonna land! So don't furrrget to check the Turf Map for ambushes before you take off!",

"Each piece of gear has certain abilities that can help you in battle. Press to open the main menu, and select Abilities within Status to check 'em all out!",

"Press to open the Equip menu. The Equip menu lets you change weapons and gear as well as adjust your control settings. You'll be changing weapons and gear A LOT, so remember: purrress for the Equip menu!",

"Use the same gear often enough, and it'll level up and gain cool secondary abilities! The effects aren't as strong as primary abilities, but more is always better, right?.. You won't know what kinds of abilities your gear will get until it levels up though... Which just means leveling up diffurrrent gear will give diffurrrent abilities for every situation!",

"Do you have any ability chunks yet? When you scrub gear or reset abilities, the original abilities turn into ability chunks. Ability chunks don't do a lot on their own, but combining them lets you add an ability to gear! Have you talked to Murch? He knows all about ability chunks. He's over in the square.",

"Equipping several of the same types of ability will cause each of that ability to get less effective. If you really want to get to see what you're capable of, you'll need to balance out your abilities.",

"Ever have trouble aiming at opponents or changing your direction purrrcisely? Tilt to change direction, or tilt the controller to aim with extra purrrcision!.. I happen to know of a few targets you can break if you want some purrractice...",

"Kid form makes you an easy target, so try to stay hidden in your ink when you're not attacking. Not only will it be harder for opponents to spot you, but you'll also refill your ink tank faster!",

"You know you can't swim, right? And that your ink dissolves in water?! Kinda strange, huh? Just be careful, and watch your step around water, ya hear!",

"You ARE remembering to check the Turf Map with, right?.. Don't just stand there after you get splatted. Use the Turf Map to plan your next move. Try to find an area with fewer bad guys, or Super Jump to a teammate and help 'em out!",

"If you hold to go into swim form, you can slip through chain-link fences and grates! Even better, your main weapon's attacks will pass through too!.. I'm sure there's a grate or two around here you can practice swimming through...",

"When you get splatted, you lose some of your special gauge. And the more special gauge you have, the more you'll lose!.. That means you should always be using your specials, but you still gotta be smart about it... Take a sec and get to know each special and a strategy for when to use 'em. Then USE 'em!",

"Press to transform and swim up inked walls. Then press to climb even faster!",

"In Splat Zones, the team that keeps control of the Splat Zones in the stage wins! You'll need to plan out the best way to keep the Splat Zones free of enemy ink. Don't try to be a hero. Coordinate to attack together as a four-purrrson team!",

"In Tower Control, the team that rides the tower into the opponent's goal wins. You can make the tower's path safer by splatting any oppawnents in its way!",

"In Rainmaker, the team that carries the Rainmaker to the other team's goal wins. Bring the Rainmaker to the checkpoint. Then break the checkpoint, and the next stop is the goal. The Rainmaker is strong, but not at close range. You'll need teamwork to clear the way!",

"The Splat Bomb is the most basic kind of sub weapon. The explosion timer starts when it lands. You can make it explode faster by rolling it. Try throwing some Splat Bombs, and see how many targets you can break at once!",

"Suction Bombs are bombs that attach to the ground or to walls. They take slightly longer to explode than Splat Bombs, but the blast radius is a bit larger. You should try breaking a few targets with Suction Bombs. It's purrretty fun!",

"Burst Bombs detonate on impact. They aren't very strong, but they don't use much ink, so you can throw two back to back! But don't take my worrrd for it. Go bust a target with some Burst Bombs!",

"Curling Bombs slide on the ground and bounce off walls. You can also adjust the detonation timing by holding them to keep them at the ready. Try throwing one into a fight, then use the path it creates to chase opponents! Curling Bombs can be hard to get the hang of, so why not practice on some targets!",

"The Point Sensor is a sub weapon for marking and tracking enemies, even if they hide in ink. Marked enemies can be seen by your whole team, so never pass up a chance to mark one! The effect of the Point Sensor lasts for a bit, so if you get hit by one, play it safe. Try throwing a few Point Sensors around!",

"The Splash Wall is a sub weapon that shields you from enemy fire. But!  Your team's ink passes right through it, so it's great for fighting on the front lines. It takes a little while to set up, though, so be careful about when and where you use it. You might want to try using up a Splash Wall here before you use one in battle!",

"The Toxic Mist sub weapon makes a cloud that slows down your opponents. Even better, opponents caught in the cloud will also start losing ink! The longer they're in the Toxic Mist, the more ink they'll lose. Purrretty cool, huh? If you like, you can use the Toxic Mist here and see how it works!",

"The Autobomb can chase down opponents on its own. As soon as it lands, it detects nearby opponents, then heads toward the nearest one. If you think an opponent is hiding out, these are great for making them break cover! Autobombs are really fun. Try breaking a few targets with them!",

"The Tenta Missiles special weapon can lock on to lots of opponents and fire missiles at them. If your opponents clump together, you could even splat the entire enemy team at once! That's not all!  It also tracks its targets, showing you where they are for a little while. You really should try it for yourself. Go launch a few Tenta Missiles at some targets!",

"Ink Mines let you set traps that detect and damage opponents who get too near. When an opponent sets one off, it explodes, which marks them and deals damage. You can place two Ink Mines at once. Put them on paths you think your opponents will use. Why don't you practice placing a couple Ink Mines?",

"The Inkjet is a special weapon that's both a jet pack AND a missile launcher! The rockets explode on impact, dealing damage to nearby opponents. You should try to aim down at the enemy's feet, which is where the jet pack comes in... Just be careful. Flying above everyone using the jet pack makes you an easy target... You need to keep moving up there, so hit to boost upward, or use swim with to drop. That was a lot, but I purrromise it's easy. Go use the Inkjet to break some targets!",

"The Ink Storm is a special weapon that creates a cloud that rains ink. You just throw out the cloud, and it'll rain down ink as it moves along. You'll slowly start to take damage under an Ink Storm, so either get out quick or whether it... You know, the targets here are having a purrretty good day... Go hit 'em with an Ink Storm!",

"The Sprinkler is a sub weapon that sprays ink all around it. It keeps working even if you move away from it, so it's great furrr guarding an area... It gets weaker over time, though, so be sure to set up a new one every now and then. Sprinklers are purrretty handy!  Try one out for yourself.",

"The Squid Beakon sub weapon lets you place a signal that your team can Super Jump to. You can use it to give your team another way to get into the battle quickly. Pro tip: if your opponents set out a Squid Beakon, act fast to find it and destroy it! Maybe seeing Squid Beakons in action will make more sense. Try placing a few yourself!",

"Your rank is an expression of the skill you show in Anarchy Battles. To raise your rank, just play some Anarchy Battles and earn some Rank Points. Anarchy Battles come in lots of flavors, like Splat Zones, Tower Control, and Rainmaker... And if you press in the battle pot menu, you can find an explanation for each one!",

"Did you know that gear comes in lots of diffurrrent brands? Me-ow. Each brand has its own style and unique design for the fashionable to pay attention to. Certain brands gain purrrticular abilities more easily than other brands too. Crab-N-Go also has drinks that make it easier to get an ability, no matter the brand!",

"Shooters, such as the Splattershot, are your basic aim-and-fire main weapons. Mastering these means learning to target opponents and knowing when you've hit them. When you have the enemy in your sights, the targeting reticle will change to a symbol. Once you see that symbol, pull the trigger, If your attack hits your opponent, you should feel a sharp reaction. But you're not done yet!  You may need to adjust your aim and shoot some more!",

"Splash Walls and Big Bubblers can block your ink from hitting an opponent. But!  If either gets hit by a Splat Bomb or a Suction Bomb, the bomb will explode right then! Don't give opponents hiding near a Splash Wall a chance to relax. Outsmart them!.. But on the other paw, if you set up a Splash Wall, opponents CAN do this to you... ",

"You been to the shop in the lobby yet? The food and drinks sold there can boost the expurrrience and cash you earn from battle. Although you'll need tickets to buy the goods, so round some up before stopping by!",

"If you want to look at how you're doing, go to the lobby terminal and hit View Replays. There you can watch replays of many of the battles you've been in. You can also watch other people's replays by entering a Replay Code. Watching yourself play, or seeing how others play, can be a great way to impurrrove!",

"Everrr gotten lost during a battle? If you have, maybe you should visit the stages on your own and do some recon. To set up a trip and get to know a stage, just talk to the Recon Guide in the square!",

"Wondering what the on gear means? That's how much star power each item has. Gear with three can have 3 secondary abilities. That's good! Check out the shops for items that come with lots of star power by default. You can also rebuy an item you already own to raise its star power! Murch knows more. He's in the square. Go make your gear be all it can be!",

"Each weapon has a Freshness rating, which grows as you use it. You'll get bonuses for boosting a weapon's rating, like Sheldon Licenses, stickers, and badges! Stickers and badges are great for showing everyone which weapons you like to use.",

"Did you know you can make changes to your Splashtag at the lobby terminal? Setting up your own banner, badges, and title is a great way to show off your personal style. You get badges by doing special tasks, while tags and titles come from the catalog or Shell-Out Machine.",

"Don't forget to put your stickers and decorations up in your locker! The locker room is in the lobby. Get yours decked out so you can show off your style. You can look at everyone else's lockers too. If you spot one you like, tell the owner it's Fresh!",

"Wanna do a Squid Surge? Swim onto a wall, hold, then release it, and off you'll go! The Squid Surge is perfect when you need to climb a wall fast to get the drop on someone. If you've got a minute, why not practice your Squid Surge?",

"When you're swimming in a hurry, you can tilt the other way and tap to do a Squid Roll! It's the perfect move for when a bomb lands in your face and you gotta get out of there FAST. You can also Squid Roll when swimming on a wall. Just tilt away from the wall and tap. Squid Rolling out of a wall is a great way to surprise an opponent. They almost never see it coming! You should try doing a few Squid Rolls. Purrractice makes perfect!",

"You start every battle on a spawner, then fly into the stage by doing a Squid Spawn. On the spawner, tilt the controller to pick a spot to land, then steer in the air to change to direction. Get splatted, and you'll return to the spawner. Pick your spot, and hit to make a comeback! You can also open the Turf Map after you get splatted if you'd rather return using a Super Jump!",

"You've been leveling up!  Time to put your skills to the test in some Anarchy Battles! Anarchy Battles are where all the serious players go for their serious splitting. Want in? Go to the battle pot, and hit to read up on how Anarchy Battles work. Good luck!",

"Pro tip: try doing recon for Anarchy Battles. Just tell the Recon Guide what mode to use. Stages can change based on what mode you're in. Do some recon, and don't get caught off guard!",

"The Angle Shooter sub weapon shoots in a straight line and leaves a trail along its path. But the really fun part is that if it hits a wall or the ground, it will BOUNCE! Opponents get marked if they touch the trail, or if they're hit. And it's pretty damaging too! Try bouncing shots around corners to mark opponents so your team can see where they are! In fact, since you're here, you could bounce a few Angle Shooter shots around right now!",

"The Trizooka special weapon launches a trio of powerful shots that spiral toward their target. Press it to get your special and start its timer. You can fire up to three times with it. Oh yeah!  The Trizooka launches ink in an arc, so tilt your aim upward to hit faraway opponents. Why not take that Trizooka for a spin and smash some targets?",

"The Big Bubbler special weapon makes a force field to protect you and your team... The force field will stop ink and bombs... except when an opponent walks inside and fires! If an opponent uses a Big Bubbler, hit the device inside or the top part to break the barrier... You know, I bet that'll make more sense if you try using a Big Bubbler for yourself...",

"The Killer Wail 5.1 special sets up devices that can lock onto and attack up to three targets. The lasers they fire can even go through walls, so there's nowhere to hide if one's locked on! There's a delay between when each device activates too. Use that to chase down opponents! The Killer Wail 5.1 is also great at breaking targets. Try it for yourself!",

"The Zipcaster special weapon lets you zip around the stages and stick to walls or floors. Aim where you want to go, and hit to zip over. You can even chain zips together! Try zipping to a wall right behind an opponent, then attacking with!  Surprise! The Zipcaster is fun, but it can be tricky, so go get some practice while you break targets.",

"Set up a Wave Breaker special weapon, and it'll send shock waves in all directions. Use to set it near a hiding spot, and the shock wave will damage AND mark opponents. Oh!  And just so you know if an opponent sets one up, you can jump over the shock wave! Go set up a Wave Breaker so you can see how they work. You're in furrr some fun!",

"The Crab Tank special weapon is, well... It's a tank in the shape of a crab! Hold for rapid-fire attacks from its claws, or press to fire its mouth cannon! It's a little slow, but if you hold, it'll turn into its mobile mode so it can move faster. Want to take the Crab Tank for a spin? Go furrr it!  Smash up some targets!",

"With chargers, such as the Splat Charger, you build up a charge to fire a powerful shot. You can even hold a charge for a li'l bit while swimming by holding it as you press to swim. Try charging up out of sight, then hop into swim form and POW! Surprise attack! But don't let me tell you how to do it. Go charge up some shots of your own!",

"Rollers, like the Splat Roller, are main weapons that can attack either side to side or up and down! If you're standing still or moving, pressing will fling ink horizontally, side to side. But if you're jumping, pressing will fling the ink vertically, up and down. It flies really far too! You'll need to use both attacks if you want to get good with rollers, so go get some practice.",

"Blasters like the, um... Blaster... are main weapons that shoot big blobs of exploding ink. You can catch enemies around corners in the explosion, or land a direct hit for big damage! Why don't you give blasters a try? I have a feeling you'll like 'em!",

"Brushes like the Octobrush let you sprint toward enemies while painting the ground under you. Hold and tilt to sprint, then ink defense lines or create ink paths for your team. But be careful!  If you run out of ink, your running speed will drop back to normal. Why don't you brush up on your brush skills for a while?",

"Splatlings like the Heavy Splatling can fire ink so fast it's almost like one big stream! How far they can fire, and for how long, is based on how long you charge them. Hold to start charging, then watch your targeting reticle. Two charges is the max. The first charge maxes out the range. The second maxes out how long the shooting lasts. Get a full charge, then let go of to start your weapon firing. Give it a try!",

"Dualies, such as the Splat Dualies, give you a weapon for each hand! Dualies also let you do a speedy Dodge Roll. While firing with, tilt and press It takes a second to recover after rolling, but you'll have better aim for a short while after. Also!  Dodge Rolls use a lot of ink, so try to keep enough ink to dodge your way out of danger! Now, get out there with your dualies and do some Dodge Rolls!",

" ..Sloshers such as, well... the Slosher are weapons that throw out great big splashes of ink. With most sloshers, swinging the controller as you attack will control where the ink flies. Purrrfecting the controller-swing trick is tough, but it's what makes sloshers so powerful! Speaking of purrractice, why not spend time with some sloshers now?",

"Brellas, such as the Splat Brella, are main weapons that can block attacks. Holding opens one up so it can block. Be careful they'll break after too many hits. Also, some brellas can be launched forward if you hold long enough! Once launched or broken, brellas can't be opened for a bit. But don't worry they'll be back! If you're going to purrractice with brellas, be sure to try both shielding AND launching!",

"Stringers, such as the Tri-Stringer, are main weapons that launch several ink shots at once. Hold to charge, then release to shoot. Charging boosts the weapon's range and power. If you release while standing or running around, you'll fire a side-to-side spread of shots. But if you're jumping when you release, the shots will launch vertically, up and down! Stringers are a bit like chargers, except it's tougher for opponents to see where you're aiming. Give stringers a try sometime. I bet you'll like them!",

"Splatanas like the Splatana Stamper are main weapons that can fling a powerful arc of ink! Press to do a horizontal slash, or hold it and release to send ink flying with a charged slash! Also, when you do a charged slash, if you tilt forward on, you'll do a powerful rush attack! Splatanas slice up targets nicely. Go see furrr yourself!",

"The Ultra Stamp special weapon is basically a giant hammer. Just hold to start swinging, and steer yourself with! You can also press to throw the stamp. Watch your aim it doesn't come back! Go give the Ultra Stamp a few swings and break some targets!",

"The Tacticooler special sets up a stand with drinks to give your team a boost. Press to set it up by your team, then allies can walk up to it to get a boost. Drinks give brief boosts, such as moving faster while on an opponent's ink. And if you're splatted while boosted, you can come back right away. That ends the boost though. Anyway, you look thirsty. Go try setting up a Tacticooler!",

"The Ink Vac is a special weapon that sucks up opponents' ink and launches it back at them. Holding will start pulling in your opponent's ink before it fires it all back. It'll also suck in ink from bombs and special weapons too! Why not give the Ink Vac a try? I'm purrretty sure you'll like it!",

"The Fizzy Bomb can be charged up so that it will explode up to three times. Hold to start charging, then release it to throw. Each explosion is kinda small, so aim well. You can charge faster by holding and shaking the controller, or by moving around a bunch! You should try throwing a few Fizzy Bombs and get the hang of them. Go break some targets!",

"The Reefslider special weapon is a shark-shaped float that you ride into your opponents. The float travels in a straight line, exploding at the end of its range, or earlier if you hit. This weapon is great for pushing deep into enemy territory or chasing down opponents. See how you like it. Go ride a Reefslider into some targets!",

"The Torpedo sub weapon is basically an opponent-seeking missile! Press to throw it. It'll detect an enemy, then fly toward them before exploding. They can be shot down in flight, though, so you'll need to think before using one. You should definitely try throwing out a Torpedo or two!",

"The Triple Inkstrike special weapon sends out beacons that call torpedoes down from above! Press it to get it ready, then hit it to put out a beacon. You can use up to three. You can try setting them out all over, or set them all in the same spot to REALLY blast an area! Try the Triple Inkstrike on some targets, and see how you like it!",

"The Booyah Bomb lets you gather power into a big ball of exploding ink to throw at enemies! If you and your allies Booyah!  with, you'll charge up faster so you can attack sooner! Anyone who does a Booyah!  to help you charge gets a little of their special gauge filled. It'll make sense once you see it in action, so go break some targets with a Booyah Bomb!",

"Have you picked up a catalog yet? You can get one over at Hotlantis. Once you have a catalog, you can raise your catalog level. Do that, and you'll get rewards! You earn catalog levels with Catalog Points, which you get from battles and Salmon Run Shifts. And each day, the first battle you win or shift you complete will earn you lots of bonus points! Catalogs are limited-time, though, so if you like what you see in one, don't wait!",

"You know what the copy machine is, right? It's the robot set up by the wall in the lobby. It can be activated by going up to it and pressing it. Press again to deactivate it. The copy machine copies what you do. Attack with or use a sub with, and it'll do it too. It's great furrr testing the Splash Wall or Big Bubbler, or when trying gear abilities!",

"In Clam Blitz, the team that throws the most clams into their opponents' basket wins! First, combine clams into a power clam, then use that to break the barrier around the basket. Once the barrier's gone, throw as many clams as you can into your opponents' basket to win!",

"Star power maxes at five, but even at three, it'll earn you gear experience faster!  You'll need cash to get gear to three, but then the experience boost lasts furrrever. More star power means you'll get ability chunks faster too, so boost your star power!",

"Have you tried the Shell-Out Machine in the lobby? It has some purrretty good prizes! Of course, it costs cash to play, but once a day you can get a discount! .. I've heard you can win a sparkling capsule there!  Wish I had that kind of luck..."]


#-CODE-#
@client.event
async def on_ready():


    @tasks.loop(hours=1) 
    async def myLoop():
        
        
        test_chan = client.get_channel('CHANNEL_KEY_HERE_WITHOUT_QUOTES')
        
        image = discord.File(random.choice(myfiles))

        msg = f"{random.choice(myjudd)} ({random.choice(myqoutes)})"

        embed = discord.Embed(title= (random.choice(myjudd)), description=f"@Judd pings ({random.choice(myqoutes)})", color=0x444444) #creates embed
        
        file = discord.File(random.choice(myfiles), filename=(random.choice(myfiles)))
        
        embed.set_image(url="attachment://image.png")
        
        await test_chan.send(file=file, embed=embed)

    myLoop.start()


#-This doesn't work at this moment-
@client.event
async def on_message(message):
    
    if message.content == 'headpat':
        
        test_chan = client.get_channel('CHANNEL_KEY_HERE_WITHOUT_QUOTES')

        await test_chan.send(random.choice(myjuddmeow), file=discord.File(random.choice(myjuddpet)))



#-Run Bot On Server-
client.run('BOT_KEY_HERE')
