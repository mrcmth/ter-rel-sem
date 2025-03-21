import requests
from bs4 import BeautifulSoup

api_url = "https://jdm-api.demo.lirmm.fr"

request_resource = "/v0/node_by_name"
request_path_parameters = "/chocolat"

get_request = api_url + request_resource + request_path_parameters
print(f"Requête (GET): {get_request}\n")

print("Envoi de requête à l'API JDM...\n")
api_get_response = requests.get(get_request)

def print_dict_nicely(d : dict):
    first_element_printed = False
    print("{ ", end="")
    for key in d:
        if first_element_printed:
            print(",\n  ", end="")
        
        print(f"{key} : {d[key]}", end="")
        first_element_printed = True
    print(" }")

if api_get_response.status_code == 200:
    api_get_result = api_get_response.json()
    #print(type(api_get_result))
    print("Réponse:")
    print_dict_nicely(api_get_result)
else:
    print("Requête échouée.")

##################################################################

print("\nRequête page Wikipedia:")

page_wiki_gastronomie = requests.get("https://fr.wikipedia.org/wiki/Gastronomie")

if page_wiki_gastronomie.status_code == 200:
    
    wiki_html_soup = BeautifulSoup(page_wiki_gastronomie.text)
    if False:
        print("HTML:")
        print(wiki_html_soup.prettify())

    """
    print("\nParagraphs:")
    n = 0
    for p_element in wiki_html_soup.find_all("p"):
        p_text = p_element.string
        if (p_text != None):
            n += 1
            print(f"<p> #{n}:")
            print(p_element.string, end="\n\n")
    """

    print("\nContenu de la page wiki:")
    wiki_content = wiki_html_soup.find(id="bodyContent")
    print(wiki_content.get_text())
else:
    print("Echec de requête.")