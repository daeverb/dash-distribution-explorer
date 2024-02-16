### Binomial Distribution

**What It Is:** The binomial distribution models the number of successes in a fixed number of independent trials, each with the same probability of success. It's like flipping a coin multiple times and counting how many times it lands on heads.

**Key Features:**
- **Type:** Discrete.
- **Trials:** Must be a fixed number, $n$.
- **Success or Failure:** Each trial has two possible outcomes (binary).
- **Constant Probability:** The probability of success, $p$, remains the same in each trial.
- **Independence:** The outcome of one trial doesn’t affect another.

**Real-life Example:** Consider a survey asking if people like ice cream. If you ask 100 people and 60% generally do, the binomial distribution can predict the likelihood of 70 people saying "yes".

**Parameters and PMF:**
- **Key Parameters:** Number of trials $n$, probability of success in each trial $p$.
- **PMF:** $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$ where $k$ is the number of successes and $\binom{n}{k}=\frac {n!}{k!(n-k)!}$, read as $n$ choose $k$.
  - *$n$ choose $k$:* In how many ways you can pick a group of $k$ items from a larger set of $n$ items, without caring about the order in which you pick them.

### Poisson Distribution

**What It Is:** The Poisson distribution measures the probability of a given number of events happening in a fixed interval of time or space, assuming these events occur with a known average rate and independently of the time since the last event.

**Key Features:**
- **Type:** Discrete.
- **Interval:** Time or space where events occur.
- **Rate:** Average number of occurrences in a given interval, $\lambda$.
- **Independence:** Events occur independently.

**Real-life Example:** If a bakery sells an average of 30 cakes per day, the Poisson distribution can estimate the probability of selling exactly 25 cakes tomorrow.

**Parameters and PMF:**
- **Key Parameters:** Average rate of success $\lambda$.
- **PMF:** $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$ where $k$ is the number of events.

### Geometric Distribution

**What It Is:** The geometric distribution models the number of trials needed to achieve the first success in a series of independent Bernoulli trials, each with the same probability of success.

**Key Features:**
- **Type:** Discrete.
- **Success Probability:** Constant probability of success in each trial, $p$.
- **Trial Count:** Focuses on the count until the first success.

**Real-life Example:** If there's a 10% chance of raining each day, the geometric distribution can tell you the probability that the first rain will happen on the fifth day.

**Parameters and PMF:**
- **Key Parameters:** Probability of success in each trial $p$.
- **PMF:** $P(X = k) = (1-p)^{k-1}p$ where $k$ is the number of trials until the first success.

### Negative Binomial Distribution

**What It Is:** This distribution extends the geometric distribution by modeling the number of trials needed to achieve a specified number of successes, rather than just the first success.

**Key Features:**
- **Type:** Discrete.
- **Successes Required:** The target number of successes, $r$, is specified.
- **Success Probability:** Each trial has a constant probability of success, $p$.

**Real-life Example:** If a scientist needs 5 bacteria samples to exhibit a certain trait that has a 20% chance of occurring, the negative binomial distribution can predict how many samples they must observe on average.

**Parameters and PMF:**
- **Key Parameters:** Number of successes $r$, probability of success in each trial $p$.
- **PMF:** $P(X = k) = \binom{k-1}{r-1} p^r (1-p)^{k-r}$ where $k$ is the total number of trials.

### Normal (Gaussian) Distribution

**What It Is:** The normal distribution models a continuous variable where most observations cluster around a central mean value, with probabilities for values further from the mean decreasing symmetrically.

**Key Features:**
- **Type:** Continuous.
- **Mean ($\mu$) and Standard Deviation ($\sigma$):** Determine the distribution's center and width.
- **Symmetry:** The distribution is symmetric about the mean.
- **Bell Shape:** The characteristic "bell curve" shape.

**Real-life Example:** Adult heights within a specific gender and population tend to follow a normal distribution, with most people being of average height and fewer people being extremely tall or short.

**Parameters and PDF:**
- **Key Parameters:** Mean $\mu$, standard deviation $\sigma$.
- **PDF:** $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$

### Exponential Distribution

**What It Is:** The exponential distribution models the time between events in a Poisson process, describing the intervals between independent events that happen at a constant average rate.

**Key Features:**
- **Type:** Continuous.
- **Rate Parameter ($\lambda$)**: Determines the average rate of events per time unit.
- **Memoryless Property:** The probability of an event occurring in the future is independent of how much time has already elapsed.

**Real-life Example:** The time between earthquakes in a given region can be modeled with an exponential distribution if they occur independently and at a constant average rate.

**Parameters and PDF:**
- **Key Parameters:** Rate parameter $\lambda$ (the reciprocal of the mean).
- **PDF:** $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$.

### Uniform Distribution

**What It Is:** The uniform distribution assigns equal probability to all outcomes in a defined range, whether for discrete cases (like rolling a fair die) or continuous cases (like picking a random point along a line).

**Key Features:**
- **Type:** Continuous.
- **Bounds $a$ and $b$:** All values within these bounds are equally likely.
- **Flat Probability Curve:** For continuous uniform distributions, this means a constant probability density function between $a$ and $b$.

**Real-life Example:** If you randomly choose a number between 1 and 100, each number has an equal chance of being selected.

**Parameters and PDF:**
- **Key Parameters:** Lower bound $a$, upper bound $b$.
- **PDF:** $f(x) = \frac{1}{b-a}$ for $x$ in $[a, b]$.

### Beta Distribution

**What It Is:** The beta distribution models probabilities that vary within a 0 to 1 interval, useful for modeling events with uncertain probabilities, especially in Bayesian statistics.

**Key Features:**
- **Type:** Continuous.
- **Shape Parameters ($\alpha$ and $\beta$)**: Control the distribution's shape, allowing it to assume a variety of forms from uniform to skewed.
- **Versatility:** It can model a wide range of probability distributions on $[0, 1]$, making it particularly useful for representing proportions or percentages with uncertainty.

**Real-life Example:** When launching a new product, a company might use past launch data to model the probability of achieving different market share levels within the first year. The Beta distribution, with parameters shaped by prior successes ($\alpha$) and failures ($\beta$), can estimate the probability of capturing any specific percentage of the market: plot the pdf's from AB-testing (i.e. one with $\alpha_A$ and $\beta_A$, and one with $\alpha_B$ and $\beta_B$).

**Parameters and PDF:**
- **Key Parameters:** Shape parameters $\alpha$ and $\beta$, which determine the shape of the distribution.
- **PDF:** $f(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)}$ for $x$ in $[0, 1]$, where $B(\alpha, \beta)$ is the Beta function.

### Gamma Distribution

**What It Is:** The Gamma distribution is a two-parameter family of continuous probability distributions that extends the exponential distribution for modeling waiting times over multiple events. It's particularly useful when the event rate ($\lambda$) varies.

**Key Features:**
- **Type:** Continuous.
- **Shape and Scale Parameters ($k$ and $\theta$):** $k$ (or $\alpha$) shapes the distribution, and $\theta$ (scale) stretches or compresses it horizontally. These parameters allow the Gamma distribution to adapt to different types of skewed data.
- **Flexibility:** Can model a wide range of processes, from skewed distributions like service times in a system to the amount of rainfall accumulated in a reservoir over time.

**Real-life Example:** In healthcare, the Gamma distribution can model the length of stay of patients in a hospital for different conditions. By adjusting the shape and scale parameters based on historical data, administrators can better predict patient flows and manage resources, such as bed availability and staffing needs.

These detailed explanations aim to provide a foundational understanding of some key statistical distributions, illustrating their practical significance with relatable examples. Each distribution offers a unique lens through which to view and analyze data, tailored to specific characteristics of the phenomena being studied.

**Parameters and PDF:**
- **Key Parameters:** shape parameter ($k$ or $\alpha$) influences the form of the distribution, and scale parameter ($\theta$) determines the stretch or compression of the distribution on the horizontal axis, affecting the dispersion of data points.
- **PDF:** $f(x; k, \theta) = \frac{x^{k-1}e^{-x/\theta}}{\theta^k \Gamma(k)}$ for $x \ge 0$, where $\Gamma(k)$ is the gamma function, a generalization of factorial that interpolates the factorial function for non-integer values of $k$. 
