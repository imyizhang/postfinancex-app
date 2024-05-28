<br>

<img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png" alt="Streamlit logo" style="margin-top:50px"></img> 



# PostFinanceX - AI Copilot Knowledge Development Journey

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://postfinance.streamlit.app/)

We are dedicated to a robust and progressive AI Copilot Knowledge Development Journey.

**Our focus** is on scaling our enterprise Retrieval-Augmented Generation (RAG) solution by evolving from Prompt Engineering to Flow Engineering, ensuring a more holistic and resilient framework.

**Our vision** is to enhance our system's precision and reliability, enabling it to handle complex scenarios with greater robustness and efficiency, ultimately facilitating a seamless integration of AI-driven insights into enterprise operations.



## Enterprise RAG Solution

![image-20240528132950421](/Users/yizhang/Library/Application Support/typora-user-images/image-20240528132950421.png)



## Deliverables

### PostFinanceX

[![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&color=black&label)](https://github.com/imyizhang/postfinancex) [![PyPI](https://badgen.net/pypi/v/postfinancex?icon=pypi&color=black&label)](https://www.pypi.org/project/postfinancex)

**Scenario:**

As a developer at PostFinance, I want to further develop the product

**Targeted audience:**

Developers at PostFinance

**Installation:**

```bash
pip install postfinancex
```



### Chat

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://postfinance.streamlit.app/)

**Scenario:**

As an employee at PostFinance, I want to get insights from recorded Customer Calls in the Call Center with the ease of question answering

**Targeted audience:**

Employees at PostFinance

**Live demo:**

1. First of all, enable custom mode, and **make sure the tools are enabled**: `graph_qa`, `vector_search`

2. Get started with searching for some facts:

   ```
   What is the most commonly used language in recorded customer calls?
   ```

3. Try another one:

   ```
   How many recorded customer calls are there?
   ```



**Scenario:** 

As a customer of PostFinance, I need some help with the ease of question answering

**Targeted audience:**

Customers of PostFinance

**Live demo:**

1. First of all, enable custom mode, and **make sure the tools are enabled**: `vector_search`

2. Get started with a topic on:

   ```
   What is the overdraft fee?
   ```

3. Try another one depending on the response, for example:

   ```
   How could I avoid it?
   ```



### Analytics

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://postfinance.streamlit.app/Analytics)

**Scenario:**

As an employee at PostFinance, I want to get insights from data storytelling report visualizing comprehensive analytics on recorded Customer Calls in the Call Center

**Targeted audience:**

Employees at PostFinance



### Review

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://postfinance.streamlit.app/Review)

**Scenario:**

As an employee at PostFinance, I want to review Transcripts, Translations and Annotations of recorded Customer Calls in the Call Center

**Targeted audience:**

Employees at PostFinance



### Translate

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://postfinance.streamlit.app/Translate)

**Scenario:**

As an employee at PostFinance, I want to translate Transcripts of recorded Customer Calls in the Call Center

**Targeted audience:**

Employees at PostFinance

**Live demo:**

1. Get started with a translated transcript (Swiss German) in Markdown format:

   ```markdown
   **Skript 10 - Anforderung von Kontodokumenten**
   
   **Call-Center-Mitarbeiter (CCM):** "Guten Tag, hier spricht [Name] von der [Bankname] Kundenbetreuung. Wie kann ich Ihnen heute helfen?"
   
   **Kunde (K):** "Hallo, mein Name ist [Kundenname]. Ich hätte gerne eine Kopie meiner Kontoauszüge der letzten drei Monate. Könnten Sie mir dabei helfen?"
   
   **CCM:** "Natürlich, das mache ich gerne für Sie, [Kundenname]. Kann ich bitte Ihre Kontonummer oder Ihre Kundennummer haben, um Ihr Konto zu verifizieren?"
   
   **K:** "Ja, meine Kontonummer ist [Nummer]."
   
   **CCM:** "Vielen Dank, [Kundenname]. Ich habe Ihr Konto gefunden. Bevor ich fortfahre, kann ich bitte noch ein Sicherheitsmerkmal abfragen, wie etwa Ihr Geburtsdatum oder Ihre Adresse?"
   
   **K:** "Mein Geburtsdatum ist der [Datum]."
   
   **CCM:** "Perfekt, danke für die Bestätigung. Ich sehe hier, dass wir Ihnen die Kontoauszüge auf zwei Arten zukommen lassen können: entweder per Post oder digital per E-Mail. Welche Option bevorzugen Sie?"
   
   **K:** "Per E-Mail wäre toll."
   
   **CCM:** "In Ordnung, ich sende Ihnen die Kontoauszüge der letzten drei Monate an Ihre bei uns hinterlegte E-Mail-Adresse. Das sollte innerhalb der nächsten 24 Stunden geschehen. Gibt es noch etwas, bei dem ich Ihnen behilflich sein kann?"
   
   **K:** "Nein, das war's, vielen Dank für Ihre Hilfe."
   
   **CCM:** "Sehr gerne, [Kundenname]. Sollten Sie weitere Fragen haben oder Unterstützung benötigen, zögern Sie bitte nicht, uns erneut zu kontaktieren. Ich wünsche Ihnen einen schönen Tag!"
   
   **K:** "Danke, das wünsch ich Ihnen auch. Auf Wiederhören."
   
   **CCM:** "Auf Wiederhören!"
   ```



### Annotate

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://postfinance.streamlit.app/Annotate)

**Scenario:**

As an employee at PostFinance, I want to annotate Transcripts of recorded Customer Calls in the Call Center with only single click

**Targeted audience:**

Employees at PostFinance

**Live demo:**

1. Get started with a translated transcript (English) in Markdown format:

   ```markdown
   **Script 10 - Request for Account Documents**
   
   **Call-Center Employee (CCE):** "Hello, this is [Name] from [Bankname] Customer Service. How can I help you today?"
   
   **Customer (C):** "Hello, my name is [Customer Name]. I would like a copy of my account statements for the past three months. Can you help me with that?"
   
   **CCE:** "Sure, I can do that for you, [Customer Name]. May I please have your account number or customer number to verify your account?"
   
   **C:** "Yes, my account number is [Number]."
   
   **CCE:** "Thank you, [Customer Name]. I have found your account. Before I proceed, may I confirm a security feature, such as your date of birth or address?"
   
   **C:** "My date of birth is [Date]."
   
   **CCE:** "Perfect, thank you for confirming. I see that we can provide you with account statements in two ways: either by mail or digitally by email. Which option would you prefer?"
   
   **C:** "By email would be great."
   
   **CCE:** "Alright, I will send you the account statements for the past three months to the email address we have on file for you. This should happen within the next 24 hours. Is there anything else I can help you with?"
   
   **C:** "No, that was it. Thank you for your help."
   
   **CCE:** "You're welcome, [Customer Name]. If you have any other questions or need further assistance, please don't hesitate to contact us again. I wish you a nice day!"
   
   **C:** "Thank you, you too. Goodbye."
   
   **CCE:** "Goodbye!"
   ```



## Roadmap

### As-Is Scenario

Call Center employees at PostFinance aim to resolve customers' problems, release new products or services, or enhance customer relationships through customer interactions.

**Pain Points:**

* Lack of understanding of customer needs and problems 
* High, manual effort for post-processing of Customer Calls
* Large amount of unused Customer Calls



### To-Be Scenario

#### Phase 1: Knowledge Discovery

**User Story:** As a Call Center employee at PostFinance, I want to have recorded Customer Calls automatically transcribed, translated and annotated in order to facilitate further processing.

**Definition of Done:**

- [ ] Support to transcribe Customer Calls
- [x] Support to translate Transcripts
- [x] Support to annotate Translations
- [x] Support to store Transcripts, Translations and Annotations in database



**User Story:** As a Call Center employee at PostFinance, I want to identify the intents of recorded Customer Calls, i.e., to identify customers' questions, problems or requests in order to have a better understanding of the unused Customer Calls.

>**Type: Question**
>
>Description: The customer is asking a technical question or a how-to question about the products or services.
>
>**Type: Problem**
>
>Description: The customer is describing a problem they are having. They might say they are trying something, but it's not working. They might say they are getting an error or unexpected results.
>
>**Type: Request**
>
>Description: The customer is requesting something. They might say they are needing information about something to be sent to their email address or mail address.

**Definition of Done:**

- [x] Support to identify customers' questions, problems or requests as Annotations given Translations of Customer Calls
- [x] Support to cite the sources of Customer Calls



**User Story:** As a Call Center employee at PostFinance, I want to review Transcripts, Translations and Annotations of Customer Calls in order to have full assurance of the discovered knowledge.

**Definition of Done:**

- [ ] Support human review for Transcript of a Customer Call on the Review page
- [x] Support human review for Translation of a Transcript on the Review page
- [x] Support human review for Annotation of a Translation on the Review page



**User Story:** As a Call Center employee at PostFinance, I want to get insights from data storytelling report visualizing comprehensive analytics on recorded Customer Calls in the Call Center in order to resolve the problems and to offer better customer experience.

**Definition of Done:**

- [x] Support data storytelling report on the Analytics page



#### Phase 2: Knowledge Sharing 

**User Story:** As an employee at PostFinance, I want to get insights from recorded Customer Calls in the Call Center with the ease of question answering in order to offer better products or services.

**Definition of Done:**

- [x] Support to chat with recorded Customer Calls using enterprise RAG solution on the Chat page



**User Story:** As a customer of PostFinance, I need some help with the ease of question answering in order to meet the needs with better self-service experience.

**Definition of Done:**

- [x] Support to chat with recorded Customer Calls using enterprise RAG solution on the Chat page



**User Story:** As a developer of PostFinance, I want to further develop products in order to scale the current solution, facilitating knowledge development.

**Definition of Done:**

- [x] Support to use open-source Python package PostFinanceX