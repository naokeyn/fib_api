from flask import Flask, request, jsonify
from src.fib import fib

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "status": 404,
        "message": "Page not found."
    }), 404


@app.route("/fib", methods=["GET"])
def index():
    
    # クエリパラメータを取得
    params = request.args.to_dict()
    
    # クエリパラメータの存在確認
    try:
        n = params["n"]
    except KeyError as e:
        return jsonify({
            "status": 400,
            "message": "Bad request. `N` required but not found."
        }), 400

    # パラメータが負 or 数字じゃないとき
    if not n.isdigit():
        return jsonify({
            "status": 400,
            "message": "Bad request. Input must be a one-byte non-negative integer"
        }), 400
    
    # nが200以上のとき
    # 桁落ちしてしまうため無効化
    elif int(n) >= 200:
        return jsonify({
            "status": 400,
            "message": "Bad request. Input must be between 0 and 200"
        }), 400
    
    resp = {
        "result": fib(int(n))
    }
    
    return jsonify(resp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
    # app.run(port=5000)
