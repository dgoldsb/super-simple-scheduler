"""
Author: Dylan Goldsborough
Date: February 2017
Description: main flask file for the household hub
"""
from __future__ import print_function
from flask import Flask, render_template, request, redirect, url_for
import dbconn
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():
    '''
    Shows the main page, with the main thing:
    the roster with chores so people do their fucking jobs
    '''
    if request.method == 'POST':
        if request.form["goto"] == 'swap':
            return redirect(url_for('start'))
        if request.form["goto"] == 'fill':
            return redirect(url_for('fill'))
    planning = dbconn.get_planning()
    offend = dbconn.get_offenders()
    return render_template('start.html', planning=planning
                           , offenders=offend)

@app.route('/switch', methods=['GET', 'POST'])
def switch():
    '''
    Let's you switch chores around
    '''
    if request.method == 'POST':
        return redirect(url_for('start'))
    if request.method == 'GET':
        planning = dbconn.get_planning(2)
        return render_template('switch.html', planning=planning)

@app.route('/fill', methods=['GET', 'POST'])
def fill():
    '''
    Let's you mark stuff as done in the choreschedule
    '''
    if request.method == 'POST':
        dbconn.flip_done(request.form["date"], request.form["CID"])
        return redirect(url_for('start'))
    if request.method == 'GET':
        planning = dbconn.get_planning(True)
        return render_template('fill.html', planning=planning)

if __name__ == '__main__':
    app.run(host='10.0.0.100', port=1025, debug=True)
    #app.run(debug=True)
