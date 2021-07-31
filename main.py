from flask import Flask,request,render_template
import os
app=Flask(__name__)

@app.route("/word_count")
def word_count():
    reason=request.args.get("reason")
    return render_template("word_result.html",reason=reason)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))