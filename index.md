## ADama Model

Dama means checkerboard in Turkish. The hypothetical optimal car formation in a 3x3 grid is a checkerboard, allowing a car to move forward and merge sideways without any disruption to the flow. 

<img src="img/1_checker.png" alt="hi" class="inline"/>

ADama is a nod to one of my favorite shows, [Battlestar Galactica](https://www.youtube.com/watch?v=evodPpqb9H4). 

A cellular automaton (CA) is a search function around a cell. The conventional update rule is based on the cell values in a cell's neighborhood.

<img src="img/2_CAupdate.png" alt="hi" class="inline"/>

There is an inherent attraction and repulsion between two cars in a lane. The tailing car is aiming to move forward into the front car's current position in the next time frame. However, the car in the back needs to leave a trailing distance to avoid crashing into the front. This is akin to a repulsion force.

<img src="img/3_drivingAR.png" alt="hi" class="inline"/>

I hypothesize this attraction-repulsion between two cars in a lane is a **long-range dipole interaction** in the driving direction, and in its normal direction the lane merging, the **dipole vanishes**.

In order to simulate the act of driving in a CA, I had to inverse the update rule to initiate the motion from a cell, as it is the case with a car. A car is similar to a free radical.  

You can use the [editor on GitHub](https://github.com/goktu/ADama/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/goktu/ADama/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
