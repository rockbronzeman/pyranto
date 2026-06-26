from tokenize import generate_tokens, untokenize
from importlib import import_module

def runpyr(file, lang):
    keywords, errors = load_localization(lang, "run")
    code = translate(file, keywords)
    try:
        exec(code) # currently technically unsafe, as anything could execute if valid
    except Exception as e:
        handle_error(e, errors)

def printpyr(file, lang):
    keywords = load_localization(lang, "print")
    code = translate(file, keywords)
    print(code)

def reverse_print(file, lang):
    keywords = load_localization(lang, "reverse")
    code = translate(file, keywords)
    print(code)

def load_localization(lang, mode):
    localization = import_module(f"pyranto.languages.{lang}")
    match mode:
        case "run":     return localization.keywords, localization.errors
        case "print":   return localization.keywords
        case "reverse": return localization.reverse

def translate(file, keywords):
    tokens = []
    with open(file) as f:
        
            for token in generate_tokens(f.readline):
                
                tokens.append((token[0],keywords.get(token[1],token[1])))

    return(untokenize(tokens))

def handle_error(e, errors):
    print("error lmao")