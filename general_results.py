import json
from time import time, ctime
import os


def results(test_func):
    """results: Decorator that generate json file to associated tests
    :param test_func: Test Function that uses this decorator
    """
    def result_wrapper(*args, **kwargs):
        expected_value = -1
        actual_value = -1
        class_method_names = -1
        result = False
        try:
            args = test_func(*args, **kwargs)
            expected_value = args[0]
            actual_value = args[1]
            class_method_names = args[2]
            print("Test Case: {} -> {}".format(class_method_names[0], class_method_names[1]))
            print("Expected value: {} || Actual value: {}".format(expected_value, actual_value))
            result = expected_value == actual_value
        except IndexError as e:
            print(e)
            print("Calling function does not provide required parameters")
            result = False
        except Exception as e:
            print(e)
            result = False
        finally:
            update_test_report(expected_value, actual_value, class_method_names, result)
            return result
    return result_wrapper


def prepare_test_result_json(file_name):
    """prepare_test_result_json: creating json file with Test Case Results
    :param file_name: name of the json file
    """
    os.remove(file_name)
    data = {'Test Steps': []}
    with open(file_name, 'a') as f:
        f.write(json.dumps(data))


def update_test_report(expected_value, actual_value, class_method_names, result):
    """update_test_report: Update Test Case Json file with Test Step result
    :param expected_value: Any Type
    :param actual_value: Any Type
    :param class_method_names: String
    :param result: Boolean
    """
    test_results = {
        class_method_names[1]: {
            'result': list(map(lambda x: "Pass" if x else "Fail", [result]))[0],
            'expected value': expected_value,
            'actual value': actual_value,
            'time': ctime(time())
        },
    },

    with open(str(class_method_names[0]) + '.json', 'r') as f:
        test_result_data = json.load(f)
        test_result_data["Test Steps"].append(test_results)

    with open('PythonOrgNavigationMenu.json', 'w') as f:
        f.write(json.dumps(test_result_data))
