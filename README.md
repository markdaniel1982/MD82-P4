# My Fishing Adventures

### My Adventures in Northern Sweden

![My Fishing Adventures](documentation/images/logotext.png)

Portfolio 4 project as part of the Diploma in Full Stack Software Development by Code Institute.
___

My Fishing Adventures is a blog, mainly to record and share my fishing trips, but also share other types/categories of content and allow users to interact with myself and other

It is a fullstack blog site that allows users to read blog posts, create an account and comment on the posts.

Link to live site - [https://md82p4blog.herokuapp.com/](https://md82p4blog.herokuapp.com/)

## CONTENTS

- [My Fishing Adventures](#my-fishing-adventures)
    - [My Adventures in Northern Sweden](#my-adventures-in-northern-sweden)
  - [CONTENTS](#contents)
  - [Site Objectives](#site-objectives)
- [User Experience/UX](#user-experienceux)
  - [Target Audience](#target-audience)
  - [User Stories](#user-stories)
    - [New Visitor Goals](#new-visitor-goals)
    - [Existing Visitor Goals](#existing-visitor-goals)
- [Design Choices](#design-choices)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Logo and Favicon](#logo-and-favicon)
- [Features](#features)
  - [Registration](#registration)
- [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Programming Languages, Frameworks and Libraries Used](#programming-languages-frameworks-and-libraries-used)
- [Agile](#agile)
- [Testing](#testing)
  - [Testing](#testing-1)
    - [User](#user)
  - [Bugs](#bugs)
  - [Validation Testing](#validation-testing)
    - [HTML \& CSS](#html--css)
  - [How to Write Your README](#how-to-write-your-readme)
    - [Headings](#headings)
    - [Links](#links)
    - [Inserting Images](#inserting-images)
    - [ Italic, Bold and Code](#italic-bold-and-code)
    - [Strikethrough \& Bullet Points](#strikethrough--bullet-points)
    - [Code Blocks](#code-blocks)
    - [Tables](#tables)
  - [Nice Extras \& Other Interesting Tools](#nice-extras--other-interesting-tools)
  - [Further Reading](#further-reading)
  - [Credits](#credits)
    - [Media](#media)
    - [Acknowledgments](#acknowledgments)

___

## Site Objectives

Design and create a blog site to demonstrate an increasing understanding of the libraries and frameworks available to developers.

My three main objectives were:

- ### Create a readable, clean and responsive front end

  I wanted to make the site easily accessible and intuitively navigated for the users. Django and Bootstrap were used to create and style the front end.

- ### Make use of available backend functionality

  The use of the backend framework allows users to create a profile, comment on any of the blog posts on the site, as well as deleting their own comments should they wish to.

- ### Store data on an external cloud database

  I used ElephantSQL to store the PostgreSQL databse for this project.

___

# User Experience/UX

## Target Audience

- Users that are interested in fishing, northern Swedish landscapes and cats!

## User Stories

### New Visitor Goals

- To understand what the site and content is about.
- How to navigate the site.
- Create an account and engage with the site and other users and site owner.

### Existing Visitor Goals

- Log in and out of their account.
- Read blog posts and comments on each post.
- Add their own comments on blog posts on the site to engage with site owner and other users.

___

# Design Choices

## Colour Scheme

The colour scheme used for this project was based on the colors from Code Institute's 'I think therefore i blog' walkthrough module. I have added and modified many aspects of the styling and colours to suit my intentions. It is a fairly neutral scheme, with mostly only the actionable aspects (buttons/links etc) displayed in brighter colours for ease of navigation or site use.

## Typography

The main font used is Verdana, but Tangerine was used for the main logo text on the navbar

## Logo and Favicon

The logo was created using an online logo creator - [Brandcrowd](https://www.brandcrowd.com/)

# Features

## Registration

The user can create an account

![Create an Account](documentation/images/create_account.png)

View Blog Posts on Home Page

![View Blog Posts on Home Page](documentation/images/home.png)

Browse by Post Category

![Browse by Post Category](documentation/images/browse_by_category.png)

Comment on Blog Posts.

*Also shown here is the trashcan which allows users to delete their own comments should they wish.*

![Comment on Blog Posts](documentation/images/commenting.png)

# Future Features

- Add option for users to edit comments
- Add option for users to upload photos into the comments

___

# Technologies Used

Here are the technologies used to build this project:

- [Github](https://github.com) To host and store the data for the site.
- [CodeAnywhere](https://www.codeanywhere.com) the IDE where the site was built.
- [PEP8 Validator](https://pep8ci.herokuapp.com/) Used to check python code for errors
- [ElephandSQL](https://www.elephantsql.com/) Used to store PostgreSQL database.
- [Cloudinary](https://cloudinary.com/) Used as cloud storage for images uploaded as part of the blog posts
- [Heroku](https://id.heroku.com/login) Used to deploy the project

# Programming Languages, Frameworks and Libraries Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

# Agile

This project was designed using Agile methodology, utilising the Project Board and Issues sections in GitHub

- [Project Board](https://github.com/users/markdaniel1982/projects/4/views/1)

# Testing

As each section or function/Model was built during this project, I was testing for functionality and styling issues that may have arisen, which were corrected or fixed before continuing. I also had friends test the site by signing up, adding and deleting comments using various devices on varying platforms (IOS, Android, Mobile Tablet etc) and reporting back any issues they encountered with functionality or styling.

## Testing

*For any Fails, there is a more detailed description below the table*

ADMIN
| TEST | OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
| Create Blog Post | Post successfully created and displayed | Pass |
| Edit Blog Post | Error thrown when editing post title & slug <sup>(1)</sup> | FAIL |
| Edit Blog Post (after fix) | Post content and category updated successfully | Pass |
| Delete User Comments | Comment deleted successfully | Pass |
| Delete Blog Post | Post deleted successfully | Pass |

<sup>(1)</sup> - While testing the ability to edit posts (Limited to Admin only), I had a problem when editing the title and slug of the post. this was due to the URL not being able to find the slug of the post to route it after the edit. At this stage, I felt the easiest fix was to remove the ability to edit the post title and slug in the browser, but this functionality is still available via the django admin panel.

### User

| TEST | OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
| Create Account | Created successfully | Pass |
| Login | Login Successful | Pass |
| Logout | Logout Successful | Pass |
| Read Full Blog Post | PostDetail page loaded successfully | Pass |
| Add Comment under Blogpost | Comment Added Successfully | Pass |
| Delete Comment | Comment Deleted | Pass |
| Filter Posts by category | Posts marked as desired category displayed successfully | Pass |

## Bugs

One of my users reported that they were unable to sign up when including an email address (although the inclusion of an email address is not required), but myself and others were unable to replicate this issue so the bug was marked as closed.

At different points throughout this project, I encountered various bugs involving the styling. These usually appeared after adding a new section or template page. These were all fixed using Bootstrap classes or custom CSS to override any issues caused by Bootstrap itself.

Towards the end of completion, I had an issue with the database, where I had made a change to the Post Model, but hadn't migrated the changes after undoing the changes in the code relating to that change. This required me to reset the database, which was done with help from Rebecca via the Code Institute's Tutor Support. The changes related to the Category Model and the choices available when creating an account.

To enable me to reset the database, I first had to comment out the code (related to "choices" in the model) to stop the code being run and causing an error. Once this was done, the database was reset, seemingly without issue.

Then I had a problem with the "Create a Post" page. When adding a new blog post via the browser, the images were not being sent to cloudinary for cloud storage, and the ElephantSQL cloud database was also not recieving any data. This was a very simple f

## Validation Testing

### HTML & CSS

HTML & CSS testing was completed using [W3 Validator](https://validator.w3.org/)



## How to Write Your README

README files are written using markdown, a lightweight plain text syntax.

There are some really cool features in markdown that you might want to include in your README, and I've included some below. I've also included some links to some further reading on markdown.

### Headings

Just like with HTML, markdown has headings. Markdown headings are very similar to HTML headings: there are 6 heading levels, you can only use one level 1 heading per page and ach heading level is smaller than the last.

To create a heading in Markdown you use a hash symbol (#) followed by a space and the heading. The number of hashes denotes the level of the heading - so for a level 1 heading you use 1 hash, a level 2 has 2 hashes etc. The example below shows how you would write a level 3 heading:

  ![Heading Example](documentation/heading-example.png)

### Links

Links are also really useful in Markdown, and are really simple to write. There are two ways to include links in your README:  

You can paste a link into your README and it will display as a link, <https://www.github.com/kera-cudmore> - but these can throw a markdown lint error, look a bit messy especially if the link is rather lengthy, and sometimes the URL address doesn't make it clear as to what the link redirects to.

My preferred way to add a link which addresses both these issues is to make a link the following way: place the name of the link that will be visible in the README enclosed in square brackets followed by the link enclosed in parentheses. [View My GitHub Profile Here](https://www.github.com )

  ![Link Example](documentation/link-example.png)

You can also create a link with headings. When you create a heading, GitHub will generate an ID based on this. This is really useful if you then want to create a link to that heading within your README.  (A good example of this is the contents section.) They are very similar to a link - We need to put the text that will be displayed into the square brackets and then within the parentheses we use a hash followed by the heading - note that we can't use spaces so these need to be changed to a dash)

![Heading Links Example](documentation/heading-links.png)

### Inserting Images

Images can be inserted in your README in the same way as a link, if you only want the name of the image to be displayed.

If you want the image itself to be visible in the README, you just need to place an exclamation mark at the front of the link, example shown below:

![Inserting an Image Link Example](documentation/imagelink-example.png)

Its important to be mindful of what you use in the square brackets of an image link, as this is what will be displayed on the page if the image fails to load, so make sure to use something descriptive, similar to an image alt tag.

When using images in your README, its good practice to compress the image first (PNG format seems to work best), I can recommend [tinyPNG](https://tinypng.com/). I then like to keep all images etc used within the README in a folder called *documentation*. This is good practice as it keeps the sites assets seperate from the assets used in your documentation.

###  Italic, Bold and Code

*Italic text* we can either use an asterisk or an underscore before and after the text.

**Bold text** we can either use double asterisks or double underscores before and after the text.

`Code` we enclose the text in backticks.

![Styled Text Examples](documentation/styledtext-example.png)

### Strikethrough & Bullet Points

~~strikethrough~~ We use double tilder before and after.

- Bullet points, we use either an asterisk or a dash.
  - Nested Bullet Points are created by indenting two spaces
    - Another Nested Bullet Point

![Strikethrough & Bullet Point Example](documentation/strikethrough-bullet-example.png)

To create a numbered list we simply put a number followed by a full stop, then a space before the content.

1. First item
2. Second item
3. Third Item

![Numbered list example code](documentation/numbered-list-example.png)

### Code Blocks

Code blocks can be used in Markdown to display a larger block of code. To create a code block you need to prefix the text with three backticks and end with three backticks after.

Code blocks can be language specific, you simply need to add the language after the first set of backticks - if you don't want to use a specific language, you can use text.

**Plain Text Code Block:**

```text
function fibonacci(num, memo) {
  memo = memo || {};

  if (memo[num]) return memo[num];
  if (num <= 1) return 1;

  return memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo);
}
```

**JavaScript Code Block:**

```javascript
function fibonacci(num, memo) {
  memo = memo || {};

  if (memo[num]) return memo[num];
  if (num <= 1) return 1;

  return memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo);
}
```

Code Block Markdown Examples:

![Code Block Examples](documentation/codeblock-example.png)

### Tables

Tables can be a great way to display information in your README, but can be a bit fiddly to get your head around at first. Tables are created using the pipe symbol ( | ) which is placed on either side of the content, creating the sides of the table. The first row of the table will be the headings for the table. This is then followed by a row with 3 dashes in each cell, and then you just add the contents for the table in the following rows.

| Table Heading 1 | Table Heading 2 |
| --- | --- |
| I'm a piece of information in a table | Me too! |
| 1| 2 |
| 2 | 3 |

Markdown for creating a table:

![Table Example](documentation/table-example.png)

You can also justify the contents within a table! You simply need to add a colon to the second row of dashes - place the colon on the left of the dashes for left justification, to the right of the dashes for right justification and to center the text, place a colon on each side of the dashes.

| Table Heading 1 for justification example | Table Heading 2 For justification example |
| :--- | :--- |
| Justify contents| To the Left |

| Table Heading 1 for justification example | Table Heading 2 For justification example |
| ---: | ---: |
| Justify contents | To the Right |

| Table Heading 1 for justification example | Table Heading 2 For justification example |
| :---: | :---: |
| Justify contents | In the Center |

![Table Justification Example Code](documentation/table-justification-example.png)
 - - -

## Nice Extras & Other Interesting Tools

Nice extras we could include in the README:

[shields.io Badges](https://shields.io/) -  lots of badges relating to site builds. I like to add these after the site image at the top of my README. I like to include the following badges in my projects, but have an explore and see if there are any others you could use (they are also great to include in your GitHub Profile!)

- GitHub last commit (Shows when the last commit to the repo was)
- GitHub contributors (Great to show at a glance you are the only contributor to your project)
- GitHub language count (Shows how many languages used in project)
- GitHub top language (to display top language used in the project)
- W3C validation (shows at a glance whether your HTML passes validation)

![Shields.io Exmaple Badges](documentation/shields-example.png)

[Gyazo GIF](https://gyazo.com) - A tool that allows you to capture a short video recording of your screen as a GIF. I like to use this to document a bug I might have (For example in my second project, each time a button was pressed the score would increase when it shouldn't have - this was a great way to capture what was happening). Have a look, or perhaps you have your own preferred screen recording tool you prefer.

[Chrome Extension Spell Checker](https://chrome.google.com/webstore/detail/webpage-spell-check/mgdhaoimpabdhmacaclbbjddhngchjik) - I love to use this both on my site and to check over my README before submission, as its easy to get spelling errors creeping into your project as you burn the midnight oil towards the end as your deadline is looming.

[Chrome Exension WAVE](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh) - WAVE is a web accessibility evaluation tool developed by [WebAIM.org](https://wave.webaim.org/). It provides visual feedback about the accessibility of your web content by injecting icons and indicators into your page. No automated tool can tell you if your page is accessible, but WAVE facilitates human evaluation and educates about accessibility issues. All analysis is done entirely within the Chrome browser allowing secure valuation of intranet, local, password protected, and other sensitive web pages. I believe there is also an extension for Firefox.

[Web Disability Simulator](https://chrome.google.com/webstore/detail/web-disability-simulator/olioanlbgbpmdlgjnnampnnlohigkjla) - A fantastic chrome extension that allows you to simulate how certain disabilities can affect the users experience of your site. Really useful if you're using colour to represent a result - for example in a quiz.

- - -

## Further Reading

- [Markdown Syntax](https://www.markdownguide.org/basic-syntax/) - This site is really comprehensive on all the different things you can do in Markdown.
- [Markdown Table Generator](https://www.tablesgenerator.com/markdown_tables) - This may be useful to have a play around with to better understand how tables work in Markdown.
- [Markdown Cheatsheet](https://github.com/atapas/markdown-cheatsheet) - A great markdown cheatsheet created by Atapas.
- [Code Institute Sample README](https://github.com/Code-Institute-Solutions/SampleREADME) - Sample README created by the Code Institute

## Credits

### Media

• All screenshots of code used in this README were taken by myself from my own milestone project repositories or Code Institute hackathon projects I have participated in.

• [README hero image](https://www.slidescarnival.com/aliena-free-presentation-template/4597) - Slide template from Slide Carnival

### Acknowledgments

- [Ed](https://github.com/Edb83) - For letting me know about the heading links feature.
- [Dave](https://github.com/daveyjh) - For letting me know about table justification in markdown.
- Nerd Alert - For cheering me on while creating this webinar, and for proof-reading my documents.
- A big thank you to Jim at Code Institute for the opportunity to be a channel lead for the Milestone 1 slack channel.
