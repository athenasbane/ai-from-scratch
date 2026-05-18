# Types of Learning 

There are three types of machine learning: 

## Supervised Learning

Buckle in... theres some maths stuff here that sounds really difficult at first then becomes pretty simple. 

In supervised learning the dataset is the collection of "labeled examples" 

$$\{(x_i, y_i)\}_{i=1}^N$$

What does this mess mean?

Lets start at the beginning with $x_i$ this is a feature vector. This of this as a list of numbers in python `[3, 85, 4.2, 1]` that we want the machine learning algorithum to learn from these numbers represent some thing i.e.

```
number of bedrooms
size in square metres
distance from city centre
has garden
```

So lets get this clear for $x_i$ using this example. Say we have three examples of housing information and are trying to predict house prices from it. our dataset (in the $x$ position) would look like this:

```
[
[3,85,4.2,1],
[4,100,7.2,0],
[3,78,10.1,1]
]
```

I will come back to it but $N=3$ in this example as we have three feature vectors. 

So $x_1$ = [3,85,4.2,1] (Important note these aren't 0 indexed like in python lists so 1 is the first element)

Within that feature vector there features 3, 85, 4.2, 1 they are noted as $x^{(j)}$ where $j$ equals the number in the vector so $x^{(1)}$ = 3 $x^{(2)}$ = 85 etc so if we are talking about the third feature in the second vector we can note that with $x_2^3$ (which equals 7.2)

So when we are refering generally to the label of say "size in square meters" we can note that as $x^{(2)}$ $k=1$,...,$N$ as it is all of the second features in the dataset.

$y_i$ can be a "finite set of classes" meaning it is example of a category e.g. "spam" "not_spam" but it could be a load of other things but usually it is a class as described or a number. Think of this as the answer that we are training the model to predict. For our example it would be the house price. $x_i$ is the data we are looking at to predict $y_i$. More on this when we understand how supervised learning works. 
```
[
      x               y
  ([3, 85, 4.2, 1], 280000),
  ([4, 100, 7.2, 0], 310000),
  ([3, 78, 10.1, 1], 240000)
]
```

The dataset is made of pairs of inputs and answers, starting at example 1 and continuing up to example N.
$N$ the number of $x_i$ and $y_i$ so in our example it would be $\{(x_i, y_i)\}_{i=1}^{N=3}$ 

## How does this work?

So in this example we have a **dataset** as described above. We need a **learning algorithm** once that learning algorithm is applied to the dataset it produces what is called a **model**. 

Lets use one learning algorithm that is called Support Vector Machine (SVM). This algorithm requires that the positive label (remember labels are the $y_i$) is a positive 1 and the negative label is a negative 1. 