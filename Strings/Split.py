# """""" multiline accepted si pot sa pun mai multe linii si le vede ca si un string

text = """ 
History (from Ancient Greek: ἱστορία, romanized: historíā, lit. 'inquiry; knowledge acquired by investigation')[2] is the study and the documentation of the past.[3][4] Events before the invention of writing systems are considered prehistory. "History" is an umbrella term comprising past events as well as the memory, discovery, collection, organization, presentation, and interpretation of these events. Historians seek knowledge of the past using historical sources such as written documents, oral accounts, art and material artifacts, and ecological markers.[5]

History is also an academic discipline which uses narrative to describe, examine, question, and analyze past events, and investigate their patterns of cause and effect.[6][7] Historians often debate which narrative best explains an event, as well as the significance of different causes and effects. Historians also debate the nature of history as an end in itself, as well as its usefulness to give perspective on the problems of the present.[6][8][9][10]

Stories common to a particular culture, but not supported by external sources (such as the tales surrounding King Arthur), are usually classified as cultural heritage or legends.[11][12] History differs from myth in that it is supported by verifiable evidence. However, ancient cultural influences have helped spawn variant interpretations of the nature of history which have evolved over the centuries and continue to change today. The modern study of history is wide-ranging, and includes the study of specific regions and the study of certain topical or thematic elements of historical investigation. History is often taught as a part of primary and secondary education, and the academic study of history is a major discipline in university studies.

Herodotus, a 5th-century BC Greek historian, is often considered the "father of history" in the Western tradition,[13] although he has also been criticized as the "father of lies".[14][15] Along with his contemporary Thucydides, he helped form the foundations for the modern study of past events and societies.[16] Their works continue to be read today, and the gap between the culture-focused Herodotus and the military-focused Thucydides remains a point of contention or approach in modern historical writing. In East Asia, a state chronicle, the Spring and Autumn Annals, was reputed to date from as early as 722 BC, although only 2nd-century BC texts have survived.

"""


print(len(text.split())) # cate cuvinte sunt
                         # text.split practic transforma textul intr-o lista








word_dictionary = {}

for word in text.split():
    if word in word_dictionary:
        #word_dictionary[word] = word_dictionary[word] +1 linia 29 si 30 fac acelasi lucru
        word_dictionary[word] += 1
    else:
        word_dictionary[word] = 1

print(word_dictionary)