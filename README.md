# Cancer-Classifier-CSCI141-F19-

Name: Dante Bianco

Description: Given a data file containing hundreds of patient
records with values describing measurements of cancer tumors and whether or not each tumor
is malignant or benign, develop a simple rule-based classifier that can be used to predict whether
an as-yet-unseen tumor is malignant or benign.
The general idea is that malignant tumors are different than benign tumors. Malignant tumors
tend to have larger radii, to be more smooth, to be more symmetric, etc. Measurements have
been taken on many tumors whose class (malignant or benign) is known. The code you are
going to write will get the average score across all the malignant tumors for an attribute (e.g.
‘area’) as well as the average score for that attribute for benign tumors. Let’s say that the
average area for malignant tumors is 100, and for benign tumors is 50. We can then use that
information to try to predict whether a given tumor is malignant or benign.
Imagine you are presented with a new tumor and told the area was 99. All else being equal,
we would have reason to think this tumor is more likely to be malignant than had its area
been 51. Based on this intuition, we are going to create a simple classification scheme. We
will calculate the midpoint between the malignant average and the benign average (75 in our
hypothetical example), and simply say that for each new tumor, if its value for that attribute
is greater than or equal to the midpoint value for that attribute, that is one vote for the tumor
being malignant. Each attribute that we are using produces a vote, and at the end of counting
votes for each attribute, if the malignant votes are greater than or equal to the benign votes,
we predict that the tumor is malignant.
