import unittest
import requests

class TestWebApi(unittest.TestCase):
    
    # TARGET_URL = "http://localhost:5000/fib"
    TARGET_URL = "https://naokey.pythonanywhere.com/fib"
    
    def check_response(self, params: dict, excepted_status: int, excepted_result=None):
        """_summary_

        Args:
            params (dict): クエリパラメータをdictで指定
            excepted_status (int): 求められるステータスコード
            excepted_result (any, optional): 求められる結果. Defaults to None.
        """
        resp = requests.get(self.TARGET_URL, params=params)
        self.assertEqual(resp.status_code, excepted_status)
        
        if excepted_result is not None:
            self.assertEqual(resp.json()["result"], excepted_result)
    
    
    def test_valid_query(self):
        
        test_cases = [
            {"n": 0, "result": 1},
            {"n": 10, "result": 55},
            {"n": 99, "result": 218922995834555169026}
        ]
        for case in test_cases:
            
            self.check_response(
                params={"n": case["n"]}, 
                excepted_status=200,
                excepted_result=case["result"]
            )
    
    def test_invalid_query(self):
        
        test_cases = [
            {"n": 300},
            {"n": -10},
            {"n": "abc"},
            {"n": ""},
            {"hoge": 10}
        ]
        
        for case in test_cases:
            self.check_response(
                params=case,
                excepted_status=400
            )


if __name__ == "__main__":
    unittest.main()
