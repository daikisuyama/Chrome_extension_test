from flask import Flask,request,render_template
app=Flask(__name__)

@app.route("/word_count/<reason>")
def word_count():
    reason=request.args.get("reason")
    return render_template("word_result.html",reason=reason)

if __name__ == "__main__":
    app.run(debug=True)