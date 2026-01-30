# Day 43 – Color Vocab Website Project

## Project Overview

This project is a simple HTML and CSS based static webpage where I started learning about how to style a webpage using CSS. In this project, I learned how CSS works with HTML, different ways to add CSS styles, and how to use selectors to target HTML elements. By using colors, images, and text styling, I built a small static webpage that displays Spanish color names along with their images. The main goal of this project was to understand CSS fundamentals and how styling improves the look and structure of a webpage.

## What I Have Learned

* **CSS Style Add Types**: Learned about the three different ways to add CSS to an HTML file.
  * **Inline CSS**: Writing CSS directly inside an HTML tag using the style attribute.
  * **Internal CSS**: Writing CSS inside the `<style></style>` tag within the `<head></head>` section of the HTML file.
  * **External CSS**: Writing CSS in a separate .css file and linking it to the HTML file using the `<link rel="stylesheet" />` tag. This is the most recommended and clean way.
* **Class Selector**: : Learned how to use class selectors in CSS using .class-name to apply the same style to multiple HTML elements, such as .color-title.
* **ID Selector**: Learned how to use id selectors using #id-name to apply styles to a unique element, such as #red, #blue, and #green.
* **Attribute Selector**: Learned that CSS can target elements based on attributes, such as selecting elements that contain specific attributes like li[value= "4"] which will change that element attribute .
* **Universal Selector**: Learned about the universal selector * which can be used to apply styles to all elements on the webpage.
* **CSS Styling Properties**: Learned how to use basic CSS properties like color, font-weight, width, and height to update and control the appearance of HTML elements.

## How It Works

* **HTML Structure**: The webpage uses standard HTML structure starting with `<!DOCTYPE html>`, followed by `<html></html>`, `<head></head>`, and `<body></body>`.
* **External CSS Linking:**: The CSS file is linked to the HTML file using the `<link rel="stylesheet" href="./style.css" />` tag inside the <head> section.
* **Text Styling**: The class selector .color-title is used to style multiple `<h2>` elements together to make their font-weight: normal.
* **Color Identification**: All spanish text  are styled using id selectors like #red, #blue, #orange, #green, and #yellow which are their actual english meaning to match their actual colors.
* **Image Styling**: The <img /> tag is styled using a selector to give all images the same width and height for consistency.
* **Content Display**: Each color name is displayed using `<h2>` tags and paired with an image using the `<img />` element.

## Project Highlights

* Learned how to make CSS and HTML work together
* learned about inline, internal, and external CSS styles and how to use them.
* Learned and applied different CSS selectors like class, id, attribute, universal selectors.

