# Day 77 – Computation with NumPy and N-Dimensional Arrays

## Overview

This is a data analysis and numerical computing project where I used NumPy, Matplotlib, and image data to explore how multidimensional arrays work. The project focused on understanding NumPy's powerful ndarray object, performing mathematical operations on arrays, generating data for visualisations, and manipulating images using numerical computations.

Through this project, I learned how NumPy makes working with large amounts of numerical data much faster and more efficient than standard Python lists. I also explored concepts such as array dimensions, slicing, broadcasting, matrix multiplication, random number generation, and image processing. 

## Notebook Link
https://drive.google.com/file/d/1ejIxn0oAR0qbX0idEDFpIQ6DYVMD_JI3/view?usp=drive_link


## What I Have Learned

* **NumPy's ndarrays**: Learned how NumPy's ndarray provides a fast and efficient way to store and manipulate numerical data. Unlike Python lists, ndarrays support vectorised operations that allow calculations to be performed on entire arrays at once.

* **Creating Arrays with NumPy**: Learned how to create 1-dimensional, 2-dimensional, and n-dimensional arrays manually using np.array(). These arrays form the foundation for all numerical computations in NumPy.

* **Generating Arrays Automatically with .arange(), .random(), .linspace()**: Learned how to generate arrays automatically using functions such as .arange(), .random(), and .linspace(). These methods make it easy to create sequences, random values, and evenly spaced data points.

* **Array Shape and Dimensions**: Used .shape and .ndim to determine the size and dimensionality of arrays. Understanding array structure is important when performing calculations and transformations.

* **Indexing and Slicing ndarrays**: Learned how to retrieve specific values, rows, columns, and subsets using indexing and slicing. This allows precise control over which parts of an array are being analysed or modified.

* **How to Slice and Subset ndarrays Based on Their Indices**: Used slicing techniques to extract specific sections of arrays, reverse arrays, retrieve subsets, and filter values based on conditions. Slicing makes data manipulation much more efficient.

* **Conditional Selection and Filtering**: Learned how to use conditional logic and functions such as np.where() to locate specific elements inside an array. This helps identify values that meet particular criteria.

* **Generating Data for Visualisation**: Used .linspace() to generate evenly spaced values and create coordinates for plotting graphs with Matplotlib. NumPy makes it easy to generate mathematical data for visualisation.

* **Visualise Data with Matplotlib**: Learned how NumPy arrays can be directly used with Matplotlib to create charts and visualise mathematical relationships between variables.

* **Broadcasting in NumPy**: Learned how NumPy automatically adjusts array operations through broadcasting. This allows mathematical operations between arrays and scalars without manually matching dimensions.

* **Linear Algebra with NumPy**: Used vector addition, scalar multiplication, matrix multiplication, .matmul(), and the @ operator to perform common linear algebra operations. These operations are widely used in machine learning and scientific computing.

* **Scalar and Vector Operations**: Learned how arithmetic operations can be applied to entire arrays at once. NumPy automatically performs calculations on every element without requiring loops.

* **Using NumPy Broadcasting to Make Array Shapes Compatible**: Learned how broadcasting allows arrays of different shapes to work together during calculations. This makes numerical computations more flexible and efficient.

* **How to Manipulate Images as ndarrays**: Learned that digital images can be represented as multidimensional NumPy arrays. By modifying array values, it becomes possible to transform and edit images programmatically.

* **Grayscale Image Conversion**: Learned how to use matrix multiplication and colour channel weights to transform RGB images into grayscale images. This is a common image-processing technique.

* **Image Manipulation with NumPy**: Used NumPy operations to flip images, rotate images, and create negative (solarized) versions of images. These transformations demonstrate how image manipulation is fundamentally numerical computation.

## How It Works

### Creating and Exploring NumPy Arrays

* **Creating 1-Dimensional Arrays**: Used np.array() to create vectors and store numerical values inside NumPy arrays.

* **Creating 2-Dimensional Arrays**: Built matrices using nested lists and explored how rows and columns are represented inside NumPy.

* **Working with N-Dimensional Arrays**: Created higher-dimensional arrays and analysed their structure using .shape and .ndim.

* **Understanding Array Structure**: Understood how NumPy organises data across multiple axes and dimensions.

### Accessing and Manipulating Data

* **Accessing Individual Elements**: Used indexing to retrieve specific values from arrays.

* **Retrieving Rows and Columns**: Used slicing operations to access complete rows, columns, and subsets of data.

* **Filtering Values**: Used conditions and boolean logic to extract values that matched specific requirements.

* **Finding Non-Zero Elements**: Applied np.where() to locate the positions of non-zero values within arrays.


### Generating Arrays and Numerical Data

* **Generating Sequential Values**: Used .arange() to create arrays containing sequential numbers.

* **Generating Random Data**: Used NumPy's random functions to create arrays filled with random values.

* **Generating Evenly Spaced Values**: Used .linspace() to create evenly spaced points between two values.

* **Creating Plot Data**: Generated x and y coordinates using NumPy arrays and visualised them using Matplotlib.

### Linear Algebra and Broadcasting

* **Vector Operations**: Used NumPy arrays to perform vector addition and other arithmetic operations. This demonstrated how NumPy performs element-wise calculations automatically and more efficiently than traditional Python lists.
* **Broadcasting and Scalar Calculations**: Applied scalar values directly to entire arrays without using loops. NumPy's broadcasting feature automatically adjusted array shapes, making mathematical operations simple and efficient.
* **Matrix Multiplication**: Used .matmul() and the @ operator to perform matrix multiplication. This helped demonstrate how NumPy handles linear algebra operations that are commonly used in machine learning and scientific computing.

### Working with Images as NumPy Arrays

* **Understanding Image Data**: Explored how digital images are stored as multidimensional arrays containing pixel values and colour channel information. Analysing image shapes helped understand how computers represent visual data.
* **Grayscale Image Conversion**: Converted RGB images into grayscale by combining colour channels using weighted values. This demonstrated how image processing can be performed through mathematical operations on arrays.
* **Image Manipulation and Transformations**: Used NumPy operations to flip, rotate, and create negative versions of images. These transformations showed how modifying array values directly affects the appearance of an image.

### Key Insights Found

#### NumPy Array Insights
* NumPy arrays made mathematical operations much simpler by allowing calculations on entire datasets at once instead of using loops.
* Understanding array dimensions and shapes became essential when working with multidimensional data and performing transformations.
* NumPy's vectorised operations provided a cleaner and more efficient way to handle numerical computations.

#### Broadcasting Insights
* Broadcasting allowed scalar values to be applied across entire arrays without manually iterating through elements.
* Arrays with compatible shapes could be combined using simple mathematical expressions.

#### Linear Algebra Insights
* Matrix multiplication produced different results from element-wise multiplication, highlighting the importance of choosing the correct operation.
* Compatible matrix dimensions were required for successful matrix multiplication.
* NumPy's built-in linear algebra functions made working with matrices much more straightforward.

#### Image Processing Insights
* Images could be represented and manipulated as multidimensional NumPy arrays.
* Grayscale images were created by combining RGB colour channels using weighted values.
* Image transformations such as flipping, rotating, and creating negative images could be performed directly through array operations.

## Highlights

* **NumPy Fundamentals**: Created and manipulated 1D, 2D, and n-dimensional arrays.
* **Array Analysis**: Used .shape and .ndim to understand array structures.
* **Indexing and Slicing**: Accessed specific values and subsets within arrays.
* **Array Generation**: Used .arange(), .random(), and .linspace() to generate numerical data
* **Conditional Operations**: Located values using filtering and np.where().
* **Broadcasting**: Applied mathematical operations across arrays efficiently.
* **Linear Algebra**: Performed vector operations and matrix multiplication.
* **Image Manipulation**: Treated images as NumPy arrays for analysis and transformation.
