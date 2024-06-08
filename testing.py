from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import os

# Load the trained model
model = YOLO(r'C:\Users\ranuj\Documents\6. Semester\Machine Learning II\ML2 Final Project\licenseplate-recognition-training-kumarran26\runs\detect\train4-100epochs-8.5h\weights\best.pt')

# Load an image for prediction
image_path = r'testing_pictures\IMG_0031.JPG'
image = cv2.imread(image_path)

# Make a prediction
results = model.predict(source=image_path)

# Visualize the results
annotated_image = results[0].plot()
plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
plt.show()

# Save the annotated image
output_dir = 'testing_runs'
os.makedirs(output_dir, exist_ok=True)
output_filename = f"tested_{os.path.basename(image_path)}"
output_path = os.path.join(output_dir, output_filename)
cv2.imwrite(output_path, annotated_image)
print(f"Annotated image saved to {output_path}")
