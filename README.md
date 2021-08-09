# Re-ranking system with BERT for biomedical concept normalization

## Abstract
In recent years, various neural network architectures have been successfully applied to natural language processing (NLP) tasks such as named entity normalization.
Named entity normalization is a fundamental task for extracting information in free text, which aims to map entity mentions in a text to gold standard entities in a given domain-specific ontology; however, the normalization task in the biomedical domain is still challenging 
because of multiple synonyms, various acronyms, and numerous lexical variations.
In this study, we regard the task of biomedical entity normalization as a ranking problem, and propose an approach to rank normalized concepts. We additionally employ two factors that can notably affect the performance of normalization, such as task-specific pre-training (Task-PT) and calibration approach. 
Among five different biomedical benchmark corpora, our experimental results show that our proposed model achieved significant improvements over the previous methods and advanced the state-of-the-art performance for biomedical entity normalization, with up to 0.5\% increase in accuracy and 1.2\% increase in F-score.


## Data
**NCBI disease corpus**
- Doğan RI, Leaman R, Lu Z. NCBI disease corpus: a resource for disease name recognition and concept normalization. J Biomed Inform. 2014 Feb;47:1-10. doi: 10.1016/j.jbi.2013.12.006. Epub 2014 Jan 3. PMID: 24393765; PMCID: PMC3951655.
- https://www.ncbi.nlm.nih.gov/CBBresearch/Dogan/DISEASE/

**Biocreative V CDR corpus**
- Li J, Sun Y, Johnson RJ, Sciaky D, Wei CH, Leaman R, Davis AP, Mattingly CJ, Wiegers TC, Lu Z. BioCreative V CDR task corpus: a resource for chemical disease relation extraction. Database (Oxford). 2016 May 9;2016:baw068. doi: 10.1093/database/baw068. PMID: 27161011; PMCID: PMC4860626.
- http://www.biocreative.org/tasks/biocreative-v/track-3-cdr/.








# Repository Quick Start template
## Index
  - [Overview](#overview) 
  - [Getting Started](#getting-started)
  - [Contributing](#contributing)
  - [Authors](#authors)
  - [License](#license)
<!--  Other options to write Readme
  - [Deployment](#deployment)
  - [Used or Referenced Projects](Used-or-Referenced-Projects)
-->
## About RepositoryTemplate
<!--Wirte one paragraph of project description -->  
This project's purpose is to create a make Repository with a collection of default settings  

## Overview
<!-- Write Overview about this project -->
**If you use this template, you can use this function**
- Issue Template
- Pull Request Template
- Commit Template
- Readme Template
- Contribute Template
- Pull Request Build Test(With Github Actions)

## Getting Started
**click `Use this template` and use this template!**
<!--
### Depencies
 Write about need to install the software and how to install them 
-->
### Installing
<!-- A step by step series of examples that tell you how to get a development 
env running

Say what the step will be

    Give the example

And repeat

    until finished
-->
1. Click `Use this template` button 
2. Create New Repository
3. Update Readme and Others(Other features are noted in comments.)
<!--
## Deployment
 Add additional notes about how to deploy this on a live system
 -->
## Contributing
<!-- Write the way to contribute -->
I am looking for someone to help with this project. Please advise and point out.  
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Authors
  - [Always0ne](https://github.com/Always0ne) - **SangIl Hwang** - <si8363@soongsil.ac.kr>

See also the list of [contributors](https://github.com/always0ne/readmeTemplate/contributors)
who participated in this project.
<!--
## Used or Referenced Projects
 - [referenced Project](project link) - **LICENSE** - little-bit introduce
-->

