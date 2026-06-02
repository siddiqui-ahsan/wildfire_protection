import gradio as gr

from responder.feedback import record_feedback
from responder.predictor import predict_fire_risk


def predict_image(image):
    predicted_label, confidence, _image_id = predict_fire_risk(image)

    return (
        f"{predicted_label.upper()} "
        f"— confidence: {confidence:.1%}"
    )


with gr.Blocks() as demo:
    gr.Markdown("# Wildfire Classifier")

    image = gr.Image(type="pil", label="Satellite image")
    prediction_output = gr.Textbox(label="Prediction", interactive=False)

    predict_button = gr.Button("Run prediction")

    with gr.Row():
        thumbs_up = gr.Button("👍", size="sm")
        thumbs_down = gr.Button("👎", size="sm")

    feedback_message = gr.Textbox(
        label="Feedback",
        interactive=False,
    )

    predict_button.click(
        fn=predict_image,
        inputs=image,
        outputs=prediction_output,
    )

    thumbs_up.click(
        fn=lambda: record_feedback("up"),
        outputs=feedback_message,
    )

    thumbs_down.click(
        fn=lambda: record_feedback("down"),
        outputs=feedback_message,
    )


if __name__ == "__main__":
    demo.launch()