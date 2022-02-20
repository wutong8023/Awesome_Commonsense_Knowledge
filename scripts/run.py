from utils import generate_md_file
import bibtexparser
from config import *

file_name = 'bibtex.bib'
with open(file_name) as bibtex_file:
    bibtex_str = bibtex_file.read()
bib_db = bibtexparser.loads(bibtex_str, parser=bibtexparser.bparser.BibTexParser(ignore_nonstandard_types=False))


def check_repetition(DB=bib_db):
    bib_dict = {}
    for entry in DB.entries:
        title = entry["title"]
        title = str(title).strip()
        title = title.replace("{", "").replace("}", "")
        if title in bib_dict.keys():
            bib_dict[title] = bib_dict[title] + 1
        else:
            bib_dict[title] = 1
    repet_bib = [i for i in bib_dict.keys() if bib_dict[i] > 1]
    
    if len(repet_bib) != 0:
        print("Attention! Repetition detected in the bibtex file! Please check the following entries:")
        print("---------------------------")
    for i, title in enumerate(repet_bib):
        print(i + 1, title)


def plot_titles(titles):
    return '\n' + "## " + titles[0] + '\n'


def get_outline(list_classif, count_list, filename, dicrib, add_hyperlink=False):
    # todo: could be removed
    external_link = "[![](https://img.shields.io/badge/Awesome_Continual_Learning-yellow)](https://github.com/wutong8023/Awesome_Continual_Learning.git) " \
                    "[![](https://img.shields.io/badge/Awesome_Few_Shot_learning-green)](https://github.com/wutong8023/Awesome_Few_Shot_Learning.git) " \
                    "[![](https://img.shields.io/badge/Awesome_Information_Extraction-blue)](https://github.com/wutong8023/Awesome_Information_Extraction.git) " \
                    "[![](https://img.shields.io/badge/Awesome_Ideas-orange)](https://github.com/wutong8023/Awesome_Ideas.git)\n\n"
    
    if filename.startswith("" + your_research_topic + "4nlp"):
        str_outline = external_link
        str_outline += "# " + your_research_topic_full_name + " Literature in NLP \n"
    elif filename.startswith("" + your_research_topic + "4cv"):
        str_outline = external_link
        str_outline += "# " + your_research_topic_full_name + " Literature in CV \n"
    else:
        str_outline = external_link
        str_outline += "# " + your_research_topic_full_name + " Literature \n"
    
    str_outline += "This repository is maintained by [{author_info}]({personal_link}). " \
                   "Please don't hesitate to send me an email to collaborate or fix some entries (wutong8023 AT gmail.com). \n" \
                   "The automation script of this repo is powered by " \
                   "[Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git).\n\n" \
                   "You can directly use our bibtex.bib in overleaf with this " \
                   "[link]({bib_link_overleaf}).\n\n" \
                   "".format(author_info=author_info, personal_link=personal_link, bib_link_overleaf=bib_link_overleaf)
    
    str_outline += dicrib + "\n\n"
    
    str_outline += "## Outline \n"
    
    if add_hyperlink:
        hyperlink = f"![](https://img.shields.io/badge/Hyperlink-{color})"
        link = base_link + filename + '#hyperlink'
        str_outline += "- [" + hyperlink + "](" + link + ')\n'
    
    for i, item in enumerate(list_classif):
        paper_number = "![](https://img.shields.io/badge/{}-{}-{})".format(
            item[0].replace(" ", "_").replace("-", "_"), str(count_list[i]), color)
        link = base_link + "" + filename + "#" + item[0].replace(" ", "-").lower()
        paper_number = "[{}]({})".format(paper_number, link)
        
        str_outline += "- " + paper_number + '\n'
    
    return str_outline

def get_hyperlink(hyperlinks, mapping_name):
    str_hyperlink = "## Hyperlink \n"
    
    hyperlinks = sorted(hyperlinks)
    
    # Note: please check the branch name carefully!
    str_hyperlink += f"- [Homepage]({base_link}README.md)\n"
    for i, item in enumerate(hyperlinks):
        str_hyperlink += "- "
        all_link = "![](https://img.shields.io/badge/ALL-green)"
        # nlp_link = "![](https://img.shields.io/badge/NLP-green)"
        # cv_link = "![](https://img.shields.io/badge/CV-green)"

        # str_hyperlink += f"[[NLP]]({base_link + your_research_topic}4nlp/{item})"
        # str_hyperlink += f"  [[CV]]({base_link + your_research_topic}4cv/{item})"
        str_hyperlink += f" [{mapping_name[item]}]({base_link + your_research_topic}4all/{item})\n"
    
    return str_hyperlink

def plot_content(index, keys, dir_path, disc, list_type, plot_titles=plot_titles, sub_dirs=None, mapping_name=None):
    # generate_md_file(DB=bib_db, list_classif=list_type, key=keys, plot_title_fct=plot_titles,
    #                  filename="README.md", add_comments=True, dir_path=sub_dirs[0][index], filter_key="keywords",
    #                  filter_content=["NLP", "Multi-Modal"], mapping_name=mapping_name,
    #                  discrib=disc + ", filtered by NLP area.", add_hyperlink=True, hyperlinks=dir_path,
    #                  get_outline=get_outline, get_hyperlink=get_hyperlink)
    # generate_md_file(DB=bib_db, list_classif=list_type, key=keys, plot_title_fct=plot_titles,
    #                  filename="README.md", add_comments=True, dir_path=sub_dirs[1][index],
    #                  filter_key="keywords", mapping_name=mapping_name,
    #                  filter_content=["CV", "Multi-Modal", ],
    #                  discrib=disc + ", filtered by CV area.", add_hyperlink=True,
    #                  hyperlinks=dir_path, get_outline=get_outline, get_hyperlink=get_hyperlink)
    for dir_ in [sub_dirs[0][index], "./"]:
        generate_md_file(DB=bib_db, list_classif=list_type, key=keys, plot_title_fct=plot_titles,
                         filename="README.md", add_comments=True, dir_path=dir_,
                         mapping_name=mapping_name,
                         discrib=disc + ".", add_hyperlink=True, hyperlinks=dir_path, get_outline=get_outline,
                         get_hyperlink=get_hyperlink)
        if index != 0:
            break


# check repetition
check_repetition()

dir_path = [
"./", 
"contribution", 
"time", 
"application", 
"data_source", 
"construction", 
"utilization",
"author", 
"benchmark",
"venue"]

dir_path_dict = {dir_p: index for index, dir_p in enumerate(dir_path)}

mapping_name = {
    "./": "Summary",
    "venue": "Published Venue",
    "time": "Published Time",
    "application": "Application",
    "contribution": "Contribution",
    "data_source": "Data Source",
    "construction": "Knowledge Construction",
    "utilization": "Knowledge Utilization",
    "benchmark": "Benchmarks",
    "author": "Author",
}
dir_path_IE4all = ["" + your_research_topic + "4all/" + dp for dp in dir_path]
# dir_path_IE4nlp = ["" + your_research_topic + "4nlp/" + dp for dp in dir_path]
# dir_path_IE4cv = ["" + your_research_topic + "4cv/" + dp for dp in dir_path]
sub_dirs = [dir_path_IE4all]

# 0 Home
list_type = [[venue] for venue in fined_taxonomy["Conference"]]
list_type += fined_taxonomy["Journal"]
list_type.append(fined_taxonomy["Preprint"])
indexs = [0, -1]
disc = "This page categorizes the literature by their **Published Venue**."
for index in indexs:
    plot_content(index=index, keys=["booktitle", "journal"], dir_path=dir_path, disc=disc, list_type=list_type,
                 sub_dirs=sub_dirs, mapping_name=mapping_name)

# 1 Contribution
list_type = [[typ] for typ in fined_taxonomy["Contribution"]]
index = dir_path_dict["contribution"]
disc = "This page categorizes the literature by their **Main Contribution**."
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 2 time
list_type = [[str(year)] for year in range(1980, 2030)][::-1]
index = dir_path_dict["time"]
disc = "This page categorizes the literature by their **Released Time**."
plot_content(index=index, keys=["year"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 3 Data Source
list_type = [[sp] for sp in fined_taxonomy["Data Source"]]
index = dir_path_dict["data_source"]
disc = "This page categorizes the literature by their **Data Source of Commonsense Knowledge Base**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 4 construction method
list_type = []
for key in fined_taxonomy["Knowledge Construction"]:
    if key in fined_taxonomy.keys():
        list_type += [[k] for k in fined_taxonomy[key]]
    else:
        list_type.append([key])
index = dir_path_dict["construction"]
disc = "This page categorizes the literature by their **Construction Method of Commonsense Knowledge Bases**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)


# 5 application
list_type = [[app] for app in fined_taxonomy["Application"]]
index = dir_path_dict["application"]
disc = "This page categorizes the literature by their **Downstream Application**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 6 Utilization
list_type = []
for key in fined_taxonomy["Knowledge Utilization"]:
    if key in fined_taxonomy.keys():
        list_type += [[k] for k in fined_taxonomy[key]]
    else:
        list_type.append([key])
index = dir_path_dict["utilization"]
disc = "This page categorizes the literature by their **Utilization Manner of Commonsense Knowledge**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 7 Benchmarks
list_type = []
for key in fined_taxonomy["Benchmarks"]:
    if key in fined_taxonomy.keys():
        list_type += [[k] for k in fined_taxonomy[key]]
    else:
        list_type.append([key])
index = dir_path_dict["benchmark"]
disc = "This page categorizes the literature by their **Evaluation Benchmarks of Commonsense Knowledge**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type, sub_dirs=sub_dirs,
             mapping_name=mapping_name)

# 12 Author
index = dir_path_dict["author"]
disc = "This page categorizes the literature by their **Authors** who contributed at least 2 papers in this area."
plot_content(index=index, keys=["author"], dir_path=dir_path, disc=disc, list_type=None, sub_dirs=sub_dirs, mapping_name=mapping_name)
