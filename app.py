from flask import Flask, render_template, request
import DNA_Eiwit

app = Flask(__name__)


@app.route('/')
def hello_world():
    dna = request.args.get("dna", "")
    eiwit = DNA_Eiwit.dna_to_protein(dna)
    return render_template("Pagina.html", eiwit=eiwit)


if __name__ == '__main__':
    app.run()
