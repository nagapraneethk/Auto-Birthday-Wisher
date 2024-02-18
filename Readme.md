## Birthday Reminder Project

This project automates sending personalized birthday emails to your loved ones based on a CSV file containing birthdays and email addresses. It uses secure environment variables to store your email password and provides different letter templates for personalization.


**Features:**

* Reads birthdays from a CSV file.
* Checks for birthdays on the current date.
* Sends personalized emails with templates and recipient names.
* Uses secure environment variables for sensitive information.

**Requirements:**

* Python 3
* Libraries listed in `requirements.txt`

**Installation:**

1. Clone this repository: `git clone https://github.com/nagapraneethk/birthday-reminder.git`
2. Install dependencies: `pip install -r requirements.txt`

**Usage:**

1. **Create a CSV file named `birthdays.csv` in the project directory with the following columns:**
    * `name`: Name of the person
    * `month`: Month of birth (integer)
    * `day`: Day of birth (integer)
    * `email`: Email address
   

2. **Set the `EMAIL_PASSWORD` environment variable with your email password.**

    Here's how to do it:

    * **Windows:**
    
       * Using Environment Variables:
         1. Right-click "This PC" -> "Properties" -> "Advanced system settings".
         2. Click "Environment Variables".
         3. Under "System variables", click "New".
         4. For "Variable name", enter `EMAIL_PASSWORD`.
         5. For "Variable value", enter your email password and click "OK".
        
       * Using Command Prompt:  
         1. Open a terminal and type `setx EMAIL_PASSWORD "your_actual_password"`.
         2. Replace `your_password` with your actual password.

    * **MacOS/Linux:**

      1. Open a terminal and type `export EMAIL_PASSWORD=your_password`.
      2. Replace `your_password` with your actual password.
   

3. **Choose the appropriate SMTP server and port for your email provider.** 

    Please note that using personal email accounts for mass mailing might violate their terms of service. Consider using dedicated email marketing services or obtaining consent from recipients before sending emails. Here are some common providers and their details:

    | Email Provider | SMTP Server | Port |
    |---|---|---|
    | Gmail | `smtp.gmail.com` | 465 |
    | Outlook.com | `smtp-mail.outlook.com` | 587 |
    | Yahoo Mail | `smtp.mail.yahoo.com` | 465 |
    | AOL Mail | `smtp.aol.com` | 587 |
    | Zoho Mail | `smtp.zoho.com` | 465 |

    (Additional providers may require different details, consult their documentation)


4. **Update the script with your chosen SMTP server, port, and email credentials.** You can find placeholders in the script marked with comments like `# Replace with your SMTP server` and `# Replace with your email and password`.


5. Run the script: `python birthday_reminder.py`

**Customization:**

* You can create multiple template files (named `letter_{number}.txt`) in the `./letter_templates` directory with different messages.
* Modify the script to adjust sending behavior or personalization options.

**Notes:**

* This script is for educational purposes and might require further optimization for production use.
* Ensure compliance with email provider terms and conditions.

**Contributing:**

We welcome pull requests and suggestions for improvement. Please follow the contributing guidelines if you wish to contribute.

