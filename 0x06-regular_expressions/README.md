# 0x06. Regular expression
A regular expression (regex or regexp for short) is a special text string for describing a search pattern.

# Brief Introduction
Twelve characters have special meanings in regular expressions: the backslash `\`, the caret `^`, the dollar sign `$`, the period or dot `.`, the vertical bar or pipe symbol `|`, the question mark `?`, the asterisk or star `*`, the plus sign `+`, the opening parenthesis `(`, the closing parenthesis `)`, the opening square bracket `[`, and the opening curly brace `{`. These special characters are often called “metacharacters”. Most of them are errors when used alone.

1. **Backslash** `\`

Used to escape metacharacter and match it literally. Example: To match a file named README.md, you'd write it like this `README\.md`.
2. **Caret** `^`

Used to denote the start of a string. `^hello` would only match 'hello' if it is at the beginning of a string.
3. **Dollar Sign** `$`

Denotes the end of a string. Example `world$` would only match 'world' if it is at the end of a string.
4. **Period** `.`

Matches any single character except newlinne characters. Example `scho.l` will match 'school', 'scholl' etc.
5. **Vertical Bar** `|`

Acts as an OR operator and matches either symbol. Example `cat|dog` will match 'cat' or 'dog'.
6. **Question Mark** `?`

Makes the preceding character optional. Example `colou?r` will take both 'color' and 'colour'.
7. **Asterisk** `*`

Matches zero or more occurences of the character. Example `.txt` will match all '.txt' files in a folder. `g*gle` will match 'google' or even 'ggle'.
8. **Plus sign** `+`

Matches one or more occurences of the preceding character. Example `go+gle` will match 'google', 'gooogle'
9. **Opening parenthesis** `(`

Marks the start of a capturing group. Used to group expressions or capture part of the matched text.
10. **Closing parenthesis** `)`

Marks the end of a capturing group.
11. **Opening square bracket** `[`

Defines a character class. Example `[aeiou]` matches any vowel.
12. **Opening curly brace** `{`

Denotes a quantifier for specifying the exact number of occureneces. Example `a{3}` will match 'aaa'
