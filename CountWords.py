#Cuantas veces se repite cada palabra del texto? examen tecnico de empresa real.

def tolowercase(texto):
    lowercase = texto.lower()
    return lowercase
    
def cleantext(textlower):
    cleanedtext = textlower.replace(",", "").replace(".", "")
    
    separatedtext= cleanedtext.split(" ")
    return separatedtext
    
def countwords(cleantext):
    dictionary = {}
    for word in cleantext:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
            
    return dictionary

texto= "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar."

lowercase = tolowercase(texto)
cleanedtext = cleantext(lowercase)
countword = countwords(cleanedtext)
print(countword)