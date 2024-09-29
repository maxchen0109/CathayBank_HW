import requests
import pytest
import yaml
import os
from datetime import datetime
import re


base_url = "https://swapi.dev/api"


def get_test_data(yaml_file_path):
    """
    功能：讀取存放測試資料的路徑，並回傳
    參數：
        yaml_file_path ：測試資料的路徑
    """
    with open(yaml_file_path, "r", encoding="utf8") as f:
        return yaml.safe_load(f)


class TestSWAPIFilms:

    @pytest.mark.parametrize(
        "test_case",
        get_test_data(
            "".join([os.getcwd(), "/Star War/resources/star_war_test_data_p1.yaml"])
        ),
    )
    @pytest.mark.p1
    def test_normal_get_films(self, test_case):
        """
        功能：驗證傳入合法值的資料
        參數：
            test_case ：從設計的測試資料取得
        """
        if test_case["priority"].upper():
            response = requests.get("".join([base_url, test_case["uri"]]))
            assert (
                response.status_code == test_case["expected_status_code"]
            ), f"status_code= '{response.status_code}' is not expected"

            response_data = response.json()

            # 若查詢參數為 /films 時，將回傳的 results 列表取出，並每個進行資料型別驗證
            if test_case["uri"] == "/films":
                assert (
                    response_data["count"] == test_case["expected_episode_count"]
                ), f'count= {response_data["count"]} is not expected'
                results = response_data["results"]
                for result in results:
                    self.validate_data_types(result, test_case)
            else:
                self.validate_data_types(response_data, test_case)

    @pytest.mark.parametrize(
        "test_case",
        get_test_data(
            "".join([os.getcwd(), "/Star War/resources/star_war_test_data_p2.yaml"])
        ),
    )
    @pytest.mark.p2
    def test_boundary_value_get_films(self, test_case):
        """
        功能：驗證傳入邊界值的資料
        參數：
            test_case ：從設計的測試資料取得
        """
        response = requests.get("".join([base_url, test_case["uri"]]))
        assert (
            response.status_code == test_case["expected_status_code"]
        ), f"status_code= '{response.status_code}' is not expected"

        response_data = response.json()
        self.validate_data_types(response_data, test_case)

    @pytest.mark.parametrize(
        "test_case",
        get_test_data(
            "".join([os.getcwd(), "/Star War/resources/star_war_test_data_p3.yaml"])
        ),
    )
    @pytest.mark.p3
    def test_invalid_get_films(self, test_case):
        """
        功能：驗證傳入無效的資料與
        參數：
            test_case ：從設計的測試資料取得
        """

        if "method" in test_case:
            if test_case["method"].lower() == "post":
                response = requests.post("".join([base_url, test_case["uri"]]))
            if test_case["method"].lower() == "put":
                response = requests.put("".join([base_url, test_case["uri"]]))
        else:
            response = requests.get("".join([base_url, test_case["uri"]]))
        assert (
            response.status_code == test_case["expected_status_code"]
        ), f"status_code= '{response.status_code}' is not expected"

        response_data = response.json()
        self.validate_data_types(response_data, test_case)

    def validate_data_types(self, actual_data, expected_data):
        """
        功能：驗證資料型態
        參數：
            actual_data ：回傳值內容
            expected_data ：從設計的測試資料取得
        """
        if "expected_data_types" in expected_data:
            # 欄位數量驗證
            extra_field = set(actual_data.keys()).difference(
                expected_data["expected_data_types"].keys()
            )
            assert len(extra_field) == 0, f"Response extra field: '{extra_field}'"

            for field, expected_type in expected_data["expected_data_types"].items():
                # 資料型別驗證
                class_mapping = {"str": str, "int": int, "list": list}
                assert isinstance(
                    actual_data[field], class_mapping[expected_type]
                ), f"Field '{field}' has incorrect type"

                # ISO 8601 格式驗證
                if field in ["release_date", "created", "edited"]:
                    try:
                        datetime.fromisoformat(actual_data[field])
                    except ValueError:
                        assert False, f"Field '{field}' is not in ISO 8601 format"

                # URL 格式驗證
                if field in [
                    "url",
                    "species",
                    "starships",
                    "vehicles",
                    "characters",
                    "planets",
                ]:
                    pattern = (
                        r"^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[\w.-]*)*/?$"
                    )
                    if field == "url":
                        assert (
                            re.compile(pattern).match(item) is not None
                        ), f"Field '{field}' contains invalid URL format"
                    else:
                        for item in actual_data[field]:
                            assert (
                                re.compile(pattern).match(item) is not None
                            ), f"Field '{field}' contains invalid URL format"
