from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product-qc')
def product_qc():
    return render_template('product_qc.html')


@app.route('/a-plus-qc')
def a_plus_qc():
    return "This is the A+ QC Tool."

if __name__ == '__main__':
    app.run(debug=True)
