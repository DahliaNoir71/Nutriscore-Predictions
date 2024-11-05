import os

from services.testing.test_displayers import (display_predictions,
                                                  plot_predictions_heatmap)
from services.testing.test_model import (load_data_for_test,
                                             make_predictions,
                                             calculate_accuracy,
                                             get_accuracy_report)
from config import Config


def main():
    """
    Main function to load data, make predictions, calculate accuracy, and display the report.
    """
    print("Début de prédictions")
    model, scaler, df_test = load_data_for_test(Config.DUMP_MODEL_NAME,
                                                Config.DUMP_SCALER_NAME,
                                                Config.DUMP_TEST_NAME)
    df_test = make_predictions(model, scaler, df_test)
    display_predictions(df_test)
    correct_predictions, total_predictions, accuracy_percentage = calculate_accuracy(df_test)
    report = get_accuracy_report(correct_predictions, total_predictions, accuracy_percentage)
    plot_predictions_heatmap(df_test, report)

# Call the main function
if __name__ == "__main__":
    main()