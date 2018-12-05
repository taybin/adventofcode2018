import re

def react(content):
    start = len(content)
    after = None
    while(start != after):
        start = len(content)
        content = re.sub("(aA|bB|cC|dD|eE|fF|gG|hH|iI|jJ|kK|lL|mM|nN|oO|pP|qQ|rR|sS|tT|uU|vV|wW|xX|yY|zZ|Aa|Bb|Cc|Dd|Ee|Ff|Gg|Hh|Ii|Jj|Kk|Ll|Mm|Nn|Oo|Pp|Qq|Rr|Ss|Tt|Uu|Vv|Ww|Xx|Yy|Zz)", '', content)
        after = len(content)
    return len(content)

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for c in letters:
    with open('input.txt') as f:
        content = f.read()
    content = re.sub(c,'',content)
    content = re.sub(c.upper(), '', content)
    print(c, react(content))
