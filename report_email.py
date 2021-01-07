#!/usr/bin/env python3

import json
import sys
import os, datetime, reports
import emails

def process_data(path):
  summary = ""
  list_of_files = os.listdir(path)
  for file in list_of_files:
      if file.endswith("txt"):
          with open(path + file, "r") as f:
              data = f.read()
              data = data.split("\n")
              summary += "name: " + data[0] + "<br/>" + "weight: " + data[1] + "<br/><br/>"
  return summary

def main(argv):
  """Process the file data from path and generate a full report out of it."""
  # TODO: read data from txt
  path = "supplier-data/descriptions/"
  summary = process_data(path)

  #print(summary)
  # TODO: turn this into a PDF report
  time = datetime.datetime.now().strftime('%Y-%m-%d') #today's date
  title = "Process Updated on " + time 
  attachment = "/tmp/processed.pdf" #filename and file path
  reports.generate_report(attachment, title, summary) #create file

  # TODO: send the PDF report as an email attachment
  sender = "me@example.com"
  receiver = "automation@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send(message)

if __name__ == "__main__":
  main(sys.argv)
