---
# layout: splash
permalink: /teaching/BDA2023/syllabus/
title: "Applied Bayesian Data Analysis"
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
toc_sticky: true
---

__Instructor:__ Stephen Kissler <br>
__Class times:__ TBD <br>
__Class location:__ TBD <br>
__Office hours:__ TBD <br>

## Motivation and learning objectives

## Prerequisites

Students should have completed the Calculus I/II sequence and Introductory Probability. Students should also have basic experience coding in R, Python, MATLAB, and/or Julia. We will extensively use the [Stan platform](https://mc-stan.org/) for Bayesian computation, though no experience with that is necessary. Examples will be conducted in R.  

## Class structure

### The flipped classroom

This course uses a flipped classrom approach. Lectures are split into two parts of roughly 25 minutes each. The first part covers the motivation and theory for the day's topic, while the second covers practical worked examples. 

We'll use class time to discuss key topics and to work together through additional examples, mainly drawn from the assigned problem sets. These sessions will be more than just a study hall: I will guide the sessions from the back of the classroom, and students will work through the problems on the board. It's a bit like an oral exam, except I'll be feeding you a lot more information and I won't be evaluating you on what you do or don't know, only whether or not you participate. To get the most from class time, it's important to watch the lectures and have taken a crack at the problem set __before__ each class!

For the in-class examples, I'll randomly call on students using a random name generator (code [here]()) to present concepts and work through problems at the board. I recognize there will be days when you're away or just not on your game, so the board-work will be on an opt-in basis. Opting in will count for part of your grade (see __Evaluation__); to get full points, you'll need to opt in to at least 30 of the 39 class sessions, so that we should have a decently large pool of students opting in each day. 

### Problem sets

Every other week, I'll assign a problem set. The problem set will be released on the course webpage on Mondays at 9am and will be due on Fridays (12 days later) at 5pm, with adjustments made for holidays (e.g., if there's a Monday holiday, I'll release the problem set on Tuesday morning). Feel free to work with other students on the problem sets, but the write-ups should obviously reflect your own work. Problem sets will involve a mix of derivation-type problems and computational problems. 

### Projects 

The end-of-term project makes up a major part of the course grade. The project is intended to involve a variety of the topics we've discusse during the course. A project proposal is due at the end of Week 9, leaving six weeks for completion. 

You can work on teams of up to three; pairs and solo-work is fine, too, and I'll adjust my expectations accordingly (a group of three should be able to accomplish somewhat more than a single person!). 


## Textbook and materials 

This course will be based principally on _Bayesian Data Analysis, 3rd Edition_ by Gelman, Carlin, Stern, Dunson, Vehtari, and Rubin. 

<center>
	<img src="/assets/images/bda_cover.png" width="33%">
</center>

A full PDF of the textbook is availble [here](http://www.stat.columbia.edu/~gelman/book/) along with additional materials. 

We'll also dip briefly into Rasmussen and Williams' _Gaussian Processes for Machine Learning_, available [here](http://gaussianprocess.org/gpml/chapters/RW.pdf)

## Evaluation

30% of the course grade will be based on the final project. 10% will be based on in-class participation. The remaining 60% will be evenly split between weekly homework assignments. There are no exams. 

## Schedule

__Week 1: Probability and inference (BDA 1)__
- __Class 1:__ Basics of Bayesian inference (BDA 1.1-1.4)
- __Class 2:__ Probability as a measure of uncertainty (BDA 1.5-1.8)
- __Class 3:__ Computation and software (BDA 1.9-1.10)

__Week 2: Single-parameter models (BDA 2)__
- __Class 1:__ Posteriors (BDA 2.1-2.3)
- __Class 2:__ Priors 1 (BDA 2.4-2.7)
- __Class 3:__ Priors 2 (BDA 2.8-2.9)

__Week 3: Multi-parameter models (BDA 3)__
- __Class 1:__ Normal data (BDA 3.1-3.3)
- __Class 2:__ Categorical data (BDA 3.4)
- __Class 3:__ Multivariate normal data (BDA 3.5-3.8)

__Week 4: Hierarchical models (BDA 5)__
- __Class 1:__ Constructing priors (BDA 5.1) 
- __Class 2:__ Constructing models (BDA 5.3-5.5)
- __Class 3:__ Meta-analysis (BDA 5.6-5.7)

__Week 5: Model evaluation (BDA 6-7)__
- __Class 1:__ Posterior predictive checking (BDA 6.1-6.4)
- __Class 2:__ Cross-validation (BDA 7.1-7.2)
- __Class 3:__ Model comparison (BDA 7.3-7.4)

__Week 6: Modeling accounting for data collection (BDA 8)__
- __Class 1:__ Data collection models (BDA 8.1-8.3)
- __Class 2:__ Designed experiments (BDA 8.4-8.5)
- __Class 3:__ Observational studies (BDA 8.6-8.7)

__Week 7: Introduction to Bayesian computation (BDA 10)__
- __Class 1:__ Numerical integration (BDA 10.1-10.2)
- __Class 2:__ Sampling (BDA 10.3-10.5)
- __Class 3:__ Computing environments (BDA 10.6-10.7)

__Week 8: Markov chain simultion (BDA 11-12)__
- __Class 1:__ Gibbs, Metropolis, and Metropolis-Hastings (BDA 11.1-11.3)
- __Class 2:__ Inference and assessing convergence (BDA 11.4-11.5)
- __Class 3:__ Efficient sampling (BDA 12.1-12.5)

__Week 9: Introduction to regression models (BDA 14)__
- __Class 1:__ A Bayesian approach to regression (BDA 14.1-14.4)
- __Class 2:__ Assembling a regression model (BDA 14.5-14.6)
- __Class 3:__ Dealing with unequal variances and correlations (BDA 14.7-14.8)

__Week 10: Hierarchical linear models (BDA 15)__
- __Class 1:__ Batching regression coefficients (BDA 15.1-15.2)
- __Class 2:__ Varying intercepts and slopes (BDA 15.4-15.5)
- __Class 3:__ Analaysis of variance (BDA 15.6-15.7)

__Week 11: Generalized linear models (BDA 16)__
- __Class 1:__ Working with GLMs (BDA 16.1-16.2)
- __Class 2:__ Single-parameter GLMs (BDA 16.3-16.5)
- __Class 3:__ Multivariate GLMs (BDA 16.6-16.7)

__Week 12: Finite mixture models (BDA 22)__
- __Class 1:__ Setting up mixture models (BDA 22.1-22.2)
- __Class 2:__ Label switching and specifying mixture components (BDA 22.3-22.4)
- __Class 3:__ Mixture models for classification and regression (BDA 22.5)

__Week 13: Gaussian process models (BDA 21)__
- __Class 1:__ Gaussian process regression (BDA 21.1-22.2)
- __Class 2:__ Latent Gaussian process models (BDA 21.3-21.4)
- __Class 3:__ Density estimation and regression (BDA 21.5)

__Week 14: Project wrap-up__

__Week 15: Project presentations__

## University Policies

### University Code of Conduct 

Both students and faculty are responsible for maintaining an appropriate learning environment in all instructional settings, whether in person, remote or online. Those who fail to adhere to such behavioral standards may be subject to discipline. Professional courtesy and sensitivity are especially important with respect to individuals and topics dealing with race, color, national origin, sex, pregnancy, age, disability, creed, religion, sexual orientation, gender identity, gender expression, veteran status, political affiliation or political philosophy. For more information, see the policies on [classroom behavior](http://www.colorado.edu/policies/student-classroom-and-course-related-behavior) and the [Student Code of Conduct](https://www.colorado.edu/sccr/sites/default/files/attached-files/2020-2021_student_code_of_conduct_0.pdf).

### Accommodation for Disabilities

If you qualify for accommodations because of a disability, please submit your accommodation letter from Disability Services to your faculty member in a timely manner so that your needs can be addressed. Disability Services determines accommodations based on documented disabilities in the academic environment. Information on requesting accommodations is located on the [Disability Services website](https://www.colorado.edu/disabilityservices/). Contact Disability Services at 303-492-8671 or dsinfo@colorado.edu for further assistance. If you have a temporary medical condition, see [Temporary Medical Conditions](http://www.colorado.edu/disabilityservices/students/temporary-medical-conditions) on the Disability Services website.

### Preferred Student Names and Pronouns

CU Boulder recognizes that students' legal information doesn't always align with how they identify. Students may update their preferred names and pronouns via the student portal; those preferred names and pronouns are listed on instructors' class rosters. In the absence of such updates, the name that appears on the class roster is the student's legal name.

### Honor Code

All students enrolled in a University of Colorado Boulder course are responsible for knowing and adhering to the Honor Code. Violations of the policy may include: plagiarism, cheating, fabrication, lying, bribery, threat, unauthorized access to academic materials, clicker fraud, submitting the same or similar work in more than one course without permission from all course instructors involved, and aiding academic dishonesty. If you have read this far into the syllabus, well done! Send me a picture or video of the coolest animal (your opinion) for a small bump to your grade. All incidents of academic misconduct will be reported to the Honor Code (honor@colorado.edu); 303-492-5550). Students found responsible for violating the academic integrity policy will be subject to nonacademic sanctions from the Honor Code as well as academic sanctions from the faculty member. Additional information regarding the Honor Code academic integrity policy can be found at the [Honor Code Office website](https://www.colorado.edu/osccr/honor-code).

### Sexual Misconduct, Discrimination, Harassment and/or Related Retaliation

The University of Colorado Boulder (CU Boulder) is committed to fostering an inclusive and welcoming learning, working, and living environment. CU Boulder will not tolerate acts of sexual misconduct (harassment, exploitation, and assault), intimate partner violence (dating or domestic violence), stalking, or protected-class discrimination or harassment by members of our community. Individuals who believe they have been subject to misconduct or retaliatory actions for reporting a concern should contact the Office of Institutional Equity and Compliance (OIEC) at 303-492-2127 or cureport@colorado.edu. Information about the OIEC, university policies, [anonymous reporting](https://cuboulder.qualtrics.com/jfe/form/SV_0PnqVK4kkIJIZnf), and the campus resources can be found on the [OIEC website](http://www.colorado.edu/institutionalequity/).

Please know that faculty and graduate instructors have a responsibility to inform OIEC when made aware of incidents of sexual misconduct, dating and domestic violence, stalking, discrimination, harassment and/or related retaliation, to ensure that individuals impacted receive information about options for reporting and support resources.

### Religious Holidays
Campus policy regarding religious observances requires that faculty make every effort to deal reasonably and fairly with all students who, because of religious obligations, have conflicts with scheduled exams, assignments or required attendance. In this class, please let me know of upcoming religious holidays at least two weeks ahead of time if you will need an accommodation. See the [campus policy regarding religious observances](http://www.colorado.edu/policies/observance-religious-holidays-and-absences-classes-andor-exams) for full details.




