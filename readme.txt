This project reimplements the adjective ranking method described in "Good, Great, Excellent: Global Inference of Semantic Intensities"
by Gerard de Melo and Mohit Bansal. Transactions of the ACL (to appear).

== Application Dependencies 

This application assumes the google n-gram raw dataset is in some local directory with the following struture:

/path/to/ngram/1gms
/path/to/ngram/2gms
/path/to/ngram/3gms
/path/to/ngram/4gms
/path/to/ngram/5gms

Additionally, this project ships with parts of google ngram grepped over normalized (case folding) data using the following patterns:

just
but just
still
but still
although still
though still

but not
if not
although not
though not
even
almost
not only
not just


== Running the application 

On console, initialize the application by:

app = App("path/to/project","path/to/ngram")


Run on all patterns over all words

app.run()

After adding new patterns and/or new words

app.refresh()


== Inspecting Results      

To output rank of words word1 ... wordn, computed by application, do:

app.rank([word1, word2, ..., wordn])

This will output a tuple with
    (1) list of lists:
        [[word_i, word_j], [word_k], [word_l,..],..]
        
        where words words within each list is of equal intensity. 
        And words in higher ranked lists are stronger than those of lower ranked ones.

    (2) Raw milp object with actual values for each variable

== Computing score over all test set

app.score()

Ranks all words in testset.txt and output a dictionary with:
    (1) Average Kendall's tau score.
    (2) Absolute-average Kendall's tau score.
    (3) Generator outputting computed rankings of test set


== Adding new patterns     

modify these files:
path/to/good-great/inputs/strong-weak-patterns.txt
path/to/good-great/inputs/weak-storng-patterns.txt

according to format given

and do app.refresh()

== Adding new words        

modify this file:
path/to/good-great/inputs/testset.txt
according to format given

and do app.refresh()





