import os
import shutil
import tensorflow as tf

model = tf.keras.models.load_model('/Users/morgandixon/Desktop/reviewd')
input_dir = '/Users/morgandixon/Downloads/reviews1'
output_dir = '/Users/morgandixon/Desktop/reviews2'

# Get the total number of files in the input directory
num_files = len([name for name in os.listdir(input_dir) if name.endswith('.txt')])

file_num = 0
# Iterate over the text files in the input directory
for filename in os.listdir(input_dir):
    if not filename.endswith('.txt'):
        continue
    file_num += 1
    with open(os.path.join(input_dir, filename), 'r') as f:
        input_data = f.read()
    input_data = [input_data]
    prediction = model.predict(input_data)[0]

    # Print the file number and the total number of files, followed by the prediction and the filename
    print(f"Processing file {file_num}/{num_files}: Prediction for {filename}: {prediction.item():.2f}")  # use the item method to extract the float value
    if prediction <= 0.4:
        shutil.copy(os.path.join(input_dir, filename), output_dir)  # copy the file to the output directory
