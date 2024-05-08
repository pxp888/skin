# skin
skin cancer detection


## Caveat 

### This is a difficult data set.  

While I was able to get a network to converge, the final results were never close to what I would consider usable in practice.  

I'm using a relatively small CNN, which is fast to train so it makes experimentation easy, but the final test accuracy is too low to be useful for an application as serious as cancer.  

However, when studying the work others have done with the same dataset on Kaggle, it becomes clear that this is a common problem even with much larger networks.  

The most successful approach I saw was written by someone who seems to be an especially knowledgable author.  He used a very large pre-trained model as a base model, extensive data preparation, and managed to achieve a final F1 score of 73%. 

This is lower than what the same author has achieved with similar techniques on other datasets.  

This is linked to here:  

[https://www.kaggle.com/code/gpiosenka/skin-cancer-f1-score-73](https://www.kaggle.com/code/gpiosenka/skin-cancer-f1-score-73)



### Possible Causes

**Uneven Class Representation** 

While the dataset contains roughly ten thousand images, they are not evenly divided over the classes of interest, with some classes having as little as one hundred images.  

**Possible mis-labelling?** 

I don't have the knowledge to check this, but it is possible that some of the samples are mis-labelled which could cause issues. 

