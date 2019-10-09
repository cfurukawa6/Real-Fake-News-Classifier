# Real-Fake-News-Classifier
Semester Project for CPTS 437 (Machine Learning)

## Link to lates version
https://colab.research.google.com/drive/1FkxtTqvz3NmTYaebUoaSTGR1DSdMX7gW

## Problem
- Everyday we are faced with the difficult issue of separating real and fake news
- Sometimes figuring out is difficult and honestly really annoying 
- Given a News article, we want to know if its reliable and factual

## Data
- There are hidden similarities between different “real news” articles
- “Fake News” are hard to classify because there are many types
  * Satire articles
  * Pseudo science
  * Highly biased
  * Propaganda
  * Factually inaccurate
- “Real News” should be more similar to each other and thus easier to identify

## Hypothesis 
- Around 200k different articles from different online outlets
- Roughly 50/50 split between real news and fake news
- Original data had multiple labels for articles that are not considered “real news”
- Author did not provide documentation for the dataset

## Methods 
- Change original labels into binary labels
  * We don’t care if “fake news” is actually “junksci”, only if its real
- Vectorize the data
  * Each unique word becomes a feature
- TF-IDF
  * Reduce the effect of the varying length of articles
  * Reduce the effect of common words
- Remove stop words
  * Remove unimportant words from feature list to reduce dimension
- Stemming
  * Reduce inflected or derived words to their own stem/base/root
  * E.g. fishing/fisher/fished -> fish
- Ensemble
  * Ensemble will predict based on a majority vote of the classifiers
## Future Work
- Tuning hyper parameter on a couple classifiers
- Grid search takes too long
- Find/extract/collect data with more reliable labels
  * The data we have is noisy, some labels are not correct
- Expand to identify non-English articles
  * Need different way to vectorize
  * Need different stemmer

