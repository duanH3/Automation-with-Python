# Automation-with-Python

You work for an e-commerce store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all items from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of the items (in lbs) that were uploaded. The email should have a PDF attached with the name of the items and its total weight (in lbs).

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.
What you'll do

#TODO    
1) Process the supplier images (resize)
2) Write a script that summarizes and processes sales data into different categories and upload the descriptions 
3) Generate a PDF using Python
4) Automatically send a PDF by email
5) Write a script to check the health status of the system
