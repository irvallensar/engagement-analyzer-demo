# Engagement Analyzer
The **Engagement Analyzer** is a full-stack Natural Language Processing (NLP) web application designed to computationally identify and classify stance-taking and rhetorical engagement features in academic writing. 

Powered by a custom **Data-Augmented RoBERTa (DA-RoBERTa)** model, this tool extends Automated Writing Evaluation (AWE) systems beyond basic grammar checks by visualizing how writers interact with their audience, manage external voices, and construct arguments.

## 🚀 Live Demo
**Try the interactive web app here:** [Live Demo](https://engagement-analyzer-demo-ig9ypcamgyyyzg7efhawkk.streamlit.app/)

## ![Engagement Analyzer UI](images/demo_ui.jpg)

## 📖 How to Use the Engagement Analyzer

The interface is designed for real-time inference and token-level visualization. 

1. **Input Text:** Paste any academic abstract, essay excerpt, or argumentative paragraph into the main text area. (A default academic excerpt is provided for immediate testing).
2. **Analyze:** Click the **"Analyze Text"** button to send the text through the DA-RoBERTa inference pipeline.
3. **Interpret the Visualizations:** The model will highlight specific spans of text corresponding to different rhetorical moves. 
4. **Filter Labels:** Use the "Select entity labels" dropdown above the results to isolate specific types of engagement (e.g., viewing only where the author uses `COUNTER` arguments).

*(Note: The model is trained on a strict Token Boundary standard. Due to the architecture of standard Named Entity Recognition (NER), the model prioritizes the dominant span in cases of nested rhetorical markers).*

## 🏷️ The 10 Engagement Categories

The model extracts markers across 10 engagement labels:

 `ATTRIBUTION`, `CITATION`, `COUNTER`, `DENY`, `ENDOPHORIC`, `ENTERTAIN`, `JUSTIFYING`, `MONOGLOSS`, `PROCLAIM`, `SOURCES`

Below are the definition of the engagement labels:

**Attribution**  is an utterance which signifies dialogic space as the writer attributes the proposition to an external source. The attribution can be made to explicitly or implicitly referenced external sources, presenting the idea as a version of the truth where the writer essentially has no stake in reporting the idea (e.g., **[ Dawkins ]** believes that religion is not an adaptive evolutionary vestige, but in fact a cultural virus).

**Citation** represents a segment of the text where external sources are referenced. This includes narrative citations where the author's name is explicitly referenced in the prose, as well as in-text parenthetical citations (e.g., **Schapiro et al. (2001)** demonstrated...).

**Counter** is an utterance which expresses the present proposition as replacing and thus countering another proposition which would have been expected. It often signals concession and counter-expectations (e.g., **Although provisional**, our model has implications for pedagogy).

**Deny** is an utterance which invokes a contrary position but which at the same time rejects it directly. The contrary position is hence given very little dialogic space (e.g., The author **did not provide** any information about the method).

**Endophoric** markers are text segments that refer to information in other parts of its own text (e.g., **As described** above, other participants felt financial and psychological constraints...).

**Entertain** is an utterance which opens the dialogic space by acknowledging a proposition as one possibility amongst others (e.g., **It appears that** maximum price fixing does the greatest harm...).

**Justifying** is an utterance which engages in persuasion through justification or substantiation. It is typically achieved by subordinate clauses, prepositional phrases, or logical connectors expressing causal relations and causes (e.g., **Because of** the event happening next year, the housing prices have gone up...).

**Monogloss** is an utterance which does not employ any value of engagement. Such an utterance ignores the dialogic potential, treating the idea as an established fact or bare assertion without recognizing alternative viewpoints (e.g., Television **has helped** to shrink the relative distance between people...).

**Proclaim** represents contraction moves where the writer advances their own views on a topic, narrowing or closing down the space for negotiation. This encompasses assuming the readers agree, explicitly underscoring the view as valid, or using external data as undeniably correct (e.g., **There is no doubt that** globalization has a deep effect on China).

**Sources** represent a segment of the text where sources of information are referenced in the form of nominalized expressions, as opposed to parenthetical academic citations (e.g., **Previous studies** showed...).


## 🧠 Model Architecture & Performance
* **Base Model:** `roberta-base`
* **Augmentation:** Synthetic data generated via Large Language Models (LLMs) was injected into the training pipeline to address extreme class imbalances in pragmatically complex minority classes (Tier 3).
* **Performance:** The DA-RoBERTa model achieved a **0.7472 Macro F1** score under fixed-split evaluation, demonstrating superior stability over standard baselines.

## 🛠️ Technical Stack
* **Machine Learning:** PyTorch, Hugging Face Transformers, spaCy
* **Web Framework:** Streamlit, spacy-streamlit
* **Deployment:** Streamlit Community Cloud, Git Large File Storage (LFS)

## 💻 Local Installation
**⚠️ Important Environment Note:** This project strictly requires **Python 3.10**. Newer versions (such as 3.11 or 3.12) may fail during pip installation because the `spacy-alignments` tokenizer requires specific pre-built wheels to avoid compiling Rust code from scratch. Before deploying the app, go to "Advanced Settings" and select Python 3.10 for the environment.

If you wish to run the inference pipeline locally:

```bash
# 1. Clone the repository
git clone [https://github.com/irvallensar/engagement-analyzer-demo.git](https://github.com/irvallensar/engagement-analyzer-demo.git)
cd engagement-analyzer-demo

# 2. Pull the model weights via Git LFS
git lfs pull

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
