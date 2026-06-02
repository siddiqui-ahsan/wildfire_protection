from PIL import Image
import numpy as np

def predict_fire_risk(image)-> tuple[str, float, str]:
    """Predict wildfire risk from a satellite image.    

    Args:
        image: A PIL Image object representing a satellite image.  
    
    Returns:
        A tuple containing:
            - predicted_label: A string indicating the predicted wildfire risk ("fire" or "no_fire").
            - confidence: A float representing the confidence level of the prediction (between 0 and 1).
            - image_id: A string identifier for the input image.
    """

    # Placeholder function for wildfire risk prediction

    label = "fire" if np.random.rand() > 0.5 else "no_fire"

    return  label, 0.85, "example_image_id"