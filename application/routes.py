from flask import render_template, request
import json, datetime, calendar

from application import app

with open("application/static/zoomInfo.json") as file:
    zoomInfo = json.load(file)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/generate", methods=["get", "post"])
def generate():
    e1 = request.args.get("e1") == "on"
    e2 = request.args.get("e2") == "on"
    e3 = request.args.get("e3") == "on"
    peerLeader = request.args.get("peerLeader")
    topic = request.args.get("topic")
    rawDate = datetime.datetime.strptime(request.args.get("date"), "%Y-%m-%dT%H:%M")
    date = datetime.datetime.strftime(rawDate, "%m/%d")
    day = calendar.day_name[rawDate.weekday()]
    time = datetime.datetime.strftime(rawDate, "%I:%M %p")
    studentName = request.args.get("studentName")
    studentGrade = request.args.get("studentGrade")
    tutor = request.args.get("tutor")
    gca = request.args.get("gca") == "on"
    newTutor = request.args.get("newTutor") == "on"
    lessonPlan = request.args.get("lessonPlan")

    for leaderInfo in zoomInfo:
        if leaderInfo["Peer Leader"] == peerLeader:
            zoomLink = leaderInfo["Zoom Info"]["Zoom Link"]
            meetingId = leaderInfo["Zoom Info"]["MeetingID"]
            password = leaderInfo["Zoom Info"]["Password"]
    if zoomLink is None:
        zoomLink = "Sorry, your zoom info could not be found."
        meetingId = "Sorry, your zoom info could not be found."
        password = "Sorry, your zoom info could not be found."

    return render_template("template.html",
                           e1 = e1,
                           e2 = e2,
                           e3 = e3,
                           peerLeader=peerLeader,
                           topic=topic,
                           date=date,
                           day=day,
                           time=time,
                           studentName=studentName,
                           studentGrade=studentGrade,
                           tutor=tutor,
                           gca=gca,
                           newTutor=newTutor,
                           zoomLink = zoomLink,
                           meetingId = meetingId,
                           password = password,
                           lessonPlan = lessonPlan)
