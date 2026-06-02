from unicodedata import name

import pandas as pd
import streamlit as st

# from developer.training_history import show_training_history

# MODELS_DIR = "./models/"
# TRAINING_CSV_SUFFIX = "_training_history.csv"
# EVALUATION_PATH = "./models/evaluation_predictions.csv"



# def main():
#     st.title("ML Dashboard")

#     st.header("Training History")
#     show_training_history(MODELS_DIR, TRAINING_CSV_SUFFIX)

#     st.header("Evaluation")
#     evaluation_df = pd.read_csv(EVALUATION_PATH)
#     st.dataframe(evaluation_df)

##### FROM SCRATCH #####

from developer.training_history import get_training_dataframe, select_model, select_metrics


FILE_RESNET = "./models/resnet18_training_history.csv"
FILE_MOBILENET = "./models/mobilenet_v3_small_training_history.csv"

PATHS_STR = [FILE_RESNET, FILE_MOBILENET]

# def main():
#     st.title("ML Dashboard")
#     st.text("Learning the art of using STREAMLIT.")

#     model_storage={}
#     for path in PATHS_STR:
#         model_name, model_df = get_training_dataframe(path)
#         # show_training_history(path)
#         # model_names.append(model_name)
#         model_storage[model_name] = model_df

#     model_names = list(model_storage.keys())
    
#     selected_option = select_model(model_names)
#     st.text(selected_option)


#     # How to access the right training history from the name alone?

#     selected_df = model_storage[selected_option]

#     st.line_chart(selected_df, x="epoch", y=["val_loss","train_loss"], width="stretch")


#     selected
# if __name__ == "__main__":
#     main()


def main():
    st.title("ML Dashboard")
    st.text("Learning the art of using STREAMLIT.")

    model_storage={}
    for path in PATHS_STR:
        model_name, model_metrics, model_df = get_training_dataframe(path)
        model_storage[model_name] = model_df

    model_names = list(model_storage.keys())
    
    selected_option = select_model(model_names)
    
    # st.text(selected_option)


    # How to access the right training history from the name alone?

    selected_df = model_storage[selected_option]

    st.line_chart(selected_df, x="epoch", y=["val_loss","train_loss"], width="stretch")

    selected_metrics = select_metrics(model_metrics)
    # st.text(selected_metrics)

    # st.dataframe(model_storage.values([["architecture", "epoch", selected_metrics]]))
    # st.dataframe(list(model_storage.values())[1].loc[:, ["architecture", "epoch", selected_metrics]])
    dfs = []
    for name, df in model_storage.items():
        st.write(f"Model: {name}")
        selected_df = df[["epoch", selected_metrics]]
        # st.dataframe(selected_df)
        temp = df.loc[:, ["epoch", selected_metrics]].copy()
        temp["model"] = name   # label each curve
        dfs.append(temp)

    concatenated_df = pd.concat(dfs, ignore_index=True)
    st.line_chart(
    concatenated_df,
    x="epoch",
    y=selected_metrics,
    color="model",   # streamlit uses this to separate curves
    width="stretch"
)


if __name__ == "__main__":
    main()