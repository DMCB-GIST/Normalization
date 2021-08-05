# Re-ranking system with BERT for biomedical concept normalization

In recent years, various neural network architectures have been successfully applied to natural language processing (NLP) tasks such as named entity normalization.
Named entity normalization is a fundamental task for extracting information in free text, which aims to map entity mentions in a text to gold standard entities in a given domain-specific ontology; however, the normalization task in the biomedical domain is still challenging 
because of multiple synonyms, various acronyms, and numerous lexical variations.
In this study, we regard the task of biomedical entity normalization as a ranking problem, and propose an approach to rank normalized concepts. We additionally employ two factors that can notably affect the performance of normalization, such as task-specific pre-training (Task-PT) and calibration approach. 
Among five different biomedical benchmark corpora, our experimental results show that our proposed model achieved significant improvements over the previous methods and advanced the state-of-the-art performance for biomedical entity normalization, with up to 0.5\% increase in accuracy and 1.2\% increase in F-score.
