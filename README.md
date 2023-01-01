# MyPetMatch
#### Video Demo:  <URL HERE>
#### Description:

## ABOUT THE PROJECT

<img src="https://user-images.githubusercontent.com/61602443/210157927-155bff56-0f41-46e0-9800-3c3479b86d0b.png" width="25%">

I created this project as my final project for Harvard's CS50 Introduction to Computer Science class. Pets are part of millions of people's lives, and millions of these furry, feathered friends are waiting in shelters all around the US. I wanted to create a fun website where users can fill out a simple form and get matched with pets in their immediate area. My hope for this project is to motivate those families/people to adopt a pet by simplifying the process. 

Since this is a final project for a class, all of the kinks have not been worked out. However, my hope is to continue to enhance this project as time goes on and I gain more skills. 


## BUILT WITH

<ul>
  <li>Python</li>
  <li>Flask</li>
  <li>HTML</li>
  <li>CSS</li>
  <li>Petfinder API</li>
  <li>Bootstrap</li>
</ul>
  
  ### Files Descriptions
  
  #### homepage.html
  This is a page that just welcomes the user to the page, and tries to incentive the user to adopt with a paragraph and some statistics. There are call to action buttons that take the user to a form to find shelter pets.
  
  #### index.html
  This page started off as the main page for this project. As the project progressed I felt like the site needed an introduction, so this became a secondary page, but still the most important page of the project. The main objective is for it to ask the user some basic questions on their preference in order to search the API to meet their requirements. 
  
  #### results.html
  This is a simple page that simply displays the results from our query and allows the user to see images of pets around them, their name, and a short description. It also contains a simple call to action button that takes the user to the pet's main page on **petfinder.com** where they can learn more about their prefered pet, as well as get in touch to begind the adoption procedure. 
  
  #### layout.html
  Template page that contains HTML boilerplate information to be used across the pages we create. It also holds the header information along with a logo image. On the head tag of this file, you'll find the CSS, bootstrap and font links that we use throughout the site. 
  
  #### failure.html
  A simple page that displays when there is an error in the user's form input. As of now it only displays on simple errors of the form and informs on what went wrong so the user can go back and correct it.
  
  #### app.py
  This is the main "brain" of our site. It handles the forms actions and inputs. It also makes the API requests to the Petfinder API by formatting query strings. It contains headers and parameters. We also have a functionality to verify the zip code the user submitted through the use of a different API that looks up if the zipcode is valid or not. 
  
  #### index.css
  Our style sheet that we use to design certain elements throughout the site, like changing the color of headings, font sizes, background images, etc.
  
  #### index.js
  A javascript file that I used to test certain features, but is not a main component of our site.
  
  ## FINAL THOUGHTS
  
  At the beginning of this project my vision was to have a simple form that displayed pets around the user's area. As I worked on the site, I found my list of wanted features continued to grow. Like mentioned earlier my vision began as a simple form that would return results, however from a UX perspective I found that implementing a home page that would describe the goal of the site as well as some statistics would result in better user engagement. Although at first I was not proud of this project, because it fell short of my vision for it. I came out wanting to continue it in the future and get it to what I first envisioned this project to be. I think starting this project from scratch was very intimidating, but it helped me realize that I did in fact learned much more than I originally thought, and further solidified my interest in continuing to learn programming. 
  
  
