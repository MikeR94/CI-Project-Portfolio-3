# **_The Formula 1 Hub - Project Portfolio 3 - Python_**

The Formula 1 Hub is a command line interface styled application that allows players to test their knowledge on Formula 1. The quiz consists of 3 different levels to choose from, granting more points for harder difficulties. The quiz has 10 questions for each difficulty and if the player answers all questions, they will receive points based on the difficulty selected. Additionally the Formula 1 Hub will allow players to view additional information regarding the upcoming Formula 1 2022 Season such as the current drivers, the 2022 calendar and some interesting Formula 1 facts.

You can view the live site here - <a href="https://mr-project-portfolio-3.herokuapp.com/" target="_blank" rel="noopener">The F1 Hub</a>

![The F1 Hub responsive design](assets/images/readme-images/preview-image.png)

# Contents

* [**Objective**](<#objective>)
* [**User Experience UX**](<#user-experience-ux>)
    * [Design Prototype](<#design-prototype>)
    * [Site Structure](<#site-structure>)
    * [Python Logic](<#python-logic>)
    * [Design Choices](<#design-choices>)
    *  [Typography](<#typography>)
    *  [Colour Scheme](<#colour-scheme>)
* [**Features**](<#features>)
    * [Startup Display](<#startup-display>)
    * [Main Menu](<#main-menu>)
    * [Quiz Hub Menu](<#quiz-hub-menu>)
    * [Quiz](<#quiz>)
    * [Quiz Leaderboards](<#quiz-leaderboards>)
    * [Quiz Statistics](<#quiz-statistics>)
    * [Quiz Rules](<#quiz-rules>)
    * [F1 Info Hub Menu](<#f1-info-hub-menu>)
    * [View F1 Fact](<#view-f1-fact>)
    * [Select A Track](<#select-a-track>)
    * [F1 2022 Calendar](<#f1-2022-calendar>)
    * [F1 2022 Drivers](<#f1-2022-drivers>)
    * [Submit Feedback](<#submit-feedback>)
    * [Exit App](<#exit-app>)
* [**Future Features**](<#future-features>)
    * [Latest News](<#latest-news>)
    * [Polls](<#polls>)
* [**Technologies Used**](<#technologies-used>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Media**](<#media>)
    * [**Code**](<#code>)
*  [**Acknowledgments**](<#acknowledgements>)
*  [**Personal Development**](<#personal-development>)


# Objective

In my third project, I intend to create a visually appealing command line interface application where players can test their knowledge on Formula 1 and also provide some insightful, interesting and useful information regarding the upcoming 2022 season. The main objective is to demonstrate competency in Python whilst adhering to high presentation standards.

[Back to top](<#contents>)

# User Experience (UX)

## Design Prototype

The very first design prototype was created using [Balsamiq](https://balsamiq.com/). I only designed the very bare minimum using this program so that I could have a basic idea of what I wanted to achieve. Additionally because this is a command line interface application, there is only a small amount of room to come up with ideas on how to present it so I decided that I wanted the command line interface to be housed within a computer screen to give it a more presentable look and then I would add a Formula 1 styled background to enhance the visual appearance.<br /><br />


![Balsamiq Start Prototype](assets/images/readme-images/balsamiq-prototype.png)


[Back to top](<#contents>)

## Site Structure

The Formula 1 Hub is a one-page website that, in the center, has a command line interface. When the application starts up, the player will be greeted with a nicely styled initial startup screen and then asked to enter a username. The application is designed with the user experience in mind so at every stage, the user will be asked if they wish to return to either the Quiz Hub Menu, F1 Info Hub Menu or the Main Menu. The application also has a 'RUN APP' button located at the bottom of the screen which the user can press and reload the application if they wish to do so.

## Python Logic

I decided to create a logic flow chart to detail the entire flow of the application. Creating this gave me a brilliant overview of how everything works and how the user will navigate the application. The logic flow chart was created using an excellent [VSCode](https://code.visualstudio.com/) extension called [Draw.io](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio).

![Python Logic Chart](assets/images/readme-images/f1-hub-logic-flow.png)

## Design Choices

 * ### Typography
      The main additional typography chosen to enhance the site was to introduce ASCI art to add an additional dynamic to the presentation. The ASCI art was used for the start-up display and the thank you message when the user exits the application. 

 * ### Colour Scheme
      The application utilises a brilliant Python package called [Colorama](https://pypi.org/project/colorama/) which allows developers to change the colour of the text <br /><br />

## Existing Features
  * ### Startup Display

      * This is the first part of the quiz the player will see when visiting and is designed to allow the player to immediately get started with playing the quiz.
      * In the middle of the website the player will see the quiz application complimented by a beautiful space background.
      * Within the quiz application, the player will be greeted and then asked to submit a name and then click next to be directed to select a difficulty.
      * If the player inputs a name that doesn't meet validation, the player will be given feedback on how to fill the name input correctly.<br /><br />

<details><summary><b>Desktop Home/Landing Page Image</b></summary>

![Startup Display Image](assets/images/readme-images/startup-display-image.png)
</details><br />

<details><summary><b>Responsive Home/Landing Page Image</b></summary>

![Responsive Home Image](assets/images/readme-images/responsive-home-page-image.png)
</details><br />

[Back to top](<#contents>)

  * ### Navigation Bar

    * Located at the top of the quiz application and provides the player the ability to navigate back to the home page, enter the menu and turn the game sounds on or off. Whilst the player is currently playing the quiz, the hamburger icon will disappear and will be replaced with additional features such as "Current Question Number", "Time Left" and "Score" to give the player more information and provide a better player experience.
    * An additional GitHub icon will be visible on the contact page for players to see the repository in a new window.<br /><br />

<details><summary><b>Desktop Navigation Bar Image</b></summary>

![Navigation Bar Desktop Image](assets/images/readme-images/desktop-nav-bar-image.png)
</details><br />

<details><summary><b>Desktop Navigation Bar Image (Contact Page)</b></summary>

![Navigation Bar Desktop Contact Image](assets/images/readme-images/desktop-nav-bar-contact-image.png)
</details><br />

<details><summary><b>Desktop Navigation Bar Image (During Quiz)</b></summary>

![Navigation Bar Responsive Image](assets/images/readme-images/desktop-nav-bar-quiz-image.png)
</details><br />

<details><summary><b>Responsive Navigation Bar Image (During Quiz)</b></summary>

![Navigation Bar Responsive Image](assets/images/readme-images/responsive-nav-bar-quiz-image.png)
</details><br />

[Back to top](<#contents>)