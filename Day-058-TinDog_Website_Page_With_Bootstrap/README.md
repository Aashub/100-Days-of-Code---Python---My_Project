# Day 58 – TinDog Website with Bootstrap

## Project Overview

This is a front-end website project called TinDog (a Tinder-inspired app for dogs) built using HTML, CSS, and the Bootstrap framework. The website features a modern, responsive design with a gradient hero section, feature highlights with icons, a testimonial section with user reviews, pricing plans for different dog breeds, and a footer with navigation links. The project demonstrates how to leverage Bootstrap's pre-built components and grid system to quickly create a professional-looking landing page while adding custom CSS for personalization.


## What I Have Learned

* **Bootstrap**: Bootstrap is a free and open-source CSS framework created by developers at Twitter (Mark Otto and Jacob Thornton) to promote consistency across internal tools. It was released as an open-source project in 2011 and has since become one of the most popular front-end frameworks. Bootstrap provides pre-written HTML, CSS, and JavaScript code for common website components like navigation bars, cards, buttons, forms, and modals, saving developers time and ensuring responsive design across different devices.

* **Using Bootstrap via External Link**: Learned how to include Bootstrap in a project by adding a CDN (Content Delivery Network) link in the HTML `<head>` section and the JavaScript bundle before the closing `</body>` tag. This allows access to all Bootstrap components without downloading any files locally.

* **Customizing Bootstrap Components**: Understood how to override Bootstrap's default styles by adding custom CSS classes. For example, while Bootstrap provides default button styles, this project customizes button colors, hover states, and spacing. The pricing section demonstrates customizing card borders, header colors, and button styles to match the website's theme while maintaining Bootstrap's core functionality.

* **12-Column Bootstrap Layout System**: Learned about Bootstrap's responsive grid system which divides the page into 12 columns. Used classes like row, col, col-lg-3, col-sm-12 to create layouts that automatically adjust based on screen size. For example, in the testimonial section, col-lg-3 col-sm-12 makes each brand logo take 3 columns on large screens (4 per row) but full width on small screens (stacked vertically).

* **Bootstrap Components**: Explored and implemented various Bootstrap components including Navbar, Buttons, Cards, Grid System, Icons, Footer.

## How It Works

* **Bootstrap CDN Integration**: The Bootstrap framework is included via CDN links in the HTML head and body, giving access to all pre-built components, responsive grid classes, and utility styles throughout the website.

* **Title Section**: The hero section uses Bootstrap's container and grid system with `row flex-lg-row-reverse` class to position the iPhone image on the right and heading text on the left on large screens, while stacking them on mobile. The gradient background is applied via custom CSS gradient-background class with a linear gradient animation that cycles through blue, pink, and coral colors. Download buttons use Bootstrap button classes (btn btn-light btn-lg and btn btn-outline-light btn-lg) with SVG icons from Bootstrap Icons library for Apple and Google Play.

* **Features Section**: Three feature columns are created using Bootstrap's responsive grid with `row-cols-1 row-cols-lg-3` to stack on mobile and display in 3 columns on desktop. Each feature includes an icon square using Bootstrap's `icon-square` class with SVG icons, a heading, and descriptive text. The layout uses flexbox utilities (d-flex align-items-start) to align icons properly with content.

* **Testimonial Section**: This section displays a user testimonial with quote text, a rounded profile image (using custom CSS `rounded_circle_frame` class with `border-radius: 50%`) to make profile shape round, and the user's name. Below that, four brand logos (TechCrunch, Mashable, BizInsider, TNW) are arranged using Bootstrap's grid with `col-lg-3 col-sm-12` classes this makes them display in a row of 4 on large screens but stack vertically as full-width columns on mobile devices.

* **Pricing Section**: Three pricing cards are created using Bootstrap's card component with `card`, `card-header`, `card-body`, and `card-title` classes. The cards are arranged using `row-cols-1` `row-cols-md-3` to stack on mobile and display side-by-side on medium screens. The third card (Mastiff) uses `border-dark` and `text-bg-dark` Bootstrap classes to highlight it as a featured option with a dark header. Each card includes a price, feature list, and action button with appropriate Bootstrap button classes.

* **Footer Section**: The footer uses Bootstrap's responsive grid with `row-cols-1` `row-cols-sm-2` `row-cols-md-5` to create a multi-column layout. It includes brand information and three navigation sections with links. The gradient background from the hero section is reused here for visual consistency using the same gradient-background class.

* **CSS Styling**: Custom CSS handles the animated gradient background using @keyframes gradient-animation that changes background position over 18 seconds for a smooth color transition. The icon-square class creates consistent 3rem square containers with border radius for feature icons. The testimonial image is made circular with border-radius: 50% and centered with margin utilities, while typography styling controls the font weight and spacing for the dog name and other text elements.


## Project Highlights

* **Bootstrap**: Learned about bootstrap and how to use it.
* **12-Column Layout System**: Learned about Bootstrap's responsive grid system which divides the page into 12 columns using classes. 
* **Bootstrap Framework Integration**: Learned & Successfully integrated Bootstrap via CDN to leverage pre-built components and responsive grid system for rapid development.
* **Responsive Design**: Ensured the website looks great on all devices using Bootstrap's responsive classes which make sure that all the things looks good across all the devices.
* **SVG Icon Integration**: Used Bootstrap Icons library to add scalable vector icons throughout the site for better performance and scalability.





