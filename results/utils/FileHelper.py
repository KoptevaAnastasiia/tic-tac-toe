from results.config import RESULTS_PATH
from results.types import ResultsList
import json


class FileHelper:
    def __init__(self):
        self.results: ResultsList

    def fill_results_data(self):
        try:
            with open(RESULTS_PATH) as file:
                self.results = json.load(file)

        except FileNotFoundError:
            self.clear_results_data()

        except json.decoder.JSONDecodeError:
            self.clear_results_data()

    def save_results_data(self):
        with open(RESULTS_PATH, "w") as file:
            json.dump(self.results, file)

    def clear_results_data(self):
        with open(RESULTS_PATH, "w") as file:
            json.dump([], file)

        self.results = []
