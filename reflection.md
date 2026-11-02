# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

Bug 1: Hints are wrong. Expected hints that acuratlly tell whether the guess is higher or lower. The console consistantly gave inaccurate hints. This is due to app.py file function check_guess lines 35 - 50

Bug 2: New game does not let me make guesses. When you click new game after winning or losing  it is supposed to reset counter, score and make the game playable again. The game still shows You won/losing statement and stops without allowing guesses for the the next number. In app.py file, if new_game doesn't reset st.session.status to playing around line 135-150. 

Bug xtra: number of guess counter is off

Bug 3 Takes invalid edge cases. When I enter decimals, excessivly large numbers above 100 or negative number, they are all taken as valid inputs/guesses with no error which uses up an attempt. File app.py has parse_guess around line 14.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60 when the secret is 40/any number above guess | "Too High" hint telling me to go lower | Shows "Go HIGHER!" | none | app.py, check_guess (lines 36-40) |

| Click "New Game" after a win or loss, then guess | Fresh game that accepts guesses | "New game started." shows, but "Game over" or "You already won" blocks play | none  | app.py, if new_game: block (lines 134-138): status never reset |


| Guess 500 or -5 | Error message, no attempt used | Accepted as a guess and an attempt is used | none | app.py, parse_guess (lines 14-29) |

AI(claude) said that the first error on the hint is due to a mix up in the comparison logic with guess>number.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

For Bug 1 (wrong hints), Claude said the problem was a mix-up in the comparison logic in check_guess. The "Too High" and "Too Low" messages were swapped. It also found a second cause I had missed, on even attempts the secret was converted with str(secret), so the guess and secret were compared as strings instead of numbers. Its fix was to compare two ints numerically and put the correct hint with each outcome.

While fixing bugs, Claude kept suggesting that I move functions between files, such as pulling more helpers out of app.py into logic_utils.py and restructuring the modules. I did not accept this as written because it was out of scope and over-engineered. The bugs were small logic errors, and a big refactor made the diff harder to read and added a chance of new bugs. I kept only the one move that made sense with the project instructions, check_guess going into logic_utils.py with the corrected hints, and left the rest of the code where it was. 
I used Claude (Sonnet) as my only AI tool on this project.



---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I asked claude to run tests and give me potential test cases for me to try out.
 I verified it by re-running the game and checking that it now says correct hints. I also guessed across several attempts, including even-numbered ones, to confirm the hints stayed right, I also checked that the game started fresh when clicked new game new counters and and allowed guessses. I also checked the areas of the code that were edited and looked them over(despite my limited coding knowledge)
 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time a button is clicked or text is entered, Streamlit runs the code again, resetting normal variables. st.session_state saves important game information, like the secret number, guesses, score, and game status, between runs.

Bug 2 happened because "New Game" did not reset the game status. The game still thought it was over and blocked new guesses. Resetting all the game information fixed this.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

  One habit I will use is the fix me prompt whenever dealing with errors
One thing I would do differently next time is not close up different claude session till done with all editing or save the promt progress
It changes how specific I need to get with prompts but also how to error check. Using test cases and checking edited code.
