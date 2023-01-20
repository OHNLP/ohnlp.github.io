Title: About
Date: 2010-09-01
Modified: 2023-01-20
Slug: about
Authors: OHNLP Working Group
Summary: About OHNLP


# Getting Involved in OHNLP

Visit the [OHNLP Getting Involved](./get-involved.html) page.


# What is the Goal of OHNLP?

The goal of the Open Health Natural Language Processing Consortium is to establish an open source consortium to promote past and current development efforts and to encourage participation in advancing future efforts. The purpose of this consortium is to facilitate and encourage new annotator and pipeline development, exchange insights and collaborate on novel biomedical natural language processing systems and develop gold-standard corpora for development and testing. The Consortium promotes the open source UIMA framework and SDK as the basis for biomedical NLP systems. Applications created within UIMA consist of software components (referred to as annotators) and their associated configuration files and external resources. Within the framework, one can also create complete pipelines composed of a sequence of annotators and the data flow between them.

# Why use NLP?

The clinical and research medical community creates, manages and uses a wide variety of semi-structured and unstructured textual documents. To perform research, to improve standards of care and to evaluate treatment outcomes easily — and ideally, in an automated fashion — access to the content of these documents is required. The knowledge contained in unstructured textual documents (e.g., pathology reports, clinical notes), is critical to achieving all of these goals. For instance, clinical research usually requires the identification of cohorts that follow precisely defined patient- and disease-related inclusion and exclusion parameters. Biomedical NLP systems extract structured information from textual reports, facilitating searching, comparing and summarization.

# What is NLP?

Natural language processing (NLP) is a field of computer science and linguistics concerned with the interactions between computers and human (natural) languages. NLP is used to classify, extract, encode and summarize from text documents. A clinical NLP application will unlock the text to be used for decision support, outbreak detection and quality review.There are two main approaches to NLP use application, the symbolic approach and the statistical approach.

- Symbolic NLP includes:
    - Morphological Knowledge (how words are created)
    - Lexical Knowledge (string matching)
    - Syntactic Knowledge (how words can be combine to form sentences)
    - Semantic Knowledge (what words mean)
    - Pragmatic Knowledge (how sentences are used in different situations)
    - Discourse Knowledge (how the preceding sentences affect interpretation of next sentences)

- Statistical NLP includes:
    - Modeling document content as bag-of-words (if “cough” appears > fluid)
    - Modeling probabilistic relationships among words and phrases (“purulent discharge” > fluid; “upon discharge > release)
    - Modeling probabilistic relationships between words and concepts (caries, cavity, abrasion > caries)

# What are the NLP use cases in the clinical domain?

- **Patient cohort identification** - Current cohort identification mechanism available in clinical research is cost-prohibitive to many investigators and unable to scale to the demands and response time needed. Tools assisting cohort identification have the potential to greatly reduce the cost. We have a data extraction and cohort identification solution enabled by NLP to allow investigators to define a set of inclusion/exclusion criteria and enable investigators to query both structured and unstructured clinical information simultaneously. The result can be used for both feasibility study and potential participant recruitment
- **Clinical decision support** - Developing automated systems to assist decision making in clinical settings can also utilize clinical narratives. One use case is in automating colonoscopy follow-up. After a colonoscopy examination, a patient is supposed to receive a follow-up letter, recommending a schedule for future colonoscopies based on current test results, patient history, and family medical history. This process is currently done by human experts, which is error-prone, expensive, and time consuming. NLP can be applied to extract necessary information for decision support from pathology and colonoscopy reports, and to build patient profiles that become the basis for determining automatic follow-up recommendation. Since a certain portion of important information associated with follow up recommendations requires semantic understanding to be precisely extracted, the use of semantic parsing in clinical reports will boost the quality of patient profiles and therefore facilitate better colonoscopy surveillance
- **Health care quality research** - User-defined and empirically induced search patterns can be used to measure compliance with NCQA guidelines for treatment of patients with diabetes and automated health-related quality of life determination from text of physician’s observations and prediction of subsequent healthcare utilization based on NLP-derived quality of life measurements.
- **Personalized medicine** - The patients’ medication histories and their responses are of great concern to future medical treatment. In particular, the detection of medication side effects is an important issue for patient safety and pharmaco vigilance. The tracking of patient’s medication intake along with the accompanying side effects plays critical roles to advance personalized medicine and identify genetic marker of undesired medication effects. A substantial amount of medication related information resides in unstructured clinical narratives and also a fair amount of it requires better contextual understanding to be correctly retrieved.
- **BioSurveillance** - NLP has been used for biosurveillance for detecting emerging infectious diseases and acts of bioterrorism by collecting and analyzing clinical data from health care organizations. These data include the chief complaint fields from outpatient encounters and emergency department visits. Currently, biosurveillance systems retrieve chief complaint section of the encounter note and administrative codes such as ICD-9-CM. Keyword searches look for the occurrence of such word forms as “sore throat” but may miss such related notions as “pain upon swallowing” or “throat feels raw.” NLP techniques such as distributed semantics that can automatically detect words and phrases that are semantic related to a list of provided keywords would enable more accurate identification of cases.
- **Drug development** - NLP can also accelerate the development of drugs. One application is to mine drugs that can be repurposed based on a large set EMR data. After using NLP techniques for medication, diagnosis, and smoking status extraction, we replicate the finding that Metformin can be repurposed for cancer treatment. NLP can also facilitate the post market surveillance of a drug or discover adverse drug events.
- **Meaningful Use Stage 2** - NLP also plays a crucial role in meeting the requirements of the Meaningful Use Stage 2 with respect to documentation related to “transition of care (ToC)”, “data portability”, and “clinical summary”. In order to generating clinical documents meeting the requirements, clinical information regarding allergy, medication, social history such as smoking status, problem lists is required to be structured. Generating and maintaining such clinical information require either structural entries at the point of data entry or the translation of unstructured data in various clinical narratives to structured format. As most of the EMRs do not currently meet the requirements and meanwhile, historically, such information is in clinical narratives, NLP can be used to assist the generation of structured clinical information in meeting the meaningful use requirement.
- **Text Summarization** - There are two different use cases of text summarization. One is to accelerate the chart review process so that clinical information in multiple reports of the same patient can be extracted and visualized so that clinicians can quickly grasp major past medical history of a patient without performing lengthy chart reviews. The second use case is to summarize clinical information across a group of patients enabled using NLP techniques. The new annotation process will be able to group and summarize annotation text hits at both patient and document levels. This information could be used by researchers or physicians to identify medical terms that will help them to find patients cohorts based on term frequency and/or relevance by combining this information along with all other produced annotation information.