HANGMAN GAME

Hangman is a python terminal game that runs in the Code Institute Terminal mock terminal on Heroku.  

Users have to guess the letters of the word to win the game.

# How To Play

Hangman is based on a the classic pen-and-paper game that many of us played in school when classes would finish early or just before the holidays were going to begin.

You have 7 lives (attempts) to guess the word.

The player simply enters a letter of the alphabet on the keyboard.

If the player guesses correctly the letter will be displayed and all lives will be intact.

If the player guessses incorrectly then a life will be deducted.

After guessing the letter the player will be prompted keep guessing until the word is displayed or until the number of lives reaches 0.

## Features

-Existing Features

    -Each hidden letter is displayed as an underscore '_'.

    -The number of lives are displayed after each guess is attempted.

    -There are 3 levels of difficulty: Easy, Medium, Hard.

    -Accepts user input.

    -Play again option.

    -Input validation and error correcting
        -You must enter characters in the English alphabet.

        -You cannot enter the same character more than once.

        -You can enter upper case or lower case letters.

-Future Features

    -Add more levels of difficulty.

    -Add more words to each difficulty level.

### Data Model

I used a json file to store the data for each difficulty level.

I created a variable and assigned it to the value of the json file.

#### Testing

Languages used

    -HTML5
    -CSS3

Frameworks, languages and programs used

    1.Google Fonts:
        -Google Fonts were used to import the 'roboto' font into the style.css file which was used throughout the project on all pages

    2.Font Awesome:
        -Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

    3.Git:
        -Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

    4.Github
        -GitHub is used to store the projects code after being pushed from Git.

    5.Balsamiq
        -Balsamiq was used to create the wireframes during the design process.


##### Deployment

    The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

    -W3C Markup Validator

    -W3C CSS Validator

Testing User Stories from User Experience (UX) Section

    -First Time Visitor Goals

        1.As a First Time Visitor, I want to easily understand the main purpose of the site.

            a.Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath there is a Hero Image with Text.
            
            b.There are 3 main categories immediately below the hero image.
            
            c.The 3 main categories are each further split into 4 points each respectively.

        2.As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.

            a.The site has been designed to be fluid and never to entrap the user. At the top of each page there is a clean navigation bar, each link describes what the page they will end up at clearly.
            
            b.At the bottom of the first 3 pages there is a redirection call to action to ensure the user always has somewhere to go and doesn't feel trapped as they get to the bottom of the page.
            
            c.On the Contact Us Page, after a form response is submitted, the page refreshes and the user is brought to the top of the page where the navigation bar is.

        3.As a First Time Visitor, I want to see if this site is applicable to me. I also want to locate their social media links to see their followings on social media to determine how trusted and known they are.

            a.Once the new visitor has looked at the site and read through the categories and points, they will know exactly how this site relates to them.
            
            b.The user can also scroll to the bottom of any page on the site to locate social media links in the footer.
            
    -Returning Visitor Goals

        1.As a Returning Visitor, I want to find information that I may not have previously thought of.

            a.The user can also go to the Tips page which will prompt them with more ideas by seeing the images and reading the information in the corresponding paragraphs.

            b.This can be easily done on the Questions page by filling out the form.

        2.As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.

            a.The navigation bar clearly highlights the "Questions" Page.

            b.Here they can fill out the form on the page or they can message the organisation on social media.
            
            c.The footer contains links to Facebook, Instagram, SnapChat an Twitter page.

            d.Whichever link they click, it will be open up in a new tab to ensure the user can easily get back to the website.

    -Frequent User Goals

        1.As a Frequent User, I want to check to see if there are any new information that was not there before.

            a.The user would already be comfortable with the website layout.

        2.As a Frequent User, I want to ask a question that did not come into my mind earlier.

            a.The user would already be comfortable with the website layout and can easily click on "Questions" in the navigation bar.

Further Testing

        1.The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.

        2.The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.

        3.A large amount of testing was done to ensure that all pages were linking correctly.

        4.Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

##### Deployment

GitHub Pages

The project was deployed to GitHub Pages using the following steps...

        1.Log in to GitHub and locate the GitHub Repository

        2.At the top of the Repository (not top of page), locate the "Settings" Button on the menu.

        3.Scroll down the Settings page until you locate the "GitHub Pages" Section.

        4.Under "Source", click the dropdown called "None" and select "Master Branch".

        5.The page will automatically refresh.

        6.Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.

Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

        1.Log in to GitHub and locate the GitHub Repository.

        2.At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.

        3.You should now have a copy of the original repository in your GitHub account.

Making a Local Clone

        1.Log in to GitHub and locate the GitHub Repository.

        2.Under the repository name, click "Clone or download".

        3.To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.

        4.Open Git Bash.

        5.Change the current working directory to the location where you want the cloned directory to be made.

        6.Type git clone, and then paste the URL you copied in Step 3.

        $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

        7.Press Enter. Your local clone will be created.

        $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
        
        > Cloning into `CI-Clone`...
        > remote: Counting objects: 10, done.
        > remote: Compressing objects: 100% (8/8), done.
        > remove: Total 10 (delta 1), reused 10 (delta 1)
        > Unpacking objects: 100% (10/10), done.

###### Credits

-Content
    -The icons in the footers of each of my pages were taken from font awesome.

    -All content was written by the developer.

-Media
    -The image from the home page (hero-image) was taken from google search.

    -The images from the tips page were all taken from google search.

    -The image question page was taken from google search.

-Acknowledgements

    -My Mentor for continuous and helpful feedback.

    -Tutor support at Code Institute for their support.



