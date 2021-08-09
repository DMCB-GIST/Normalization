# Re-ranking system with BERT for biomedical concept normalization

## Abstract
<!-- Write Overview about this project -->
In recent years, various neural network architectures have been successfully applied to natural language processing (NLP) tasks such as named entity normalization.
Named entity normalization is a fundamental task for extracting information in free text, which aims to map entity mentions in a text to gold standard entities in a given domain-specific ontology; however, the normalization task in the biomedical domain is still challenging 
because of multiple synonyms, various acronyms, and numerous lexical variations.
In this study, we regard the task of biomedical entity normalization as a ranking problem, and propose an approach to rank normalized concepts. We additionally employ two factors that can notably affect the performance of normalization, such as task-specific pre-training (Task-PT) and calibration approach. 
Among five different biomedical benchmark corpora, our experimental results show that our proposed model achieved significant improvements over the previous methods and advanced the state-of-the-art performance for biomedical entity normalization, with up to 0.5% increase in accuracy and 1.2% increase in F-score.

## Architecture
https://user-images.githubusercontent.com/88476469/128655625-6a165da4-c2b5-4a2f-95cc-e7cd39f84470.jpg


## Data
**NCBI disease corpus**
- Doğan RI, Leaman R, Lu Z. NCBI disease corpus: a resource for disease name recognition and concept normalization. J Biomed Inform. 2014 Feb;47:1-10. doi: 10.1016/j.jbi.2013.12.006. Epub 2014 Jan 3. PMID: 24393765; PMCID: PMC3951655.
- https://www.ncbi.nlm.nih.gov/CBBresearch/Dogan/DISEASE/

**Biocreative V CDR corpus**
- Li J, Sun Y, Johnson RJ, Sciaky D, Wei CH, Leaman R, Davis AP, Mattingly CJ, Wiegers TC, Lu Z. BioCreative V CDR task corpus: a resource for chemical disease relation extraction. Database (Oxford). 2016 May 9;2016:baw068. doi: 10.1093/database/baw068. PMID: 27161011; PMCID: PMC4860626.
- http://www.biocreative.org/tasks/biocreative-v/track-3-cdr/.

**BioCreative II human gene normalization corpus**
- Smith L, Tanabe LK, Ando RJ, et al. Overview of BioCreative II gene mention recognition. Genome Biol. 2008;9 Suppl 2(Suppl 2):S2. doi:10.1186/gb-2008-9-s2-s2
- https://biocreative.bioinformatics.udel.edu/tasks/biocreative-ii/task-1b-human-gene-normalizati/

**Plant corpus**
- Cho, H., Choi, W. & Lee, H. A method for named entity normalization in biomedical articles: application to diseases and plants. BMC Bioinformatics 18, 451 (2017). doi:10.1186/s12859-017-1857-8.
- http://gcancer.org/plant
