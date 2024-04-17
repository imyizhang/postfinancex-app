# PostFinanceX - AI Copilot Knowledge Development Journey

## As-Is Scenario

Employees at the PostFinance Customer Center aim to resolve customers' problems, release new products or services, or enhance customer relationships through customer interactions.

**Pain Points:**

* Lack of understanding of customer needs and problems 
* High, manual effort for post-processing of Customer Calls
* Large amount of unused Customer Calls



## To-Be Scenario

### Phase 1: Knowledge Discovery

**User Story:** As an employee at the PostFinance Customer Center, I want to have recorded Customer Calls automatically transcribed, translated and annotated in order to facilitate further processing.

**Definition of Done:**

- [ ] Support to transcribe Customer Calls
- [x] Support to translate Transcripts
- [x] Support to annotate Translations
- [x] Support to store Transcripts, Translations and Annotations in database
- [ ] Support to monitor a directory or a database, once a Customer Call is added, it would be automatically transcribed, translated and annotated



**User Story:** As an employee at the PostFinance Customer Center, I want to identify the intents of recorded Customer Calls, i.e., to identify customers' Requests, Questions or Problems in order to have a better understanding of the unused Customer Calls.

**Definition of Done:**

- [x] Support to identify customers' Requests, Questions or Problems as Annotations of Customer Calls, specifically Translations of Customer Calls
- [x] Support to cite the source part of a Customer Call, specifically Translation of the Customer Call



**User Story:** As an employee at the PostFinance Customer Center, I want to review Transcript, Translation and Annotation of Customer Calls in order to have full assurance of the discovered knowledge.

**Definition of Done:**

- [ ] Support human review for Transcript of a Customer Call on the Review page
- [x] Support human review for Translation of a Transcript on the Review page
- [x] Support human review for Annotation of a Translation on the Review page



**User Story:** As an employee at the PostFinance Customer Center, I want to know the most frequently asked questions from the customers in order to resolve the problems and to offer better customer experience.

**Definition of Done:**

- [ ] Support data storytelling with database queries on the Dashboard page



### Phase 2: Knowledge Sharing 

**User Story:** As an employee at the PostFinance, I want to get insights from Customer Calls at the PostFinance Customer Center with the ease of question answering in order to offer better products or services.

**Definition of Done:**

- [ ] Support to chat with Customer Calls, specifically Translations of Customer Calls on the Chat page