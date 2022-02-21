"""
Configuration

Author: Tong
Time: 24-06-2021
"""
user_id = "wutong8023"  # github id
author_info = "Tongtong Wu"  # used in introduction
personal_link = "https://wutong8023.site"  # used in introduction
repo_name = "Awesome_Commonsense_Knowledge"  # repository name
branch_name = "blob/main"  # branch name
your_research_topic = "CommonKnow"  # used for dictionary name
your_research_topic_full_name = "Commonsense Knowledge Construction and Application"  # used for title
bib_link_overleaf = "https://www.overleaf.com/read/rgscdxhxbwhp"  # used for overleaf
color = "blue"

base_link = f"https://github.com/{user_id}/{repo_name}/{branch_name}/"

# user customized taxonomy
fined_taxonomy = {
    "Conference": ["ACL", "EMNLP", "NAACL", "COLING", "EACL", "CoNLL", "ICML", "ICLR", "NeurIPS", "AISTATS", "AAAI",
                   "IJCAI", "WWW", "MM", "CVPR", "ESWC", "ICCV", "ECCV", "WACV",
                   "SIGDIAL"],
    
    "Journal": [
        ["TACL", "Transactions of the Association for Computational Linguistics", "Trans. Assoc. Comput. Linguistics"],
        ["TKDE", "IEEE Transactions on Knowledge and Data Engineering", "{IEEE} Trans. Knowl. Data Eng."],
        ["TNNLS", "IEEE Transactions on Neural Networks and Learning Systems",
         "{IEEE} Trans. Neural Networks Learn. Syst."],
        ["IPM", "Information Processing and Managemen", "Inf. Process. Manag."],
        ["KBS", "Knowledge-BasedSystems", "Knowl. Based Syst."]],
    
    "Preprint": ["arXiv", "CoRR", "arxiv"],
    
    # 1: resource type
    "Contribution": [
    "Survey", 
    "Important", 
    "New Knowledge Base",
    "New Benchmark",
    "New Settings or Metrics", 
    "New Application",
    "Empirical Study", 
    "Theory", 
    "New Backbone Model", 
    "New Method", 
    "Thesis", 
    "Library", 
    "Workshop",
    "Other Type"],

    # 2: Creation Method
    "Knowledge Construction": 
    ["Crowdsourcing", 
    "Automatic", 
    "Manual",
    "Knowledge Integration", 
    "Other Construction Method"],
    
    # 3: Data Source
    "Data Source": [
        "Wikipedia",
        "Other Data Source"],
    
    
    # 4: Application
    "Application": [
        "Relation Extraction", 
        "Event Extraction",   
        "Question Answering",
        "Sequence Matching and Inference", 
        "Dialogue System", 
        "Other Application", 
        ],
    
    # 5: Utilization Method
    "Knowledge Utilization": [
        
        "Other Utilization Method",
        ],
    
    
    # 6: Benchmarks
    "Benchmarks": {
        "Question Answering Benchmark (2 Option)",
        "Question Answering Benchmark (3 Option)",
        "Inference Benchmark (2 Option)",
        "Inference Benchmark (4 Option)", 
        "Emotion Classification Benchmark", 
        "Human Needs Classification Benchmark", 
        "Motivation Classification Benchmark",
        "Intent Classification Benchmark", 
        "Reaction Classification Benchmark",  
        "Natural Language Understanding Benchmark", 
        "Other Benchmarks"
    }

}
