import spacy
import re

nlp = spacy.load("fr_core_news_lg")

#Texte récupéré
texte_ex = """Le pot-au-feu (inv.) est une recette de cuisine traditionnelle emblématique historique de la cuisine française, 
et du repas gastronomique des Français, à base de viande de bœuf cuisant longuement à feu très doux dans un bouillon de légumes (poireau, carotte, navet, oignon, céleri, chou et bouquet garni). 
La présence de pommes de terre est discutée, puisqu’elles ne faisaient pas partie de la recette d’origine, 
la pomme de terre n’ayant été introduite en France par Antoine Parmentier qu’à la fin du XVIIIe siècle. 
Historiquement, c’est plutôt le panais qui jouait son rôle."""

stop_words = {"le", "la", "les", "l'", "un", "une", "des", "d'", "c'"}

def pretraitement(texte):
    print("Pré-traitement...")
    print(f"Texte brut: \"\n{texte}\n\"")
    doc = nlp(texte.lower())
    texte_lemmatise = " ".join([token.lemma_ for token in doc if token.text not in stop_words])
    print(f"Texte pré-traité: \"\n{texte_lemmatise}\n\"")
    return texte_lemmatise

patternes_relations = { 
    "r_is_a" : [
    r"(\b\w+\b) être (\b\w+\b)"
], "r_has_part" : [
    r" à base de "
]
}

def traitement(texte):
    print("Traitement...")
    for relation in patternes_relations:
        print(f"Relations '{relation}':")
        for patterne in patternes_relations[relation]:
            match_patterne = re.findall(patterne, texte)
            for couple_entitees in match_patterne:
                print((couple_entitees[0], relation ,couple_entitees[1]))
                

#a = pretraitement(texte_ex)
#b = traitement(a)

doc = nlp(texte_ex)
for token in doc:
    if token.pos_ == "NOUN":
        print(f"{token.text} - à gauche: \"{token.nbor(-1)}\" + à droite: \"{token.nbor(1)}\"")

for groupe_de_noms in doc.noun_chunks:
    print(f"{groupe_de_noms.text}")