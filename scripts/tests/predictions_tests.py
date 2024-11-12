from services.loaders.loaders import (load_model,
                                      load_scaler,
                                      load_test_data)
from services.testing.test_displayers import (display_predictions,
                                                  plot_predictions_heatmap)
from services.testing.test_model import (make_predictions,
                                         calculate_accuracy,
                                         get_accuracy_report)
from config import Config


def main():
    """
    Main function to load data, make predictions, calculate accuracy, and display the report.
    """
    print("Début de prédictions")
    model = load_model(Config.DUMP_MODEL_NAME)
    scaler = load_scaler(Config.DUMP_SCALER_NAME)
    df_test = load_test_data(Config.DUMP_TEST_NAME)
    df_predictions = make_predictions(model, scaler, df_test)
    display_predictions(df_predictions)
    correct_predictions, total_predictions, accuracy_percentage = calculate_accuracy(df_predictions)
    report = get_accuracy_report(correct_predictions, total_predictions, accuracy_percentage)
    plot_predictions_heatmap(df_predictions, report)

# Call the main function
if __name__ == "__main__":
    main()