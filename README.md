# Mathematics for data science

## General information

*Lecturer:* Aleksandr Avdiushenko, ovalur@gmail.com

*Telegram:* My telegram nick is @ovalur

[Course Group in Telegram](https://t.me/+DyEyzMhEtJoxYmEy)

This group will be for discussion and prompt resolution of any issues related to the course. This will be the fastest way to contact me.

<a href='TBA'><h3>Classes Zoom link</h3></a>

## Why this course

Once you join a new university program, it's natural to be eager to learn all the IT concepts involved. However, you might not have a strong enough mathematical background. Perhaps you've studied these topics before and forgotten them, or maybe you never had the necessary math courses at all. Our programs are designed with students in mind, so we've created this course to provide essential math fundamentals crucial for IT. We aim to help you reach your desired level in mathematics.

It's clear that you can't learn in six months what passionate young students typically master in 2 years at mathematical departments between the ages of 17-18. Therefore, this course will be structured differently than traditional math courses designed for mathematicians. We will focus on the interface approach, which is familiar to you from programming languages and originates from mathematics. In fact, you can divide mathematics into interface and implementation. To apply mathematics effectively, it's sufficient to grasp the interface of a particular theory, without knowing the specifics of its implementation (which often varies significantly). Math students spend a considerable amount of time studying the implementations of mathematical theories, building consistent theories with the right properties, or the right interfaces. In contrast, we will focus on utilizing already established theories. The main drawback of this approach is that you will likely not be able to create your own mathematical theory. However, our goal is not to become professional mathematicians. One advantage of this approach is the speed of learning. That being said, we must remember that there are no miracles — our brain can only absorb a certain amount of material within a given time frame. The pace of this course will often push us close to that limit. I will do my best to ensure that you have enough motivation and drive to reach the end. Much like sports, the coach can show you the most effective path to the goal, but you must walk that path yourself. I hope this journey will be both interesting and beneficial.

## Course program
In the fascinating field of mathematics, there are several branches that continue to find practical applications. We will focus on the most important ones: linear algebra, probability theory, and mathematical statistics. Linear algebra and probability theory serve as the primary areas of application. The volume of material in linear algebra is equivalent to the Higher School of Economics (HSE) course for the PMI program, but without proofs and with revised priorities. The probability theory course is based on courses taught at the mathematical departments of Russian universities; however, it omits the formal technical complexities associated with constructing a consistent probability theory. The primary challenge of probability theory is that, due to the intricate structure of formal set theory, a naive, straightforward approach often leads to contradictions. The main goal of probability theory for mathematicians is to address these low-level set-theoretic issues. In our course, we will simply bypass these problems and concentrate on the substance of the subject matter.
Also we will cover mathematical statistics, focusing on topics such as basic models, estimation properties, random sample generation, hypothesis testing, parametric and non-parametric tests, ANOVA family, bootstrap, and an introduction to Bayesian statistics.

### Linear algebra
* Systems of linear equations, matrices, operations, block operations, reversibility and non-degeneracy.
* Determinants (3 approaches), oriented volumes, explicit inverse matrix formulas, characteristic polynomial, polynomial calculus in matrices, spectrum, Hamilton-Cayley theorem.
* Vector spaces and subspaces, dimensions, matrix ranks: row rank, column rank, factorial rank, tensor rank, minor rank. Properties of ranks and inequalities on ranks.
* Linear mappings and their matrix description, change of coordinates. The image and the core, their geometric meaning, connection to the dimension. Linear operator invariants: trace, determinant, characteristic polynomial. Eigenvalues and vectors, connection with the spectrum. A note about complex numbers. Diagonalizability and related matrix expansions.
* Bilinear forms. Quadratic forms and symmetric bilinear forms. Signature, its geometric meaning, methods for determining the signature. Relationship with LU-decomposition. Dot products, angles and distances. Orthogonalization and QR decomposition. Linear manifolds and linear classifiers, margins.
* Operators in Euclidean spaces. Motions and orthogonal matrices and their classification. Self-adjoint operators and symmetric matrices, their diagonalizability. Singular value decomposition (SVD). Finding SVD.

### Probability theory
* Probability space, random events, how to understand them. Probability (measure) and conditional probability, independence of events, geometric meaning. Bayes formulas and full probability.
* Random variables, how to understand them. Distribution functions, probabilities (measures) on the line and how to set them. Classes of distributions, examples of discrete and continuous distributions. Joint distribution. Characteristics of random variables: mathematical expectation, variance, moments, median (in a good case). Normal or Gaussian distribution.
* Random vector or multidimensional random variable, how to understand and set them. Classes of distributions, examples of discrete and continuous distributions. Recovery of distributions of coordinates. Mathematical expectation and covariance matrix. Independence of random variables. Properties of mathematical expectation and dispersion for independent random variables.
* Conditional mathematical expectations and probabilities. Bayes formulas and full probability for the continuous case. Distribution of the sum of independent random variables and convolution of densities. Multivariate Gaussian distribution.

### Mathematical statistics
* The basic model of mathematical statistics (how to relate the formalism of probability theory to sample measurements). Estimates and their properties. Why convergence and limit theorems are needed. Types of convergences and the relationship between them. Laws of large numbers and Chebyshev's inequality. Sample mean and sample variance, sample covariance matrix, correlation coefficient. Maximum likelihood method. PCA and SVD. Central limit theorem and the Berry-Essen inequality.
* Generating a random sample. Probability integral transformation. Direct and non-direct methods. Accept-Reject algorithm. MCMC algorithms, Metropolis Algorithm.
* Hypothesis testing. Formal problem of hypothesis testing. Differences of parametric and non-parametric tests. Confidence intervals. Examples of hypotheses and tests. 
* Parametric and non-parametric tests. Type-I, Type-II errors, p-value. Choosing the methods. Student-T and U-Mann-Whitney. Normality tests, Shapiro-Wilk W-Test.
* ANOVA family. Formal problem. ANOVA assumptions. Theoretical basis of one way ANOVA. Two-way ANOVA. N-way ANOVA, non-parametric ANOVA, ANCOVA.
* Bootstrap. Theory and practice.
* Introduction in Bayesian Statistics. Theory and practice.


## Homework and grading rules
* The course consists of 13 classes. There will be a homework assignment for each class. The deadline for each homework assignment is 10 days from the date of publication (the deadline will be indicated in the assignment). 
* If an assignment is submitted after the deadline, the final grade is calculated using the formula $O_{\text{final}} = 0.7^t O_{\text{hw}}$, where $t$ is the time after the deadline in days without rounding, $O_{\text{hw}}$ is the grade for the homework assignment if it had been submitted on time, and $O_{\text{final}}$ is the grade awarded for the late homework assignment.
* Homework assignments must be submitted in written form (handwritten or using \LaTeX, virtual boards are also acceptable). The work should be submitted as a single multi-page PDF file (you can use the `notebloc` app on your mobile phone, as it does a good job of whitening the background and produces photos of acceptable size). All pages must be vertically oriented and in sequential order. Please make sure to adhere to this requirement. We would be very grateful for your cooperation.
* The rules for determining the final grade will be announced later, but by default, it is assumed that all 13 homework assignments must be completed. The threshold value for passing the course will be announced later.
