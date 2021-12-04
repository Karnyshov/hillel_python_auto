import re

sections_dict = {}
section_pattern = re.compile('>\s?(.+?)\s?</a>')
subsection_pattern = re.compile('a _ngcontent-sc.+?href="(.+?)".+?class="">\s?(.+?)\s?</a>')

with open('rozetka.html', encoding='utf8') as f:
    for section_text in f.read().split('class="tile-cats__heading ng-star-inserted"'):
        section_found = section_pattern.search(section_text)
        if section_found:
            section_data = []
            for subsection in subsection_pattern.finditer(section_text):
                if subsection:
                    section_data.append(subsection.groups())
            if section_data:
                sections_dict.setdefault(section_found.groups()[0], tuple(section_data))
            section_data.clear()
    f.close()

with open('results.txt', 'w', encoding='utf8') as f:
    for section, subsections in sections_dict.items():
        f.write(f'\t{section}\t'.center(120, "-") + "\n")
        for items in subsections:
            f.write("{1:.<50}\t{0:>}\n".format(*items))
            f.flush()
        f.write("\n" * 2)
f.close()

# Write sections_dict data into file like:
# -----------------------------------------------	Велосипеди та аксесуари	------------------------------------------------
# Велосипеди........................................	https://rozetka.com.ua/bicycles/c83884/
# Велокомп'ютери....................................	https://rozetka.com.ua/velokompyutery/c268129/
# Велоаксесуари.....................................	https://rozetka.com.ua/aksessuary-dlya-velosipedov/c269513/
# Велозапчастини....................................	https://rozetka.com.ua/zapchasti-dlia-velosipedov/c4625505/
# Велорезина........................................	https://rozetka.com.ua/velorezina/c3919396/
# Велорукавиці......................................	https://rozetka.com.ua/velosipednye-perchatki/c268120/
#
#
# ---------------------------------------------------	Електротранспорт	---------------------------------------------------
# Електросамокати...................................	https://rozetka.com.ua/elektrosamokati/c4657382/
