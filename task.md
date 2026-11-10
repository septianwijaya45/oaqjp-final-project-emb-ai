Final Project - Overview and Review Criteria

Estimated time needed: 5 minutes
Project Overview
For this final project, you will assume the role of a software engineer who needs to develop an AI-based web application. You will analyze the scenario and perform the following tasks:
Task 1: Clone the project repository
Task 2: Create an emotion detection application using Watson NLP library
Task 3: Format the output of the application
Task 4: Package the application
Task 5: Run unit tests on your application
Task 6: Deploy the application using Flask
Task 7: Incorporate error handling
Task 8: Run static code analysis
Evaluation Criteria – 16 Points
You can submit your project deliverables in one of the following ways:
Option 1: AI-Graded Submission and Evaluation When you choose Option 1, you will be redirected to an AI tool where you can upload your deliverables, which may include URLs, terminal outputs, code snippets, or screenshots. You will then receive an AI-generated grade that will automatically reflects on your progress page.
Option 2: Peer-Graded Submission and Evaluation When you choose Option 2, you will upload your deliverables—such as URLs, terminal outputs, code snippets, or screenshots—through the My Submission section. Your submission will then be reviewed either by your peers or by AI grader.
We recommend using Option 1 for faster grading. However, if you face any issues or cannot access it, you may use Option 2 instead.
If you encounter any grading problems, please reach out to the Course Team through the Discussion Forums.
Please find the details of the Grading Criteria below:
Task 1: Submit the GitHub repository URL
Submit the public GitHub repository URL of the README.md file, which contains the project name details. (1 point)
Task 2: Create an emotion detection application using the Watson NLP library
Activity 1: Submit the code from the emotion_detection.py file that shows the application function. (1 point)
Activity 2: Submit the terminal output showing that the application was imported and tested without errors. (1 point)
Task 3: Format the output of the application
Activity 1: Submit the code from the emotion_detection.py file showing that the modified emotion_detector function returns the correct output format. (1 point)
Activity 2: Submit the terminal output showing that the output format is accurate. (1 point)
Task 4: Validate the EmotionDetection package
Activity 1: Submit the public GitHub repository URL of the init.py file which includes the code to import the application module. (1 point)
Activity 2: Submit the terminal output validating that EmotionDetection is a valid package. (1 point)
Task 5: Run unit tests on your application
Activity 1: Submit the code from the test_emotion_detection.py file showing the required unit tests. (1 point)
Activity 2: Submit the terminal output showing that all unit tests passed. (1 point)
Task 6: Deploy the application using Flask
Activity 1: Submit the code from the server.py file showing the web deployment of the application using Flask. (1 point)
Activity 2: Upload the screenshot named 6b_deployment_test.png showing the application deployment. (1 point)
Task 7: Incorporate error handling
Activity 1: Submit the code from the emotion_detection.py file showing the updated emotion_detector function for status code 400. (1 point)
Activity 2: Submit the code from the server.py file showing the handling of blank input errors. (1 point)
Activity 3: Upload the screenshot named 7c_error_handling_interface.png validating error handling functionality. (1 point)
Task 8: Run static code analysis
Activity 1: Submit the code from the server.py file demonstrating the execution of static code analysis. (1 point)
Activity 2: Submit the terminal output showing a perfect score for static code analysis. (1 point)

You will need to provide clear screenshots for each of the activities mentioned below for grading.
Task 1: Clone the project repository
Repository folder structure (1 point)
Task 2: Create an emotion detection application using Watson NLP library
Activity 1: Write code for the application function (1 point)
Activity 2: Import the application without errors (1 point)
Task 3: Format the output of the application
Activity 1: Modify the emotion_detector function accurately for it to return the provided output format (1 point)
Activity 2: Check that the output format is accurate (1 point)
Task 4: Package the application
Activity 1: Create the folder structure for packaging the application and create the init.py file (1 point)
Activity 2: Verify that the output is as expected (1 point)
Task 5: Run unit tests on your application
Activity 1: Create the required unit tests (1 point)
Activity 2: Run unit tests until all pass (1 point)
Task 6: Deploy the application using Flask
Activity 1: Update server.py with the right contents (1 point)
Activity 2: Deploy the application (1 point)
Task 7: Incorporate error handling
Activity 1: Update the emotion_detector function for status code, 400 (1 point)
Activity 2: Update the server.py file to manage blank input errors (1 point)
Activity 3: Validate error handling functionality (1 point)
Task 8: Run static code analysis
Activity 1: Update the server.py to highlight the code that gets 10/10 (1 point)
Activity 2: Get a perfect score for static code analysis (1 point)
Author(s)
Ratima Raj Singh

Note
Please ensure that all updates and changes made during each task are properly completed and saved before proceeding to the next steps.
As mentioned in the “Final Project Overview”, you can submit your project deliverables through either Option 1: AI-Graded Submission and Evaluation or Option 2: Peer-Graded Submission and Evaluation.
For Option 1: AI-Graded Submission and Evaluation:
Submission requires:
GitHub repository URL under Task 1 and Task 4 (Activity 1).
Code snippets under Tasks 2 to 8 for Activity 1, and under Task 7 for Activities 1 and 2 (excluding Task 4).
Terminal outputs under Tasks 2 to 4 and Task 8 for Activity 2.
Screenshots under Task 6 for Activity 2 and Task 7 for Activity 3.
For Option 2: Peer-Graded Submission and Evaluation:
Submission requires screenshots for all activities under Tasks 1 to 8.
Please run this lab in the Skills Network Theia Lab environment itself, not in your local IDE (like VS Code). The API used here is hosted on the Skills Network platform and is only accessible within the Theia Lab.

Task 1: Fork and Clone the project repository
Important Note:
1. Create a GitHub account: If you don't have one, go to https://github.com and create it.
2. Fork the repository: Open the link to the original repository and click the Fork button to create a copy in your own account.
3. Clone your repository: Return to this lab. Copy the URL of your forked repository and run the following command in the terminal: git clone [YOUR_REPOSITORY_URL]
Warning: The lab environment is not persistent. All files will be deleted when you leave the lab. Make sure to commit your changes frequently to save your progress and keep a backup of your code on your local computer.
 
The GitHub repository of the project is available on the URL mentioned below. As a first step you need to Fork this repository, click the Fork button at the top-right corner of the repository page.
bash


https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai.git


Run
You can find instructions on how to fork the repository by visiting exercise 2 in this \\\\\\\_Hands-on Lab: Get familiar with Git Commands\\\\\\\_.
Note: Ensure your forked repository is Public. This action will create a copy of the forked repository within your GitHub account.
Open a new Terminal and make the directory final_project using mkdir command.
Clone this forked GitHub repository using the Cloud IDE terminal to your project to a folder named final_project. You can find instructions on how to get the clone URL of the repository by visiting exercise 3 in this \\\\\\\_Hands-on Lab: Get familiar with Git Commands\\\\\\\_.
After the cloning is complete, use the terminal to change the current directory final_project.
Go to your forked repository and open the README.md and add the project name in the file as Final project. Ensure you use this exact name as this is required for the AI-graded submission.
Assessment:
For Option 1 - AI Graded Submission and Evaluation: Copy and save the public GitHub repository URL of the README.md file, which contains the project name Final project for the Final project submission and Evaluation
For Option 2 -Peer-Graded Submission and Evaluation: Take the screenshot of your folder structure and save it as 1_folder_structure.png for Peer Assignment.

Task 2: Create an emotion detection application using the Watson NLP library
The Watson NLP libraries are embedded. Therefore, there is no need of importing them to your code. You only need to send a post request to the correct function in the library and receive the output.
For this project, you'll use the Emotion Predict function of the Watson NLP Library. For accessing this function, the URL, the headers, and the input json format is as follows.
plaintext


URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyze } }



Note that the text_to_analyze is being used as a variable that holds the actual written text that needs to be analysed.
Create a file named emotion_detection.py in final_project folder.
In the emotion_detection.py file, write the function to run emotion detection using the appropriate Emotion Detection function. Name this function emotion_detector.
Note: Assume that the text to be analysed is passed to the function as an argument and is stored in the variable text_to_analyze. The value being returned must be the text attribute of the response object as received from the Emotion Detection function.
Assessment:
For Option 1 - AI Graded Submission and Evaluation: Copy and paste code from the emotion_detection.py file that shows the application function in a text file and save it as 2a_emotion_detection for the Final project submission and evaluation.
For Option 2 -Peer-Graded Submission and Evaluation: Take a screenshot of the code you write and save it as 2a_emotion_detection.png for Peer Assignment.
The application should now be importable using Python shell. Open a python3 shell.
Import the application.
After you successfully import the application, test your application with the text: "I love this new technology."
Assessment:
For Option 1 - AI Graded Submission and Evaluation: Copy and paste terminal output showing that the application was imported and tested without errors in a text file and save it as 2b_application_creation for the Final project submission and evaluation.
For Option 2 -Peer-Graded Submission and Evaluation: Take a screenshot of the terminal with all three steps included in it along with the final output. Name this file 2b_application_creation.pngfor Peer Assignment.
Optional:
At any point of time if you want to push your code to your forked GitHub repository, you can do so by following the instructions provided in this link.

Task 3: Format the output of the application
Convert the response text into a dictionary using the json library functions.
Note the content formatting in this dictionary.
Extract the required set of emotions, including anger, disgust, fear, joy and sadness, along with their scores.
Write the code logic to find the dominant emotion, which is the emotion with the highest score.
Then, modify the emotion_detector function to return the following output format.
plaintext


{
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': '<name of the dominant emotion>'
}



Assessment:
For Option 1 - AI Graded Submission and Evaluation: Copy and paste code from the emotion_detection.py file showing that the modified emotion_detector function returns the correct output format in a text file and save it as 3a_output_formatting for the Final project submission and evaluation.
For Option 2 -Peer-Graded Submission and Evaluation: Take a screenshot of the modified function code and save it as 3a_output_formatting.png for Peer Assignment.
Test the application in the python3 shell again, with the statement I am so happy I am doing this.
Verify that the dominant emotion of the received response is joy.
Assessment:
For Option 1 - AI Graded Submission and Evaluation: Copy and paste the terminal output showing that the output format is accurate in a text file and save it as 3b_formatted_output_test for the Final project submission and evaluation.
For Option 2 -Peer-Graded Submission and Evaluation: Take a screenshot of the output from the terminal shell and save it as 3b_formatted_output_test.png for Peer Assignment.
Optional
At any point of time if you want to push your code to your forked GitHub repository, you can do so by following the instructions provided in this link.

Task 4: Package the application
In this task, you will package the application created in the previous steps.
Perform the relevant steps in creation of the package. Set the name of the package to EmotionDetection.
Assessment:
For Option 1 - AI Graded Submission and Evaluation: Ensure that you have pushed your init.py file to your forked GitHub repository by following the instructions link. in the provided link. Then, copy and save the public GitHub URL of the __init__.py file that contains the code to import the application module for the Final project submission and evaluation.
For Option 2 -Peer-Graded Submission and Evaluation: Take a screenshot of the contents of the init file along with the final folder structure of the final_project directory. Make sure to fit both of the images into a single screenshot and name it 4a_packaging.pngfor Peer Assignment.
To make sure that the EmotionDetection is a valid package, you need to test the package. To do this:
Run a python shell in the terminal.
Import the emotion_detector function from the package.
If the package is created accurately, you will not receive any error messages.
Test run the function again with the statement I hate working long hours.
Verify that the output displays the dominant emotion as anger.
Assessment:
For Option 1 - AI Graded Submission and Evaluation: Copy and paste the terminal output validating that EmotionDetection is a valid package and save it as 4b_packaging_test for the Final project submission and evaluation.
For Option 2 -Peer-Graded Submission and Evaluation: Take a screenshot of this terminal output and save it as 4b_packaging_test.pngfor Peer Assignment.

ask 5: Run unit tests on your application
With a functional application being available, you now need to run unit tests to validate the application output.
To run unit tests, create a new file, test_emotion_detection.py that calls the required application function from the package and tests it for the following statements and dominant emotions.
Statement
Dominant Emotion
I am glad this happened
joy
I am really mad about this
anger
I feel disgusted just hearing about this
disgust
I am so sad about this
sadness
I am really afraid that this will happen
fear


Assessment: For Option 1 - AI Graded Submission and Evaluation: Copy and paste the code from the test_emotion_detection.py file showing the required unit tests in a text file and save it as 5a_unit_testing for the Final project submission and evaluation.
For Option 2 -Peer-Graded Submission and Evaluation: Take a screenshot of the code and save it as 5a_unit_testing.png  for Peer Assignment.
Execute the test_emotion_detection.py file on terminal.
Check the unit test output to verify that the unit tests have passed.
Assessment:For Option 1 - AI Graded Submission and Evaluation: Copy and paste the terminal output showing that all unit tests passed in a text file and save it as 5b_unit_testing_result for the Final project submission and evaluation.
For Option 2 -Peer-Graded Submission and Evaluation: Take a screenshot of the terminal output showing the test results and save it as 5b_unit_testing_result.png for Peer Assignment.
Optional:
At any point of time if you want to push your code to your forked GitHub repository, you can do so by following the instructions provided in this link.

Task 6: Web deployment of the application using Flask
After all the tests are successfully completed, you need to deploy the application on the web. This will enable the customer to access and use the application.
Note: The index.html file in the templates folder and mywebscript.js file in the static folder have been provided as a part of the repo. These files do not need to be updated in this project.
You have to create the server.py file from scratch. Note the following requirements of this task.
Note: server.py is a part of final_project folder.
Make sure that the Flask decorator for the application calling function is /emotionDetector.
The customer has requested the output to be displayed in the format as displayed in the example below.
Example Output Let's say that you want to evaluate the statement I love my life. The statement is processed as follows:
json


{
"anger": 0.006274985, 
"disgust": 0.0025598293, 
"fear": 0.009251528, 
"joy": 0.9680386, 
"sadness": 0.049744144, 
"dominant_emotion":"joy"
}



The response is displayed as:
For the given statement, the system response is 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is joy.
Application needs to be deployed on localhost:5000
Assessment:
For Option 1 - AI Graded Submission and Evaluation: Copy and paste the code from the server.py file showing the web deployment of the application using Flask in a text file and save it as 6a_server for the Final project submission and evaluation.
For Option 2 -Peer-Graded Submission and Evaluation: Take a screenshot of the final contents of server.py and name it 6a_server.png for Peer Assignment.
Assessment : Take a screenshot of the final deployed application, testing it for the statement "I think I am having fun". Name this image as 6b_deployment_test.png both for Option 1 -Final project submission and evaluation and For Option 2 -Peer-Graded Submission and Evaluation.
Optional:
At any point of time if you want to push your code to your forked GitHub repository, you can do so by following the instructions provided in this link.

ask 7: Incorporate Error handling
Incorporate the error handling capability in your function emotion_detector to manage blank entries from users, i.e. running the application without any input.
Access the status_code attribute of the server response to correctly display the system response for blank entries.
For status_code = 400, make the function return the same dictionary, but with values for all keys being None.
Assessment:
For Option 1 - AI Graded Submission and Evaluation: Copy and paste the code from the emotion_detection.py file showing the updated emotion_detector function for status code 400 in a text file and save it as 7a_error_handling_function for the Final project submission and evaluation.
For Option 2 -Peer-Graded Submission and Evaluation: Take a screenshot of the modified function and name it 7a_error_handling_function.pngfor Peer Assignment.
Modify server.py to incorporate error handling when the dominant_emotion is None. In this scenario, the response should display a message Invalid text! Please try again!.
Assessment:
For Option 1 - AI Graded Submission and Evaluation: Copy and paste the code from the server.py file showing the handling of blank input errors in a text file and save it as 7b_error_handling_server for the Final project submission and evaluation.
For Option 2 -Peer-Graded Submission and Evaluation: Take a screenshot of this edited file and save it as 7b_error_handling_server.png for Peer Assignment.
Deploy the application and test it for blank entries.
The output should display the error message, Invalid text! Please try again!.
Assessment:
Take a screenshot of the output displaying the error message and name it 7c_error_handling_interface.png both for Option 1 -Final project submission and evaluation and For Option 2 -Peer-Graded Submission and Evaluation.
Optional:
At any point of time if you want to push your code to your forked GitHub repository, you can do so by following the instructions provided in this link.
Task 8: Run static code analysis
Finally, its time to check code compliance.
Run static code analysis on the code you created. Use PyLint library on server.py file and try to generate a 10/10 score. You will have to modify the server.py file to get this score.
Assessment:
For Option 1 - AI Graded Submission and Evaluation: Copy and paste the code from the server.py file demonstrating the execution of static code analysis in a text file and save it as 8a_server_modified for the Final project submission and evaluation.
For Option 2 -Peer-Graded Submission and Evaluation: Take a screenshot of the modified file and name it as 8a_server_modified.png for Peer Assignment.
Note: The difference between a 9/10 score and a 10/10 score may be use of Docstrings. Include Docstrings in all functions of your codes.
Assessment :
For Option 1 - AI Graded Submission and Evaluation: Copy and paste the terminal output showing a perfect score for static code analysis in a text file and save it as 8b_static_code_analysis for the Final project submission and evaluation.
For Option 2 -Peer-Graded Submission and Evaluation: Take a screenshot of a 10/10 output on the terminal after running static code analysis. Name the screenshot as 8b_static_code_analysis.png for Peer Assignment.

