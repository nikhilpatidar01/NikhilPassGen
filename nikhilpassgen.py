import random
from datetime import datetime

# 🎨 RGB Text
def rgb(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

# 📥 Prompt with RGB
def prompt_rgb(r, g, b, msg):
    return input(f"\033[38;2;{r};{g};{b}m{msg}\033[0m").strip()

# 💻 Leetspeak
def leet(word):
    return word.replace('a', '@').replace('s', '$').replace('i', '1').replace('o', '0').replace('e', '3')

# 🌈 Color Palettes
title_color = (0, 255, 255)
subtitle_color = (255, 215, 0)
github_color = (135, 206, 250)
insta_color = (255, 105, 180)

# 🖼 Banner
banner = f"""
{rgb(*title_color, "███╗   ██╗██╗██╗  ██╗██╗  ██╗██╗██╗     ██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗")}
{rgb(*title_color, "████╗  ██║██║██║ ██╔╝██║  ██║██║██║     ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║")}
{rgb(*title_color, "██╔██╗ ██║██║█████╔╝ ███████║██║██║     ██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║")}
{rgb(*title_color, "██║╚██╗██║██║██╔═██╗ ██╔══██║██║██║     ██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║")}
{rgb(*title_color, "██║ ╚████║██║██║  ██╗██║  ██║██║███████╗██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║")}
{rgb(*title_color, "╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝")}
                                                                                                    
{rgb(*subtitle_color, "                          🔐 NikhilPassGen - v1.0 🔐")}
{rgb(*github_color,    "           GitHub   : https://github.com/nikhilpatidar01")}
{rgb(*insta_color,     "           Instagram: https://instagram.com/nikhilpatidar01")}
"""

print(banner)

# 🌐 Inputs (Optional)
name = prompt_rgb(0, 255, 128, "Enter your Name                  : ").capitalize()
surname = prompt_rgb(0, 255, 128, "Enter your Surname               : ").capitalize()
dob = prompt_rgb(255, 165, 0, "Enter DOB (DDMMYYYY)             : ")
mobile = prompt_rgb(255, 165, 0, "Enter Mobile Number              : ")
suggest_chars = prompt_rgb(173, 255, 47, "Suggest Special Chars (e.g. @#$%!_): ")
suggest_words = prompt_rgb(173, 255, 47, "Suggest Words (e.g. hacker, admin, root): ")

# ✅ Basic safe validation
dob_day = dob[0:2] if len(dob) >= 2 else ""
dob_month = dob[2:4] if len(dob) >= 4 else ""
dob_year = dob[4:] if len(dob) == 8 else ""
dob_parts = [dob_day, dob_month, dob_year, dob] if dob else []

mobile_tail = mobile[-4:] if len(mobile) >= 4 else ""
mobile_short = mobile[-6:] if len(mobile) >= 6 else ""

# Show passwords?
show = prompt_rgb(255, 192, 203, "Show passwords while generating? (yes/no): ").strip().lower()

# File setup
filename = prompt_rgb(135, 206, 250, "Filename to save passwords (default: smartpass.txt): ")
if not filename:
    filename = "nikhilpassword"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{filename}_{timestamp}.txt"

# 🧠 Wordlists
chars = list(suggest_chars) + ["", "123", "1234", "2024", dob_year, mobile_tail]
base_words = []

if suggest_words:
    base_words += [w.strip() for w in suggest_words.split(",")]

# Add optional info
if name: base_words += [name, name.lower()]
if surname: base_words += [surname, surname.lower()]
if name and surname:
    base_words += [name+surname, surname+name]
if dob:
    base_words += [dob, name+dob_day, surname+dob_year]
if mobile:
    base_words += [mobile]

# Add variants
words = []
for word in base_words:
    words.extend([word, word[::-1], word.upper(), word.capitalize(), leet(word)])

# ✨ Gen Passwords
passwords = set()
for word in words:
    for c in chars:
        for sym in suggest_chars:
            for pwd in [f"{word}{c}{sym}", f"{sym}{word}{c}", f"{word}{sym}{c}"]:
                if len(passwords) >= 1000:
                    break
                passwords.add(pwd)

# Shuffle
passwords = list(passwords)
random.shuffle(passwords)

# 💾 Save
with open(filename, "w") as file:
    print(f"\n{rgb(0, 255, 0, f'Generating top {len(passwords)} smart passwords...')}\n")
    for pwd in passwords[:1000]:
        file.write(pwd + "\n")
        if show == "yes":
            print(pwd)

print(f"\n✅ {rgb(0, 255, 0, f'Saved {min(1000, len(passwords))} passwords to: {filename}')} 🔐")
