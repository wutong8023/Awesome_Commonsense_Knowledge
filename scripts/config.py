"""
Configuration

Author: Tong
Time: 24-06-2021
"""
user_id = "wutong8023"  # github id
author_info = "Tongtong Wu"  # used in introduction
personal_link = "https://wutong8023.site"  # used in introduction
repo_name = "Text2Event"  # repository name
branch_name = "blob/main"  # branch name
your_research_topic = "EE"  # used for dictionary name
your_research_topic_full_name = "Event Extraction"  # used for title
bib_link_overleaf = "https://www.overleaf.com/read/rgscdxhxbwhp"  # used for overleaf
color = "blue"

base_link = f"https://github.com/{user_id}/{repo_name}/{branch_name}/paper_list/"

# user customized taxonomy
fined_taxonomy = {
    "Conference": ["ACL", "EMNLP", "NAACL", "COLING", "EACL", "CoNLL", "ICML", "ICLR", "NeurIPS", "AISTATS", "AAAI",
                   "IJCAI", "WWW", "MM", "CVPR", "ICCV", "ECCV", "WACV"],
    
    "Journal": [
        ["TACL", "Transactions of the Association for Computational Linguistics", "Trans. Assoc. Comput. Linguistics"],
        ["TKDE", "IEEE Transactions on Knowledge and Data Engineering", "{IEEE} Trans. Knowl. Data Eng."],
        ["TNNLS", "IEEE Transactions on Neural Networks and Learning Systems",
         "{IEEE} Trans. Neural Networks Learn. Syst."],
        ["IPM", "Information Processing and Managemen", "Inf. Process. Manag."],
        ["KBS", "Knowledge-BasedSystems", "Knowl. Based Syst."]],
    
    "Preprint": ["arXiv", "CoRR", "arxiv"],
    
    # 1: resource type
    "Contribution": ["Survey", "Important", 
    "New Settings or Metrics", 
    "New Application",
    "Empirical Study", "Theory", "New Backbone Model", "New Method", "Thesis", "Library", "Workshop",
                     "Other Type"],

    # 2: Creation Method
    "Knowledge Construction": 
    ["Crowdsourcing", 
    "Automatic Information Extraction", "Knowledge Integration",
    "Knowledge Consolidation", 
    "Other"],
    
    # 3: Data Source
    "Data Source": [
        "Wikipedia", 
        "Other"],
    
    
    # 4: Application
    "Application": [
        "Relation Extraction", 
        "Event Extraction",   
        "Question Answering",
        "Other Application", 
        ],
    
    # 5: Utilization Method
    "Knowledge Utilization": [
        "Other Approach",
        ],
    
    
    # 6: Benchmarks
    "Benchmarks": {
        "Other Benchmarks"
    }

}
