# Enron_Email_Usecase

![demo](/assets/demo.png)

# Run

```bash
python venv venv
pip install -r requirements.txt
streamlit run app.py
```

## Roadmap:

-   11/04: email file to df
-   12/04: [M] NLP model, topic modeling [A] MVP v1
-   13/04: [M] MVP iteration... [A] MVP v2
-   14/04: [M] Polish MVP [A]Slide finish
-   15/04: [M] Rehearse

## MVP

classify 5 fams email → everyone’s mail → UI interface

## Tasks:

### Day 1:

-   Explore dataset, inditify emails from 5 VIPs
-   Classify emails
-   Read news/links from given material

### Summary Day 1:

-   [x] Morning brandstorming: define project timeline, goal, expectation of MVP. `Hsin, Alex, Saina`
-   [x] Explore dataset to df from 5 VIPs `Hsin, Alex, Saina`
-   [ ] Classify emails<br/>
-   [ ] Read news/links from given material<br/>

---

### Day 2:

-   [ ] Classify emails <br/>
        ~~Read news/links from given material~~ (discard)
-   [ ] Topic modeling
-   [x] Learning NLTK, sellecting correct methods for this project
-   [x] Preprocessing & Cleaning the sample dataset using NLTK for sub-dataset `moring`

### Summary Day 2:

Moring: we finished preprocessing email body with sample dataset
Afternoon: We planed to move on to Topic modeling, then followed the dicussion with Pierre, we decided to Learn LDP/K-mean in order to do Top modeling.

#### Difficulty:

Topic modeling is not as planed, we have to change our apporach(more deatils read above)
Ps, if you have questions we are available :-)

---

### Day 3:

-   [x] Topic modeling: try LDA method following tutorial `Hsin, Saina`
-   [x] continue eploring K-mean `Alex`
-   [x] Stat Streamlit UI

### Summary Day 3:

We have a productive day, we managed to finish all the tasks and started to implement streamlit

#### Difficulty:

-   Try to merge the code and make sure everyone is working on same code base. (solved)

---

### Day 4:

-   [x] streamlit MVP `Alex`
-   [x] Tweaking topic modeling `Saina Hsin`
-   [x] Slide `everyone`

### Summary Day 4:

Hsin and Saina spent morning on tweaking LDA model until the topics and keywords make sense.
Alex worked on implementing streamlit, we finally have a MVP.
In the afternoon, we spent 20 mins talking about slide structure and Saina worked on preparing slide.

#### Difficulty:

## Having trouble on combining topics and e-mail dataframe.(resolved)

### Day 5:

### Summary Day 5:

#### Difficulty:
