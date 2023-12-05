from flask import Flask, render_template

from demo.spark_configurer import get_spark_session
from demo.vender_applicant import update_from_data_hub, update_cron, get_count_diff, get_count_txn

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    update_cron()
    return 'Hello World!'


@app.route('/applicant')
def applicant():

    data = [0, 10, 15, 8, 22, 18, 25]
    return render_template("base.html", data=get_count_diff(), labels=get_count_txn())


if __name__ == '__main__':
    app.run()
