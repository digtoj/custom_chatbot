from bs4 import BeautifulSoup
import re
# Pfad zur HTML-Datei
input_html_path = './data/html/dual.html'
output_text_path = './extracted_information.txt'

# Hilfsfunktion, um übliche Reinigungen durchzuführen
def clean_text(text):
    # Entfernen von HTML-Tags
    text = BeautifulSoup(text, "html.parser").get_text()
    # Ersetzen von mehrfachen Leerzeichen, Zeilenumbrüchen und Tabs durch ein einfaches Leerzeichen
    text = re.sub(r'\s+', ' ', text)
    # Entfernen von führenden und nachfolgenden Leerzeichen
    return text.strip()

# Einlesen der HTML-Datei
with open(input_html_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Erstellen des Soup-Objekts
soup = BeautifulSoup(content, 'html.parser')

# Extraktion von Überschriften und Texten
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
paragraphs = soup.find_all('p')
links = soup.find_all('a')
tables = soup.find_all('table')

# Textinhalte sammeln
extracted_content = []

for heading in headings:
    extracted_content.append(f"Überschrift: {clean_text(heading.text)}")

for paragraph in paragraphs:
    extracted_content.append(f"Absatz: {clean_text(paragraph.text)}")

for link in links:
    href = link.get('href', '#')
    link_text = clean_text(link.text)
    extracted_content.append(f"Link: {link_text} URL: {href}")

# Tabelleninhalte extrahieren und bereinigen
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all(['td', 'th'])
        col_text = ' | '.join([clean_text(col.text) for col in cols])
        extracted_content.append(f"Tabellenzeile: {col_text}")

# Inhalt in einer Textdatei speichern
with open(output_text_path, 'w', encoding='utf-8') as file:
    file.write('\n'.join(extracted_content))

print(f"Daten wurden extrahiert und bereinigt in {output_text_path} gespeichert.")