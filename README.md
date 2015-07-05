# scurvy2fountain
Converts scurvy screenplay text file format to Fountain screenplay text file format

This is just a super basic Python script I wrote to parse plain text screenplays written in [scurvy](https://marginalhacks.com/Hacks/scurvy) format to [Fountain](http://fountain.io). It is probably written poorly, because it's the first Python script I've ever written, but it works. (I should note that this is for Python 3.)

To give more detail:

The biggest advantage of writing in scurvy (a format probably no one has ever heard of) is that it lets you use aliases. So you can define an alias like this
```
R:=Roger
```
and the script will parse dialog from this
```
R: Hey there!
```
to this
```
ROGER
Hey there!
```
It will also parse "{R}" to "Roger" for non-dialogue lines.

This makes writing dialogue fast and easy!

You can read the [scurvy docs](https://marginalhacks.com/Hacks/scurvy/) (or read below) to see how to format your screenplay. But you don't even have to be that picky. **This script doesn't care if you ever indent with tabs or not** (it converts every tab to a space <sup><sub>because at some point you would have forgotten a tab and messed everything up</sub></sup>). It's also designed to retain extra Fountain formatting. For instance, if you add \*italics\* using asterisks, they will carry over into the resulting Fountain output script!

The disadvantages of writing in scurvy are many. It doesn't handle formatting like bold or italics. It doesn't easily convert to PDF. The Final Draft format it exports to is deprecated. It forces you to indent with a lot of useless tabs. And it stopped being developed like 10 years ago. It was great for its time, but now that Fountain exists, why not combine the best parts of both formats?

The advantages of Fountain are that it makes formatting a screenplay a breeze with tools like [Afterwriting.com](http://afterwriting.com). It supports all kinds of text formatting, and it even supports dual dialogue (something no one should ever use, ever!).

But a huge disadvantage is that it forces you to type every character name in caps for every single line of dialogue. This seems like something that was overlooked. The creators of Fountain should have (and should still) consider adding alias formatting to their markup as it would make everyone's life better.

Extra hacks
===
There are a couple of weird hacks I had to add.

One is the way the comments are handled. Since scurvy comments use "#", they will be converted to the slash-asterisk style comments used in Fountain. Unfortunately, sections in Fountain use "#" as well. So to compensate, use "|#" for a section in your scurvy file (or "|" followed by any number of #'s). This will be converted to "#" in the resulting Fountain output. (This was something I debated even including, and it's a candidate for removal. It would be easier to manually comment with slash-asterisk and use # for sections, scurvy support be damned. But I digress.)

To force a new line, use "||". This is for cases when you need to add a separate parenthetical during dialogue. So for instance, if you want
```
TODD
(to Bob)
Hey!
(to Sarah)
Bye!
```
you'll need to put
```
Todd: (to Bob) Hey!||(to Sarah) Bye!
```
Then I added some features out of laziness. To force a line to be in caps, start it with "!". To force a character's name in all caps (for non-dialogue aliases), use "{!x}" where x is the alias you've defined. For instance
```
r:=Rob
!int. living room - day
{!r} is all alone. {r} cries to himself.
```
becomes
```
INT. LIVING ROOM - DAY
ROB is all alone. Rob cries to himself.
```
The script also converts "(cont)" and "(cont'd)" and a few other variations to "(CONT'D)" for consistency's sake, and it will force a Fountain scene transition (marked with ">") for things like "Cut to:", "Fade out:", "Dissolve:", etc. There's a possibility (i.e. a pretty good chance) that you'll still have to do some final tweaking and editing to the Fountain output script, but for the most part it should convert faithfully.

Todo
===

The only thing that this script definitely won't convert is the title page information. You'll have to add that to the resulting Fountain output script manually. (If you try to add it to the beginning of the scurvy file, you'll end up with dialogue!)

Also, it should be more robust. It will be if I get better at learning Python!

Example
===

Input:
```
# Yay! Screenwriting is fun!
# I am going to make a lot of money!
#-----------------------------------
A:=Andy
T:=Tom
INT. MESSY KITCHEN - MORNING
Paper plates, pizza boxes, and paper towels are strewn everywhere. The SINK overflows with dirty dishes. Outside the kitchen window, the sky is grey. One HAND turns on the FAUCET while another holds a glass under it. To fit above the mess of dishes, the glass has to tilt almost entirely sideways. WATER just pours out.
{!A} (late 20's, average-looking), clean-cut and dressed for work, looks visibly frustrated.
A: (groans, almost growling) Urghhh...
The glass is almost totally empty. {A} slowly tilts it like he's going to drink it, but instead peers inside it to watch the water pour out, DRIBBLING onto the floor.
Fred (V.O.): (screaming) AAAAHHHHHH!!!!!!
A: Gosh darn heck.
{A} hears a DOOR open and loud FOOTSTEPS. {!T} (late 20's), wears pajama pants and a t-shirt and has bed head. He walks into the kitchen.
A (cont): (grumbles reluctantly) Morning.
T: Somebody should *really* do something about those dishes.
{A} glares at him.
cut to:
!int. clean kitchen - morning
A spotless silver sink shimmers in the sunlight pouring in through the kitchen window. A HAND opens a CABINET while another reaches in to pick out one sparkling clear glass from several arranged in perfect rows. The hands flawlessly move the glass under the faucet and turn on the water. The glass fills to the brim and the faucet is shut off.
{A} takes a drink of water and swallows.
A: Ahhh.
FOOTSTEPS are heard as {T} walks into frame.
A (cont): (cheerily) Good morning!
T: (smiles) Good morning!
A: Thanks for taking care of the dishes last night. I really appreciate it.
T: No problem!
```
Output:
```
/*  Yay! Screenwriting is fun! */
/*  I am going to make a lot of money! */
/* ----------------------------------- */
INT. MESSY KITCHEN - MORNING

Paper plates, pizza boxes, and paper towels are strewn everywhere. The SINK overflows with dirty dishes. Outside the kitchen window, the sky is grey. One HAND turns on the FAUCET while another holds a glass under it. To fit above the mess of dishes, the glass has to tilt almost entirely sideways. WATER just pours out.

ANDY (late 20's, average-looking), clean-cut and dressed for work, looks visibly frustrated.

ANDY
(groans, almost growling)
Urghhh...

The glass is almost totally empty. Andy slowly tilts it like he's going to drink it, but instead peers inside it to watch the water pour out, DRIBBLING onto the floor.

FRED (V.O.)
(screaming)
AAAAHHHHHH!!!!!!

ANDY
Gosh darn heck.

Andy hears a DOOR open and loud FOOTSTEPS. TOM (late 20's), wears pajama pants and a t-shirt and has bed head. He walks into the kitchen.

ANDY
(grumbles reluctantly)
Morning.

TOM
Somebody should *really* do something about those dishes.

Andy glares at him.

> CUT TO:

INT. CLEAN KITCHEN - MORNING

A spotless silver sink shimmers in the sunlight pouring in through the kitchen window. A HAND opens a CABINET while another reaches in to pick out one sparkling clear glass from several arranged in perfect rows. The hands flawlessly move the glass under the faucet and turn on the water. The glass fills to the brim and the faucet is shut off.

Andy takes a drink of water and swallows.

ANDY
Ahhh.

FOOTSTEPS are heard as Tom walks into frame.

ANDY (CONT'D)
(cheerily)
Good morning!

TOM
(smiles)
Good morning!

ANDY
Thanks for taking care of the dishes last night. I really appreciate it.

TOM
No problem!
```
[Click here to see the PDF output from Afterwriting.com](https://www.dropbox.com/s/4eve1o82ye0lh6i/output.pdf?dl=0)

Usage
===
python scurvy2fountain.py [text file]

This will create a file.fountain text file.

License
===
You're free to use this pretty much however you want. Make it better and claim it as your own, doesn't really bother me. Give me some credit if you feel like it.

Happy writing!
===
