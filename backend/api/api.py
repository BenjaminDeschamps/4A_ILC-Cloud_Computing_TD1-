from flask import Flask, request
import sys
import tweet
import client

app = Flask(__name__)


@app.route("/addTweet", methods=['POST'])
def newTweet(client c1):


@app.route("/", methods=['GET', 'POST'])
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)
