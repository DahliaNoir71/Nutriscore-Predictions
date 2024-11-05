from app.services.training.train_displayers import display_model_evaluations
from app.services.training.train_model import prepare_and_train_model
from app.services.predictions import predictions


def main():
    """
    This function orchestrates the entire process of preparing and training a model,
    making predictions on a test set, and displaying the model's evaluations.

    Parameters:
    None

    Returns:
    None
    """
    model, scaler, x_test, y_test = prepare_and_train_model()
    y_prediction_test, y_prediction_prob_test = predictions(model,
                                                            scaler,
                                                            x_test)
    display_model_evaluations(y_test,
                              y_prediction_test,
                              y_prediction_prob_test,
                              model)

# Call the main function
if __name__ == "__main__":
    main()