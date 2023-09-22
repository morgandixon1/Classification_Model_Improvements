import tensorflow as tf

# add a directory to the folder with the models.
model1 = tf.keras.models.load_model('/Users/morgandixon/Desktop/Models/religion_model')
# model2 = tf.keras.models.load_model('/Users/morgandixon/Desktop/Models/Politicalmodelv2')
while True:
    # Get input data from the terminal
    input_data = input("Enter the input data (enter 'q' to quit): ")
    if input_data == 'q':
        break
    input_data = [input_data]

    # Use the model to make a prediction on the input data
    prediction1 = model1.predict(input_data)[0]
    # prediction2 = model2.predict(input_data)[0]
    # Print the prediction result
    print(f"Prediction: {prediction1[0]:.2f}")
    if prediction1 <= 0.3:
        print("model 1 threshold")
    else:
        print("Bot Response")
    # print(f"Prediction: {prediction2[0]:.2f}")
    # if prediction2 <= 0.3:
    #     print("Model 2 threshold")
    # else:
    #     print("Bot Response")
