# Author: Dante Bianco
# Date: November 19, 2019
# Description: cancer_classifier.py for Assignment 5 


###############################################################################
# GLOBAL CONSTANT
# For use as dictionary keys
# You can use this list throughout the program without passing it to a function
# DO NOT MODIFY
ATTRS = []
ATTRS.append("ID")
ATTRS.append("radius")
ATTRS.append("texture")
ATTRS.append("perimeter")
ATTRS.append("area")
ATTRS.append("smoothness")
ATTRS.append("compactness")
ATTRS.append("concavity")
ATTRS.append("concave")
ATTRS.append("symmetry")
ATTRS.append("fractal")
ATTRS.append("class")
###############################################################################


def make_training_set(filename):
    """ Read trainig data from the file whose path is filename.
        Return a list of records, where each record is a dictionary
        containing a value for each of the 12 keys in ATTRS.
    """
    # COMPLETE - DO NOT MODIFY
    training_records = []
    # Read in file
    for line in open(filename,'r'):
        if '#' in line:
            continue
        line = line.strip('\n')
        line_list = line.split(',')
        
        # Create a dictionary for the line and map the attributes in
        # ATTRS to the corresponding values in the line of the file
        record = {}
        
        # read patient ID as an int:
        record[ATTRS[0]] = int(line_list[0].strip())
        
        # read attributes 1 through 10 as floats:
        for i in range(1,11):
            record[ATTRS[i]] = float(line_list[i])
        
        # read the class (label), which is "M", or "B" as a string:
        record[ATTRS[11]] = line_list[31].strip() 

        # Add the dictionary to a list
        training_records.append(record)        

    return training_records


def make_test_set(filename):
    """ Read test data from the file whose path is filename.
        Return a list with the same form as the training
        set, except that each dictionary has an additional
        key "prediction" initialized to "none" that will be
        used to store the label predicted by the classifier. 
    """
    # COMPLETE - DO NOT MODIFY
    test_records = make_training_set(filename)

    for record in test_records:
        record["prediction"] = "none"

    return test_records


def classify_average_m(training_records):
    """ Calculate the average of each attribute in relation to a malignant tumor.
        Preconditions: Take the list training records
        Postconditions: Return a dict with the average values of each attribute stored within.
    """
     
    # calculating the averages of each attribute in relation to a malignant tumor
    classifier_m = {"radius": 0, "texture": 0, "perimeter": 0, "area": 0, "smoothness": 0, "compactness": 0, "concavity": 0, "concave": 0, "symmetry": 0, "fractal": 0}
    # dictionary to store the averages
    dict_avg_m = {"radius": 0, "texture": 0, "perimeter": 0, "area": 0, "smoothness": 0, "compactness": 0, "concavity": 0, "concave": 0, "symmetry": 0, "fractal": 0}
    
    # a loop that adds the previously stored value and adds the newest value
    count = 0
    for record in training_records:
        if "M" in record["class"]:
            classifier_m["radius"] = classifier_m["radius"] + record["radius"]
            classifier_m["texture"] = classifier_m["texture"] + record["texture"]
            classifier_m["perimeter"] = classifier_m["perimeter"] + record["perimeter"]
            classifier_m["area"] = classifier_m["area"] + record["area"]
            classifier_m["smoothness"] = classifier_m["smoothness"] + record["smoothness"]
            classifier_m["compactness"] = classifier_m["compactness"] + record["compactness"]
            classifier_m["concavity"] = classifier_m["concavity"] + record["concavity"]
            classifier_m["concave"] = classifier_m["concave"] + record["concave"]
            classifier_m["symmetry"] = classifier_m["symmetry"] + record["symmetry"]
            classifier_m["fractal"] = classifier_m["fractal"] + record["fractal"]
           
            count += 1
    
    # averages the value for each attribute in relation to malignant tumors
    (dict_avg_m["radius"]) = classifier_m["radius"] / count
    (dict_avg_m["texture"]) = classifier_m["texture"] / count
    (dict_avg_m["perimeter"]) = classifier_m["perimeter"] / count
    (dict_avg_m["area"]) = classifier_m["area"] / count
    (dict_avg_m["smoothness"]) = classifier_m["smoothness"] / count
    (dict_avg_m["compactness"]) = classifier_m["compactness"] / count
    (dict_avg_m["concavity"]) = classifier_m["concavity"] / count
    (dict_avg_m["concave"]) = classifier_m["concave"] / count
    (dict_avg_m["symmetry"]) = classifier_m["symmetry"] / count
    (dict_avg_m["fractal"]) = classifier_m["fractal"] / count
    
    return dict_avg_m
    
def classify_average_b(training_records):
    """Calculate the average of each attribute in relation to a benign tumor.
        Preconditions: Take the list training records
        Postconditions: Return a dict with the average values of each attribute stored within.
    """
    # calculating the averages of each attribute in relation to a benign tumor  
    classifier_b = {"radius": 0, "texture": 0, "perimeter": 0, "area": 0, "smoothness": 0, "compactness": 0, "concavity": 0, "concave": 0, "symmetry": 0, "fractal": 0}
    dict_avg_b = {"radius": 0, "texture": 0, "perimeter": 0, "area": 0, "smoothness": 0, "compactness": 0, "concavity": 0, "concave": 0, "symmetry": 0, "fractal": 0}

    count = 0
    for record in training_records:
        if "B" in record["class"]:
            classifier_b["radius"] = classifier_b["radius"] + record["radius"]
            classifier_b["texture"] = classifier_b["texture"] + record["texture"]
            classifier_b["perimeter"] = classifier_b["perimeter"] + record["perimeter"]
            classifier_b["area"] = classifier_b["area"] + record["area"]
            classifier_b["smoothness"] = classifier_b["smoothness"] + record["smoothness"]
            classifier_b["compactness"] = classifier_b["compactness"] + record["compactness"]
            classifier_b["concavity"] = classifier_b["concavity"] + record["concavity"]
            classifier_b["concave"] = classifier_b["concave"] + record["concave"]
            classifier_b["symmetry"] = classifier_b["symmetry"] + record["symmetry"]
            classifier_b["fractal"] = classifier_b["fractal"] + record["fractal"]
            
            count += 1
    # averages the values for each attribute in relation to benign tumors   
    (dict_avg_b["radius"]) = classifier_b["radius"] / count
    (dict_avg_b["texture"]) = classifier_b["texture"] / count
    (dict_avg_b["perimeter"]) = classifier_b["perimeter"] / count
    (dict_avg_b["area"]) = classifier_b["area"] / count
    (dict_avg_b["smoothness"]) = classifier_b["smoothness"] / count
    (dict_avg_b["compactness"]) = classifier_b["compactness"] / count
    (dict_avg_b["concavity"]) = classifier_b["concavity"] / count
    (dict_avg_b["concave"]) = classifier_b["concave"] / count
    (dict_avg_b["symmetry"]) = classifier_b["symmetry"] / count
    (dict_avg_b["fractal"]) = classifier_b["fractal"] / count
    
    return dict_avg_b


def train_classifier(training_records):
    """ Return a dict containing the midpoint between averages
        among each class (malignant and benign) of each attribute.
        (See the A5 writeup for a more complete description)
        Precondition: training_records is a list of patient record
                      dictionaries, each of which has the keys
                      in the global variable ATTRS
        Postcondition: the returned dict has midpoint values calculated
                       from the training set for all 10 attributes except
                       "ID" and"class".
    """
    # TODO 1 - implement this function        
    
    #call to the helper functions above
    dict_avg_m = classify_average_m(training_set)
    dict_avg_b = classify_average_b(training_set)
    
    # classifier dictionary
    classifier = {"radius": 0, "texture": 0, "perimeter": 0, "area": 0, "smoothness": 0, "compactness": 0, "concavity": 0, "concave": 0, "symmetry": 0, "fractal": 0}

    # calculations for each of the attributes given the averages between both
    # malignant and benign tumors for each respective attribute
    classifier["radius"] = ((dict_avg_m["radius"] + dict_avg_b["radius"]) / 2)
    classifier["texture"] = ((dict_avg_m["texture"] + dict_avg_b["texture"]) / 2)
    classifier["perimeter"] = ((dict_avg_m["perimeter"] + dict_avg_b["perimeter"]) / 2)
    classifier["area"] = ((dict_avg_m["area"] + dict_avg_b["area"]) / 2)
    classifier["smoothness"] = ((dict_avg_m["smoothness"] + dict_avg_b["smoothness"]) / 2)
    classifier["compactness"] = ((dict_avg_m["compactness"] + dict_avg_b["compactness"]) / 2)
    classifier["concavity"] = ((dict_avg_m["concavity"] + dict_avg_b["concavity"]) / 2)
    classifier["concave"] = ((dict_avg_m["concave"] + dict_avg_b["concave"]) / 2)
    classifier["symmetry"] = ((dict_avg_m["symmetry"] + dict_avg_b["symmetry"]) / 2)
    classifier["fractal"] = ((dict_avg_m["fractal"] + dict_avg_b["fractal"]) / 2)


    return classifier


def classify(test_records, classifier):
    """ Use the given classifier to make a prediction for each record in
        test_records, a list of dictionary patient records with the keys in
        the global variable ATTRS. A record is classified as malignant
        if at least 5 of the attribute values are above the classifier's
        threshold.
        Precondition: classifier is a dict with midpoint values for all
                      keys in ATTRS except "ID" and "class"
        Postcondition: each record in test_records has the "prediction" key
                       filled in with the predicted class, either "M" or "B"
    """
    # TODO 2 - implement this function
    
    # 1) # If the tumor’s value for an attribute is greater than or equal to the
         # midpoint value for that attribute, cast one vote for the tumor being malignant
    
    # 2) # If the tumor’s attribute value is less than the midpoint,
         # cast one vote for the tumor being benign
    
    # 3) # Tally up the votes cast according to these rules for each of the ten attributes.
         # If the malignant votes are greater than or equal to the benign votes,
         # we predict that the tumor is malignant
    
    for record in test_records:
        malignant = 0
        benign = 0
        for attribute in classifier.keys():
            # 1)
            if  record[attribute] <= classifier[attribute]:
                benign += 1
                # 2)
            else:
                malignant += 1
        # 3)
        if malignant >= benign:
            record["prediction"] = "M" 
        else:
            record["prediction"] = "B"   
    

def report_accuracy(test_records):
    """ Print the accuracy of the predictions made by the classifier
        on the test set as a percentage of correct predictions.
        Precondition: each record in the test set has a "prediction"
        key that maps to the predicted class label ("M" or "B"), as well
        as a "class" key that maps to the true class label. """
    # TODO 3 - implement this function
    
    count = 0
    correct = 0
    for record in test_records:
        # every time the loop runs the count increases
        count += 1
        if record["prediction"] == record["class"]:
            # every time the prediction is correct, the correct count increases 
            correct += 1
    # prints the classifier accuracy
    print("Classifier accuracy:", ((correct / count) * 100))
    

def helper_table(test_record, classifier):
    """ Creates the table that will be printed out via check_patients.
         Precondition: Use test_records to print each attribute's value based on
         the given patient ID and also print the values stored within the classifier dict.
    """
    # Calculates whether or not the certain attribute is malignant or benign
    votes = {}
    for record in test_record:
        for attribute in classifier.keys():
            if test_record[attribute] <= classifier[attribute]:
                votes[attribute] = "Benign"
            else:
                votes[attribute] = "Malignant"
                
    # the monstrosity that is the table
    # Header Line
    print("Attribute".rjust(11), "Patient".rjust(9), "Classifier".rjust(13), "Vote".rjust(12))
   
    # the row of the table that prints all the information regarding the rdius of that
    # patients tumor
    print("radius".rjust(11), ("{:.4f}".format(test_record["radius"])).rjust(9), ("{:.4f}".format(classifier["radius"])).rjust(13), votes["radius"].rjust(12))
    
    # the row of the table that prints all the information regarding the texture of that
    # patients tumor
    print("texture".rjust(11), ("{:.4f}".format(test_record["texture"])).rjust(9), ("{:.4f}".format(classifier["texture"])).rjust(13), votes["texture"].rjust(12))
    
    # the row of the table that prints all the information regarding the perimeter of that
    # patients tumor
    print("perimeter".rjust(11), ("{:.4f}".format(test_record["perimeter"])).rjust(9), ("{:.4f}".format(classifier["perimeter"])).rjust(13), votes["perimeter"].rjust(12))
    
    # the row of the table that prints all the information regarding the area of that
    # patients tumor
    print("area".rjust(11), ("{:.4f}".format(test_record["area"])).rjust(9), ("{:.4f}".format(classifier["area"])).rjust(13), votes["area"].rjust(12))
    
    # the row of the table that prints all the information regarding the smoothness of that
    # patients tumor
    print("smoothness".rjust(11), ("{:.4f}".format(test_record["smoothness"])).rjust(9), ("{:.4f}".format(classifier["smoothness"])).rjust(13), votes["smoothness"].rjust(12))
    
    # the row of the table that prints all the information regarding the compactness of that
    # patients tumor
    print("compactness".rjust(11), ("{:.4f}".format(test_record["compactness"])).rjust(9), ("{:.4f}".format(classifier["compactness"])).rjust(13), votes["compactness"].rjust(12))
    
    # the row of the table that prints all the information regarding the concavity of that
    # patients tumor
    print("concavity".rjust(11), ("{:.4f}".format(test_record["concavity"])).rjust(9), ("{:.4f}".format(classifier["concavity"])).rjust(13), votes["concavity"].rjust(12))
    
    # the row of the table that prints all the information regarding the concave aspect
    # of that patients tumor
    print("concave".rjust(11), ("{:.4f}".format(test_record["concave"])).rjust(9), ("{:.4f}".format(classifier["concave"])).rjust(13), votes["concave"].rjust(12))
    
    # the row of the table that prints all the information regarding the symmetry of that
    # patients tumor
    print("symmetry".rjust(11), ("{:.4f}".format(test_record["symmetry"])).rjust(9), ("{:.4f}".format(classifier["symmetry"])).rjust(13), votes["symmetry"].rjust(12))
    
    # the row of the table that prints all the information regarding the fractal of that
    # patients tumor
    print("fractal".rjust(11), ("{:.4f}".format(test_record["fractal"])).rjust(9), ("{:.4f}".format(classifier["fractal"])).rjust(13), votes["fractal"].rjust(12))


def check_patients(test_records, classifier):
    """ Repeatedly prompt the user for a Patient ID until the user
        enters "quit". For each patient ID entered, search the test
        set for the record with that ID, print a message and prompt
        the user again. If the patient is in the test set, print a
        table: for each attribute, list the name, the patient's value,
        the classifier's midpoint value, and the vote cast by the
        classifier. After the table, output the final prediction made
        by the classifier.
        If the patient ID is not in the test set, print a message and
        repeat the prompt. Assume the user enters an integer or quit
        when prompted for the patient ID.
    """
    # TODO 4 - implement this function
    
    
    # prompt user for an ID
    # while the user has not entered "quit":
    input_quit = False
    while not input_quit:
        patient_id = input("Enter a patient ID to see classification details: ")
        # determine whether the entered patient ID is in the test set
        if patient_id == "quit":
            input_quit = True
            break
        found = False
        for record in test_records:
            patient_id = int(patient_id)
            if patient_id == record["ID"]: 
                # print a table of results (see the handout and sample output)
                helper_table(record, classifier)
                print("Classfier's diagnosis:", record["class"])
                found = True
                break
        # otherwise,
        if found == False:
            # print a message saying the patient ID wasn't found
            print("Your ID has not been found within the system.")
        # prompt the user for another ID
            

if __name__ == "__main__": 
    # Main program - COMPLETE
    # Do not modify except to uncomment each code block as described.
    
    # load the training set
    print("Reading in training data...")
    training_data_file = "cancerTrainingData.txt"
    training_set = make_training_set(training_data_file)
    print("Done reading training data.")
    
    # load the test set 
    print("Reading in test data...")
    test_file = "cancerTestingData.txt"
    test_set = make_test_set(test_file)
    print("Done reading test data.\n")

    # train the classifier: uncomment this block once you've
    # implemented train_classifier
    print("Training classifier..."    )
    classifier = train_classifier(training_set)
    print("Classifier cutoffs:")
    for key in ATTRS[1:11]:
       print("    ", key, ": ", classifier[key], sep="")
    print("Done training classifier.\n")

    # use the classifier to make predictions on the test set:
    # uncomment the following block once you've written classify
    # and report_accuracy
    print("Making predictions and reporting accuracy")
    classify(test_set, classifier)
    report_accuracy(test_set)
    print("Done classifying.\n")

    # prompt the user for patient IDs and provide details on
    # the diagnosis: uncomment this line when you've
    # implemented check_patients
    check_patients(test_set, classifier)
