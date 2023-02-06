# Rutgers-API
This is a reverse engineering of the API that Rutgers uses to assign and aggregate all of their courses. I did not see anyone else publish and explain the information they found so I made my own.

## Overview

Currently this code will create a treeemap of all the classes at rutgers scaled by the amount of sections they have and sorted into which department they are classified as.

This is an example of what it may look like:

![Rutgers section treemap](https://media.discordapp.net/attachments/749403737730187328/1072209301059412039/RutgersAPI.png)

You can see pretty intuitively that 198, Computer Science, is the biggest department at rutgers, but the class with the most amount of sections is 01:355:101 which is Expository Writing, a requirement for all incoming freshmen.

## The Code

The link to find this json data is here:
```
https://sis.rutgers.edu/soc/api/courses.json?year=2023&term=1&campus=NB
````

Campuses:
* NB: New Brunwick
* NK: Newark
* CM: Camden

You can change the term number and the year to suit your needs, although from my experience future or past courses are not archived.

## Further Projects

Many have created course snipers so they can immediately know when a course section opens up.

* SwiftRU: Within 1 second
* TrackRU (discontinued): Within 5-10 seconds
* TSniper: Within 5-10 seconds
* SchedRU: Within 10-20 seconds
* RUCourseSniper: Within 5-10 seconds
